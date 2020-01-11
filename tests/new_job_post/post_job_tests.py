from pages.new_job_post.post_job_page import Post_Job_Page
from pages.home.login_page import LoginPage
from utilities.read_data import getCSVData
import utilities.custom_logger as cl
import logging
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class PostJob(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.postjob = Post_Job_Page(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_ValidSignUP(self, firstName, lastName, email, password, confirmPassword):
        self.registeration.clickSignUP1()
        self.registeration.Register(firstName, lastName, email, password, confirmPassword)
        result = self.registeration.succseefullRegistration()
        self.ts.markFinal("Valid Sign UP ", result, "Passed")

    @pytest.mark.run(order=2)
    def test_Login(self):
        self.lp.login("test15@test.com", "Test_1234")


    @pytest.mark.run(order=3)
    @data(*getCSVData("testdata2.csv"))
    @unpack
    def test_postJob(self, jobTitle, jobDescription, jobCategory, jobSkill, day, Month, Year):
        self.postjob.postJob(jobTitle, jobDescription, jobCategory, jobSkill, day, Month, Year, -105, 0, 105, 0)


