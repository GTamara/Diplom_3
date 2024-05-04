from constants.urls import Urls
from locators.users.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def get_login_page(self):
        self.driver.get(Urls.HOST + Urls.LOGIN_PAGE_PATH)
        # WebDriverWait(self.driver, Constants.TIMEOUT).until(
        #     EC.invisibility_of_element_located(SharedLocators.LOADING_ANIMATION)
        # )
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


    # def get_forgot_password_page(self):
    #     self.driver.get(Urls.HOST_URL + Urls.FORGOT_PASSWORD_PAGE_PATH)
    #     # self.find_element_with_wait(HeaderLocators.LOGO)
    #     WebDriverWait(self.driver, Constants.TIMEOUT).until(
    #         EC.invisibility_of_element_located(ForgotPasswordLocators.FORGOT_PASSWORD_LOADING_ANIMATION)
    #     )