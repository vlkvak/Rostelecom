from locators import *
from settings import *


#Тест кейсы на валидацию полей страницы регистрации
#Проверки проводятся с 18 по 21 пункт тест кейса Ростелеком (см. README)

#RTA-018
def test_registr_page(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_REG_TAB).click()

    assert browser.find_element(*RegPageLoc.LOCATOR_REG_FIELD).text == 'Регистрация'
    print("\nПереход на страницу регистрации прошел успешно")
    print("\nTest RTA-0018 complete")

#Позитивные проверки - успешный пользовательский сценарий

#RTA-019
def test_registration_newreg(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()

    assert browser_reg_page.find_element(*RegPageLoc.LOCATOR_REGISTRATION_CODE_FIELD).text == 'Подтверждение email'
    print("\nПереход на страницу получения кода подтверждения прошел успешно ")
    print("\nTest RTA-0019 complete")

#Негативные проверки

#RTA-020
def test_registration_invalid_engname(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname_en)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]

    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\nПоявилось сообщение об ошибке ввода имени")
    print("\nTest RTA-0020 complete - 1")

def test_registration_invalid_name1rus(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys('Ж')
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]

    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\nПоявилось сообщение об ошибке ввода имени")
    print("\nTest RTA-0020 complete - 2")

def test_registration_namerus31(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys("унарголшариранвфуйцпаристмрневдм")
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]

    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\nПоявилось сообщение об ошибке ввода имени")
    print("\nTest RTA-0020 complete - 3")

def test_registration_invalid_englastname(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname_en)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    last_name_error_message = error_message[0]

    assert last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print ("\n last_name_error_message.text")
    print("\nПоявилось сообщение об ошибке ввода фамилии ")
    print("\nTest RTA-0020 complete - 4")

def test_registration_invalid_lastname1(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys('ь')
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    last_name_error_message = error_message[0]

    assert last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\nПоявилось сообщение об ошибке ввода фамилии ")
    print("\nTest RTA-0020 complete - 5")

def test_registration_invalid_lastname31(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys('оаРОАШившвоврвгуЙЦукшкияЧавкхзж')
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    lastname_error_message = error_message[0]

    assert lastname_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\nПоявилось сообщение об ошибке ввода фамилии ")
    print("\nTest RTA-0020 complete - 6")

def test_registration_invalid_mail(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys('wjeoddk.com')
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    mail_error_message = error_message[0]

    assert  mail_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или email в формате example@email.ru'

    print("\nПоявилось сообщение об ошибке ввода адреса электронной почты или номера мобильного телефона ")
    print("\nTest RTA-0020 complete - 7")


def test_registration_invalid_pass7number(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('0000000')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Длина пароля должна быть не менее 8 символов'

    print("\nПоявилось сообщение об ошибке в выборе пароля")
    print("\nTest RTA-0020 complete - 8")

def test_registration_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('Ёээё1234')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать только латинские буквы'

    print("\nПоявилось сообщение об ошибке в выборе пароля")
    print("\nTest RTA-0020 complete - 9")

def test_registration_invalid_pass(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('12345678')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'

    print("\nПоявилось сообщение об ошибке в выборе пароля")
    print("\nTest RTA-0020 complete - 10")


def test_registration_invalid_pass_A(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('01234567RRR')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну строчную букву'

    print("\nПоявилось сообщение об ошибке в выборе пароля")
    print("\nTest RTA-0020 complete - 11")

def test_registration_invalid_pass_a(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('01234567rrr')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'

    print("\nПоявилось сообщение об ошибке в выборе пароля")
    print("\nTest RTA-0020 complete - 12")


#RTA-0021
def test_registration_two_pass(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys('Aa123456789')
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароли не совпадают'

    print("\n Появилось сообщение об ошибке подтверждения пароля ")
    print("\nTest RTA-0021 complete")

#RTA-022
def test_registration_alreadyreg(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(valid_firstname)
    input_field[1].send_keys(valid_lastname)
    input_field[3].send_keys(valid_email)
    input_field[4].send_keys(valid_pass)
    input_field[5].send_keys(valid_pass)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()

    assert browser_reg_page.find_element(*RegPageLoc.LOCATOR_REGISTRATION_CODE_FIELD).text == 'Регистрация'
    print("\nОшибка - пользователь уже зарегистрирован ")
    print("\nTest RTA-0022 complete")