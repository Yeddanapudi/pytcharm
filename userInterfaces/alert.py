import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import  Keys

driver=webdriver.Chrome(executable_path="c:\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='OKTab']/button").click()
time.sleep(3)

print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()




