from locators.orders.constructor_page_locators import ConstructorPageLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    def click_constructor_header_link(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_LINK)

    def is_constructor_page(self):
        return bool(
            self.find_element_with_wait(ConstructorPageLocators.PAGE_HEADING)
        )

    def wait_for_constructor_page_ready(self):
        self.find_element_with_wait(ConstructorPageLocators.PAGE_HEADING)
        self.find_element_with_wait(ConstructorPageLocators.BURGER_INGREDIENTS_SECTION)
        self.driver.find_elements(*ConstructorPageLocators.BURGER_INGREDIENT)


