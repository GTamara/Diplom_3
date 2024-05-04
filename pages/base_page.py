from selenium.webdriver import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Constants
from locators.shared_locators import SharedLocators


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_with_wait(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        # WebDriverWait(self.driver, Constants.TIMEOUT).until(
        #     EC.visibility_of_all_elements_located(locator)
        # )
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple[str, str]):
        # self.find_element_with_wait(locator)
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
            # EC.visibility_of_all_elements_located(locator)
        )
        # WebDriverWait(self.driver, Constants.TIMEOUT).until(
        #     EC.element_to_be_clickable(locator)
        #     # EC.visibility_of_all_elements_located(locator)
        # )
        self.find_element_with_wait(locator).click()

    def scroll_to_element(self, locator: tuple[str, str]):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def format_locator(
            locator: tuple[str, str],
            num: int | str
    ) -> tuple[str, str]:
        method, selector = locator
        formatted_locator: str = selector.format(num)
        return method, formatted_locator

    def get_text_node(self, locator: tuple[str, str]):
        x = self.find_element_with_wait(locator).text
        return self.find_element_with_wait(locator).text

    def fill_text_field(self, locator: tuple[str, str], value):
        return self.find_element_with_wait(locator).send_keys(value)
    
    def fill_dropdown(
        self, 
        dropdown_locator: tuple[str, str], 
        option_locator: tuple[str, str]
    ):
        self.click_element(dropdown_locator)
        self.click_element(option_locator)

    def fill_datepicker_manualy(
        self,
        locator: tuple[str, str], 
        value
    ):
        self.fill_text_field(locator, value)
        self.find_element_with_wait(*locator).send_keys(Keys.ESCAPE)

    def set_checkbox_value(self, locator: tuple[str, str], checked):
        checkbox = self.find_element_with_wait(locator)
        current_value = checkbox.get_attribute('checked')
        if bool(current_value) != checked:
            checkbox.click()

    def switch_to_next_browser_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_value_from_text_field(self, locator: tuple[str, str]):
        control = self.find_element_with_wait(locator)
        return control.get_attribute('value')

    def are_elements_present_on_page(self, locator: tuple[str, str]):
        return bool(
            len(self.driver.find_elements(*locator))
        )

    def wait_for_loading_animation_completed(self):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.invisibility_of_element_located(SharedLocators.LOADING_ANIMATION)
        )

