from pages.base_page import BasePage
from selene import browser, have
from utils.helper import step
import allure


class AuthPage(BasePage):

    def __init__(self):
        self.spending_title = browser.element('[id="spendings"]')
        self.spending_bottom_title = browser.element('[class="MuiBox-root css-11i3wq6"]')
        self.register_form = browser.element('[class="form__register"]')
        self.username = browser.element('input[name=username]')
        self.password = browser.element('input[name=password]')
        self.submit_password_field = browser.element('input[name=passwordSubmit]')
        self.submit_button = browser.element('button[type=submit]')
        self.successful_registration = browser.element('.form__paragraph')
        self.unsuccessful_registration = browser.element('.form__error')

    @step
    @allure.step('UI: open registration page')
    def open_registration_page(self, url: str):
        browser.open(f'{url}/login')

    @step
    @allure.step('UI: check title')
    def spending_title_exists(self, title: str):
        self.spending_title.should(have.text(title))

    @step
    @allure.step('UI: check bottom title')
    def spending_bottom_title_exists(self, title: str):
        self.spending_bottom_title.should(have.text(title))

    @step
    @allure.step('UI: registration user')
    def registration_user(self, username: str, password: str):
        self.register_form.click()
        self.username.set_value(username)
        self.password.set_value(password)
        self.submit_password_field.set_value(password)
        self.submit_button.click()

    @step
    @allure.step('UI: check text')
    def text_should_be_visible(self, text: str):
        self.successful_registration.should(have.text(text))

    @step
    @allure.step('UI: unsuccessful registration')
    def text_unsuccessful_registration(self, text: str):
        self.unsuccessful_registration.should(have.text(text))


auth_page = AuthPage()
