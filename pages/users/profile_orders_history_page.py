import allure

from locators.users.profile_orders_history_locators import OrdersProfileHistoryLocators
from pages.base_page import BasePage


class ProfileOrdersHistoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__orders_quantity = len(
            self.driver.find_elements(
                *OrdersProfileHistoryLocators.ORDER_ITEM
            )
        )

    @property  # теперь это — геттер свойства
    def orders_quantity(self) -> int:
        return self.__orders_quantity

    @allure.step('Получить список номеров заказов пользователя')
    def get_order_numbers_list(self) -> list[str]:
        order_numbers_list = []
        for order in range(self.orders_quantity):
            order_number = self.find_element_with_wait(
                OrdersProfileHistoryLocators.INDEXED_ORDERS_ITEM_ORDER_NUMBER
            ).text
            order_numbers_list.append(order_number)
        return order_numbers_list
        # order_numbers_list = map(lambda order: x ** 2, numbers)
