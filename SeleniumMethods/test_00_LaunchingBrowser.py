from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
import pytest
from time import sleep

@pytest.mark.Chrome
def test_chrome_browser():
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    assert driver.title == "HubSpot Login"
    print("url: ", driver.current_url)
    driver.close()

@pytest.mark.FF
def test_firefox_browser():
    path = "/Users/bobit/Documents/Drivers/geckodriver"
    driver = Firefox(executable_path=path)
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    assert driver.title == "HubSpot Login"
    print("url: ", driver.current_url)
    driver.close()
