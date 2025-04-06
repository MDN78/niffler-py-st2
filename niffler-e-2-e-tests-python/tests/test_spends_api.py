import pytest

from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from fixtures.auth_fixtures import auth_api_token
from models.category import CategoryAdd
from _pytest.fixtures import FixtureRequest
from databases.spend_db import SpendDb
from models.enums import Category
from marks import Pages, TestData


@pytest.mark.skip
def test_auth(auth_api_token):
    print(auth_api_token)


def test_add_new_category_via_api(category_client: CategoryHttpClient, spend_db: SpendDb):
    category_name = Category.TEST_CATEGORY3
    category = category_client.add_category((CategoryAdd(name=category_name)))
    assert category.name == category_name
    assert category.id is not None
    assert category.username == 'stas'
    spend_db.delete_category(category.id)


@TestData.category(Category.TEST_CATEGORY4)
def test_get_all_categories_via_api(category, category_client: CategoryHttpClient, spend_db: SpendDb):
    categories = category_client.get_categories()
    assert len(categories) > 0

#
# def test_add_new_category_via_api(envs, auth_api_token, spend_db: SpendDb):
#     category_name = Category.TEST_CATEGORY3
#     category = CategoryHttpClient(envs, auth_api_token).add_category((CategoryAdd(name=category_name)))
#     assert category.name == category_name
#     assert category.id is not None
#     assert category.username == 'stas'
#     spend_db.delete_category(category.id)
