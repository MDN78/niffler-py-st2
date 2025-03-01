from pages.base_page import BasePage
from selene import browser, have, be, command


class SpendPage(BasePage):
    def __init__(self):
        self.new_spend_button = browser.element('//a[.="New spending"]')
        self.title_new_spending_list = browser.element('.MuiTypography-root.MuiTypography-h5.css-w1t7b3')
        self.spending = browser.element('#spendings')
        self.amount = browser.element('#amount')
        self.category = browser.element('#category')
        self.description = browser.element('#description')
        self.button_add_spending = browser.element('#save')
        self.category_name = lambda name_category: browser.element('#spendings tbody').should(
            have.text(f"{name_category}"))
        self.delete_button = browser.element('#delete')
        self.delete_button_approve = browser.element("//div[@role='dialog']//button[contains(text(), 'Delete')]")
        self.text_attention = browser.element('[class="input__helper-text"]')
        self.spending_body = browser.element('#spendings tbody')
        self.edit_spending = browser.element('button[type=button][aria-label="Edit spending"]')
        self.currency = browser.element('#currency')
        self.select_currency = lambda currency: browser.element(f'//span[.="{currency}"]')
        self.button_save = browser.element('#save')
        self.successful_change = browser.element('//div[.="Spending is edited successfully"]')
        self.description_field = browser.element('[id="description"]')
        self.description_successful_editing_text = browser.element('//div[.="Spending is edited successfully"]')
        self.spending_tb = browser.element('#spendings tbody .MuiCheckbox-root')

        # browser.element('[id="category"]').clear().send_keys("transport")
        # browser.element('#save').click()
        # browser.element('//div[.="Spending is edited successfully"]').should(
        #     have.text("Spending is edited successfully"))

    def create_spend(self, amount: int, test_category: str, description: str):
        self.new_spend_button.click()
        self.title_new_spending_list.should(have.text('Add new spending'))
        self.amount.set_value(amount)
        self.category.set_value(f'{test_category}')
        self.description.set_value(f'{description}')
        self.button_add_spending.click()

    def create_spend_without_amount(self, test_category: str, description: str):
        self.new_spend_button.click()
        self.title_new_spending_list.should(have.text('Add new spending'))
        self.category.set_value(f'{test_category}')
        self.description.set_value(f'{description}')
        self.button_add_spending.click()

    def page_should_have_text(self, text: str):
        self.text_attention.should(have.text(text))

    def create_create_spend_without_category(self, amount: int, description: str):
        self.new_spend_button.click()
        self.title_new_spending_list.should(have.text('Add new spending'))
        self.amount.set_value(amount)
        self.description.set_value(f'{description}')
        self.button_add_spending.click()

    def edit_description(self, description: str):
        self.edit_spending.click()
        self.description_field.clear().send_keys(description)
        self.button_save.click()

    def edit_spending_currency(self, currency: str):
        self.edit_spending.click()
        self.currency.click()
        self.select_currency(currency).click()
        self.button_save.click()

    def edit_category(self, category: str):
        self.edit_spending.click()
        self.category.clear().send_keys(category)
        self.button_add_spending.click()

    def description_should_be_edited(self, message: str):
        self.description_successful_editing_text.should(have.text(message))

    def action_should_have_signal_text(self, text: str):
        self.successful_change.should(have.text(text))

    def spending_page_should_have_text(self, description: str):
        self.spending_body.should(have.text(description))

    def delete_spend_after_action(self):
        self.spending_tb.perform(command.js.scroll_into_view).click()
        self.delete_button.click()
        self.delete_button_approve.click()
        self.spending.should(have.text("There are no spendings"))

    def delete_spend(self, name_category: str):
        self.category_name(name_category).click()
        self.delete_button.click()
        self.delete_button_approve.click()


spend_page = SpendPage()
