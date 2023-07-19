# test_login_ddt_modifying.py
#this py file OR code is as per me RA,
# i made this to open and close web browser again n again inside a loop. BUt was unsuccessful.
# normal loop with hard coded url name, id, pw is working, But below code in which
# variables/parameters/arguments etc r passing between multiple files, the LOOP is NOT working.
#So still modifying....

# specific to selenium version 4.8.3

import pytest
from selenium import webdriver
#frm  python_package.Module_name import class
from pageObjects.LoginPage import LoginPage
#from  package.Module         import class
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:  # Test case , 1 test-case can contain many tests, as demonstrated below.
    baseURL = ReadConfig.getApplicationURL()  # Accessing method getApplicationURL() of class ReadConfig
    path= ".\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()


    def test_login_ddt(self, setup):        # data driven test , 'setup' is Fn. called in this method as parameter,
        self.logger.info("********** Test_002_DDT_Login ************ ")
        self.logger.info("**** Verifying Login DDT test****")

        x = setup    # storing setup as local attribute so that we can pass it to for loop below
        # self.driver = setup  # setup contains "webdriver.Chrome()" passed here by @pytest.fixture() present in "conftest.py" file
        # self.driver.get(self.baseURL)
        # self.lp = LoginPage(self.driver)  # creating object lp of class LoginPage

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print(f"Number of Rows in Excel sheet: {self.rows}")

        list_results = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.driver = x  # setup contains "webdriver.Chrome()" passed here by @pytest.fixture() present in "conftest.py" file
            self.driver.get("http://admin-demo.nopcommerce.com")
            # self.driver.get(self.baseURL)

            self.lp = LoginPage(self.driver)  # creating object lp of class LoginPage

            self.lp.setUserName(self.user)     # will clear username field, then puts new username
            self.lp.setPassword(self.password) # will clear password field, then puts new password
            self.lp.clickLogin()
            time.sleep(5) # after login will wait for 5 seconds for next page to load

            act_title = self.driver.title  # actual title , Variable to store webpage Title/name
            exp_title = "Dashboard / nopCommerce administration"

            # in below 4 conditions we r assuming that- on giving wrong credentials, it will open login pg or
            #..dashboard pg. So no need to close website and reopen at login pg. But what if it opens any 3rd pg,
            #..then we have to close website and reopen at login pg. I tried to do this in below code but i failed.
            #So, try it in spare time, i think some features of selenium.webdriver will be needed that i dont know.
            if act_title==exp_title and self.exp=="Pass":
                self.logger.info("********* 1 I/P set passed *********")
                list_results.append("pass")
                self.lp.clickLogout()

            elif act_title == exp_title and self.exp == "Fail":
                self.logger.info("********* 1 I/P set failed *********")
                self.driver.save_screenshot(".\\Screenshots\\" + "DDT_test_login_right Pg on wrong credentials.png")
                list_results.append("fail")
                self.lp.clickLogout()

            elif act_title != exp_title and self.exp=="Pass":
                self.logger.error("********* 1 I/P set failed *********")
                self.driver.save_screenshot(".\\Screenshots\\" + "DDT_test_login_wrong Pg on right credentials.png")
                list_results.append("fail")

            elif act_title != exp_title and self.exp=="Fail":
                self.logger.info("********* 1 I/P set passed *********")
                list_results.append("pass")

            time.sleep(5)
            self.driver.quit()
            time.sleep(5)

        print (list_results)
        if "fail" in list_results:
            self.logger.error("********* Login DDT test failed*********")
            # self.driver.close()
            assert False
        else:
            self.logger.info("********* Login DDT test Passed*********")
            # self.driver.close()
            assert True

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")


# pytest -v -s --html=Reports/report6.html testCases/test_login_ddt.py
# pytest -v -s testCases/test_login_ddt_modifying.py

