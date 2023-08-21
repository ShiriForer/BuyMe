from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from BuyMe import BuyMeIntroPage, RegistrationForm, HomeScreen

class test_Buyme(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("C:\\Users\\shiri pc\\Desktop\\chromedriver_win32\\chromedriver.exe"))
        self.driver.get("https://buyme.co.il/")
        # implicit wait
        self.driver.implicitly_wait(10)
        # page load timeout
        self.driver.set_page_load_timeout(30)

    # add here explicit waits? And for which fields?
    # def test_explicit_wait(self):
    #     # explicit wait
    #     element = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable((By.CLASS_NAME, "er8xn")))
    #     element.send_keys('helo')

    def tearDown(self):
        self.driver.quit()

class test_BuyMeIntroPage(TestCase):
    def test_intro_page(self):
        self.intro_page = BuyMeIntroPage(self.driver)
        self.intro_page.close_intro_banner()
        self.intro_page.click_to_register()
        self.intro_page.register()


class test_RegistrationForm(TestCase):
    def test_registration_form(self):
        self.registration_form = RegistrationForm(self.driver)
        self.registration_form.fill_in_first_name()
        self.registration_form.fill_in_email_address()
        self.registration_form.fill_in_password()
        self.registration_form.confirm_password()
        self.registration_form.agree_to_terms()
        self.registration_form.submit_registration_form()

class test_HomeScreen(TestCase):
    def test_home_screen(self):
        self.home_screen = HomeScreen(self.driver)
        self.home_screen.pick_price_point()
        self.home_screen.pick_region()
        self.home_screen.pick_category()
        self.home_screen.find_gift()