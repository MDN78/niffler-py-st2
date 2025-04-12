import pytest
from clients.spends_client import SpendsHttpClient
# from fixtures.auth_fixtures import auth_api_token
from models.category import CategoryAdd
from databases.spend_db import SpendDb
from models.enums import Category
from models.spend import SpendAdd
from datetime import datetime
from models.spend import Spend
from marks import TestData

pytestmark = [pytest.mark.allure_label("Spends API", label_type="epic")]


def test_auth_token_fixture(auth_api_token):
    assert auth_api_token is not None
    # print(auth_api_token)


def test_add_spend(spends_client: SpendsHttpClient, spend_db: SpendDb):
    data = SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY5),
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        currency="RUB",
    )
    new_spend = spends_client.add_spend(data)

    assert new_spend.category.name == Category.TEST_CATEGORY5
    assert new_spend.description == data.description

    spends_client.remove_spends(new_spend.id)
    spend_db.delete_category(new_spend.category.id)


def test_add_spend_without_description(spends_client: SpendsHttpClient, spend_db: SpendDb):
    data = SpendAdd(
        amount=108.51,
        description="",
        category=CategoryAdd(name=Category.TEST_CATEGORY5),
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        currency="RUB",
    )
    new_spend = spends_client.add_spend(data)

    assert new_spend.category.name == Category.TEST_CATEGORY5
    assert new_spend.description == ''

    spends_client.remove_spends(new_spend.id)
    spend_db.delete_category(new_spend.category.id)


def test_add_spend_with_minimal_amount(spends_client: SpendsHttpClient, spend_db: SpendDb):
    data = SpendAdd(
        amount=0.01,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY5),
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        currency="RUB",
    )
    new_spend = spends_client.add_spend(data)

    assert new_spend.category.name == Category.TEST_CATEGORY5
    assert new_spend.amount == 0.01

    spends_client.remove_spends(new_spend.id)
    spend_db.delete_category(new_spend.category.id)


def test_remove_spend(spends_client: SpendsHttpClient, spend_db: SpendDb):
    data = SpendAdd(
        amount=10500,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY6),
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        currency="RUB",
    )
    new_spend = spends_client.add_spend(data)

    spends_client.remove_spends(new_spend.id)
    response = spends_client.get_spends()
    assert response == []
    spend_db.delete_category(new_spend.category.id)


@TestData.category(Category.TEST_CATEGORY7)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY7),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_update_spend_description(category, spends, spends_client: SpendsHttpClient, spend_db):
    updated_info = Spend(
        id=spends.id,
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        category=spends.category,
        currency="RUB",
        amount=10500,
        description='for test',
        username=spends.username
    )
    updated_spend = spends_client.update_spend(updated_info)
    assert updated_spend.description == 'for test'
    assert updated_spend.username == spends.username


@TestData.category(Category.TEST_CATEGORY7)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY7),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_update_spend_currency_EUR(category, spends, spends_client: SpendsHttpClient, spend_db):
    updated_info = Spend(
        id=spends.id,
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        category=spends.category,
        currency="EUR",
        amount=10500,
        description='QA.GURU Python Advanced 2',
        username=spends.username
    )
    updated_spend = spends_client.update_spend(updated_info)
    assert updated_spend.currency == 'EUR'
    assert updated_spend.username == spends.username


@TestData.category(Category.TEST_CATEGORY7)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY7),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_update_spend_currency_KZT(category, spends, spends_client: SpendsHttpClient, spend_db):
    updated_info = Spend(
        id=spends.id,
        spendDate=datetime.now().strftime("%Y-%m-%d"),
        category=spends.category,
        currency="KZT",
        amount=10500,
        description='QA.GURU Python Advanced 2',
        username=spends.username
    )
    updated_spend = spends_client.update_spend(updated_info)
    assert updated_spend.currency == 'KZT'
    assert updated_spend.username == spends.username

#
# def test_update_spend_description(spends_client: SpendsHttpClient, spend_db: SpendDb):
#     data = SpendAdd(
#         amount=10500,
#         description="QA.GURU Python Advanced 2",
#         category=CategoryAdd(name=Category.TEST_CATEGORY7),
#         spendDate=datetime.now().strftime("%Y-%m-%d"),
#         currency="RUB",
#     )
#     new_spend = spends_client.add_spend(data)
#     print(new_spend)
#     updated_info = Spend(
#         id=new_spend.id,
#         spendDate=datetime.now().strftime("%Y-%m-%d"),
#         category=new_spend.category,
#         currency="RUB",
#         amount=10500,
#         description='for test',
#         username=new_spend.username
#     )
#
#     updated_spend = spends_client.update_spend(updated_info)
#     print(updated_spend)


# def test_update_spend_description(spends_client: SpendsHttpClient, spend_db: SpendDb):
#     data = SpendAdd(
#         amount=10500,
#         description="QA.GURU Python Advanced 2",
#         category=CategoryAdd(name=Category.TEST_CATEGORY7),
#         spendDate=datetime.now().strftime("%Y-%m-%d"),
#         currency="RUB",
#     )
#     new_spend = spends_client.add_spend(data)
#     print(new_spend)
#     updated_info = Spend(
#         id=new_spend.id,
#         spendDate=datetime.now().strftime("%Y-%m-%d"),
#         category=new_spend.category,
#         currency="RUB",
#         amount=10500,
#         description='for test',
#         username=new_spend.username
#     )
#
#     updated_spend = spends_client.update_spend(updated_info)
#     print(updated_spend)
