import pytest
from selene import browser
from models.config import Envs
from urllib.parse import urljoin


@pytest.fixture()
def profile_page(envs: Envs, auth: str):
    profile_url = urljoin(envs.frontend_url, "/profile")
    browser.open(profile_url)


@pytest.fixture()
def main_page(auth: str, envs: Envs):
    browser.open(envs.frontend_url)


# @pytest.fixture()
# def main_page(auth_api_token: str, envs: Envs):
#     browser.open('http://auth.niffler.dc:9000/login')
#     browser.driver.add_cookie({"name": "Authorization", "value": f'Bearer {auth_api_token}'})
#     browser.driver.refresh()
#     browser.open(envs.frontend_url)

# @pytest.fixture()
# def main_page(auth_api_token: str, envs: Envs):
#     browser.driver.(
#         {
#            'Authorization': f'Bearer {auth_api_token}'
#         }
#     )
#     browser.open(envs.frontend_url)


# @pytest.fixture()
# def main_page(auth_api_token: str, envs: Envs):
#     browser.open(envs.registration_url)
#     browser.execute_script(f"localStorage.setItem('id_token', '{auth_api_token}')")
#     # browser.open(envs.login_url)
#     browser.open("http://frontend.niffler.dc/main")



