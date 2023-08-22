import logging
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from BuyMe import BuyMeIntroPage, RegistrationForm#, HomeScreen


# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logging.basicConfig(
#                     filename='logfile.log', # set the output file
#                     filemode='a', # set it to append rather than overwrite
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', # determine the format of the output message
#                     datefmt='%H:%M:%S', # determine the format of the output time
#                     level=logging.ERROR) # determine the minimum message level it will accept
#
# logger.info("Logged INFO message"'")
# logger.warning("Logged WARNING message")
# logger.error('Logged ERROR message')

class test_Buyme(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("C:\\Users\\shiri pc\\Desktop\\chromedriver_win32\\chromedriver.exe"))
        self.driver.get("https://buyme.co.il/")
        # implicit wait
        self.driver.implicitly_wait(10)
        # page load timeout
        self.driver.set_page_load_timeout(30)

    def test_intro_page(self):
        self.intro_page = BuyMeIntroPage(self.driver)
        #self.intro_page.close_intro_banner()
        self.intro_page.click_to_register()
        self.intro_page.register()

    def test_registration_form(self):
        self.registration_form = RegistrationForm(self.driver)
        self.registration_form.fill_in_first_name()
        self.registration_form.fill_in_email_address()
        self.registration_form.fill_in_password()
        self.registration_form.confirm_password()
        self.registration_form.agree_to_terms()
        self.registration_form.submit_registration_form()

    # def test_home_screen(self):
    #     self.home_screen = HomeScreen(self.driver)
    #     self.home_screen.pick_price_point()
    #     self.home_screen.pick_region()
    #     self.home_screen.pick_category()
    #     self.home_screen.find_gift()

    def tearDown(self):
        self.driver.quit()

