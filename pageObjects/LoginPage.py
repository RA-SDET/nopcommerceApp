# specific to selenium version 4.8.3
#from selenium import webdriver  <-this import is not needed here, becoz below code is not calling webdriver sub-module from selenium module

from selenium.webdriver.common.by import By  # Without importing this 'By' will not work in below code


class LoginPage:   # whole webpage as a class
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver #this parameter driver is passed by code which is calling class LoginPage.

    def setUserName(self, username):
        #self.driver.find_element_by_id(self.textbox_username_id).clear()             # used by Trainer,But works only in older version of Selenium
        #self.driver.find_element_by_id(self.textbox_username_id).send_keys(username) # used by Trainer,But works only in older version of Selenium
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        #self.driver.find_element_by_id(self.textbox_password_id).clear()             # used by Trainer,But works only in older version of Selenium
        #self.driver.find_element_by_id(self.textbox_password_id).send_keys(password) # used by Trainer,But works only in older version of Selenium
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        #self.driver.find_element_by_xpath(self.button_login_xpath).click()           # used by Trainer,But works only in older version of Selenium
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        #self.driver.find_element_by_link_text(self.link_logout_linktext).click()     # used by Trainer,But works only in older version of Selenium
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
