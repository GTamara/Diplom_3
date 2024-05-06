from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Constants
from constants.urls import Urls
from helper_functions.shared_helper_funcs import SharedHelperFuncs
from locators.users.forgot_password_locators import ForgotPasswordLocators
from locators.users.login_page_locators import LoginPageLocators
from locators.shared_locators import SharedLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage(BasePage):

    def get_forgot_password_page(self):
        self.driver.get(Urls.HOST + Urls.FORGOT_PASSWORD_PAGE_PATH)
        # self.find_element_with_wait(HeaderLocators.LOGO)
        # WebDriverWait(self.driver, Constants.TIMEOUT).until(
        #     EC.invisibility_of_element_located(SharedLocators.LOADING_ANIMATION)
        # )
        self.wait_for_loading_animation_completed()



    def fill_and_submit_forgot_password_form(self, email_value: str | None):
        if not email_value:
            email_value = SharedHelperFuncs().generate_random_email()
        self.fill_text_field(
            ForgotPasswordLocators.TEXT_FIELD,
            email_value
        )
        self.click_element(ForgotPasswordLocators.FORGOT_PASSWORD_BTN)

    def is_forgot_password_page(self):
        page_title = self.get_text_node(
            ForgotPasswordLocators.PAGE_HEADING
        )
        is_forgot_password_link_present_on_page = \
            self.are_elements_present_on_page(LoginPageLocators.FORGOT_PASSWORD_LINK)

        return page_title == 'Восстановление пароля' \
            and '/forgot-password' in self.driver.current_url \
            and not  is_forgot_password_link_present_on_page



