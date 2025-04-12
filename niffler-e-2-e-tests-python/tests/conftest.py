import pytest
from models.config import Envs
from pages.spend_page import spend_page
from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from databases.spend_db import SpendDb
from models.category import CategoryAdd
from _pytest.fixtures import FixtureRequest


@pytest.fixture(params=[])
def category(request: FixtureRequest, category_client: CategoryHttpClient, spend_db: SpendDb):
    category_name = request.param
    category = category_client.add_category((CategoryAdd(name=category_name)))
    yield category.name
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def category_db(request: FixtureRequest, category_client: CategoryHttpClient, spend_db: SpendDb):
    category = category_client.add_category(request.param)
    yield category
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def spends(request: FixtureRequest, spends_client: SpendsHttpClient):
    t_spend = spends_client.add_spend(request.param)
    yield t_spend
    all_spends = spends_client.get_spends()
    if t_spend.id in [spend.id for spend in all_spends]:
        spends_client.remove_spends([t_spend.id])


@pytest.fixture()
def delete_spend(request: FixtureRequest, auth: str, envs: Envs):
    name_category = request.param
    yield name_category
    spend_page.delete_spend(name_category)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selene import browser
#
# @pytest.fixture(scope="session", autouse=True)
# def driver_configuration(request):
#     chrome_options = Options()
#     # Отключаем уведомления об утечке паролей
#     chrome_options.add_argument("--password-store=basic")
#     chrome_options.add_experimental_option("prefs", {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False,
#         "profile.default_content_setting_values.notifications": 2
#     })
#
#     # Дополнительные настройки для отключения предупреждений chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) chrome_options.add_experimental_option("useAutomationExtension", False)
#
#     driver = webdriver.Chrome(options=chrome_options)
#     browser.config.driver = driver
#     yield
#     browser.quit()

