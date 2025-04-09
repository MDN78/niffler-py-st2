from marks import Pages, TestData
from pages.category_page import category_page

import pytest
from models.enums import Category

pytestmark = [pytest.mark.allure_label("Category", label_type="epic")]


@Pages.main_page
@TestData.category(Category.TEST_CATEGORY1)
def test_category_exist(category):
    category_page.category_should_be_exist(Category.TEST_CATEGORY1)
