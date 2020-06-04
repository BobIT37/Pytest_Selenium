from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_explicitly_wait(setPath):
    driver.maximize_window()
    driver.get("http://newtours.demoaut.com/")

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "userName")))
    driver.find_element_by_name("userName").send_keys("siliconeLabs")
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    driver.find_element_by_name("password").send_keys("siliconeLabs")
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "login")))
    driver.find_element_by_name("login").click()

    #implicitly wait
    driver.implicitly_wait(20)