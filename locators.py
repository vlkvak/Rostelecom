from selenium.webdriver.common.by import By

class AutoPageLoc:
    """Локаторы для полей формы авторизации"""
    LOCATOR_PHONE_TAB=(By.ID, 't-btn-tab-phone')
    LOCATOR_PHONE_FIELD = (By.XPATH, '//span[contains(text(),"Мобильный телефон")]')
    LOCATOR_PHONE_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_MAIL_TAB =(By.ID,  't-btn-tab-mail')
    LOCATOR_MAIL_FIELD = (By.XPATH, '//span[contains(text(),"Электронная почта")]')
    LOCATOR_MAIL_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//span[contains(text(),"Логин")]')
    LOCATOR_LOGIN_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_LS_FIELD = (By.XPATH, '//span[contains(text(),"Лицевой счёт")]')
    LOCATOR_LS_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_PASSWORD_TAB = (By.ID, 'password')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_ENTER_TAB = (By.ID, 'kc-login')
    LOCATOR_LK_TAB = (By.ID, 'lk-btn')
    LOCATOR_ERROR = (By.ID, 'form-error-message')
    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_REG_TAB = (By.ID, 'kc-register')
#Соцсети - Локаторы для соцсетей
    LOCATOR_VK_TAB = (By.ID, 'oidc_vk')
    LOCATOR_VK_FIELD = (By.XPATH, '//b[text()="ВКонтакте"]')
    LOCATOR_OK_TAB = (By.ID, 'oidc_ok')
    LOCATOR_OK_FIELD = (By.CLASS_NAME, 'ext-widget_h_tx')
    LOCATOR_MAILRU_TAB = (By.ID, 'oidc_mail')
    LOCATOR_MAILRU_FIELD = (By.CLASS_NAME, 'header__logo')
    LOCATOR_YANDEX_TAB = (By.ID, 'card-container__title')
    LOCATOR_YANDEX_FIELD = (By.CSS_SELECTOR,'.passp-add-account-page-title')

class PassPageLoc:
    """Локаторы для полей формы восстановления пароля"""
    LOCATOR_PassRec_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    LOCATOR_PHONE_FIELD = (By.ID, 'username')
    LOCATOR_MAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOCATOR_MAIL_FIELD = (By.ID, 'username')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LOGIN_FIELD = (By.ID, 'username')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_LS_FIELD = (By.ID, 'username')
    LOCATOR_BUTTON_CONTINUE = ( By.ID, 'reset')
    LOCATOR_CODE_FIELD = (By.CLASS_NAME, 'card-container__title')

class RegPageLoc:
    """Локаторы для полей формы регистрации"""
    LOCATOR_REG_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_BUTTON_REGISTRATION = (By.NAME, 'register')
    LOCATOR_REGISTRATION_CODE_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_INPUT_FIELD = (By.XPATH, '//input[contains(@class, "rt-input__input")]')