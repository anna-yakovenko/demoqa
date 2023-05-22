from pages.herokuapp import HeroKuapp
from pages.kuapp_remove_elements import AddElement

def test_koupp_add (browser):
    koup_page = HeroKuapp(browser)
    koup_add = AddElement(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add_element.get_text() == 'Add Element'

    assert koup_add.btn_add_element.get_dom_attribute('onclick') == 'addElement()'


    for i in range(4): #цикл (кол-во итераций)
        koup_add.btn_add_element.click() #нажать на кнопку 4 раза

    assert koup_add.btn_delete.check_count_elements(4)

    #проверка для всех элементов
    for element in koup_add.btn_delete.find_elements():
        assert element.text == 'Delete'

    while koup_add.btn_delete.exist(): #кликнуть на каждую кнопку Delete
        koup_add.btn_delete.click()

    assert not koup_add.btn_delete.exist()




