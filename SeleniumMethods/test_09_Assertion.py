from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_assertion(setPath):
    driver.maximize_window()
    driver.get("http://newtours.demoaut.com/")
    actualTitle = driver.title
    assert actualTitle == "Welcome: Mercury Tours"
    print("\nActual title: ", actualTitle)
