from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.pageData={
            'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')


    # def exist(self):
    #     try:
    #         self.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     self.find_element('#app>header>a').click()
    #
    # def click_on_the_btn_elements(self):
    #     self.find_element('#app > div > div > div.home-body > div > div:nth-child(1)').click()

    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     return False