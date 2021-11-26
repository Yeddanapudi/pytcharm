from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

drop=driver.find_element_by_id("nav-xshop")
select=Select(drop)
items=select.options
for a2 in items:
    print(items.text)




links=driver.find_element_by_id("searchDropdownBox")
select=Select(links)
test=select.options
for a1 in test:
    print(a1.text)


