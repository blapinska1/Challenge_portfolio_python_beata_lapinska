import os
import unittest
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.addplayer import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPLayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_click_on_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_login()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        add_player = AddPlayer(self.driver)
        add_player.title_of_page()

        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
