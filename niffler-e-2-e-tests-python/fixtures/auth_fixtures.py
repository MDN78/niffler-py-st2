import pytest
from models.config import Envs
from selene import browser
import allure
from allure_commons.types import AttachmentType
from clients.auth_client import AuthClient


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
