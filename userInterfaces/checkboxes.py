from selenium import webdriver
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
#from Tools.scripts.mailerdaemon import x
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://demoqa.com/radio-button");
driver.maximize_window()

status=driver.find_element_by_id("yesRadio").is_selected()

print(status)

status1=driver.find_element_by_id("yesRadio").click()

print(status1)



