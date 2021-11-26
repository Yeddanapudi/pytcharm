import time

from selenium import webdriver
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
#from Tools.scripts.mailerdaemon import x

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://demoqa.com/text-box");
driver.maximize_window()
x=input("enter your name")
driver.find_element_by_id("userName").send_keys(x)
print(x)
y=input("enter yoir mail id")
driver.find_element_by_id("userEmail").send_keys(y)
print(y)

driver.find_element_by_id("currentAddress").send_keys("kukatpally hyderabad")
driver.find_element_by_id(("permanentAddress")).send_keys("vijayawadaandhracpradesh520001")

driver.find_element_by_xpath("//*[@id='submit']").click()

test=driver.find_element_by_xpath("//*[@id='output']/div").text
print(test)

