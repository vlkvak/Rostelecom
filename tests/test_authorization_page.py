from locators import *
from settings import *
from selenium.common.exceptions import NoSuchElementException

#Тест кейсы с 1 по 15 пункт тест кейса Ростелеком (см. README)

#RTA-001
def test_athorization_get_page(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_TAB).click()
    assert browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD).text == 'Мобильный телефон'
    print("\nПереход на  - успешно")
    print("\nTest RTA-001 complete")

#RTA-002, RTA-003
def test_button_transion(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' - успешно" )

    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' - успешно" )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD ).text == 'Лицевой счёт'
    print( "\nПереход на 'Лицевой счёт' - успешно")

    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_TAB).click()
    assert browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD).text == 'Мобильный телефон'
    print("\nПереход на 'Tелефон' - успешно")


def test_button_phone(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( fake_phone )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()

    assert browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD ).text == 'Мобильный телефон'
    print( "\nПереход на 'Телефон' с 'Почта' - успешно " )


def test_button_mail(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' с 'Телефон' - успешно " )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' с 'Лицевой счет' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' с 'Логин' произошел " )


def test_button_login(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' с 'Телефон' - успешно " )

    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' с 'Почта' - успешно " )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' с 'Лицевой счет' - успешно " )


def test_button_ls(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( invalid_ls )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD ).text == 'Лицевой счёт'
    print( "\nПереход на 'Лицевой счет' с 'Почта' - успешно " )
    print("\nTests RTA-002 and RTA-003 complete")

#Позитивные проверки - успешный пользовательский сценарий

#RTA-004
def test_authorization_phone(browser):
     browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(valid_phone)
     browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
     browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
     browser.implicitly_wait(5)
     try:
         assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
     except NoSuchElementException:\
         print("\nАвторизация по Телефону - Успешно")
     print("\nTest RTA-004 complete")

#RTA-005
def test_authorization_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(valid_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по электронной почте - Успешно")
    print("\nTest RTA-005 complete")

#RTA-006
def test_authorization_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(valid_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    try:
        assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    except NoSuchElementException:\
        print("\nАвторизация по логину - Успешно ")
    print("\nTest RTA-006 complete")

# ???невозможно провести проверку т.к. нет зарегистрированного валидного логина

#RTA-007
def test_authorization_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(valid_ls)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по лицевому счету - Успешно")
    print("\nTest RTA-007 complete")

#RTA-008
def test_authorization_vk(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_VK_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_VK_FIELD).text == 'VK'
    print("\nАвторизация по VK прошла успешно")
    print("\nTest RTA-008 complete - 1")


def test_authorization_ok(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_OK_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_OK_FIELD).text == 'Одноклассники'
    print("\nАвторизация по Одноклассники прошла успешно")
    print("\nTest RTA-008 complete - 2")

def test_authorization_myworldmailru(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAILRU_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_MAILRU_FIELD).text == 'Мой Мир@Mail.ru'
    print("\nАвторизация по Мой Мир@Mail.ru прошла успешно")
    print("\nTest RTA-008 complete - 3")

def test_authorization_ya(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_YANDEX_TAB).click()
    browser.implicitly_wait(5)
    browser.find_element(*AutoPageLoc.LOCATOR_YANDEX_TAB).click()

    assert browser.find_element(*AutoPageLoc.LOCATOR_YANDEX_FIELD).text == 'Войдите с Яндекс ID'
    print("\nАвторизация по Yandex прошла успешно ")
    print ("\nTest RTA-008 complete - 4")

#Негативные проверки

#RTA-009
def test_authorization_empty_phone(browser):  # Тест не проходит из-за капчи
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_phone_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_phone_mess == 'Введите номер телефона'

    print("\nПодсказка под полем Номер - 'Введите номер телефона'")
    print("\nTest RTA-009 complete")


#RTA-010
def test_authorization_empty_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_mail_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_mail_mess == 'Введите адрес, указанный при регистрации'

    print("\nПодсказка под полем email - 'Введите адрес, указанный при регистрации'")
    print("\nTest RTA-010 complete")

#RTA-011
def test_authorization_empty_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_login_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_login_mess == 'Введите логин, указанный при регистрации'

    print("\nПодсказка под полем email - 'Введите логин, указанный при регистрации'")
    print("\nTest RTA-011 complete")

#RTA-012
def test_authorization_empty_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_ls_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_ls_mess == 'Введите номер вашего лицевого счета'

    print("\nПодсказка под полем лицевой счет - 'Введите номер вашего лицевого счета'")
    print("\nTest RTA-012 complete")

#RTA-013
def test_authorisation_invalid_password(browser):  # Тест не проходит из-за наличия капчи
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(valid_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\nПодсказка - 'Неверный логин или пароль'")
    print("\nTest RTA-013 complete")


#RTA-014
def test_authorization_invalid_login(browser): # Тест не проходит из-за капчи
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(fake_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\nПодсказка - 'Неверный логин или пароль'")
    print("\nTest RTA-014 complete")


#RTA-015
def test_autрorisation_invalid_ls(browser):  # Тест не проходит из-за капчи
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(invalid_ls)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\nПодсказка - 'Неверный логин или пароль'")
    print("\nTest RTA-015 complete")
