from components.components import WebElement
from pages.base_page import BasePage

class AutomationPractice(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.btn_submit = WebElement(driver, '#submit')
        self.form = WebElement(driver, '#userForm')
