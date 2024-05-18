from selenium.webdriver.common.by import By


class OrdersProfileHistoryLocators:

    ORDER_ITEM = By.XPATH, '//li[contains(@class, "OrderHistory_listItem_")]'
    INDEXED_ORDER_ITEM = By.XPATH, '//li[contains(@class, "OrderHistory_listItem_")][{}]'
    INDEXED_ORDERS_ITEM_ORDER_NUMBER = \
        By.XPATH, INDEXED_ORDER_ITEM[1] + '/div/p[contains(@class, "text_type_digits")]'
    INDEXED_ORDER_ITEM_INGREDIENT_ITEM = \
        By.XPATH, INDEXED_ORDER_ITEM[1] + '//li[contains(@class, "OrderHistory_ingItem_")]'


