import allure
import pytest

from data.orders_data import test_orders_list
from helper_functions.shared_methods import SharedMethods
from pages.orders.constructor_page import ConstructorPage
from pages.orders.orders_list_page import OrdersListPage
from pages.users.login_page import LoginPage
from pages.users.profile_orders_history_page import ProfileOrdersHistoryPage
from pages.users.user_profile_page import UserProfilePage


class TestOrdersList:

    @allure.title('Клик по ссылке "Лента заказов" ведет на страницу с лентой заказов')
    def test_click_orders_list_link_directs_to_orders_list_page(self, driver):
        SharedMethods.get_main_page(driver)
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_header_orders_list_link()
        orders_list_page.wait_for_orders_list_page_ready()
        assert orders_list_page.is_orders_list_page()
        assert '/feed' in driver.current_url

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

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_exist_on_orders_list_page(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.get_orders_list_page()
        orders_list_page.click_random_order_item()
        orders_list_page.click_order_popup_close_btn()

        assert orders_list_page.is_order_details_popup_hidden()

    @pytest.mark.parametrize(
        'list_for_creating_orders',
        test_orders_list
    )
    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_present_on_orders_list_page(
            self,
            driver,
            user_login_valid_creds: dict[str, str],
            list_for_creating_orders,
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_constructor_page_ready()
        for i in list_for_creating_orders:
            constructor_page.create_order(i[0], i[1])
            constructor_page.click_ingredient_popup_close_btn()

        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_header_user_profile_link()
        user_profile_page.click_order_history_link()
        profile_orders_history_page = ProfileOrdersHistoryPage(driver)
        profile_order_numbers_list = profile_orders_history_page.get_order_numbers_list()
        orders_list_page = OrdersListPage(driver)
        all_order_numbers_list = orders_list_page.get_all_order_numbers_list()
        # Проверить, что нет задвоенных заказов
        assert len(all_order_numbers_list) == len(list(set(all_order_numbers_list)))
        for i in profile_order_numbers_list:
            # проверить, что заказ {i} есть в листе всех заказов
            assert i in all_order_numbers_list

    @pytest.mark.parametrize(
        'list_for_creating_orders',
        test_orders_list
    )
    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_all_time_completed_counter_increases_after_new_order_created(
        self,
        driver,
        user_login_valid_creds: dict[str, str],
        list_for_creating_orders: list[tuple[int, int]],
    ):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.get_orders_list_page()
        # получить начальное значение счетчика
        initial_counter_value = int(
            orders_list_page.get_completed_orders_counter_value('all_time')
        )
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        constructor_page = ConstructorPage(driver)
        constructor_page.create_orders_list(list_for_creating_orders)
        # получить конечное значение счетчика после создания заказов
        orders_list_page.get_orders_list_page()
        actual_counter_value = int(
            orders_list_page.get_completed_orders_counter_value('all_time''all_time')
        )
        assert actual_counter_value - initial_counter_value == len(list_for_creating_orders)

    @pytest.mark.parametrize(
        'list_for_creating_orders',
        test_orders_list
    )
    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_all_time_completed_counter_increases_after_new_order_created(
        self,
        driver,
        user_login_valid_creds: dict[str, str],
        list_for_creating_orders: list[tuple[int, int]],
    ):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.get_orders_list_page()
        # получить начальное значение счетчика
        initial_counter_value = int(
            orders_list_page.get_completed_orders_counter_value('today')
        )
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        constructor_page = ConstructorPage(driver)
        constructor_page.create_orders_list(list_for_creating_orders)
        # получить конечное значение счетчика после создания заказов
        orders_list_page.get_orders_list_page()
        actual_counter_value = int(
            orders_list_page.get_completed_orders_counter_value('today')
        )
        assert actual_counter_value - initial_counter_value == len(list_for_creating_orders)

    @pytest.mark.parametrize(
        'sauce_quantity, filling_quantity',
        test_orders_list[len(test_orders_list) - 1]
    )
    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_just_now_created_order_have_status_in_progress(
        self,
        driver,
        user_login_valid_creds: dict[str, str],
        sauce_quantity: int, filling_quantity: int
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_constructor_page_ready()
        constructor_page.create_order(sauce_quantity, filling_quantity)
        new_order_num = constructor_page.get_new_order_num_from_popup()
        constructor_page.click_new_order_popup_close_btn()
        orders_list_page = OrdersListPage(driver)
        orders_list_page.get_orders_list_page()
        in_progress_order_num = orders_list_page.get_in_progress_order_num()
        assert in_progress_order_num[1:] == new_order_num
