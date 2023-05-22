from components.components import WebElement
from pages.base_page import BasePage


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, "div.rt-noData")
        self.btn_delete_row = WebElement(driver, "span[title='Delete']")
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_submit = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.mail = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.stroka = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div')
        self.pencil = WebElement(driver, '#edit-record-4 > svg')


