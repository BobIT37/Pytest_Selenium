from selenium.webdriver import Chrome
from time import sleep
import pytest

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_login_invalid_data(setPath):
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    username = driver.find_element_by_id("username")
    add_highlight(username)
    username.send_keys("sammy@sample.com")
    sleep(2)
    password = driver.find_element_by_id("password")
    add_highlight(password)
    password.send_keys("test12345")
    sleep(2)
    login = driver.find_element_by_id("loginBtn")
    add_highlight(login)
    login.click()
    sleep(2)
 
def add_highlight(element):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                          "background: yellow; border: 3px solid red;")