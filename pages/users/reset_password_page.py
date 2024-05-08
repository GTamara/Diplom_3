from constants.urls import Urls
from helper_functions.shared_helper_funcs import SharedHelperFuncs
from locators.users.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage
#


class ResetPasswordPage(BasePage):

    def wait_for_reset_password_page_ready(self):
        self.find_element_with_wait(ResetPasswordLocators.PAGE_HEADING)
        self.find_element_with_wait(ResetPasswordLocators.RESET_PASSWORD_BTN)
        self.find_element_with_wait(ResetPasswordLocators.LOGIN_LINK)

    def is_reset_password_page(self):
        x = self.get_text_node(
            ResetPasswordLocators.PAGE_HEADING
        ) == 'Восстановление пароля'
        return (
            self.get_text_node(
                ResetPasswordLocators.PAGE_HEADING
            ) == 'Восстановление пароля'
            and '/reset-password' in self.driver.current_url
        )

    def get_reset_password_page(self):
        self.driver.get(Urls.HOST + Urls.RESET_PASSWORD_PAGE_PATH)

    def fill_password_field(self, password_value: str | None):
        if not password_value:
            helper_funcs = SharedHelperFuncs()
            password_value = helper_funcs.generate_random_string()
        self.fill_text_field(
            ResetPasswordLocators.TEXT_FIELD_1,
            password_value
        )

    def get_password_field_type(self):
        return self.find_element_with_wait(
            ResetPasswordLocators.TEXT_FIELD_1,
        ).get_dom_attribute('type')

    def toggle_show_hide_password_icon(self):
        self.wait_for_reset_password_page_ready()
        self.click_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD_BTN)

    def get_value_from_password_text_field_1(self):
        return self.get_value_from_text_field(
            ResetPasswordLocators.TEXT_FIELD_1
        )


