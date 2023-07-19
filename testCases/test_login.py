# specific to selenium version 4.8.3
# from selenium.webdriver.common.by import By
# Above import is not needed here, but in python file which is using 'By' in its code lines.

import pytest
from selenium import webdriver

#frm  python_package.Module_name import class
from pageObjects.LoginPage import LoginPage
#from  package.Module         import class
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:  # Test case , 1 test-case can contain many tests, as demonstrated below.
    baseURL = ReadConfig.getApplicationURL()  # Accessing method getApplicationURL() of class ReadConfig
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):    # test
        self.logger.info("********** Test_001_Login ************ ")
        self.logger.info("*********** Verifying Home page title ************")
        self.driver = setup  # setup contains "webdriver.Chrome()" passed here by @pytest.fixture() present in "conftest.py" file
        self.driver.get(self.baseURL)
        act_title = self.driver.title       # actual title , Variable to store webpage Title/name
        if act_title == "Your store. Login":
                                 # test Pass, message sent to pytest/framework shayad
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")  #capturing & saving screenshot on test fail, inside a png file
            self.driver.close()
            assert False                    # test Fail, message sent to pytest/framework shayad

    def test_login(self, setup):            # test , 'setup' is Fn. called in this method as parameter,
                                            #..if setup is not found in this .py file then pytest will
                                            #..search for it in conftest.py file and if found there,
                                            #..then what whatever this Fn. returs will be passed here
                                            #..as parameter.
                                            #Note- for pytest to locate conftest.py ,it should be in
                                            # same directory/folder as the test .py file.
        self.logger.info("****Started Login Test****")
        self.driver = setup  # setup contains "webdriver.Chrome()" passed here by @pytest.fixture() present in "conftest.py" file
        # self.driver.implicitly_wait(10)   # I added on my own, but not needed. So, commented out.
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)    # creating object lp of class LoginPage
        self.lp.setUserName(self.username)  # using obj lp to call setUserName() methodo f class LoginPage, Also passing parameter "username" to it.
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title       # actual title , Variable to store webpage Title/name
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")  #capturing & saving screenshot on test fail, inside a png file
                              # OR use (".\\Screenshots\\test_login.png") # same code as above, RELATIVE PATH
                              # OR use ("C:\\Users\\ADMIN\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_login.png")  # ABSOLUTE PATH
            self.driver.close()
            assert False


'''
explaining code line->
self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                        This . above represent current project address,
                        which contains "Screenshots" folder.
                        + means concatination of folder's complete address with screenshot file name.
                        Screenshot file name is given by us as "test_login.png".
                        Always give screenshot name exactly same as test name.

(".\\Screenshots\\" + "test_login.png") == (".\\Screenshots\\test_login.png") RELATIVE PATH
                                        == ("current project address\\Screenshots\\test_login.png")  RELATIVE PATH
                                        == ("C:\\Users\\ADMIN\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_login.png")  ABSOLUTE PATH

ITS ALWAYS BETTER TO USE ABOVE CODE(relative path) INSTEAD OF GIVING ABSOLUTE PATH,
THIS MAKES YR PROJECT PORTABLE TO MOVE FROM ONE LOCATION TO ANOTHER AND DIRECTLY
RUN IT WITHOUT CHANGING CODES RELATED TO ABSOLUTE PATH/ADDRESS.

'''