import pytest
from selene import browser, have
from marks import Pages


# @pytest.mark.skip
@Pages.main_page
def test_spending_title_exists():
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))


# @pytest.mark.skip
@Pages.main_page
def test_spending_button_title_exists():
    browser.element('[class="MuiBox-root css-11i3wq6"]').should(have.text('There are no spendings'))


# @pytest.mark.skip
def test_registration_new_user(registration_url, app_unregistered_user):
    username, password = app_unregistered_user
    browser.open(f'{registration_url}/login')
    browser.element('[class="form__register"]').click()
    browser.element('input[name=username]').set_value(username)
    browser.element('input[name=password]').set_value(password)
    browser.element('input[name=passwordSubmit]').set_value(password)
    browser.element('button[type=submit]').click()
    browser.element('.form__paragraph').should(have.text("Congratulations! You've registered!"))


# @pytest.mark.skip
def test_registration_new_user_with_forbidden_name(registration_url, app_forbidden_username):
    username, password = app_forbidden_username
    browser.open(f'{registration_url}/login')
    browser.element('[class="form__register"]').click()
    browser.element('input[name=username]').set_value(username)
    browser.element('input[name=password]').set_value(password)
    browser.element('input[name=passwordSubmit]').set_value(password)
    browser.element('button[type=submit]').click()
    browser.element('.form__error').should(have.text("Allowed username length should be from 3 to 50 characters"))
