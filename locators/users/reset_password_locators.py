from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    PAGE_HEADING = By.XPATH, '//h2[text()="Восстановление пароля"]'
    TEXT_FIELD_1 = By.XPATH, '//input[@name="Введите новый пароль"]'
    SHOW_HIDE_PASSWORD_BTN = \
        By.XPATH, '//input[@name="Введите новый пароль"]/parent::*/div[contains(@class, "input__icon-action")]'
    RESET_PASSWORD_BTN = By.XPATH, '//form/button[text()="Сохранить"]'
    LOGIN_LINK = By.XPATH, '//a[@href="/login"]'

