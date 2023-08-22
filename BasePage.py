from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # capture and save screenshot for when an element is not found
    def capture_screenshot(self):
        screenshot = screenshot.png
        self.driver.save_screenshot(screenshot)
        print("The element was not found: a screenshot was saved")

    # Identify an element and click on it
    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, locator_value).click()
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot()

    # Identify an input element and enter a value
    def enter_text(self, locator_type, locator_value, text):
        try:
            self.driver.find_element(locator_type, locator_value).send_keys(text)
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot()

    # Identify a multiple choice field and select a value using select by value method
    def select_option_by_value(self, locator_type, locator_value, option_value):
        #click to open a drop-down list
        try:
            multiple_choice_field = self.driver.find_element(locator_type, locator_value)
            multiple_choice_field.click()
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot()
        # select an option from the list
        choose_option = Select(multiple_choice_field)
        choose_option.select_by_value(option_value)

    # Identify a multiple choice field and select a value using select by visible text method
    def select_option_by_visible_text(self, locator_type, locator_value, visible_text):
        # click to open the drop-down list
        try:
            multiple_choice_field = self.driver.find_element(locator_type, locator_value)
            multiple_choice_field.click()
        except (NoSuchElementException, TimeoutException):
            self.capture_screenshot()
        # select an option from the list
        choose_option = Select(multiple_choice_field)
        choose_option.select_by_visible_text(visible_text)
