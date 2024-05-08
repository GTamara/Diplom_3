import allure
from selenium.webdriver.remote.webelement import WebElement

from constants.urls import Urls
from locators.header_locators import HeaderLocators
from locators.orders.constructor_page_locators import ConstructorPageLocators
from locators.orders.orders_list_locators import OrdersListLocators
from locators.shared_locators import SharedLocators
from pages.base_page import BasePage


class OrdersListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.orders_quantity = len(
            self.driver.find_elements(*OrdersListLocators.ORDER_ITEM)
        )

    @allure.step('Открыть страницу с лентой заказов')
    def get_orders_list_page(self):
        self.driver.get(Urls.HOST + Urls.ORDERS_LIST_PATH)
        self.wait_for_orders_list_page_ready()

    @allure.step('Кликнуть ссылку "Лента заказов"')
    def click_header_orders_list_link(self):
        self.click_element(HeaderLocators.ORDERS_LIST_LINK)

    @allure.step('Подождать, пока страница с лентой заказов загрузится')
    def wait_for_orders_list_page_ready(self):
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()
        self.wait_for_all_elements_loaded(OrdersListLocators.ORDER_ITEM_INGREDIENTS_CONTAINER)

    @allure.step('Проверить,что текущая страница - "Лента заказов"')
    def is_orders_list_page(self):
        return self.find_element_with_wait(
                OrdersListLocators.PAGE_HEADING
        ).is_displayed()

    @allure.step('Проверить номер заказа в попапе')
    def check_order_num_within_popup(self, clicked_order_id: str):
        order_id_within_opened_popup = self.get_text_node(OrdersListLocators.ORDER_ID_IN_DETAILS_POPUP)
        return clicked_order_id == order_id_within_opened_popup

    @allure.step('Кликнуть случайный номер заказа и получить его id')
    def click_random_order_item_and_get_its_id(self):
        order_item_to_click_index = self.select_random_item_index(OrdersListLocators.ORDER_ITEM)
        formatted_item_locator = self.format_locator(
            OrdersListLocators.INDEXED_ORDER_ITEM_NUM,
            order_item_to_click_index + 1
        )
        order_id = self.get_text_node(
            formatted_item_locator
        )
        self.click_element(formatted_item_locator)
        return order_id

    @allure.step('Кликнуть случайный заказ в ленте заказов')
    def click_random_order_item(self):
        order_item_to_click_index = self.select_random_item_index(OrdersListLocators.ORDER_ITEM)
        formatted_item_locator = self.format_locator(
            OrdersListLocators.INDEXED_ORDER_ITEM,
            order_item_to_click_index + 1
        )
        self.click_element(formatted_item_locator)

    @allure.step('Подождать, пока элементы попапа станут кликабельными')
    def wait_for_order_details_popup_ready(self):
        # подождать, пока все элементы попапа загрузятся и кнопка закрытия попапа будет доступна для клика
        self.find_element_with_wait(OrdersListLocators.ORDER_DETAILS_POPUP)
        self.find_element_with_wait(OrdersListLocators.ORDER_DETAILS_POPUP_CLOSE_BTN)
        self.wait_for_orders_list_page_ready()

    @allure.step('Кликнуть кнопку "X" в попапе с деталями заказа')
    def click_order_popup_close_btn(self):
        # подождать, пока все элементы попапа загрузятся и кнопка закрытия попапа будет доступна для клика
        self.wait_for_order_details_popup_ready()
        self.find_element_with_wait(OrdersListLocators.ORDER_DETAILS_POPUP_CLOSE_BTN).click()

    @allure.step('Проверить, что попап с деталями заказа скрыт')
    def is_order_details_popup_hidden(self):
        self.wait_until_element_disappears(OrdersListLocators.ORDER_DETAILS_POPUP)
        return True

    @allure.step('Получить список номеров всех заказов из ленты')
    def get_all_order_numbers_list(self) -> list[str]:
        order_nums_list = []
        for i in range(self.orders_quantity):
            formatted_locator = self.format_locator(
                OrdersListLocators.INDEXED_ORDER_ITEM_NUM,
                i + 1
            )
            next_order_num = self.find_element_without_wait(formatted_locator).text
            order_nums_list.append(next_order_num)
        return order_nums_list

    @allure.step('Получить значение каунтера {counter_type}')
    def get_completed_orders_counter_value(self, counter_type: str):
        match counter_type:
            case 'all_time':
                return self.get_text_node(OrdersListLocators.ALL_TIME_COMPLETED_COUNTER)
            case 'today':
                return self.get_text_node(OrdersListLocators.TODAY_COMPLETED_COUNTER)

    @allure.step('Получить номер текущего заказа в прогрессе')
    def get_in_progress_order_num(self):
        return self.find_element_with_wait(OrdersListLocators.IN_PROGRESS_ORDER_NUM).text









