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

def test_isOptions(setPath):
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    print("\nDISPLAYED ? ", driver.find_element_by_partial_link_text("Sign up").is_displayed())
    print("\nENABLED ? ", driver.find_element_by_partial_link_text("Sign up").is_enabled())
    print("\nSELECTED ? ", driver.find_element_by_partial_link_text("Sign up").is_selected())
