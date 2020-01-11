from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class LoginPage(BasePage):

    # log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    _loginButton1 = "//nav/ul[2]/li[1]/a"
    _loginName_Field = "email"
    _password_Field = "password"
    _loginButton2 = "//span[contains(text(),'Begin')]/parent::button"

    def clickLogin1(self):
        self.elementClick(self._loginButton1, locatorType="xpath")

    def enterLoginName(self, loginName):
        self.sendKeys(loginName, self._loginName_Field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field)

    def clickLogin2(self):
         self.elementClick(self._loginButton2, locatorType="xpath")

    def login(self, username, password):
        time.sleep(5)
        self.clickLogin1()
        time.sleep(3)
        self.enterLoginName(username)
        self.enterPassword(password)
        self.clickLogin2()

    def SuccessfullLogin(self):
        result = self.isElementPresent("//a[contains(text(),'Post a Job')]", locatorType="xpath")
        return result