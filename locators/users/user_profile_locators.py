from selenium.webdriver.common.by import By


class UserProfileLocators:

    PROFILE_LINK = By.XPATH, '//nav//a[@href="/account/profile"]'
    ORDER_HISTORY_LINK = By.XPATH, '//nav//a[@href="/account/order-history"]'

    USER_DATA_FORM = By.XPATH, '//ul[contains(@class, "_profileList_")]'
    ORDER_HISTORY_LIST = By.XPATH, '//ul[contains(@class, "OrderHistory_profileList_")]'
    ORDER_HISTORY_CONTAINER = By.XPATH, \
        '//div[contains(@class, "Account_contentBox")]'
    LOGOUT_BUTTON = By.XPATH, '//button[text()="Выход"]'

    ANY = By.XPATH, '//*[text()="Загрузка"]'


