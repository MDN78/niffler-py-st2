import allure
import requests
from utils.sessions import BaseSession
from models.config import Envs
from urllib.parse import urljoin
from requests import Response
from allure_commons.types import AttachmentType
from models.spend import SpendAdd, Spend
from requests_toolbelt.utils.dump import dump_response
# from utils.helper import step


class SpendsHttpClient:
    session: requests.Session
    base_url: str

    def __init__(self, envs: Envs, token: str):
        self.session = BaseSession(base_url=envs.gateway_url)
        self.session.headers.update({
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    #     self.session.hooks["response"].append(self.attach_response)
    #
    # @staticmethod
    # @allure.step('HTTP: attach response')
    # def attach_response(response: Response, *args, **kwargs):
    #     attachment_name = response.request.method + " " + response.request.url
    #     allure.attach(dump_response(response), attachment_name, attachment_type=AttachmentType.TEXT)

    # @step
    @allure.step('HTTP: add spends')
    def add_spend(self, spend: SpendAdd) -> Spend:
        response = self.session.post("/api/spends/add", json=spend.model_dump())
        # self.raise_for_status(response)
        assert response.status_code == 201
        return Spend.model_validate(response.json())

    # @step
    @allure.step('HTTP: get spends')
    def get_spends(self) -> list[Spend]:
        response = self.session.get("/api/spends/all")
        # self.raise_for_status(response)
        assert response.status_code == 200
        return [Spend.model_validate(item) for item in response.json()]

    # @step
    @allure.step('HTTP: remove spends')
    def remove_spends(self, ids: list[str]) -> None:
        """Удааление трат без возврата ответа.
        НО, если надо проверить саму ручку удаления - то надо добавить возврат response."""
        response = self.session.delete("/api/spends/remove", params={"ids": ids})
        assert response.status_code == 200
        # self.raise_for_status(response)

    # @step
    @allure.step('HTTP: update spends')
    def update_spend(self, update: Spend) -> Spend:
        response = self.session.patch("/api/spends/edit", data=update.model_dump_json())
        # response.raise_for_status()
        assert response.status_code == 200
        return Spend.model_validate(response.json())

    # @staticmethod
    # def raise_for_status(response: requests.Response):
    #     try:
    #         response.raise_for_status()
    #     except requests.HTTPError as e:
    #         if response.status_code == 400:
    #             e.add_note(response.text)
    #             raise
