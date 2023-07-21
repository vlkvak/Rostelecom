import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://b2c.passport.rt.ru'

@pytest.fixture(scope = "session")
def browser():
    print('Запуск Google Chrome')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    print('Сессия завершена')
    browser.quit()

@pytest.fixture(scope = "session")
def browser_reg_page():

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)
    browser.find_element(By.ID, 'kc-register').click()

    yield browser

    print('Сессия завершена')
    browser.quit()


@pytest.fixture(scope = "session")
def browser_pas_page():

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)
    browser.find_element(By.ID, 'forgot_password').click()

    yield browser

    print('Сесcия завершена')
    browser.quit()