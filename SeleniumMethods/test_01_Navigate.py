from selenium.webdriver import Chrome
import pytest
from time import sleep

@pytest.mark.Chrome
def test_navigate_browser():
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://www.ebay.com")
    sleep(2)
    driver.get("https://www.amazon.com")
    sleep(2)
    driver.back()
    sleep(2)
    driver.forward()
    sleep(2)
    driver.back()
    sleep(2)
    driver.refresh()

    driver.close()