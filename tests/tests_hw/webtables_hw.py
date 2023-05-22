from pages.webtables import WebTables
import time


def test_webtables(browser):
    webtables = WebTables(browser)
    webtables.visit()
    assert webtables.btn_add.exist()
    webtables.btn_add.click()
    assert webtables.modal_dialog.exist()
    webtables.btn_submit.click()
    assert webtables.modal_dialog.exist()
    assert webtables.user_form.get_dom_attribute('class') == 'was-validated'

    webtables.first_name.send_keys('tester')
    webtables.last_name.send_keys('testerovich')
    webtables.mail.send_keys('test@test.com')
    webtables.age.send_keys('22')
    webtables.salary.send_keys('100000')
    webtables.department.send_keys('trade')
    webtables.btn_submit.click()
    assert not webtables.modal_dialog.exist()

    assert webtables.stroka.get_text() == 'tester\ntesterovich\n22\ntest@test.com\n100000\ntrade'
    webtables.pencil.click()
    assert webtables.modal_dialog.exist()

    assert webtables.first_name.get_dom_attribute('value') == 'tester'
    assert webtables.last_name.send_keys('testerovich')
    assert webtables.mail.send_keys('test@test.com')
    assert webtables.age.send_keys('22')
    assert webtables.salary.send_keys('100000')
    assert webtables.department.send_keys('trade')