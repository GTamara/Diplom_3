import json

import allure
import requests
from requests import Response
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.urls import Urls
from helper_functions.shared_helper_funcs import SharedHelperFuncs


class SharedApiMethods:

    @staticmethod
    @allure.step('Сформировать тело запроса для регистрации курьера')
    def get_register_payload() -> dict[str, str]:
        helper_funcs = SharedHelperFuncs()
        email = helper_funcs.generate_random_email(10)
        password = helper_funcs.generate_random_string(8)
        name = helper_funcs.generate_random_string(5)
        return {
            'email': email,
            'password': password,
            'name': name
        }

    @allure.step('Получить ответ на запрос регистрации нового пользователя')
    def get_register_user_payload(self) -> dict[str, str]:
        payload = self.get_register_payload()
        response = requests.post(Urls.HOST + Urls.REGISTER_USER, data=payload)
        if response.status_code == 200:
            return payload
        else:
            raise Exception('Произошла ошибка при регистрации пользователя')

    @staticmethod
    @allure.step('Логин пользователя с данными {payload}')
    def login_user(payload: dict[str, str]) -> Response:
        response = requests.post(
            Urls.HOST + Urls.LOGIN_USER,
            data=json.dumps(payload),
            headers={
                'Content-Type': 'application/json; charset=utf-8'
            }
        )
        return response

    @staticmethod
    @allure.step('Удалить юзера')
    def delete_user(token: str) -> Response:
        url = Urls.HOST + Urls.DELETE_USER
        return requests.delete(
            url=url,
            headers={'Authorization': token}
        )
