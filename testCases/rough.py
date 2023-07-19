from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

time.sleep(0)

# create WEBDRIVER OBJECT and save it in 'd', when chrome driver is stored in downloads folder

for i in range(0, 4):
    d = webdriver.Chrome(executable_path="C:\\Users\\admin\\\chromedriver_win32\\chromedriver.exe")
    d.get("https://www.google.com/")  # getting/opening a url
    d.close()  # will act as d.quit() also becoz no other tab/webpage is open in browser

    e = webdriver.Chrome(executable_path="C:\\Users\\admin\\\chromedriver_win32\\chromedriver.exe")
    e.get("https://www.facebook.com/")  # getting/opening a url
    e.close()
    time.sleep(5)

