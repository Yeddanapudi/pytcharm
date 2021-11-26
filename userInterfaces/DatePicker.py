import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element_by_id("datepicker").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[5]/a").click()


