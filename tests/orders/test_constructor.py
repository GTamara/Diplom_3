from helper_functions.shared_methods import SharedMethods
from pages.orders.constructor_page import ConstructorPage


class TestConstructorPage:

    def test_click_header_constructor_link_directs_to_constructor_page(self, driver):
        SharedMethods.get_main_page(driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_constructor_header_link()
        constructor_page.wait_for_loading_animation_completed()
        constructor_page.wait_for_constructor_page_ready()
        assert constructor_page.is_constructor_page()