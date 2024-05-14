from selenium.webdriver.common.by import By

class SignInPage:
    txt_email_id = "field-email"
    txt_pwd_id = "field-password"
    btn_pwdShow_xpath = "//button[@data-action='show-password']"
    btn_signIn_id = "submit-login"
    lnk_forgotpwd_partiallnktxt = "Forgot your password?"
    lnk_createAccount_xpath = "//*[@id='content']/div/a"

    def __init__(self,driver):
        self.driver = driver

    def clickCreateAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_createAccount_xpath).click()

    def setEmail(self,email):
        txtEmail= self.driver.find_element(By.ID,self.txt_email_id)
        txtEmail.clear()
        txtEmail.send_keys(email)

    def setPassword(self,pwd):
        txtpwd=self.driver.find_element(By.ID,self.txt_pwd_id)
        txtpwd.clear()
        txtpwd.send_keys(pwd)
    def clickSignIn(self):
        self.driver.find_element(By.ID,self.btn_signIn_id).click()

    def clickShowPassword(self):
        self.driver.find_element(By.XPATH,self.btn_pwdShow_xpath).click()