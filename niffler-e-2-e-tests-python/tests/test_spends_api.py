import pytest

from clients.spends_client import SpendsHttpClient
from fixtures.auth_fixtures import auth_api_token
from models.category import CategoryAdd
from databases.spend_db import SpendDb
from models.enums import Category
from models.spend import SpendAdd

pytestmark = [pytest.mark.allure_label("Spends API", label_type="epic")]


@pytest.mark.skip
def test_auth(auth_api_token):
    print(auth_api_token)


def test_add_spend(spends_client: SpendsHttpClient, spend_db: SpendDb):
    data = SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=Category.TEST_CATEGORY5),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
    new_spend = spends_client.add_spend(data)

    assert new_spend.category.name == Category.TEST_CATEGORY5
    assert new_spend.description == data.description

    spends_client.remove_spends(new_spend.id)
    spend_db.delete_category(new_spend.category.id)
