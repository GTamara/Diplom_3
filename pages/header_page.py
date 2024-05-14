import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Кликнуть ссылку "Конструктор"')
    def click_header_constructor_link(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_LINK)