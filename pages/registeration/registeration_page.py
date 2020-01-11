import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class Registeration_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    _signUP_Button1 = "//a[contains(text(),'sign up')]"  #xpath
    _firstName_Field = "firstName" #id
    _lastName_Field = "lastName"  #id
    _email_Field = "email" #id
    _password_Field = "password"  #id
    _confirmPassword_Field = "confirmPassword" #id
    _termsCheckBox_Field = "terms" #id
    _signUP_Button2 = "//span[contains(text(),'Sign up')]/parent::button" #xpath
    __firstName_em = "//div[contains(text(),'Please enter your First Name')]" #xpath
    __lastName_em = "//div[contains(text(),'Please enter your Last Name')]" #xpath
    __email_em = "//div[contains(text(),'Please enter your Email')]" #xpath
    __password_em = "//div[contains(text(),'Please enter your Password')]" #xpath
    __terms_em = "//div[contains(text(),'Please accept terms and conditions')]" #xpath


    def clickSignUP1(self):
        self.elementClick(self._signUP_Button1, locatorType="xpath")

    def enterFirstName(self, firstName):
        self.sendKeys(firstName, self._firstName_Field)

    def enterLastName(self, lastName):
        self.sendKeys(lastName, self._lastName_Field)

    def enterEmail(self, lastName):
        self.sendKeys(lastName, self._email_Field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field)

    def enterConfirmPassword(self, confrimPassword):
        self.sendKeys(confrimPassword, self._confirmPassword_Field)

    def checkBoxClick(self):
        self.elementClick(self._termsCheckBox_Field, locatorType="id")

    def clickSignUP2(self):
        self.elementClick(self._signUP_Button2, locatorType="xpath")

    def ValidateFailedSignUP(self):
        self.waitForElement(self._signUP_Button2, locatorType="xpath")
        self.clickSignUP2()
        firstName_em = self.isElementPresent(self.__firstName_em, locatorType="xpath")
        lastName_em = self.isElementPresent(self.__lastName_em, locatorType="xpath")
        email_em = self.isElementPresent(self.__email_em, locatorType="xpath")
        password_em = self.isElementPresent(self.__password_em, locatorType="xpath")
        terms_em = self.isElementPresent(self.__terms_em, locatorType="xpath")
        if firstName_em is True and lastName_em is True and email_em is True and password_em is True and terms_em is True:
            return True

    def Register(self, firstName, lastName, email, password, confirmPassword):
        #self.waitForElement(self._firstName_Field, locatorType="xpath")
        self.enterFirstName(firstName)
        self.enterLastName(lastName)
        self.enterEmail(email)
        self.enterPassword(password)
        self.enterConfirmPassword(confirmPassword)
        self.webScroll(500, "down")
        self.waitForElement(self._termsCheckBox_Field, locatorType="xpath")
        self.checkBoxClick()
        self.clickSignUP2()

    def succseefullRegistration(self):
        postJobExist = self.isElementPresent("//a[contains(text(),'Post a Job')]", locatorType="xpath")
        return postJobExist

