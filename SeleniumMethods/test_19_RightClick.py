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

def test_right_click(setPath):
    driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    sleep(3)
    driver.maximize_window()

    action = ActionChains(driver)
    action.context_click(driver.find_element_by_xpath("//span[text()='right click me']")).perform()
    sleep(2)

    driver.find_element_by_xpath("//ul[@class='context-menu-list context-menu-root']/li[3]").click()
    sleep(2)

    obj = driver.switch_to.alert
    msg = obj.text
    print(msg)
    sleep(2)
    obj.accept()
