from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
link=driver.find_element_by_link_text("Gmail")
actions=ActionChains(driver)
actions.context_click(link).send_keus("B").perform()
