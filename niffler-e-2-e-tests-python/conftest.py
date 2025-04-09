import os
from pytest import Item, FixtureDef, FixtureRequest
from allure_commons.reporter import AllureReporter
from allure_pytest.listener import AllureListener
from allure_commons.types import AttachmentType
import allure
import pytest
from dotenv import load_dotenv
from faker import Faker
from models.config import Envs
from utils.helper import allure_reporter

pytest_plugins = ["fixtures.auth_fixtures", "fixtures.client_fixtures", "fixtures.pages_fixtures"]


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
    password = fake.password(6)
    return name, password


@pytest.fixture(scope='session')
def app_forbidden_username() -> tuple:
    fake = Faker()
    name = 'qw'
    password = fake.password(5)
    return name, password
