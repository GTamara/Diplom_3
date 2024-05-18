import allure

from constants.urls import Urls
from helper_functions.shared_helper_funcs import SharedHelperFuncs
from locators.users.forgot_password_locators import ForgotPasswordLocators
from locators.users.login_page_locators import LoginPageLocators
from pages.shared_elements_page import SharedElementsPage


class ForgotPasswordPage(SharedElementsPage):

    @allure.step('Открыть страницу "Забыли пароль"')
    def get_forgot_password_page(self):
        self.get_page_by_url(Urls.HOST + Urls.FORGOT_PASSWORD_PAGE_PATH)
        self.wait_for_loading_animation_completed()

    @allure.step('Заполнить форму "Забыли пароль" и кликнуть кнопку')
    def fill_and_submit_forgot_password_form(self, email_value: str | None):
        if not email_value:
            email_value = SharedHelperFuncs().generate_random_email()
        self.fill_text_field(
            ForgotPasswordLocators.TEXT_FIELD,
            email_value
        )
        self.click_element(ForgotPasswordLocators.FORGOT_PASSWORD_BTN)

    @allure.step('Проверить, что текущая страница - "Забыли пароль"')
    def is_forgot_password_page(self):
        page_title = self.get_text_node(
            ForgotPasswordLocators.PAGE_HEADING
        )
        is_forgot_password_link_present_on_page = \
            self.are_elements_present_on_page(LoginPageLocators.FORGOT_PASSWORD_LINK)
        current_url = self.get_current_url()
        return page_title == 'Восстановление пароля' \
            and Urls.FORGOT_PASSWORD_PAGE_PATH in current_url \
            and not  is_forgot_password_link_present_on_page



