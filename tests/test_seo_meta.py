import time
import pytest
from pages.accordian import Accordian
from pages.demoqa_alerts import Alerts
from pages.demoqa import Demoqa
from pages.browser_tab import BrowserTab

@pytest.mark.parametrize("pages", [Accordian, Alerts, Demoqa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == "viewport"
    assert page.metaView.get_dom_attribute('content') == "width=device-width,initial-scale=1"

