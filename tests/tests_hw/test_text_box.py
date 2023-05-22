import time
from pages.text_box import TextBox

def test_text_box_page (browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    name = 'Jack Jones'
    text_box_page.full_name.send_keys(name)
    current_address = 'Los Angeles'
    text_box_page.current_address.send_keys(current_address)
    text_box_page.btn_submit.click_force()
    time.sleep(2)
    assert text_box_page.get_text() == 'Name:'+name
    # .get_text() == 'Name:'+name