from marks import Pages, TestData
from models.category import CategoryAdd
from pages.category_page import category_page
from utils.helper import check_category_in_db
from faker import Faker

fake = Faker()
name = fake.name()


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
