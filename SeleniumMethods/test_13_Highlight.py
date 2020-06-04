from selenium.webdriver import Chrome
from time import sleep
import pytest

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    #driver.quit()

def test_highlighted_element(setPath):
   driver.maximize_window()
   driver.get("https://www.facebook.com")
   element = driver.find_element_by_name("firstname")
   element.send_keys("ilhan")

   driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                         "background: yellow; border: 3px solid red;")
   sleep(2)


