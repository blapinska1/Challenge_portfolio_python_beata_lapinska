import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSignOut(unittest.TestCase):
# user01@getnada.com pass: Test-1234
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_out(self):
        user_login = LoginPage(self.driver)
        user_login.assert_scout_panel_text()
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_login()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_sign_out()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
