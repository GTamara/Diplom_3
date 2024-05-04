from selenium.webdriver.common.by import By


class OrdersListLocators:

    PAGE_HEADING = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDERS_LIST_CONTAINER = By.XPATH, '//div[contains(@class, "OrderFeed_contentBox_")]'
