import random

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
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
        return self.driver.find_element(*locator)

    def find_element_without_wait(self, locator: tuple[str, str]):
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )
        self.find_element_with_wait(locator).click()

    def click_element_containing_svg_icon(self, locator: tuple[str, str]):
        svg_element_path = locator[1] + '/*[name()="svg"]'
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.visibility_of_all_elements_located(
                (locator[0], svg_element_path)
            )
        )
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )
        element = self.find_element_with_wait(
            (locator[0], svg_element_path)
        )
        element.click()

    def scroll_to_element(self, locator: tuple[str, str]):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_web_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def format_locator(
            locator: tuple[str, str],
            num: int | str | list
    ) -> tuple[str, str]:
        method, selector = locator
        if type(num) in [int, str]:
            formatted_locator: str = selector.format(num)
        elif type(num) == list:
            formatted_locator: str = selector.format(*num)
        else:
            formatted_locator = locator
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

    def switch_to_next_browser_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_value_from_text_field(self, locator: tuple[str, str]):
        control = self.find_element_with_wait(locator)
        return control.get_attribute('value')

    def are_elements_present_on_page(self, locator: tuple[str, str]):
        return len(self.driver.find_elements(*locator)) > 0

    def wait_for_loading_animation_completed(self):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.invisibility_of_element_located(SharedLocators.LOADING_ANIMATION)
        )

    def wait_until_element_disappears(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_loading_progress_completed(self):
        self.wait_until_element_disappears(SharedLocators.CONTENT_LOADING_PROGRESS)

    def wait_for_all_elements_loaded(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, 30). \
            until(
                EC.visibility_of_all_elements_located(locator)
            )

    def select_random_item_index(self, locator: tuple[str, str]):
        items_list = self.driver.find_elements(*locator)
        index = random.randint(
            0, len(items_list) - 1
        )
        return index

    def drag_and_drop_element(self, source: tuple[str, str], target: tuple[str, str]):
        sourceElement = self.find_element_with_wait(source)
        targetElement = self.find_element_with_wait(target)
        ActionChains(self.driver).drag_and_drop(sourceElement, targetElement).perform()
        ActionChains(self.driver).click_and_hold(sourceElement).move_to_element(targetElement)

    def drag_and_drop_by_javascript(self, source: tuple[str, str], target: tuple[str, str]):
        sourceElement = self.find_element_with_wait(source)
        targetElement = self.find_element_with_wait(target)
        script_str = "function createEvent(typeOfEvent) {\n" + "var event =document.createEvent(\"CustomEvent\");\n" \
        + "event.initCustomEvent(typeOfEvent,true, true, null);\n" + "event.dataTransfer = {\n" + "data: {},\n" \
        + "setData: function (key, value) {\n" + "this.data[key] = value;\n" + "},\n" \
        + "getData: function (key) {\n" + "return this.data[key];\n" + "}\n" + "};\n" + "return event;\n" \
        + "}\n" + "\n" + "function dispatchEvent(element, event,transferData) {\n" \
        + "if (transferData !== undefined) {\n" + "event.dataTransfer = transferData;\n" + "}\n" \
        + "if (element.dispatchEvent) {\n" + "element.dispatchEvent(event);\n" \
        + "} else if (element.fireEvent) {\n" + "element.fireEvent(\"on\" + event.type, event);\n" + "}\n" \
        + "}\n" + "\n" + "function simulateHTML5DragAndDrop(element, destination) {\n" \
        + "var dragStartEvent =createEvent('dragstart');\n" + "dispatchEvent(element, dragStartEvent);\n" \
        + "var dropEvent = createEvent('drop');\n" \
        + "dispatchEvent(destination, dropEvent,dragStartEvent.dataTransfer);\n" \
        + "var dragEndEvent = createEvent('dragend');\n" \
        + "dispatchEvent(element, dragEndEvent,dropEvent.dataTransfer);\n" + "}\n" + "\n" \
        + "var source = arguments[0];\n" + "var destination = arguments[1];\n" \
        + "simulateHTML5DragAndDrop(source,destination);"
        print(script_str)
        self.driver.execute_script(script_str, sourceElement, targetElement)
