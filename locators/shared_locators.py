from selenium.webdriver.common.by import By


class SharedLocators:

    LOADING_ANIMATION = By.XPATH, '//img[@alt="loading animation"]'
    CONTENT_LOADING_PROGRESS = By.XPATH, '//main/div[text()="Загрузка..."]'
    POPUP_OVERLAY = By.XPATH, '//div[contains(@class, "modal_opened")]/div[contains(@class, "Modal_modal_overlay_")]'
    TICK_ANIMATION = By.XPATH, '//img[@alt="tick animation"]'
