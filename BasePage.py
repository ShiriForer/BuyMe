from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # capture and save screenshot for when an element is not found
    def capture_screenshot(self, missing_element_name):
        error_screenshot_path = "C:/Users/shiri pc/PycharmProjects/BuyMe/ErrorScreenshots/error_screenshot.png"
        self.driver.save_screenshot(error_screenshot_path)
        print(f"The element '{missing_element_name}' was not found: a screenshot was saved")

    # Identify an element and click on it
    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, locator_value).click()
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot(f"Element at {locator_type} = {locator_value}")

    # Identify an input element and enter a value
    def enter_text(self, locator_type, locator_value, text):
        try:
            text_field = self.driver.find_element(locator_type, locator_value)
            text_field.clear()
            text_field.send_keys(text)
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot(f"Element at {locator_type} = {locator_value}")

    # Identify a multiple choice field and select a value
    def select_option(self, locator_type, locator_value, option_value):
        try:
            multiple_choice_field = Select(self.driver.find_element(locator_type, locator_value))
            multiple_choice_field.select_by_value(option_value)
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot(f"Element at {locator_type} = {locator_value}")

