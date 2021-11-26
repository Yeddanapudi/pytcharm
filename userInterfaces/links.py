from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

links=driver.find_elements_by_tag_name("a")
print(" no of links : ",len(links))
for a1 in links:
  print(a1.text)
a1.click()

driver.back()
driver.find_elements_by_tag_name("a")


