from marks import Pages, TestData
from pages.category_page import category_page

import random
from faker import Faker

fake = Faker()

TEST_CATEGORY = fake.word()
number = random.randint(10, 1000)


@Pages.main_page
@TestData.category(TEST_CATEGORY)
def test_category_exist(category):
    category_page.category_should_be_exist(TEST_CATEGORY)

