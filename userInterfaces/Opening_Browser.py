import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#String x=inputbox("enter the name ")
driver.find_element_by_name("userName").send_keys("mercury")

driver.find_element_by_name("password").send_keys("mercury")
#time.sleep(1000)
driver.find_element_by_name("submit").click()

driver.close()



