from marks import Pages, TestData
from selene import browser, have

TEST_CATEGORY = "vehicle1"


@Pages.main_page
@TestData.category(TEST_CATEGORY)
def test_category_exist(category):
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('//li[.="Profile"]').click()
    browser.element(f'//span[.="{TEST_CATEGORY}"]').should(have.text(f'{TEST_CATEGORY}'))
