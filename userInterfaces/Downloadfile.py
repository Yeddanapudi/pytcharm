import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#driver.execute_script("window.ScrollBY(0,500)","")
driver.find_element_by_id("textbox").send_keys("manual testing")
time.sleep(2)
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
