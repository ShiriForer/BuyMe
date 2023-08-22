from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BuyMeIntroPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # If banner pops-up, close it
    def close_intro_banner(self):
        try:
            intro_banner = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.NAME, "כפתור סגירה")))
            intro_banner.click()
        except NoSuchElementException:
            pass

    # sign-in to website
    def click_to_register(self):
        self.click_element(By.CSS_SELECTOR, 'a[aria-label= "כניסה / הרשמה"]')

    # click to register as a new user
    def register(self):
        self.click_element(By.CLASS_NAME, "text-link theme")

class RegistrationForm(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = driver.find_element(By.ID, value="ember1917")
        self.reg_first_name = "יאיר"
        self.reg_email = "yeled_z@yahoo.com"
        self.password = "12345"

    # fill-in registration form
    def fill_in_first_name(self):
        self.enter_text(self.first_name_field)
        assert self.first_name_field.text == self.reg_first_name

    def fill_in_email_address(self):
        self.enter_text(By.ID, "ember1924", self.reg_email)

    def fill_in_password(self):
        self.enter_text(By.ID, "valPass", self.password)

    def confirm_password(self):
        self.enter_text(By.ID, "ember1938", self.password)

    # check "agree to terms" box
    def agree_to_terms(self):
        self.click_element(By.CLASS_NAME, "check")

    # submit form
    def submit_registration_form(self):
        self.click_element(By.ID, "ember1948")

class HomeScreen(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.price_range = '200-299 ש"ח'
        self.region = "צפון"
        self.gift = "מתנות במימוש אונליין"

    # choose the gift's price range
    def pick_price_point(self):
        self.select_option_by_visible_text(By.CSS_SELECTOR, 'div.selected-name span[title="סכום"]', self.price_range)

    # choose region
    def pick_region(self):
        self.select_option.by.visible_text(By.CSS_SELECTOR, 'div.selected-name span[title="אזור"]', self.region)

    # choose category
    def pick_category(self):
        self.select_option.by.visible_text(By.CSS_SELECTOR, 'div.selected-name span[title="קטגוריה"]', self.gift)

    # click to submit criteria and find a gift
    def find_gift(self):
        self.click_element(By.ID, "ember1295")