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

def test_drag_drop(setPath):
    driver.maximize_window()
    driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
    drag = driver.find_element_by_id("draggable")
    sleep(2)
    drop = driver.find_element_by_id("droppable")
    sleep(2)

    action = ActionChains(driver)
    action.drag_and_drop(drag, drop).perform()