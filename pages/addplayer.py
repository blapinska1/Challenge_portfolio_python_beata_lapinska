from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
    Add_player_xpath = "//*[text()='Add player']"
    expected_title = "Add player"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def click_on_add_player(self):
        self.click_on_the_element(self.Add_player_xpath)
        time.sleep(5)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title
pass
