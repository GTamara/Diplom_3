import allure

from constants.urls import Urls
from locators.header_locators import HeaderLocators
from locators.users.user_profile_locators import UserProfileLocators
from pages.shared_elements_page import SharedElementsPage


class UserProfilePage(SharedElementsPage):

    @allure.step('Открыть страницу профиля пользователя')
    def click_header_user_profile_link(self):
        self.click_element(HeaderLocators.USER_PROFILE_LINK)
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()

    @allure.step('Кликнуть ссылку "История заказов"')
    def click_order_history_link(self):
        self.click_element(UserProfileLocators.ORDER_HISTORY_LINK)
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()

    @allure.step('Кликнуть кнопку выхода из аккаунта')
    def click_logout_button(self):
        self.click_element(UserProfileLocators.LOGOUT_BUTTON)
        self.wait_for_loading_animation_completed()

    @allure.step('Проверить, что текущая страница - профиль пользователя')
    def is_user_account_page(self):
        self.find_element_with_wait(UserProfileLocators.USER_DATA_FORM)
        is_profile_link_present_on_page = self.are_elements_present_on_page(
            UserProfileLocators.PROFILE_LINK
        )
        is_profile_link_active = self.is_nav_link_active(UserProfileLocators.PROFILE_LINK)
        current_url = self.get_current_url()
        return is_profile_link_present_on_page \
            and is_profile_link_active \
            and self.find_element_with_wait(UserProfileLocators.USER_DATA_FORM) \
            and Urls.PROFILE_PAGE_PATH in current_url

    @allure.step('Проверить, что текущая страница - история заказов пользователя')
    def is_order_history_page(self):
        is_order_history_link_active = self.is_nav_link_active(UserProfileLocators.ORDER_HISTORY_LINK)
        self.wait_until_all_elements_loaded(UserProfileLocators.ORDER_HISTORY_CONTAINER)
        current_url = self.get_current_url()
        return is_order_history_link_active \
            and Urls.PROFILE_ORDERS_HISTORY in current_url \
            and self.are_elements_present_on_page(UserProfileLocators.ORDER_HISTORY_CONTAINER)

    @allure.step('Проверить, что ссылка имеет стили active')
    def is_nav_link_active(self, locator: tuple[str, str]):
        nav_link_link_class = \
            self.find_element_with_wait(locator) \
                .get_attribute('class')
        is_active = '_link_active_' in nav_link_link_class
        return is_active
