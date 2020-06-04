from selenium.webdriver import Firefox
import pytest
from time import sleep
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def browser():
    global driver
    opts = Options()
    opts.headless = True
    driver = Firefox(options=opts)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_verify_title(browser):
     driver.get("https://app.hubspot.com/login")
     sleep(5)
     assert driver.title == "HubSpot Login"

def test_login_page(browser):
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys("sammy@sample.com")
    sleep(2)
    driver.find_element_by_id("password").send_keys("test12345")
    sleep(2)
    driver.find_element_by_id("loginBtn").click()
    sleep(2)





