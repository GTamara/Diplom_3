from constants.urls import Urls
from pages.base_page import BasePage


class SharedUiMethods(BasePage):

    @staticmethod
    def get_main_page(driver):
        driver.get(Urls.HOST)
