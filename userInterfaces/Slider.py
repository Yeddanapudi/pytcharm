from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.snapdeal.com/products/appliances-choppers-blenders")
driver.maximize_window()
#driver.switch_to.frame(0)
s1=driver.find_element_by_xpath("//*[@id='content_wrapper']/div[9]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div")
actions=ActionChains(driver)
y=s1.location

actions.drag_and_drop_by_offset(s1,y,200).perform()

