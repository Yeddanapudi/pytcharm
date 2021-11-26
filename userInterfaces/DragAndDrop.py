from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(0)
drag=driver.find_element_by_id("draggable")
drop=driver.find_element_by_id("droppable")
actions=ActionChains(driver)
actions.drag_and_drop(drag,drop).perform()

