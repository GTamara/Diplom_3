from selenium.webdriver.common.by import By


class LoginPageLocators:

    PAGE_HEADING = By.XPATH, '//h2[text()="Вход"]'
    FORGOT_PASSWORD_LINK = By.CSS_SELECTOR, '//a[href="/forgot-password"]'

    EMAIL_FIELD = By.XPATH, '//label[text()="Email"]/parent::*/input'
    PASSWORD_FIELD = By.XPATH, '//label[text()="Пароль"]/parent::*/input'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'

    # MAIN_PAGE_HEADING = By.XPATH, '//div[contains(@class, "Home_Header")]'
    #
    # IMPORTANT_THINGS_QUESTION = By.CSS_SELECTOR, '#accordion__heading-{}'
    # IMPORTANT_THINGS_ANSWER = By.CSS_SELECTOR, '#accordion__panel-{}'
    #
    # ROAD_MAP_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Home_RoadMap")]//button[text()="Заказать"]'
