import allure

from constants.urls import Urls
from locators.users.login_page_locators import LoginPageLocators
from pages.shared_elements_page import SharedElementsPage


class LoginPage(SharedElementsPage):

    @allure.step('Открыть страницу авторизации')
    def get_login_page(self):
        self.get_page_by_url(Urls.HOST + Urls.LOGIN_PAGE_PATH)
        self.wait_for_loading_animation_completed()

    @allure.step('Проверить, что текущая страница - страница авторизации')
    def is_login_page(self):
        page_title = self.get_text_node(
            LoginPageLocators.PAGE_HEADING
        )
        is_login_btn = \
            self.are_elements_present_on_page(LoginPageLocators.LOGIN_BUTTON)
        return page_title == 'Вход' \
            and Urls.LOGIN_PAGE_PATH in self.driver.current_url \
            and is_login_btn

    @allure.step('Кликнуть ссылку "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Заполнить форму авторизации и кликнуть кнопку')
    def login(self, creds: dict[str, str]) -> None:
        self.get_login_page()
        self.fill_text_field(
            LoginPageLocators.EMAIL_FIELD,
            creds['email']
        )
        self.fill_text_field(
            LoginPageLocators.PASSWORD_FIELD,
            creds['password']
        )
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_loading_animation_completed()
