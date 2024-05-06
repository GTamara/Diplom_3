from selenium.webdriver.common.by import By


class OrdersListLocators:

    PAGE_HEADING = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDERS_LIST_CONTAINER = By.XPATH, '//div[contains(@class, "OrderFeed_contentBox_")]'
    ORDER_ITEM_INGREDIENTS_CONTAINER = \
        By.XPATH, '//ul[contains(@class, "OrderFeed_list")]//div[contains(@class, "OrderHistory_dataBox")]'
    
    ORDER_ITEM = \
        By.XPATH, '//ul[contains(@class, "OrderFeed_list")]//li[contains(@class, "OrderHistory_listItem_")]'
    INDEXED_ORDER_ITEM = \
        By.XPATH, ORDER_ITEM[1] + '[{}]'
    INDEXED_ORDER_ITEM_ID = By.XPATH, '//li[contains(@class, "OrderHistory_listItem_")][{}]//p[contains(@class, "text_type_digits-default")]'
    ORDER_DETAILS_POPUP = By.XPATH, '//section[contains(@class, "Modal_modal_opened_")]'
    ORDER_ID_IN_DETAILS_POPUP = \
        By.XPATH, '//section[contains(@class, "Modal_modal_opened_")]//div[contains(@class, "Modal_orderBox_")]/p[contains(@class, "text_type_digits-default")]'
    ORDER_DETAILS_POPUP_CLOSE_BTN = By.XPATH, '//section[contains(@class, "Modal_modal_opened_")]//button[contains(@class, "Modal_modal__close_")]'



