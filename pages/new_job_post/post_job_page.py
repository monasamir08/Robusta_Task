import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class Post_Job_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    __jobTitle = "jobTitle" #id
    __jobDescription = "jobDescription" #id
    __jobCategory = "//div[@class='ant-select-selection ant-select-selection--single']" #xpath
    __graphicsDesign = "//li[contains(text(),'Graphics & Design')]"  # xpath
    __videosAnimation = "//li[contains(text(),'Videos & Animation')]"  # xpath
    __writingTranslation = "//li[contains(text(),'Writing & Translation')]"  # xpath
    __requiredSkills = "//input[@class='ant-select-search__field']" #xpath
    __selectDate = "//input[@placeholder='Select date']" #xpath
    __pickMonth = "//a[@title='Choose a month']" #xpath
    __pickYear = "//a[@title='Choose a year']" #xpath
    __slider1 = "//div[@class='ant-slider-handle ant-slider-handle-1 ant-tooltip-open']" #xpath
    __slider2 = "//div[@class='ant-slider-handle ant-slider-handle-2 ant-tooltip-open']" #xpath
    __nextButton = "//span[contains(text(),'Next')]//parent::button" #xpath
    __beginButton = "//button[@type='submit']" #xpath
    __postJobButton = "//button[contains(text(),'Post Job')]" #xpath


    def enterJobTitle(self, jobTitle):
        self.sendKeys(jobTitle, self.__jobTitle)

    def enterJobDescription(self, jobDescription):
        self.sendKeys(jobDescription, self.__jobDescription)

    def enterJobCategory(self, Category):
        self.elementClick(self.__jobCategory, locatorType="xpath")
        self.elementClick("//li[contains(text(),'%s')]" % Category, locatorType="xpath")

    def enterSkills(self, skill):
        self.elementClick(self.__requiredSkills, locatorType="xpath")
        self.sendKeys(skill, self.__requiredSkills, locatorType="xpath")

    def enterDueDate(self, day, Month, year):
        self.elementClick(self.__selectDate, locatorType="xpath")
        self.elementClick(self.__pickMonth, locatorType="xpath")
        self.elementClick("//td[@title='%s']" % Month, locatorType="xpath")
        self.elementClick(self.__pickYear, locatorType="xpath")
        self.elementClick("//td[@title='%s']" % year, locatorType="xpath")
        self.elementClick("//div[@class='ant-calendar-date' and contains(text(),'%s')]" % day, locatorType="xpath")
        time.sleep(5)

    def budgetRange(self, xoffset1, yoffset1, xoffset2, yoffset2):
        self.moveSlider(self.__slider1, "xpath", xoffset1, yoffset1)
        self.moveSlider(self.__slider2, "xpath", xoffset2, yoffset2)

    def clickNext(self):
        self.elementClick(self.__nextButton, locatorType="xpath")

    def clickBegin(self):
        self.waitForElement(self.__beginButton, locatorType="xpath")
        time.sleep(3)
        self.elementClick(self.__beginButton, locatorType="xpath")

    def clickPostJob(self):
        self.waitForElement(self.__beginButton, locatorType="xpath")
        time.sleep(3)
        self.elementClick(self.__postJobButton, locatorType="xpath")

    def postJob(self, jobTitle, jobDescription, jobCategory, skill, day, Mon, Year, xoffset1, yoffset1, xoffset2, yoffset2):
        time.sleep(3)
        self.enterJobTitle(jobTitle)
        self.enterJobDescription(jobDescription)
        self.webScroll(500, "down")
        self.enterSkills(skill)
        self.clickEnter(self.__requiredSkills, "xpath")
        self.enterJobCategory(jobCategory)
        self.enterDueDate(day, Mon, Year)
        self.budgetRange(xoffset1, yoffset1, xoffset2, yoffset2)
        self.clickNext()
        self.clickBegin()
        self.clickPostJob()
        time.sleep(3)

