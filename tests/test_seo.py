import time

import pytest
from pages.accordian import Accordian
from pages.demoqa_alerts import Alerts
from pages.demoqa import Demoqa
from pages.browser_tab import BrowserTab


def test_check_title_demo(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    assert browser.title == demo_qa_page.pageData['title']

@pytest.mark.parametrize("pages", [Accordian, Alerts, Demoqa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']
