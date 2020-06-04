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

def test_scrolling(setPath):
    driver.maximize_window()
    driver.get("https://darksky.net/")

    #Scrolling to the bottom of the page
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #sleep(3)

    #Scrolling to particular section of the page
    '''
    element = driver.find_element_by_xpath("//a[@class='button']")
    sleep(2)
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    sleep(2)
    element.click()
    sleep(3)
    
    '''

    #Scrolling by pixel
    driver.execute_script("window.scrollBy(0, 950);")
    sleep(3)
