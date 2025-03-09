import os

import pytest
import random
from marks import Pages, TestData
from models.category import CategoryAdd
from pages.category_page import category_page
from pages.spend_page import spend_page
from utils.helper import check_category_in_db, check_spend_in_db
from faker import Faker

pytestmark = [pytest.mark.allure_label("Category DB", label_type="epic")]

fake = Faker()
name = fake.name()
TEST_CATEGORY = fake.word()
TEST_CATEGORY_2 = fake.word()
TEST_DESCRIPTION = fake.word()
TEST_AMOUNT = random.randint(10, 1000)


@Pages.profile_page
@TestData.category_db(CategoryAdd(
    name=f"Test category name {name}"
))
def test_edit_name_category(category_db, spend_db) -> None:
    check_category_in_db(
        spend_db,
        category_db.id,
        category_db.name,
        category_db.username,
        category_db.archived)

    old_name = category_db.name
    new_name = f"{category_db.name} junior"

    category_page.edit_category_name(old_name, new_name)
    category_page.should_be_category_name(new_name)


@Pages.profile_page
@TestData.category_db(CategoryAdd(
    name=f"Test category name {name}"
))
def test_archived_category(category_db, spend_db) -> None:
    check_category_in_db(
        spend_db,
        category_db.id,
        category_db.name,
        category_db.username,
        category_db.archived)

    category_page.archive_category(category_db.name)
    category_page.check_archived_category(category_db.name)


@Pages.main_page
def test_created_spend_exist_in_database(spend_db):
    user_name = os.getenv("TEST_USERNAME")
    spend_page.create_spend(TEST_AMOUNT, TEST_CATEGORY, TEST_DESCRIPTION)
    check_spend_in_db(spend_db, TEST_AMOUNT, TEST_CATEGORY, TEST_DESCRIPTION, user_name)
    spend_page.delete_spend(TEST_CATEGORY)
