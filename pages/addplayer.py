from pages.base_page import BasePage


class AddPlayer(BasePage):
    Add_player_xpath = "//*[text()='Add player']"
    expected_title = "Add player"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add/"
    add_player_name = "//*[@name='name']"
    add_player_last_name = "//*[@name='surname']"
    add_player_birth_date = "//*[@name='age']"
    add_player_position = "//*[@name='mainPosition']"
    add_player_leg = "//*[@id='mui-component-select-leg']"
    add_player_right_leg = "//*[text()='Right leg']"
    add_player_left_leg = "//*[text()='Left leg']"
    add_player_submit_button = "//*[text()= 'Submit']"
    players_xpath = "//*[text()= 'Players']"

    def click_on_add_player(self):
        self.wait_for_element_to_be_clickable(self.Add_player_xpath)
        self.click_on_the_element(self.Add_player_xpath)

    def click_leg_choice(self):
        self.wait_for_visibility_of_element_located(self.add_player_leg)
        self.click_on_the_element(self.add_player_leg)

    def click_left_leg(self):
        self.wait_for_visibility_of_element_located(self.add_player_left_leg)
        self.click_on_the_element(self.add_player_left_leg)

    def click_right_leg(self):
        self.wait_for_visibility_of_element_located(self.add_player_right_leg)
        self.click_on_the_element(self.add_player_right_leg)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.players_xpath)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_first_name(self, first_name):
        self.field_send_keys(self.add_player_name, first_name)

    def type_in_last_name(self, last_name):
        self.field_send_keys(self.add_player_last_name, last_name)

    def type_in_birth_date(self, birth_date):
        self.field_send_keys(self.add_player_birth_date, birth_date)

    def type_in_position(self, position):
        self.field_send_keys(self.add_player_position, position)

    def click_submit(self):
        self.click_on_the_element(self.add_player_submit_button)
        self.wait_for_element_to_be_clickable(self.add_player_submit_button)

    def click_players(self):
        self.click_on_the_element(self.players_xpath)




pass
