from pages.base_page import BasePage
from selene import browser, have


class CategoryPage(BasePage):

    def __init__(self):
        self.person_icon = browser.element('[data-testid="PersonIcon"]')
        self.profile = browser.element('//li[.="Profile"]')
        self.category_name = lambda name_category: browser.element(f'//span[.="{name_category}"]').should(
            have.text(f"{name_category}"))

    def category_should_be_exist(self, name_category: str):
        self.person_icon.click()
        self.profile.click()
        self.category_name(name_category).click()


category_page = CategoryPage()
