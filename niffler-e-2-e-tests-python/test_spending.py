import requests
from selene import browser, have, be


def test_spending_title_exists():
    browser.open('http://frontend.niffler.dc')
    browser.element('input[name=username]').set_value("stas")
    browser.element('input[name=password]').set_value("12345")
    browser.element('button[type=submit]').click()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))


def test_registration_new_user():
    browser.open('http://auth.niffler.dc:9000/login')
    browser.element('[class="form__register"]').click()
    browser.element('input[name=username]').set_value("oleg")
    browser.element('input[name=password]').set_value("12345")
    browser.element('input[name=passwordSubmit]').set_value("12345")
    browser.element('button[type=submit]').click()
    browser.element('.form__paragraph').should(have.text("Congratulations! You've registered!"))


def test_auth_unregistered_user():
    browser.open('http://frontend.niffler.dc')
    browser.element('input[name=username]').set_value("ivan")
    browser.element('input[name=password]').set_value("12345")
    browser.element('button[type=submit]').click()
    browser.element('.form__error-container').should(have.text('Неверные учетные данные пользователя'))


def test_spending_should_be_deleted_after_table_action():
    url = 'http://gateway.niffler.dc:8090/api/spends/add'

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJraWQiOiI1MTQ5MDYwNC04NzIzLTQ2Y2UtOWExMi00ZTUyY2RiODU0MGEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzdGFzIiwiYXVkIjoiY2xpZW50IiwiYXpwIjoiY2xpZW50IiwiYXV0aF90aW1lIjoxNzM5NjEyNjU1LCJpc3MiOiJodHRwOi8vYXV0aC5uaWZmbGVyLmRjOjkwMDAiLCJleHAiOjE3Mzk2MTQ0NTUsImlhdCI6MTczOTYxMjY1NSwianRpIjoiMjFiYzYyZjEtNGVmYi00MzhiLWJmMzktZTE1MzAyOTM5OGJhIiwic2lkIjoiUTlGdy1UaDhHUGota0NsQ1dLY0MwZ3QtZ0ZBejd5RURVdnM4LUZlSllIayJ9.NJEtrZfH5gOa_Z8_I6HySD_JgsIiMVQNfGtPyQVJE-S4OLGK2NGmHkTNn0LNUrRBLTT_dIXyxFRG5U76HWlgynWFda-FBAb8nmMw0mxsdxs8PzMFF58r2j8eFYBFnDLnFuZf4yiyDZGqzRjZDGFIN-8IXr7z5D4Om3hrU4c-Fd0VzYVcnppgk04DySXwBBiAD8oG9z3eueXzHjolKcQvnqE8GCk9-MLouuHgX42DP1OYzNiPDGs1r-d1BnmfXbT4sLnnf8V1LyNuFHj2I3f0QYQAoeK3UTcx-jpfbAW22YIASfY__oqI__4_LFXsp--hajyF77Y7IWRgpnWKbx60og',
        'Origin': 'http://frontend.niffler.dc',
    }

    data = {
        "amount": "108.51",
        "description": "QA.GURU Python Advanced 1",
        "category": {
            "name": "school"
        },
        "spendDate": "2024-08-08T18:39:27.955Z",
        "currency": "RUB"
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print(response.json())
    assert response.status_code == 201

    browser.open('http://frontend.niffler.dc')
    browser.element('input[name=username]').set_value("stas")
    browser.element('input[name=password]').set_value("12345")
    browser.element('button[type=submit]').click()
    browser.element('//span[.="QA.GURU Python Advanced 1"]').should(have.text("QA.GURU Python Advanced 1"))
    browser.element('input[type=checkbox]').click()
    browser.element('button[id=delete]').click()
    browser.all('//button[.="Delete"]').second.click()
    browser.element('//p[.="There are no spendings"]').should(be.visible)


def test_edit_spending():
    url = 'http://gateway.niffler.dc:8090/api/spends/add'

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJraWQiOiI1MTQ5MDYwNC04NzIzLTQ2Y2UtOWExMi00ZTUyY2RiODU0MGEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzdGFzIiwiYXVkIjoiY2xpZW50IiwiYXpwIjoiY2xpZW50IiwiYXV0aF90aW1lIjoxNzM5NjEyNjU1LCJpc3MiOiJodHRwOi8vYXV0aC5uaWZmbGVyLmRjOjkwMDAiLCJleHAiOjE3Mzk2MTQ0NTUsImlhdCI6MTczOTYxMjY1NSwianRpIjoiMjFiYzYyZjEtNGVmYi00MzhiLWJmMzktZTE1MzAyOTM5OGJhIiwic2lkIjoiUTlGdy1UaDhHUGota0NsQ1dLY0MwZ3QtZ0ZBejd5RURVdnM4LUZlSllIayJ9.NJEtrZfH5gOa_Z8_I6HySD_JgsIiMVQNfGtPyQVJE-S4OLGK2NGmHkTNn0LNUrRBLTT_dIXyxFRG5U76HWlgynWFda-FBAb8nmMw0mxsdxs8PzMFF58r2j8eFYBFnDLnFuZf4yiyDZGqzRjZDGFIN-8IXr7z5D4Om3hrU4c-Fd0VzYVcnppgk04DySXwBBiAD8oG9z3eueXzHjolKcQvnqE8GCk9-MLouuHgX42DP1OYzNiPDGs1r-d1BnmfXbT4sLnnf8V1LyNuFHj2I3f0QYQAoeK3UTcx-jpfbAW22YIASfY__oqI__4_LFXsp--hajyF77Y7IWRgpnWKbx60og',
        'Origin': 'http://frontend.niffler.dc',
    }

    data = {
        "amount": "108.51",
        "description": "QA.GURU Python Advanced 1",
        "category": {
            "name": "school"
        },
        "spendDate": "2024-08-08T18:39:27.955Z",
        "currency": "RUB"
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print(response.json())
    assert response.status_code == 201

    browser.open('http://frontend.niffler.dc')
    browser.element('input[name=username]').set_value("stas")
    browser.element('input[name=password]').set_value("12345")
    browser.element('button[type=submit]').click()
    browser.element('button[type=button][aria-label="Edit spending"]').click()
    browser.element('#currency').click()
    browser.element('//span[.="USD"]').click()
    browser.element('#save').click()
    browser.element('.MuiStack-root css-j7qwjs')
    browser.element('//div[.="Spending is edited successfully"]').should(have.text("Spending is edited successfully"))
