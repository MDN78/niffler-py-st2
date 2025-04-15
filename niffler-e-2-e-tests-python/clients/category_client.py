import allure
import requests
from utils.sessions import BaseSession
from models.config import Envs
# from requests import Response
from models.category import Category, CategoryAdd
# from allure_commons.types import AttachmentType
# from requests_toolbelt.utils.dump import dump_response
# from utils.helper import step



class CategoryHttpClient:
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
    @allure.step('HTTP: get categories')
    def get_categories(self) -> list[CategoryAdd]:
        response = self.session.get("/api/categories/all")
        # self.raise_for_status(response)
        return [CategoryAdd.model_validate(item) for item in response.json()]

    # @step
    @allure.step('HTTP: add category')
    def add_category(self, category: CategoryAdd) -> Category:
        response = self.session.post("/api/categories/add", json=category.model_dump())
        # self.raise_for_status(response)
        return Category.model_validate(response.json())

    # @staticmethod
    # def raise_for_status(response: requests.Response):
    #     try:
    #         response.raise_for_status()
    #     except requests.HTTPError as e:
    #         if response.status_code == 400:
    #             e.add_note(response.text)
    #             raise
