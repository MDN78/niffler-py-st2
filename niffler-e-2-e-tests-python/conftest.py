import os
from urllib.parse import urljoin
from pytest import Item, FixtureDef, FixtureRequest
from allure_commons.reporter import AllureReporter
from allure_pytest.listener import AllureListener
from allure_commons.types import AttachmentType
import allure
import pytest
from selene import browser
from dotenv import load_dotenv
from clients.auth_client import AuthClient
from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from faker import Faker
from pages.spend_page import spend_page
from databases.spend_db import SpendDb
from models.category import CategoryAdd
from models.config import Envs
from utils.helper import allure_reporter


def allure_logger(config) -> AllureReporter:
    listener: AllureListener = config.pluginmanager.get_plugin("allure_listener")
    return listener.allure_logger


@pytest.hookimpl(hookwrapper=True, trylast=True)  # hook call after all fixtures
def pytest_runtest_call(item: Item):
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_fixture_setup(fixturedef: FixtureDef, request: FixtureRequest):
    yield
    logger = allure_logger(request.config)
    item = logger.get_last_item()
    scope_letter = fixturedef.scope[0].upper()
    item.name = f"[{scope_letter}] " + " ".join(fixturedef.argname.split("_")).title()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    # Make result visible in fixtures
    setattr(item, "rep_" + rep.when, rep)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown(item):
    yield
    reporter = allure_reporter(item.config)
    test = reporter.get_test(None)
    test.labels = list(filter(lambda x: x.name not in ("tag"), test.labels))


@pytest.fixture(scope="session")
def envs() -> Envs:
    load_dotenv()
    envs_instance = Envs(
        frontend_url=os.getenv("FRONTEND_URL"),
        gateway_url=os.getenv("GATEWAY_URL"),
        registration_url=os.getenv("REGISTRATION_URL"),
        auth_url=os.getenv("AUTH_URL"),
        auth_secret=os.getenv("AUTH_SECRET"),
        spend_db_url=os.getenv("SPEND_DB_URL"),
        test_username=os.getenv("TEST_USERNAME"),
        test_password=os.getenv("TEST_PASSWORD")
    )
    allure.attach(envs_instance.model_dump_json(indent=2), name="envs.json", attachment_type=AttachmentType.JSON)
    return envs_instance


@pytest.fixture(scope='session')
def app_unregistered_user() -> tuple:
    fake = Faker()
    name = fake.name()
    password = fake.password(5)
    return name, password


@pytest.fixture(scope='session')
def app_forbidden_username() -> tuple:
    fake = Faker()
    name = 'qw'
    password = fake.password(5)
    return name, password


@pytest.fixture(scope='session')
def auth(envs: Envs) -> str:
    browser.open(envs.frontend_url)
    browser.element('input[name=username]').set_value(envs.test_username)
    browser.element('input[name=password]').set_value(envs.test_password)
    browser.element('button[type=submit]').click()
    token = browser.driver.execute_script('return window.localStorage.getItem("id_token")')
    allure.attach(token, name="token.txt", attachment_type=AttachmentType.TEXT)
    return token


@pytest.fixture(scope="session")
def auth_api_token(envs: Envs):
    token = AuthClient(envs).auth(envs.test_username, envs.test_password)
    allure.attach(token, name="token.txt", attachment_type=AttachmentType.TEXT)
    return token


@pytest.fixture(scope='session')
def spends_client(envs: Envs, auth: str) -> SpendsHttpClient:
    return SpendsHttpClient(envs.gateway_url, auth)


@pytest.fixture(scope='session')
def category_client(envs: Envs, auth: str) -> CategoryHttpClient:
    return CategoryHttpClient(envs.gateway_url, auth)


@pytest.fixture(scope="session")
def spend_db(envs: Envs) -> SpendDb:
    return SpendDb(envs.spend_db_url)


@pytest.fixture(params=[])
def category(request, category_client: CategoryHttpClient, spend_db: SpendDb):
    category_name = request.param
    category = category_client.add_category(CategoryAdd(name=category_name))
    yield category.name
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def category_db(request, category_client: CategoryHttpClient, spend_db: SpendDb):
    category = category_client.add_category(request.param)
    yield category
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def spends(request, spends_client: SpendsHttpClient):
    t_spend = spends_client.add_spend(request.param)
    yield t_spend
    all_spends = spends_client.get_spends()
    if t_spend.id in [spend.id for spend in all_spends]:
        spends_client.remove_spends([t_spend.id])


@pytest.fixture()
def delete_spend(request, auth: str, envs: Envs):
    name_category = request.param
    yield name_category
    spend_page.delete_spend(name_category)


@pytest.fixture()
def profile_page(envs: Envs, auth: str):
    profile_url = urljoin(envs.frontend_url, "/profile")
    browser.open(profile_url)


@pytest.fixture()
def main_page(auth: str, envs: Envs):
    browser.open(envs.frontend_url)
