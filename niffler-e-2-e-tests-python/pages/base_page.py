from selene import browser
# from utils.helper import step
import allure


class BasePage:

    # @step
    @allure.step('UI: open browser')
    def open_url(self, url: str) -> None:
        browser.open(url)
