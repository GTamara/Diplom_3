import time

import allure

from helper_functions.shared_methods import SharedMethods
from pages.orders.orders_list_page import OrdersListPage


class TestOrdersList:

    def test_click_orders_list_link_directs_to_orders_list_page(self, driver):
        SharedMethods.get_main_page(driver)
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_header_orders_list_link()
        orders_list_page.wait_for_orders_list_page_ready()
        assert orders_list_page.is_orders_list_page()

    @allure.title('Лента заказов. Клик по заказу открывает попап с деталями заказа')
    def test_click_order_item_opens_popup_with_details(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.get_orders_list_page()
        clicked_order_id = orders_list_page.click_random_order_item_and_get_its_id()
        assert orders_list_page.check_order_num_within_popup(clicked_order_id)

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_click_order_popup_close_btn_hides_popup(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.get_orders_list_page()
        orders_list_page.click_random_order_item()
        orders_list_page.click_order_popup_close_btn()

        assert orders_list_page.is_order_details_popup_hidden()


