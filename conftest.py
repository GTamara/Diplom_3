from typing import Generator, Any

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helper_functions.shared_methods import SharedMethods


@pytest.fixture(scope="function")
def firefox_driver():
    options = FirefoxOptions()
    options.add_argument('--window-size=1920, 1080')
    with allure.step('Открыть окно Firefox браузера'):
        driver = webdriver.Firefox(options=options)
        # driver.maximize_window()
    yield driver
    with allure.step('Закрыть окно Firefox браузера'):
        driver.quit()


@pytest.fixture(scope="function")
def chrome_driver():
    options = ChromeOptions()
    options.add_argument('--window-size=1920, 1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    with allure.step('Закрыть окно Chrome браузера'):
        driver.quit()


@pytest.fixture(
    scope="function",
    params=[
        'firefox_driver',
        'chrome_driver',
    ]
)
def driver(request):
    return request.getfixturevalue(request.param)

@pytest.fixture(scope="function")
def user_login_valid_creds() -> Generator[dict[str, str], Any, None]:
    shared_methods = SharedMethods()
    user_auth_data = shared_methods.get_register_user_payload()
    yield user_auth_data
    login_resp = shared_methods.login_user(user_auth_data) \
        .json()
    token = login_resp['accessToken']
    shared_methods.delete_user(token)



