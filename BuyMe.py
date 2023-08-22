from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BuyMeIntroPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    # If banner pops-up, close it
    def close_intro_banner(self):
        try:
            intro_banner = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "כפתור סגירה")))
            intro_banner.click()
        except NoSuchElementException:
            pass

    # sign-in to website
    def click_to_register(self):
        self.click_element(By.CLASS_NAME, "notSigned")

    # click to register as a new user
    def register(self):
        # self.click_element(By.CSS_SELECTOR, "div.register-or-login span.text-link.theme")
        self.click_element(By.XPATH, "//span[@aria-label='להרשמה']")


class RegistrationForm(BasePage):
    # initialize a constructor and variables for RegistrationForm class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.reg_first_name = "Yair"
        self.reg_email = "yeled_z@yahoo.com"
        self.password = "12345"

    # fill-in registration form
    def fill_in_first_name(self):
        # self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם פרטי']", self.reg_first_name)
        self.enter_text(By.XPATH, "//input[@placeholder='שם פרטי']", self.reg_first_name)
        assert self.driver.find_element(By.XPATH, "//input[@placeholder='שם פרטי']").get_attribute(
            "value") == self.reg_first_name

    def fill_in_email_address(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", self.reg_email)
        # self.enter_text(By.XPATH, "//input[@placeholder='מייל']", self.reg_email)

    def fill_in_password(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", self.password)

    def confirm_password(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']", self.password)

    # check "agree to terms" box
    def agree_to_terms(self):
        self.click_element(By.CLASS_NAME, "login-options grid register-text")

    # submit form
    def submit_registration_form(self):
        self.click_element(By.CLASS_NAME, "login-options grid bottom-lr register-text")


class HomeScreen(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        # self.price_range = '200-299 ש"ח'
        # self.region = "צפון"
        # self.gift = "מתנות במימוש אונליין"

    # choose the gift's price range
    def pick_price_point(self):
        self.select_option_by_value(By.ID, "ember1157").select_by_value('200-299 ש"ח')
    # choose region
    def pick_region(self):
        self.select_option_by_visible_text(By.CSS_SELECTOR, "span[aria-label='אזור']", self.region)

    # choose category
    def pick_category(self):
        self.select_option_by_visible_text(By.CSS_SELECTOR, "span[aria-label='קטגוריה']", self.gift)

    # click to submit criteria and find a gift
    def find_gift(self):
        self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")


class PickBusiness(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.expected_url = "https://buyme.co.il/search?budget=3&category=300&region=9"
        self.price_of_choice = "250"

    def assert_pick_business_url(self):
        assert self.driver.current_url == self.expected_url

    def pick_business(self):
        self.click_element(By.CSS_SELECTOR, "img[title='SABON']")

    def enter_and_submit_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", self.price_of_choice)
        self.click_element(By.CSS_SELECTOR, "button[type='submit']")

class SenderReceiverInfo(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.receiver_name = "Sarah"
        self.event_of_choice =
    def send_for_someone_else(self):
        self.click_element(By.CLASS_NAME, "ember-view button button-forSomeone selected")
    def fill_in_receiver_name(self):
        self.enter_text(By.CSS_SELECTOR, "input[title='שם מקבל המתנה']", self.receiver_name)
    def pick_event(self):
        self.click_element(By.NAME, "eventType")