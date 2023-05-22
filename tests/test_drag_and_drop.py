from pages.droppable import Droppable
from selenium.webdriver import ActionChains
import time
def test_drag_and_drop(browser):
    drop_page = Droppable(browser)
    action_chains = ActionChains(browser)

    drop_page.visit()
    action_chains.drag_and_drop(
        drop_page.drag.find_element(), #element
        drop_page.drop.find_element()  #target
    ).perform()

    time.sleep(1)
    assert drop_page.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(1)

    action_chains.drag_and_drop_by_offset(
        drop_page.drag.find_element(), #element
        -200, 0 #target
    ).perform()

    time.sleep(1)
    assert drop_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')

