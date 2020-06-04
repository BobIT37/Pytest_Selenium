from selenium.webdriver import Chrome
import pytest
from time import sleep

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    yield
    driver.quit()

def test_login_invalid_data(setPath):

    driver.find_element_by_id("username").send_keys("ilhan@sample.com")
    sleep(2)
    driver.find_element_by_id("password").send_keys("test12345")
    sleep(2)
    driver.find_element_by_id("loginBtn").click()
    sleep(2)