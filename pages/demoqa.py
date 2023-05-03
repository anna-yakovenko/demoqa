from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
class Demoqa(BasePage):

    def exist_icon(self):
        try:
            self.find_element('#app>header>a')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        self.find_element('#app>header>a').click()

    def equal_url(self):
        if self.get_url() == 'https://demoqa.com/':
            return True
        return False