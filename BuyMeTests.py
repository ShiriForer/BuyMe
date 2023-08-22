import logging
from unittest import TestCase
import json
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from BuyMe import BuyMeIntroPage, RegistrationForm, HomeScreen

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(
                    filename='logfile.log', # set the output file
                    filemode='a', # set it to append rather than overwrite
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', # determine the format of the output message
                    datefmt='%H:%M:%S', # determine the format of the output time
                    level=logging.ERROR) # determine the minimum message level it will accept
class test_Buyme(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service("C:\\Users\\shiri pc\\Desktop\\chromedriver_win32\\chromedriver.exe"))
        cls.driver.get("https://buyme.co.il/")
        # implicit wait
        cls.driver.implicitly_wait(10)
        # page load timeout
        cls.driver.set_page_load_timeout(30)

    def test_intro_page(self):
        logger.info("Starting test_intro_page")
        self.intro_page = BuyMeIntroPage(self.driver)
        #self.intro_page.close_intro_banner()
        self.intro_page.click_to_register()
        self.intro_page.register()
        logger.info("test_intro_page completed")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_registration_form(self):
        logger.info("Starting test_registration_form")
        self.registration_form = RegistrationForm(self.driver)
        self.registration_form.fill_in_first_name()
        self.registration_form.fill_in_email_address()
        self.registration_form.fill_in_password()
        self.registration_form.confirm_password()
        self.registration_form.agree_to_terms()
        self.registration_form.submit_registration_form()
        logger.info("test_registration_form completed")

    def test_home_screen(self):
        logger.info("Starting test_home_screen")
        self.home_screen = HomeScreen(self.driver)
        self.home_screen.pick_price_point()
        self.home_screen.pick_region()
        self.home_screen.pick_category()
        self.home_screen.find_gift()
        logger.info("test_home_screen completed")

    def test_pick_business(self):
        self.pick_business = PickBusiness(self.driver)
        self.pick_business.assert_url()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

