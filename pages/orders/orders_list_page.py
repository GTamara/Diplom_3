import random
import time

from selenium.webdriver.remote.webelement import WebElement

from constants.urls import Urls
from locators.header_locators import HeaderLocators
from locators.orders.constructor_page_locators import ConstructorPageLocators
from locators.orders.orders_list_locators import OrdersListLocators
from locators.shared_locators import SharedLocators
from pages.base_page import BasePage


class OrdersListPage(BasePage):

    def get_orders_list_page(self):
        self.driver.get(Urls.HOST + Urls.ORDERS_LIST_PATH)
        self.wait_for_orders_list_page_ready()
        # self.wait_for_loading_animation_completed()

    def click_header_orders_list_link(self):
        self.click_element(HeaderLocators.ORDERS_LIST_LINK)
        # SharedLocators.CONTENT_LOADING_PROGRESS

    def wait_for_orders_list_page_ready(self):
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()
        self.wait_for_all_elements_loaded(OrdersListLocators.ORDER_ITEM_INGREDIENTS_CONTAINER)

    def is_orders_list_page(self):
        return self.find_element_with_wait(
                OrdersListLocators.PAGE_HEADING
        ).is_displayed()

    def check_order_num_within_popup(self, clicked_order_id: str):
        order_id_within_opened_popup = self.get_text_node(OrdersListLocators.ORDER_ID_IN_DETAILS_POPUP)
        return clicked_order_id == order_id_within_opened_popup

    # def select_random_order_item_index(self):
    #     items_list = self.driver.find_elements(*OrdersListLocators.ORDER_ITEM)
    #     index = random.randint(
    #         0, len(items_list) - 1
    #     )
    #     return index

    def click_random_order_item_and_get_its_id(self):
        order_item_to_click_index = self.select_random_item_index(OrdersListLocators.ORDER_ITEM)
        formatted_item_locator = self.format_locator(
            OrdersListLocators.INDEXED_ORDER_ITEM_ID,
            order_item_to_click_index + 1
        )
        order_id = self.get_text_node(
            formatted_item_locator
        )
        self.click_element(formatted_item_locator)
        return order_id

    def click_random_order_item(self):
        order_item_to_click_index = self.select_random_item_index(OrdersListLocators.ORDER_ITEM)
        formatted_item_locator = self.format_locator(
            OrdersListLocators.INDEXED_ORDER_ITEM,
            order_item_to_click_index + 1
        )
        self.click_element(formatted_item_locator)

    def click_order_popup_close_btn(self):
        self.find_element_with_wait(OrdersListLocators.ORDER_DETAILS_POPUP_CLOSE_BTN).click()

    def is_order_details_popup_hidden(self):
        self.wait_until_element_disappears(OrdersListLocators.ORDER_DETAILS_POPUP)
        return True





