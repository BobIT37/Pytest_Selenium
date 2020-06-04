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

def test_iFrame(setPath):
    driver.maximize_window()
    driver.get("http://londonfreelance.org/courses/frames/index.html")

    driver.switch_to.frame(driver.find_element_by_name("main"))
    header = driver.find_element_by_css_selector("body > h2")
    print("\n", header.text )

    driver.switch_to.default_content()
    print(driver.title)