from selenium.webdriver import Chrome
import pytest
from time import sleep
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setPath():
    global driver
    path = "/Users/bobit/Documents/Drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_dropdown_handling(setPath):
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    sleep(3)

    selectDay = Select(driver.find_element_by_id("day"))
    selectDay.select_by_index(20)
    sleep(2)

    selectMonth = Select(driver.find_element_by_id("month"))
    selectMonth.select_by_visible_text("Jun")
    sleep(2)

    selectYear = Select(driver.find_element_by_id("year"))
    selectYear.select_by_value("1990")
    sleep(2)

