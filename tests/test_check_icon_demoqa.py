from pages.demoqa import Demoqa

def test_check_icon(browser):
    demoqa = Demoqa(browser)
    demoqa.visit()
    demoqa.icon.click()
    assert demoqa.equal_url()
    assert demoqa.icon.exist()




    #
    # driver = webdriver.Chrome()
    # driver.get('https://demoqa.com/')
    #
    # icon = driver.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    # print('Элемент найден')
    #
    #
