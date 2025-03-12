import os
import time
from urllib.parse import urljoin
import pytest
from selene import browser
from dotenv import load_dotenv
from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from faker import Faker
from pages.spend_page import spend_page
from databases.spend_db import SpendDb
from models.category import CategoryAdd
from models.config import Envs


@pytest.fixture(scope="session")
def envs() -> Envs:
    load_dotenv()
    return Envs(
        frontend_url=os.getenv("FRONTEND_URL"),
        gateway_url=os.getenv("GATEWAY_URL"),
        registration_url=os.getenv("REGISTRATION_URL"),
        spend_db_url=os.getenv("SPEND_DB_URL"),
        test_username=os.getenv("TEST_USERNAME"),
        test_password=os.getenv("TEST_PASSWORD")
    )


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
def auth(envs) -> str:
    browser.open(envs.frontend_url)
    browser.element('input[name=username]').set_value(envs.test_username)
    browser.element('input[name=password]').set_value(envs.test_password)
    browser.element('button[type=submit]').click()
    return browser.driver.execute_script('return window.localStorage.getItem("id_token")')


@pytest.fixture(scope='session')
def spends_client(envs, auth) -> SpendsHttpClient:
    return SpendsHttpClient(envs.gateway_url, auth)


@pytest.fixture(scope='session')
def category_client(envs, auth) -> CategoryHttpClient:
    return CategoryHttpClient(envs.gateway_url, auth)


@pytest.fixture(scope="session")
def spend_db(envs) -> SpendDb:
    return SpendDb(envs.spend_db_url)


@pytest.fixture(params=[])
def category(request, category_client, spend_db):
    category_name = request.param
    category = category_client.add_category(CategoryAdd(name=category_name))
    yield category.name
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def category_db(request, category_client, spend_db):
    category = category_client.add_category(request.param)
    yield category
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def spends(request, spends_client):
    t_spend = spends_client.add_spends(request.param)
    yield t_spend
    all_spends = spends_client.get_spends()
    if t_spend.id in [spend.id for spend in all_spends]:
        spends_client.remove_spends([t_spend.id])


@pytest.fixture()
def delete_spend(request, auth, envs):
    name_category = request.param
    yield name_category
    spend_page.delete_spend(name_category)


@pytest.fixture()
def profile(envs, auth):
    profile_url = urljoin(envs.frontend_url, "/profile")
    browser.open(profile_url)


@pytest.fixture()
def profile_page(envs, auth):
    profile_url = urljoin(envs.frontend_url, "/profile")
    browser.open(profile_url)


@pytest.fixture()
def main_page(auth, envs):
    browser.open(envs.frontend_url)
