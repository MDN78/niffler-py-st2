from marks import Pages, TestData
from pages.category_page import category_page
from models.category import CategoryAdd
import random
from faker import Faker

fake = Faker()

TEST_CATEGORY = fake.word()
number = random.randint(10, 1000)


@Pages.main_page
@TestData.category(TEST_CATEGORY)
def test_category_exist(category):
    category_page.category_should_be_exist(TEST_CATEGORY)

# # @Pages.profile
# @Pages.main_page
# @TestData.category(TEST_CATEGORY)
# # @TestData.category(CategoryAdd(name=f"New random {number}"))
# def test_edit_category_name(category, spend_db):
#     spend_db.check_category_in_db(category.name)
