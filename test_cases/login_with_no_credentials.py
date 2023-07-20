import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginNoCreds(unittest.TestCase):
# user01@getnada.com pass: Test-1234
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_no_credentials(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('')
        user_login.type_in_password('')
        user_login.click_login()
        user_login.assert_no_credentials()

        time.sleep(5)
    @classmethod
    def tearDown(self):
        self.driver.quit()
