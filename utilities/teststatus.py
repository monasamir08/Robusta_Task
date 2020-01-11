import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASSED")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultList.append("FAILED")
                    self.log.error("### VERIFICATION FAILURE :: " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAILED")
                self.log.error("### VERIFICATION FAILURE :: " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAILED")
            self.log.error("### EXCEPTION OCCURRED ")
            self.screenShot(resultMessage)


    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        if "FAILED" in self.resultList:
            self.log.error(testName + "Test Failed")
            self.resultList.clear()
            assert True is False
        else:
            self.log.info(testName + "Test Passed")
            self.resultList.clear()
            assert True is True
