from selenium.webdriver import Chrome
import pytest
from time import sleep

path = "/Users/bobit/Documents/Drivers/chromedriver"
driver = Chrome(executable_path=path)

@pytest.mark.Chrome
def test_navigate_browser():
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    driver.maximize_window()
    driver.find_element_by_name("proceed").click()
    sleep(4)
    alert_handling()

    driver.close()

def alert_handling():
    obj = driver.switch_to.alert
    assert obj.text == "Please enter a valid user name"
    obj.accept()