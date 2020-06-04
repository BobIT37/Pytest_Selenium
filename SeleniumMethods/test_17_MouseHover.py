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

def test_mouse_hover(setPath):
    driver.get("https://www.verizonwireless.com/")
    sleep(3)
    driver.maximize_window()

    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_xpath("//button[contains(text(), 'Phones list')]")).perform()
    sleep(2)
    phone = driver.find_element_by_id("thirdLevel00")
    phone.click()
