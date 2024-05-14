from locators.shared_locators import SharedLocators
from pages.base_page import BasePage


class SharedElementsPage(BasePage):

    def wait_for_loading_animation_completed(self):
        self.wait_until_element_disappears(SharedLocators.LOADING_ANIMATION)

    def wait_for_loading_progress_completed(self):
        self.wait_until_element_disappears(SharedLocators.CONTENT_LOADING_PROGRESS)
