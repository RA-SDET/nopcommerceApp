from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

login_pg_title = driver.title
print(login_pg_title)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()

login2_pg_title = driver.title
print(login2_pg_title)
str1 = driver.find_element(By.XPATH, "//div[@class='_9ay7']").text
print (str1)

z = "Log in to Facebook"
str2 ="The email address or mobile number you entered isn't connected to an account. Find your account and log in."

if (login2_pg_title == z) and (str1 == str2):
    print("test case failed, instead of going to my facebook page its going to Log in to Facebook AGAIN page")

    