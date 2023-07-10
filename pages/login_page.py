from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    scouts_panel_xpath = "//*[text()= 'Scouts Panel']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    expected_title = "Scouts panel - sign in"
    expected_text = "Scout Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_login(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def assert_scout_panel_text(self):
        self.assert_element_text(self.driver, self.scouts_panel_xpath, self.expected_text)

