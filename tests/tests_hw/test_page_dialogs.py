from pages.modal_dialogs import ModalDialogs
def test_modal_elements(browser):
    dialogs_page = ModalDialogs(browser)
    dialogs_page.visit()
    assert dialogs_page.btns_menu.check_count_elements(5)
