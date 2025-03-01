from marks import Pages
from pages.auth_page import auth_page


# @pytest.mark.skip
@Pages.main_page
def test_spending_title_exists():
    auth_page.spending_title_exists('History of Spendings')


# @pytest.mark.skip
@Pages.main_page
def test_spending_bottom_title_exists():
    auth_page.spending_bottom_title_exists('There are no spendings')


# @pytest.mark.skip
def test_registration_new_user(envs, app_unregistered_user):
    username, password = app_unregistered_user
    auth_page.open_registration_page(envs.registration_url)
    auth_page.registration_user(username, password)
    auth_page.text_should_be_visible("Congratulations! You've registered!")


# @pytest.mark.skip
def test_registration_new_user_with_forbidden_name(envs, app_forbidden_username):
    username, password = app_forbidden_username
    auth_page.open_registration_page(envs.registration_url)
    auth_page.registration_user(username, password)
    auth_page.text_unsuccessful_registration("Allowed username length should be from 3 to 50 characters")
