from pages.users.login_page import LoginPage
from pages.users.user_profile_page import UserProfilePage


class TestUserProfile:

    def test_click_user_account_link_directs_to_user_account(
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

    def test_click_account_history_link_directs_to_account_history(
        self,
        driver,
        user_login_valid_creds
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        user_profile_page = UserProfilePage(driver)
        user_profile_page.wait_for_loading_animation_completed()
        user_profile_page.click_header_user_profile_link()
        user_profile_page.wait_for_loading_animation_completed()
        user_profile_page.click_order_history_link()
        user_profile_page.wait_for_loading_animation_completed()

        assert user_profile_page.is_order_history_page()

    def test_logout(
        self,
        driver,
        user_login_valid_creds
    ):
        login_page = LoginPage(driver)
        login_page.login(user_login_valid_creds)
        user_profile_page = UserProfilePage(driver)
        user_profile_page.wait_for_loading_animation_completed()
        user_profile_page.click_header_user_profile_link()
        user_profile_page.wait_for_loading_animation_completed()
        user_profile_page.click_logout_button()
        user_profile_page.wait_for_loading_animation_completed()
        assert login_page.is_login_page()
