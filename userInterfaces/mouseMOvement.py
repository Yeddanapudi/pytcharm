import time
from lib2to3.pgen2.driver import Driver

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
time.sleep(2)
driver.find_element_by_name("Submit").click();

#xpath for admin
admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
admin.click()\

#ppath for user management
useradmin=driver.find_element_by_id("menu_admin_UserManagement")
useradmin.click()
#xpath for user

users=driver.find_element_by_id("menu_admin_viewSystemUsers")
users.click()

actions=ActionChains(Driver)
actions.move_to_element(admin).move_to_element(useradmin).move_to_element(users).perform()




