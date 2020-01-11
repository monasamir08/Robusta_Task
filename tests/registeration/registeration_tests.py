from pages.registeration.registeration_page import Registeration_Page
from utilities.read_data import getCSVData
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class Register(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.registeration = Registeration_Page(self.driver)
        self.ts = TestStatus(self.driver)


    # @pytest.mark.run(order=1)
    # def test_InvalidRegisteration(self):
    #     self.registeration.clickSignUP1()
    #     result = self.registeration.ValidateFailedSignUP()
    #     self.ts.markFinal("Invalid Sign Up", result, "Passed")

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_ValidSignUP(self, firstName, lastName, email, password, confirmPassword):
        self.registeration.clickSignUP1()
        self.registeration.Register(firstName, lastName, email, password, confirmPassword)
        result = self.registeration.succseefullRegistration()
        self.ts.markFinal("Valid Sign UP", result, "Passed")
