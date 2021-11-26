import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[1]/input").send_keys("test123")
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[2]/input").send_keys("ball123")
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("kukatpally")
#driver.find_element_by_xpath("//*[@id='eid'']/input").send_keys("yeddanapudi1979@yahoo.com")
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[4]/div/input").send_keys("8978882841")
driver.find_element_by_name("radiooptions").click()
driver.find_element_by_id("checkbox1").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='msdn']/div").send_keys("English")
driver.find_element_by_id("Skills").send_keys("C++")
driver.find_element_by_id("select2-country-container").send_keys("INDIA")

