from pages.accordian import Accordian
import time

def test_visible_accordian (browser):
    accordian_page = Accordian(browser) #создаем объект по классу (название произвольное)
    accordian_page.visit() #вызов метода
    assert accordian_page.content_p.visible() #проверка на видимость элемента content_p
    accordian_page.section_Heading.click()

    time.sleep(2)
    assert not accordian_page.content_p.visible()


def test_visible_accordian_default (browser):

