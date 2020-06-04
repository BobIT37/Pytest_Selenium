from selenium import webdriver
from time import sleep

path = "/Users/bobit/Documents/Drivers/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()

#byId

'''
driver.get("https://app.hubspot.com/login")
sleep(5)

driver.find_element_by_id("username").send_keys("boblerry@yahoo.com")
driver.find_element_by_id("password").send_keys("test12345")
driver.find_element_by_id("loginBtn").click()


'''


#by name
'''
driver.get("https://classic.crmpro.com/login.cfm")
driver.find_element_by_name("username").send_keys("boblerry@yahoo.com")
driver.find_element_by_name("password").send_keys("test12345")
'''

#link and partiallink

driver.get("https://app.hubspot.com/login")
sleep(5)

#driver.find_element_by_link_text("Sign up").click()
#driver.find_element_by_partial_link_text("Sign").click()

#by className
#    form-control private-form__control login-email
#driver.find_element_by_class_name("login-email").send_keys("boby@gmail.com")

#cssSelector
#driver.find_element_by_css_selector("#username").send_keys("boby@gmail.com")

#xpath
driver.find_element_by_xpath("//input[@id='username']").send_keys("bobyy@sample.com")


