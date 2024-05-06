from selenium.webdriver.common.by import By


class HeaderLocators:

    LOGO = By.XPATH, '//div[contains(@class, "_logo_")]/a[@href="/"]/*[name()="svg"]'
    USER_PROFILE_LINK = By.XPATH, '//header//a[@href="/account"]'
    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]' # /parent::a[@href="/"]/p
    ORDERS_LIST_LINK = By.XPATH, '//a[@href="/feed"]/*[name()="svg"]'
