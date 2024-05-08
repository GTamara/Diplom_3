import allure

from pages.users.forgot_password_page import ForgotPasswordPage
from pages.users.login_page import LoginPage
from pages.users.reset_password_page import ResetPasswordPage


class TestForgotPasswordPage:

    @allure.title('Клик по ссылке «Восстановить пароль» логин формы ведет на страницу "забыли пароль"')
    def test_click_forgot_password_link_directs_from_login_page_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        login_page.click_forgot_password_link()
        forgot_password_page = ForgotPasswordPage(driver)

        assert forgot_password_page.is_forgot_password_page()

    @allure.title(
        'Если поле email заполнено, клик по кнопке «Восстановить» страницы "забыли пароль" ведет на страницу '
        'восстановления пароля'
    )
    def test_click_reset_btn_with_filled_email_directs_to_reset_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.get_forgot_password_page()
        forgot_password_page.fill_and_submit_forgot_password_form(None)
        reset_password_page = ResetPasswordPage(driver)

        assert reset_password_page.is_reset_password_page()









