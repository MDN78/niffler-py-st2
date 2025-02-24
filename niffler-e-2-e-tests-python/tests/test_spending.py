from selene.core import command
from marks import Pages, TestData
from selene import browser, have, be

from models.spend import SpendAdd
from models.category import CategoryAdd

# Spend, Category,


TEST_CATEGORY = "school"


@Pages.main_page
def test_create_spends(delete_spend):
    browser.element('//a[.="New spending"]').click()
    browser.element('.MuiTypography-root.MuiTypography-h5.css-w1t7b3').should(have.text('Add new spending'))
    browser.element('#amount').set_value('100')
    browser.element('#category').set_value('school')
    browser.element('#description').set_value('Add new spending')
    browser.element('#save').click()
    browser.element('//span[.="Add new spending"]').should(be.visible).should(be.clickable)


@Pages.main_page
def test_create_spend_without_amount():
    browser.element('//a[.="New spending"]').click()
    browser.element('.MuiTypography-root.MuiTypography-h5.css-w1t7b3').should(have.text('Add new spending'))
    browser.element('#category').set_value('school')
    browser.element('#description').set_value('Add new spending')
    browser.element('#save').click()
    browser.element('[class="input__helper-text"]').should(have.text('Amount has to be not less then 0.01'))


@Pages.main_page
def test_create_spend_without_category():
    browser.element('//a[.="New spending"]').click()
    browser.element('.MuiTypography-root.MuiTypography-h5.css-w1t7b3').should(have.text('Add new spending'))
    browser.element('#amount').set_value('100')
    browser.element('#description').set_value('Add new spending')
    browser.element('#save').click()
    browser.element('[class="input__helper-text"]').should(have.text('Please choose category'))


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_delete_spending_after_table_action(category, spends):
    browser.element('//span[.="QA.GURU Python Advanced 1"]').should(have.text("QA.GURU Python Advanced 1"))
    browser.element('input[type=checkbox]').click()
    browser.element('button[id=delete]').click()
    browser.all('//button[.="Delete"]').second.click()
    browser.element('//p[.="There are no spendings"]').should(be.visible)


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_edit_spending_currency_USD(category, spends):
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('#currency').click()
    browser.element('//span[.="USD"]').click()
    browser.element('#save').click()
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_edit_spending_currency_EURO(category, spends):
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('#currency').click()
    browser.element('//span[.="EUR"]').click()
    browser.element('#save').click()
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_edit_spending_currency_KZT(category, spends):
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('#currency').click()
    browser.element('//span[.="KZT"]').click()
    browser.element('#save').click()
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_edit_spending_description(category, spends):
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('[id="description"]').clear().send_keys("New description")
    browser.element('#save').click()
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_edit_spending_category(category, spends):
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('[id="category"]').clear().send_keys("transport")
    browser.element('#save').click()
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends(
    SpendAdd(
        spendDate="2024-08-08T18:39:27.955Z",
        category=CategoryAdd(name=TEST_CATEGORY),
        currency="RUB",
        amount=108.51,
        description="QA.GURU Python Advanced 1",
    )
)
def test_edit_spending_date(category, spends):
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('[name="date"]').perform(command.js.set_value("02/04/2025"))
    browser.element('#save').click()
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))
