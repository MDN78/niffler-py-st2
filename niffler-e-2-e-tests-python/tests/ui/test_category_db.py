import os

import pytest
from marks import Pages, TestData
from models.category import CategoryAdd
from pages.category_page import category_page
from pages.spend_page import spend_page
from utils.helper import check_category_in_db, check_spend_in_db, check_category_name_in_db
from models.enums import Information, Category

pytestmark = [pytest.mark.allure_label("Category DB", label_type="epic")]


@Pages.profile_page
@TestData.category_db(CategoryAdd(
    name=f"Test category name {Information.NAME}"
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
    name=f"Test category name {Information.NAME}"
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
    spend_page.create_spend(Information.AMOUNT, Category.TEST_CATEGORY1, Information.DESCRIPTION)
    check_spend_in_db(spend_db, Information.AMOUNT, Category.TEST_CATEGORY1, Information.DESCRIPTION, user_name)
    spend_page.delete_spend(Category.TEST_CATEGORY1)


@Pages.profile_page
def test_check_category_name_changes_in_database(spend_db):
    user_name = os.getenv("TEST_USERNAME")
    category_page.create_category(Category.TEST_CATEGORY2)
    category_page.refresh_page()
    check_category_name_in_db(spend_db, user_name, Category.TEST_CATEGORY2)
