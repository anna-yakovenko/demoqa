from pages.webtables import WebTables
import time
from pages.base_page import BasePage

def test_webtables(browser):
    #проверка блока no rows found
    webtables = WebTables(browser)
    webtables.visit()
    assert not webtables.no_data.exist()

    #удаляем все записи
    while webtables.btn_delete_row.exist():
        webtables.btn_delete_row.click()

    time.sleep(3)
    assert webtables.no_data.exist()

    assert webtables.btn_add.exist()

    assert not webtables.modal_dialog.exist()
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

    # assert webtables.first_name.get_text() == 'tester'
    assert webtables.stroka.get_text() == 'tester\ntesterovich\ntest@test.com\n22\n100000\ntrade'






