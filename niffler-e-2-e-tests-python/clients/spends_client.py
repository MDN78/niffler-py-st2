import allure
import requests
from utils.sessions import BaseSession
from models.config import Envs
from models.spend import SpendAdd, Spend


class SpendsHttpClient:
    """Класс для взаимодействия с микросервисом niffler spend"""

    session: requests.Session
    base_url: str

    def __init__(self, envs: Envs, token: str):
        self.session = BaseSession(base_url=envs.gateway_url)
        self.session.headers.update({
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    @allure.step('HTTP: add spends')
    def add_spend(self, spend: SpendAdd) -> Spend:
        response = self.session.post("/api/spends/add", json=spend.model_dump())
        assert response.status_code == 201
        return Spend.model_validate(response.json())

    @allure.step('HTTP: get spends')
    def get_spends(self) -> list[Spend]:
        response = self.session.get("/api/spends/all")
        assert response.status_code == 200
        return [Spend.model_validate(item) for item in response.json()]

    @allure.step('HTTP: remove spends')
    def remove_spends(self, ids: list[str]) -> None:
        """Удааление трат без возврата ответа.
        НО, если надо проверить саму ручку удаления - то надо добавить возврат response."""
        response = self.session.delete("/api/spends/remove", params={"ids": ids})
        assert response.status_code == 200

    @allure.step('HTTP: update spends')
    def update_spend(self, update: Spend) -> Spend:
        response = self.session.patch("/api/spends/edit", data=update.model_dump_json())
        assert response.status_code == 200
        return Spend.model_validate(response.json())
