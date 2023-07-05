from pages.base_page import BasePage

# //*[contains(@type,'sub')]
class Dashboard(BasePage):
    Main_page_xpath = "//*[text()='Main page']"
    Players_xpath = "//*[text()='Players']"
    Language_xpath ="//*[text()='Polski']"
    Sign_out_xpath= "//*[text()='Sign out']"
    Players_count_xpath ="//*[@id="__next"]/div[1]/main/div[2]/div[1]/div/div[1]"
    Add_player_xpath ="//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button"
    Futbol_Kolektyw_img_xpath = "//*[contains(@class,'MuiCardMedia-root')]"
    _dev_team_contact_xpath ="//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a"
    Scouts_Panel_xpath = "//*[contains(@class,'MuiTypography-root jss16 MuiTypography-h6 MuiTypography-noWrap')]"
    Last_updated_report_xpath = "//*[text()='Last updated report']"
pass
