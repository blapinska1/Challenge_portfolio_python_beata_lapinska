import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPassword(unittest.TestCase):
# user01@getnada.com pass: Test-1234
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        user_login.click_remind_password()
        user_login.type_in_remind_email('blapinska@gmail.com')
        user_login.click_remind_send()
        time.sleep(5)
    @classmethod
    def tearDown(self):
        self.driver.quit()
