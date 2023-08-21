from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, filename):
        screenshot_filename = f"{filename}.png"
        self.driver.save_screenshot(screenshot_filename)
        print(f"Screenshot saved: {screenshot_filename}")

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def enter_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    def select_option_by_value(self, locator_type, locator_value, option_value):
        #click to open the drop-down list
        multiple_choice_field = self.driver.find_element(locator_type, locator_value).click()
        # select an option from the list
        choose_option = Select(multiple_choice_field)
        choose_option.select_by_value(option_value)

    def select_option_by_visible_text(self, locator_type, locator_value, visible_text):
        # click to open the drop-down list
        multiple_choice_field = self.driver.find_element(locator_type, locator_value).click()
        # select an option from the list
        choose_option = Select(multiple_choice_field)
        choose_option.select_by_visible_text(visible_text)
