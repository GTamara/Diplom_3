import allure

from constants.urls import Urls
from helper_functions.shared_helper_funcs import SharedHelperFuncs
from locators.users.reset_password_locators import ResetPasswordLocators
from pages.shared_elements_page import SharedElementsPage


class ResetPasswordPage(SharedElementsPage):

    @allure.step('Подождать, пока страница восстановления пароля загрузится')
    def wait_for_reset_password_page_ready(self):
        self.find_element_with_wait(ResetPasswordLocators.RESET_PASSWORD_BTN)
        self.find_element_with_wait(ResetPasswordLocators.LOGIN_LINK)
        self.wait_for_loading_animation_completed()
        self.wait_for_loading_progress_completed()

    @allure.step('Проверить, что текущая страница - страница восстановления пароля')
    def is_reset_password_page(self):
        page_title = self.get_text_node(
            ResetPasswordLocators.PAGE_HEADING
        )
        current_url = self.get_current_url()
        return page_title == 'Восстановление пароля' \
            and Urls.RESET_PASSWORD_PAGE_PATH in current_url

    @allure.step('Заполнить поле для пароля')
    def fill_password_field(self, password_value: str | None):
        if not password_value:
            helper_funcs = SharedHelperFuncs()
            password_value = helper_funcs.generate_random_string()
        self.fill_text_field(
            ResetPasswordLocators.TEXT_FIELD_1,
            password_value
        )

    @allure.step('Получить значение атрибута "type"')
    def get_password_field_type(self):
        return self.find_element_with_wait(
            ResetPasswordLocators.TEXT_FIELD_1,
        ).get_dom_attribute('type')

    @allure.step('Кликнуть иконку скрыть / показать пароль')
    def toggle_show_hide_password_icon(self):
        self.wait_for_reset_password_page_ready()
        self.click_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD_BTN)


