import allure

from constants.urls import Urls
from locators.shared_locators import SharedLocators
from locators.orders.constructor_page_locators import ConstructorPageLocators
from pages.shared_elements_page import SharedElementsPage


class ConstructorPage(SharedElementsPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.selected_ingredient_locator = {
            'locator': '',
            'category': -1,
            'index': -1,
        }

    @allure.step('Открыть главную страницу')
    def get_constructor_page(self):
        self.get_page_by_url(Urls.HOST)
        self.wait_for_constructor_page_ready()

    @allure.step('Проверить, что текущая страница - "Конструктор"')
    def is_constructor_page(self):
        return self.find_element_with_wait(ConstructorPageLocators.PAGE_HEADING).is_displayed()

    @allure.step('Подождать, пока страница конструктора загрузится')
    def wait_for_constructor_page_ready(self):
        self.wait_until_all_elements_loaded(ConstructorPageLocators.BURGER_INGREDIENT_IMAGE)

    @allure.step('Подождать, пока элементы попапа станут кликабельными')
    def wait_for_popup_ready(self):
        self.wait_until_element_disappears(SharedLocators.POPUP_OVERLAY)
        self.find_element_with_wait(ConstructorPageLocators.POPUP_CLOSE_BTN)

    @allure.step('Выбрать случайный ингредиент из раздела {category_index}')
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

    @allure.step('Кликнуть случайный ингредиент и получить его название')
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

    @allure.step('Проверить название ингредиента внутри попапа')
    def check_ingredient_title_within_popup(self, clicked_ingredient_title: str):
        ingredient_title_within_opened_popup = self.get_text_node(ConstructorPageLocators.INGREDIENT_TITLE_WITHIN_POPUP)
        return ingredient_title_within_opened_popup == clicked_ingredient_title

    @allure.step('Кликнуть случайный ингредиент из категории {category_index}')
    def click_ingredient_item(self, category_index: int):
        formatted_item_locator = self.get_random_ingredient(category_index)['locator']
        self.click_element(formatted_item_locator)

    @allure.step('Кликнуть кнопку "X" попапа с деталями ингредиента')
    def click_ingredient_popup_close_btn(self):
        self.wait_for_popup_ready()
        self.click_element_containing_svg_icon(ConstructorPageLocators.POPUP_CLOSE_BTN)

    @allure.step('Кликнуть кнопку "X" попапа с с номером нового заказа')
    def click_new_order_popup_close_btn(self):
        self.wait_for_popup_ready()

        self.click_element_containing_svg_icon(ConstructorPageLocators.POPUP_CLOSE_BTN)

    @allure.step('Проверить, что попап скрыт')
    def is_ingredient_popup_hidden(self):
        self.wait_until_element_disappears(ConstructorPageLocators.POPUP)
        return True

    @allure.step('Добавить в корзину случайный ингредиент из категории {category_index}')
    def add_ingredient_to_bucket(self, category_index: int):
        self.selected_ingredient_locator = self.get_random_ingredient(category_index)
        formatted_item_locator = self.selected_ingredient_locator['locator']
        self.drag_and_drop_by_javascript(
            formatted_item_locator,
            ConstructorPageLocators.BURGER_CONSTRUCTOR_BUCKET
        )

    @allure.step('Получить значение счетчика ингредиента')
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

    @allure.step('Создать заказ')
    def create_order(self, sauce_quantity: int, filling_quantity: int):
        self.add_ingredient_to_bucket(1)
        for i in range(sauce_quantity):
            self.add_ingredient_to_bucket(2)
        for i in range(filling_quantity):
            self.add_ingredient_to_bucket(3)
        self.click_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()

    @allure.step('Создать список заказов')
    def create_orders_list(self, list_for_creating_orders: list[tuple[int, int]]):
        self.wait_for_constructor_page_ready()
        for i in list_for_creating_orders:
            self.create_order(i[0], i[1])
            self.click_new_order_popup_close_btn()

    @allure.step('Получить номер заказа из попапа')
    def get_new_order_num_from_popup(self):
        self.find_element_with_wait(ConstructorPageLocators.POPUP)
        self.find_element_with_wait(ConstructorPageLocators.NEW_ORDER_POPUP_ORDER_TITLE)
        self.wait_for_loading_animation_completed()
        order_number = self.find_element_with_wait(ConstructorPageLocators.NEW_ORDER_POPUP_ORDER_NUMBER).text
        return order_number

    @allure.step('Получить номер нового заказа')
    def get_created_order_num(self, sauce_quantity: int, filling_quantity: int):
        self.wait_for_constructor_page_ready()
        self.create_order(sauce_quantity, filling_quantity)
        new_order_num = self.get_new_order_num_from_popup()
        self.click_new_order_popup_close_btn()
        return new_order_num
