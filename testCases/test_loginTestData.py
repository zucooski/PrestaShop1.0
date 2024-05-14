import time

import pytest
from pageObjects import HomePage,SignInPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.ExcelUtilities import *
import os

class TestLogin:
    baseurl = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    pwd = ReadConfig.getPassword()
    logger = LogGen.loggen()
    list = []

    def testLogin001(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("Going to Application.........")
        self.driver.get(self.baseurl)
        self.driver.switch_to.frame(0)

        hp = HomePage.HomePage(self.driver)
        self.logger.info("Clicking Signin.........")
        hp.clickSignIn()

        sip = SignInPage.SignInPage(self.driver)
        self.logger.info("Filling testdata.........")

        r = getRowCount()
        c = getColumnCount()

        sip.setEmail(self.email)
        sip.setPassword(self.pwd)
        sip.clickShowPassword()
        # time.sleep(10)
        self.logger.info("Clicking signin.........")
        sip.clickSignIn()

        try:
            if hp.isdisplaySignOut()==True:
                self.driver.close()
                assert True
        except:
            self.logger.info("Warning Test has failed.........")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"/screenshots/"+"testLogin_001.png")
            self.driver.get_screenshot_as_base64() #don't know its usage
            self.driver.close()
            assert False
        self.logger.info("test_login Completed")




