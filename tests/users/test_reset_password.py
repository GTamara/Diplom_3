import allure

from pages.users.forgot_password_page import ForgotPasswordPage
from pages.users.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_check_toggle_visibility_icons_toggles_text_visibility(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.get_forgot_password_page()

        forgot_password_page.fill_and_submit_forgot_password_form(None)
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_reset_password_page_ready()
        reset_password_page.fill_password_field(None)
        assert reset_password_page.get_password_field_type() == 'password'
        reset_password_page.toggle_show_hide_password_icon()
        assert reset_password_page.get_password_field_type() == 'text'


