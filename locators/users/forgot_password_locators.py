from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    PAGE_HEADING = By.XPATH, '//h2[text()="Восстановление пароля"]'
    TEXT_FIELD = By.XPATH, '//label[text()="Email"]/parent::*/input[@type="text"]'
    FORGOT_PASSWORD_BTN = By.XPATH, '//form/button[text()="Восстановить"]'

    LOGIN_LINK = By.XPATH, '//a[@href="/login"]'




