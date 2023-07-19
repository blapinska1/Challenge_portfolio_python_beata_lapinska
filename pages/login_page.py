from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    remind_password_xpath = "//*[text()= 'Remind password']"
    remind_email_xpath = "//*[@name='email']"
    remind_send_button = "//*[text()= 'Send']"
    scouts_panel_xpath = "//*[text()= 'Scouts Panel']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    expected_title = "Scouts panel - sign in"
    expected_text = "Scouts Panel"
    no_credential_xpath = "//*[text()='Please provide your username or your e-mail.']"
    expected_no_credentials = "Please provide your username or your e-mail."
    incorrect_password_xpath = "//*[text()='Identifier or password invalid.']"
    expected_incorrect_password = "Identifier or password invalid."

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

    def assert_no_credentials(self):
        self.assert_element_text(self.driver, self.no_credential_xpath, self.expected_no_credentials)

    def assert_incorrect_password(self):
        self.assert_element_text(self.driver, self.incorrect_password_xpath, self.expected_incorrect_password)

    def click_remind_password(self):
        self.click_on_the_element(self.remind_password_xpath)

    def type_in_remind_email(self, email):
        self.field_send_keys(self.remind_email_xpath, email)

    def click_remind_send(self):
        self.click_on_the_element(self.remind_send_button)
