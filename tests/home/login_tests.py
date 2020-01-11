from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_invalidLoginInvalidData(self):

        self.lp.login("eg_melgamil", "Voda_2020")
        result = self.lp.LoginFailedInvalidData()
        self.ts.markFinal("Test Invalid Login 2: ", result, "Invalid login name/password. was displayed successfully")

    @pytest.mark.run(order=3)
    def test_validLogin(self):

        self.lp.login("eg_melgamil", "Voda!2020")
        result1 = self.lp.verifyLoginPageTitle()
        self.ts.mark(result1, "Title is Incorrect")
        result2 = self.lp.SuccessfullLogin()
        self.ts.markFinal("Test Valid Login:", result2, "Login Successful")

    @pytest.mark.run(order=1)
    def test_invalidLoginEmptyFields(self):

        self.lp.login()
        result = self.lp.LoginFailedEmptyFields()
        self.ts.markFinal("Test Invalid Login 1: ", result, "Login name and password must not be empty. was displayed successfully")


if __name__ == '__main__':
    unittest.main()
