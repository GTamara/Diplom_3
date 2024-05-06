from selenium.webdriver.common.by import By


class SharedLocators:

    LOADING_ANIMATION = By.XPATH, '//img[@alt="loading animation"]'
    CONTENT_LOADING_PROGRESS = By.XPATH, '//main/div[text()="Загрузка..."]'