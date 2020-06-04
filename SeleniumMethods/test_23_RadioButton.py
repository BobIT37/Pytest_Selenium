from selenium.webdriver import Chrome
import pytest
from time import sleep

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_radio_button(setPath):
    driver.maximize_window()
    driver.get("file:///Users/bobit/PycharmProjects/Pytest_Selenium_Methods/files/index.html")
    sleep(3)
    element = driver.find_element_by_xpath("//input[@value='Mango']")
    print("\nBEFORE: ", element.is_selected())
    element.click()
    sleep(2)
    print("\nAFTER: ", element.is_selected())