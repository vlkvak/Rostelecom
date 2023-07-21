from locators import *
from settings import *

#Тест кейсы на валидацию полей страницы восстановления пароля
#Проверки проводятся с 16 по 17 пункт тест кейса Ростелеком (см. README)

#RTA-016
def test_password_change_page(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_FORGOT_PASSWORD).click()
    assert browser.find_element(*PassPageLoc.LOCATOR_PassRec_FIELD).text == 'Восстановление пароля'
    print("\nПереход на страницу восстановления прошел успешно")
    print("\nTest RTA-016 complete")

#Позитивные проверки - успешный пользовательский сценарий

#RTA-017
#Проходить только вручную, т.к. капча не отключена
def test_password_change_phone(browser_pas_page):
    browser_pas_page.find_element(*PassPageLoc.LOCATOR_PHONE_FIELD).send_keys(valid_phone)
    browser_pas_page.find_element(*PassPageLoc.LOCATOR_BUTTON_CONTINUE).click()

    assert browser_pas_page.find_element(*PassPageLoc.LOCATOR_CODE_FIELD).text == 'Восстановление пароля'
    print("\nКод подтверждения отправлен на номер мобильного телефона")

def test_password_change_mail(browser_pas_page):
    browser_pas_page.find_element(*PassPageLoc.LOCATOR_MAIL_FIELD).click()
    browser_pas_page.find_element(*PassPageLoc.LOCATOR_MAIL_FIELD).send_keys(valid_email)
    browser_pas_page.find_element(*PassPageLoc.LOCATOR_BUTTON_CONTINUE).click()

    assert browser.find_element(*PassPageLoc.LOCATOR_CODE_FIELD).text == 'Восстановление пароля'
    print("\n Код подтверждения отправлен на адрес электронной почты")
    print("\nTest RTA-017 complete")