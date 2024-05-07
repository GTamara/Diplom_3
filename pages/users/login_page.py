from constants.urls import Urls
from locators.users.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def get_login_page(self):
        self.driver.get(Urls.HOST + Urls.LOGIN_PAGE_PATH)
        self.wait_for_loading_animation_completed()

    def is_login_page(self):
        page_title = self.get_text_node(
            LoginPageLocators.PAGE_HEADING
        )
        is_login_btn = \
            self.are_elements_present_on_page(LoginPageLocators.LOGIN_BUTTON)
        x = '/login' in self.driver.current_url
        return page_title == 'Вход' \
            and '/login' in self.driver.current_url \
            and  is_login_btn


    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def login(self, creds):
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
