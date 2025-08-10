from selene import browser
import allure


class BasePage:
    """Класс взаимодействия с главной страницей приложения"""

    @allure.step('UI: open browser')
    def open_url(self, url: str) -> None:
        browser.open(url)
