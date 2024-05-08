import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.constants import Constants
from constants.urls import Urls
from locators.orders.constructor_page_locators import ConstructorPageLocators
from locators.header_locators import HeaderLocators
from locators.shared_locators import SharedLocators
from locators.orders.constructor_page_locators import ConstructorPageLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.selected_ingredient_locator = {
            'locator': '',
            'category': -1,
            'index': -1,
        }

    @allure.step('Открыть главную страницу')
    def get_constructor_page(self):
        self.driver.get(Urls.HOST)
        self.wait_for_constructor_page_ready()

    def click_constructor_header_link(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_LINK)

    def is_constructor_page(self):
        return self.find_element_with_wait(ConstructorPageLocators.PAGE_HEADING).is_displayed()

    def wait_for_constructor_page_ready(self):
        self.wait_for_all_elements_loaded(ConstructorPageLocators.BURGER_INGREDIENT_IMAGE)

    def wait_for_popup_ready(self):
        # подождать, пока все элементы попапа загрузятся и кнопка закрытия попапа будет доступна для клика
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.invisibility_of_element(
                SharedLocators.POPUP_OVERLAY
            )
        )
        self.find_element_with_wait(ConstructorPageLocators.POPUP_CLOSE_BTN)

    def get_random_ingredient(self, category_index: int):
        specified_category_ingredient_item_selector = \
            self.format_locator(
                ConstructorPageLocators.SPECIFIED_CATEGORY_INGREDIENT_ITEM,
                category_index
            )
        item_to_click_index = self.select_random_item_index(specified_category_ingredient_item_selector)
        formatted_item_locator = self.format_locator(
            ConstructorPageLocators.SPECIFIED_CATEGORY_INDEXED_INGREDIENT_ITEM,
            [
                category_index, item_to_click_index + 1
            ]
        )
        return {
            'locator': formatted_item_locator,
            'category': category_index,
            'index': item_to_click_index,
        }

    def click_random_ingredient_item_and_get_its_title(self, category_index: int):
        ingredient = self.get_random_ingredient(category_index)
        formatted_item_title_locator = self.format_locator(
            ConstructorPageLocators.SPECIFIED_CATEGORY_INDEXED_INGREDIENT_ITEM_TITLE,
            [
                category_index, ingredient['index'] + 1
            ]
        )
        ingredient_title = self.get_text_node(
            formatted_item_title_locator
        )
        self.click_element(ingredient['locator'])
        return ingredient_title

    def check_ingredient_title_within_popup(self, clicked_ingredient_title: str):
        ingredient_title_within_opened_popup = self.get_text_node(ConstructorPageLocators.INGREDIENT_TITLE_WITHIN_POPUP)
        return ingredient_title_within_opened_popup == clicked_ingredient_title

    def click_ingredient_item(self, category_index: int):
        formatted_item_locator = self.get_random_ingredient(category_index)['locator']
        self.click_element(formatted_item_locator)

    def click_ingredient_popup_close_btn(self):
        self.wait_for_popup_ready()
        self.click_element_containing_svg_icon(ConstructorPageLocators.POPUP_CLOSE_BTN)

    def click_new_order_popup_close_btn(self):
        self.wait_for_popup_ready()

        self.click_element_containing_svg_icon(ConstructorPageLocators.POPUP_CLOSE_BTN)

    def is_ingredient_popup_hidden(self):
        self.wait_until_element_disappears(ConstructorPageLocators.POPUP)
        return True

    def add_ingredient_to_bucket(self, category_index: int):
        self.selected_ingredient_locator = self.get_random_ingredient(category_index)
        formatted_item_locator = self.selected_ingredient_locator['locator']
        self.drag_and_drop_element(
            formatted_item_locator,
            ConstructorPageLocators.BURGER_CONSTRUCTOR_BUCKET
        )

    def get_selected_ingredient_counter_value(self):
        selected_ingredient_counter_locator = self.format_locator(
            ConstructorPageLocators.INDEXED_INGREDIENT_COUNTER,
            [
                self.selected_ingredient_locator['category'],
                self.selected_ingredient_locator['index'] + 1,
            ]
        )
        return int(
            self.get_text_node(selected_ingredient_counter_locator)
        )

    def create_order(self, sauce_quantity: int, filling_quantity: int):
        self.add_ingredient_to_bucket(1)
        for i in range(sauce_quantity):
            self.add_ingredient_to_bucket(2)
        for i in range(filling_quantity):
            self.add_ingredient_to_bucket(3)
        self.click_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()

    def create_orders_list(self, list_for_creating_orders: list[tuple[int, int]]):
        self.wait_for_constructor_page_ready()
        for i in list_for_creating_orders:
            self.create_order(i[0], i[1])
            self.click_new_order_popup_close_btn()

    def get_new_order_num_from_popup(self):
        self.find_element_with_wait(ConstructorPageLocators.POPUP)
        self.find_element_with_wait(ConstructorPageLocators.NEW_ORDER_POPUP_ORDER_TITLE)
        order_number = self.find_element_with_wait(ConstructorPageLocators.NEW_ORDER_POPUP_ORDER_NUMBER).text
        return order_number

    def get_created_order_num(self, sauce_quantity: int, filling_quantity: int):
        self.wait_for_constructor_page_ready()
        self.create_order(sauce_quantity, filling_quantity)
        new_order_num = self.get_new_order_num_from_popup()
        self.click_new_order_popup_close_btn()
        return new_order_num
