from selenium.webdriver.common.by import By

class HomePage:
    lnk_signin_xpath = "//*[@id='_desktop_user_info']/div/a"
    lnk_signout_xpath = "//a[@class='logout hidden-sm-down']"

    def __init__(self,driver):
        self.driver = driver

    def clickSignIn(self):
        self.driver.find_element(By.XPATH,self.lnk_signin_xpath).click()

    def isdisplaySignOut(self):
        self.driver.find_element(By.XPATH,self.lnk_signout_xpath).is_displayed()
