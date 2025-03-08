import pytest
from marks import Pages, TestData
from selene import browser

from models.spend import SpendAdd
from models.category import CategoryAdd
from pages.spend_page import spend_page

from faker import Faker

pytestmark = [pytest.mark.allure_label("Spendings", label_type="epic")]

fake = Faker()

TEST_CATEGORY = fake.word()
TEST_CATEGORY_2 = fake.country()
TEST_DESCRIPTION = fake.word()


@Pages.main_page
@Pages.delete_spend(TEST_CATEGORY)
def test_create_spends(delete_spend):
    spend_page.create_spend(100, TEST_CATEGORY, TEST_DESCRIPTION)


@Pages.main_page
def test_create_spend_without_amount():
    spend_page.create_spend_without_amount(TEST_CATEGORY, TEST_DESCRIPTION)
    spend_page.page_should_have_text('Amount has to be not less then 0.01')


@Pages.main_page
def test_create_spend_without_category():
    spend_page.create_create_spend_without_category(100, TEST_DESCRIPTION)
    spend_page.page_should_have_text('Please choose category')


@pytest.fixture()
def main_page_late(category, spends, envs):
    browser.open(envs.frontend_url)


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_delete_spending_after_table_action(category, spends):
    spend_page.spending_page_should_have_text("QA.GURU Python Advanced 2")
    spend_page.delete_spend_after_action()


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_edit_spending_currency_USD(category, spends):
    spend_page.edit_spending_currency("USD")
    spend_page.action_should_have_signal_text("Spending is edited successfully")


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_edit_spending_currency_EURO(category, spends):
    spend_page.edit_spending_currency("EUR")
    spend_page.action_should_have_signal_text("Spending is edited successfully")


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_edit_spending_currency_KZT(category, spends):
    spend_page.edit_spending_currency("KZT")
    spend_page.action_should_have_signal_text("Spending is edited successfully")


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_edit_spending_description(category, spends):
    spend_page.edit_description('New description')
    spend_page.description_should_be_edited("Spending is edited successfully")


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_edit_spending_category(category, spends):
    spend_page.edit_category('BlockHouse')
    spend_page.description_should_be_edited("Spending is edited successfully")


@pytest.mark.usefixtures("main_page_late")
@TestData.category(TEST_CATEGORY_2)
@TestData.spends(
    SpendAdd(
        amount=108.51,
        description="QA.GURU Python Advanced 2",
        category=CategoryAdd(name=TEST_CATEGORY_2),
        spendDate="2024-08-08T18:39:27.955Z",
        currency="RUB",
    )
)
def test_edit_spending_date(category, spends):
    spend_page.edit_date("02/02/2025")
    spend_page.edited_date_should_be_visible('Feb 02, 2025')
