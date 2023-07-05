from pages.base_page import BasePage

# //*[contains(@type,'sub')]
# "//*[text()='Main page']"
class MatchForm(BasePage):

    Matches_xpath = "//*[text()='Matches']"
    Reports_xpath = "//*[text()='Reports']"
    Player_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    Match_home_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    League_input_xpath = "//input[@name='league']"
    Date_input_xpath = "//input[@name='date']"
    Rating_input_xpath = "//input[@name='rating']"
    Submit_label_xpath = "//*[text()='Submit']"
    Submit_button_xpath = "//*[contains(@class,'MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary')]"
    Scouts_Panel_xpath = "//*[contains(@class,'MuiTypography-root jss7 MuiTypography-h6 MuiTypography-noWrap')]"



pass