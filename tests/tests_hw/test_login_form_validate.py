from pages.automation_practice_form import AutomationPractice

def test_login_form_validate(browser):
    test_login_form_validate = AutomationPractice(browser)
    test_login_form_validate.visit()
    assert test_login_form_validate.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert test_login_form_validate.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert test_login_form_validate.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    test_login_form_validate.btn_submit.click_force()
    assert test_login_form_validate.form.get_dom_attribute('class') == 'was-validated'
