from selenium.webdriver import Chrome
import pytest
from time import sleep

@pytest.mark.Chrome
def test_screenshot():
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://www.ebay.com")
    driver.maximize_window()
    sleep(2)
    directory = "/Users/bobit/Desktop/pics/screentshot1.png"
    driver.get_screenshot_as_file(directory)
    driver.close()
