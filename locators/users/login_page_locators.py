from selenium.webdriver.common.by import By


class LoginPageLocators:

    PAGE_HEADING = By.XPATH, '//h2[text()="Вход"]'
    FORGOT_PASSWORD_LINK = By.XPATH, '//a[@href="/forgot-password"]'

    EMAIL_FIELD = By.XPATH, '//label[text()="Email"]/parent::*/input'
    PASSWORD_FIELD = By.XPATH, '//label[text()="Пароль"]/parent::*/input'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
