from selenium.webdriver.common.by import By

class Registration:
    radiobtn_socialtitleMr_id = "field-id_gender-1"
    radiobtn_socialtitleMrs_id = "field-id_gender-2"
    txt_fname_id = "field-firstname"
    txt_lname_id = "field-lastname"
    txt_email_id = "field-email"
    txt_pwd_id = "field-password"
    txt_dob_id = "field-birthday"
    chk_offers_name = "optin"
    chk_termsAndCond_name = "psgdpr"
    chk_newsletter_name = "newsletter"
    chk_privacy_name = "customer_privacy"
    btn_save_xpath = "//input[@name='submitCreate']/following::button"


    def __init__(self,driver):
        self.driver = driver

    def clickSocialTitleMr(self):
        self.driver.find_element(By.ID,self.radiobtn_socialtitleMr_id).click()

    def clickSocialTitleMrs(self):
        self.driver.find_element(By.ID,self.radiobtn_socialtitleMrs_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txt_fname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txt_lname_id).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.ID,self.txt_pwd_id).send_keys(pwd)

    def setDOB(self,dob):
        self.driver.find_element(By.ID,self.txt_dob_id).send_keys(dob)

    def clickOffers(self):
        self.driver.find_element(By.NAME,self.chk_offers_name).click()

    def clickTerms(self):
        self.driver.find_element(By.NAME,self.chk_termsAndCond_name).click()

    def clickNewsLetter(self):
        self.driver.find_element(By.NAME,self.chk_newsletter_name).click()

    def clickPrivacy(self):
        self.driver.find_element(By.NAME,self.chk_privacy_name).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()