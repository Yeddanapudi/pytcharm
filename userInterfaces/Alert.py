import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.maximize_window()


driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a").click()
#driver.find_element_by_class_name("btn btn-danger").click()
driver.find_element_by_xpath("//*[@id='OKTab']/button").click()
test=driver.switch_to.alert
print(test.text)
test.accept()
time.sleep(2)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='CancelTab']/button").click()
test1=driver.switch_to.alert
print(test1.text)
time.sleep(2)
test1.accept()
time.sleep(2)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a").click()
driver.find_element_by_xpath("//*[@id='Textbox']/button").click()
test2=driver.switch_to.alert
print(test2.text)
time.sleep(2)
#test2.send_keys("automation tools")
test2.accept()
time.sleep(2)
msg=driver.find_element_by_id("demo1").text
print(msg)


driver.current_window_handle------currnet window id

driver.window_handles-------------child window ids





