from allure_commons.reporter import AllureReporter
from allure_pytest.listener import AllureListener
import allure


@allure.step('DB: check category in db')
def check_category_in_db(spend_db, category_id: str, expected_name: str, expected_username: str,
                         expected_archived: bool):
    category = spend_db.get_user_category(category_id)

    assert category is not None
    assert category.name == expected_name
    assert category.username == expected_username
    assert category.archived == expected_archived


@allure.step('DB: check spend in db')
def check_spend_in_db(spend_db, amount: float, category_name: str, description: str, username: str):
    result = spend_db.get_user_spends(username)

    for item in result:
        spend_sql_obj = item[0]
        assert description == spend_sql_obj.description
        assert username == spend_sql_obj.username
        assert amount == spend_sql_obj.amount
        category_sql_obj = item[1]
        assert category_name == category_sql_obj.name


@allure.step('DB: check category name in db')
def check_category_name_in_db(spend_db, username: str, target_name: str):
    spends = spend_db.get_user_categories(username)
    categories = []
    for category in spends:
        categories.append(category.name)
    assert target_name in categories


def allure_reporter(config) -> AllureReporter:
    listener: AllureListener = next(
        filter(
            lambda plugin: (isinstance(plugin, AllureListener)),
            dict(config.pluginmanager.list_name_plugin()).values(),
        ),
        None,
    )
    return listener.allure_logger
