from pages.elements_page import ElementsPage


def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()




# class ElementsPage(BasePage):
#
#     def __init__(self, driver):
#         self.base_url = 'https://demoqa.com/elements'
#         super().__init__(driver, self.base_url)
#
#         self.text_please = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
#         self.text_elements = WebElement(driver, 'div.playgound-header > div')