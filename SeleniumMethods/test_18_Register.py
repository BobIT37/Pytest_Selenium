from selenium.webdriver import Chrome, ActionChains
import pytest
from time import sleep

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_register(setPath):
    driver.get("http://newtours.demoaut.com/")
    sleep(3)
    driver.maximize_window()

    driver.find_element_by_xpath("//a[contains(text(), 'REGISTER')]").click()
    sleep(2)

    driver.find_element_by_name("firstName").send_keys("python")
    driver.find_element_by_name("lastName").send_keys("selenium")
    driver.find_element_by_name("phone").send_keys("12345676")
    driver.find_element_by_id("userName").send_keys("python@selenium.com")
    sleep(2)

    driver.find_element_by_name("address1").send_keys("Main Road")
    driver.find_element_by_name("city").send_keys("Wayne")
    driver.find_element_by_name("state").send_keys("New Jersey")
    sleep(2)

    driver.find_element_by_name("email").send_keys("python")
    driver.find_element_by_name("password").send_keys("selenium")
    driver.find_element_by_name("confirmPassword").send_keys("selenium")
    sleep(2)

    driver.find_element_by_name("register").click()
    sleep(2)




