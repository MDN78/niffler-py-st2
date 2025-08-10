import pytest
from models.config import Envs
from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from databases.spend_db import SpendDb
import allure
from databases.auth_db import UserDb
from databases.userdata_db import UserdataDb


@pytest.fixture(scope='session')
@allure.title("Activating niffler-spend's microservice client")
def spends_client(envs: Envs, auth_api_token: str) -> SpendsHttpClient:
    return SpendsHttpClient(envs, auth_api_token)


@pytest.fixture(scope="session")
@allure.title("Activating niffler-spend's spend bd")
def spend_db(envs: Envs) -> SpendDb:
    return SpendDb(envs)


@pytest.fixture(scope='session')
@allure.title("Activating niffler-spend's microservice client")
def category_client(envs: Envs, auth_api_token: str) -> CategoryHttpClient:
    return CategoryHttpClient(envs, auth_api_token)


@pytest.fixture(scope="session")
@allure.title("Activating niffler-spend's auth bd")
def auth_db(envs: Envs) -> UserDb:
    return UserDb(envs)


@pytest.fixture()
@allure.title("Activating niffler-spend's userdata bd")
def user_db(envs: Envs) -> UserdataDb:
    return UserdataDb(envs)
