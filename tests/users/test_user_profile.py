import allure

from pages.users.login_page import LoginPage
from pages.users.user_profile_page import UserProfilePage


class TestUserProfile:

    @allure.title('Клик по ссылке «Личный кабинет» осуществляет переход в раздел «Личный кабинет»')
    def test_click_user_account_link_directs_to_user_profile(
        self,
        driver,
        user_login_valid_creds
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        user_profile_page = UserProfilePage(driver)
        user_profile_page.wait_for_loading_animation_completed()
        user_profile_page.click_header_user_profile_link()

        assert user_profile_page.is_user_account_page()

    @allure.title('Клик по ссылке «История заказов» осуществляет переход в раздел «История заказов»')
    def test_click_account_history_link_directs_to_account_history(
        self,
        driver,
        user_login_valid_creds
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_header_user_profile_link()
        user_profile_page.click_order_history_link()
        with allure.step('Подождать пока закончится анимация загрузки страницы'):
            user_profile_page.wait_for_loading_animation_completed()
            user_profile_page.wait_for_loading_progress_completed()

        assert user_profile_page.is_order_history_page()

    @allure.title('Клик по кнопке "Выход" осуществляет выход из аккаунта')
    def test_logout(
        self,
        driver,
        user_login_valid_creds
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_header_user_profile_link()
        user_profile_page.click_logout_button()
        assert login_page.is_login_page()
