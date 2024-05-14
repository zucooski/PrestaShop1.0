import os
import time

from pageObjects.HomePage import HomePage
from pageObjects.RegistrationPage import Registration
from pageObjects.SignInPage import SignInPage
import pytest
from utilities import randomString


class TestRegistration:
    baseurl = "https://demo.prestashop.com/"

    def testreg001(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.driver.switch_to.frame(0)

        hp = HomePage(self.driver)
        hp.clickSignIn()

        sip = SignInPage(self.driver)
        sip.clickCreateAccount()

        rp = Registration(self.driver)
        rp.clickSocialTitleMr()
        rp.setFirstName("Jack")
        rp.setLastName("Phillips")
        self.email = randomString.randomStringGenerator()+"@gmail.com"
        rp.setEmail(self.email)
        rp.setPassword("jackphillips@777")
        rp.setDOB("01/01/1999")
        rp.clickOffers()
        rp.clickTerms()
        rp.clickNewsLetter()
        rp.clickPrivacy()
        rp.clickSave()
        try:
            if hp.isdisplaySignOut()==True:
                self.driver.close()
                assert True
        except:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"/screenshots/"+"testreg001.png")
            self.driver.close()
            assert False





