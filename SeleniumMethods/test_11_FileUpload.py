from selenium.webdriver import Chrome, ActionChains
import pytest
from time import sleep


@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    #driver.quit()

def test_file_upload(setPath):
    driver.maximize_window()
    driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

    driver.find_element_by_name("upfile").send_keys("/Users/bobit/Desktop/testFile.txt")