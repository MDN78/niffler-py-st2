from selene import browser
import allure


class BasePage:

    @allure.step('UI: open browser')
    def open_url(self, url: str) -> None:
        browser.open(url)
