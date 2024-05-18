import allure
import pytest

from constants.urls import Urls
from data.orders_data import test_orders_list
from pages.header_page import HeaderPage
from pages.orders.constructor_page import ConstructorPage
from pages.users.login_page import LoginPage


class TestConstructorPage:

    @allure.title('Клик по ссылке "Конструктор" ведет на страницу оформления заказа')
    def test_click_header_constructor_link_directs_to_constructor_page(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.get_page_by_url(Urls.HOST)
        constructor_page.wait_for_loading_animation_completed()
        HeaderPage(driver).click_header_constructor_link()
        constructor_page.wait_for_loading_animation_completed()
        constructor_page.wait_for_constructor_page_ready()
        current_url = constructor_page.get_current_url()
        assert constructor_page.is_constructor_page()
        assert current_url[:-1] == Urls.HOST

    @pytest.mark.parametrize(
        'ingredient_type_index',
        [
            1, # bun category
            2, # sauce category
            3, # filling category
        ]
    )
    @allure.title('Конструктор заказов, лента ингредиентов. Клик по ингредиенту открывает попап с деталями ингредиента')
    def test_click_order_item_opens_popup_with_details(self, driver, ingredient_type_index: int):
        constructor_page = ConstructorPage(driver)
        constructor_page.get_constructor_page()
        clicked_ingredient_title = constructor_page.click_random_ingredient_item_and_get_its_title(ingredient_type_index)
        assert constructor_page.check_ingredient_title_within_popup(clicked_ingredient_title)

    @pytest.mark.parametrize(
        'ingredient_type_index',
        [
            1, # bun category
            2, # sauce category
            3, # filling category
        ]
    )
    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_click_order_popup_close_btn_hides_popup(self, driver, ingredient_type_index: int):
        constructor_page = ConstructorPage(driver)
        constructor_page.get_constructor_page()
        constructor_page.click_ingredient_item(ingredient_type_index)
        constructor_page.click_ingredient_popup_close_btn()

        assert constructor_page.is_ingredient_popup_hidden()

    @pytest.mark.parametrize(
        'ingredient_type_index, result',
        [
            (1, 2),  # bun category, counter value
            (2, 1),  # sauce category, counter value
            (3, 1),  # filling category, counter value
        ]
    )
    @allure.title('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_counter_increases_after_ingredient_was_added(
        self,
        driver,
        ingredient_type_index: int,
        result: int
    ):
        constructor_page = ConstructorPage(driver)
        constructor_page.get_constructor_page()
        constructor_page.add_ingredient_to_bucket(ingredient_type_index)
        assert constructor_page.get_selected_ingredient_counter_value() == result

    @pytest.mark.parametrize(
        'sauce_quantity, filling_quantity', # buns_quantity = 1 for all cases
        test_orders_list[len(test_orders_list) - 1]
    )
    @allure.title('залогиненный пользователь может оформить заказ')
    def test_create_order_with_authorized_user_success(
        self,
        driver,
        user_login_valid_creds: dict[str, str],
        sauce_quantity: int, filling_quantity: int,
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_constructor_page_ready()
        constructor_page.create_order(
            sauce_quantity,
            filling_quantity
        )
        constructor_page.wait_for_loading_animation_completed()

        assert constructor_page.get_new_order_num_from_popup().isdigit()
