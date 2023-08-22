from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self):
        screenshot = screenshot.png
        self.driver.save_screenshot(screenshot)
        print("The element was not found. A screenshot was saved")

    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, locator_value).click()
        except NoSuchElementException:
            capture_screenshot()

    def enter_text(self, locator_type, locator_value, text):
        try:
            self.driver.find_element(locator_type, locator_value).send_keys(text)
        except NoSuchElementException:
            capture_screenshot()

    def select_option_by_value(self, locator_type, locator_value, option_value):
        #click to open a drop-down list
        try:
            multiple_choice_field = self.driver.find_element(locator_type, locator_value).click()
        except NoSuchElementException:
            capture_screenshot()
        # select an option from the list
        choose_option = Select(multiple_choice_field)
        choose_option.select_by_value(option_value)

    def select_option_by_visible_text(self, locator_type, locator_value, visible_text):
        # click to open the drop-down list
        try:
            multiple_choice_field = self.driver.find_element(locator_type, locator_value).click()
        except NoSuchElementException:
            capture_screenshot()
        # select an option from the list
        choose_option = Select(multiple_choice_field)
        choose_option.select_by_visible_text(visible_text)
