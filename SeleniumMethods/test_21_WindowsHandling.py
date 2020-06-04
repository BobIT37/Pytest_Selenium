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

def test_windows_handling(setPath):
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    sleep(3)

    #get the window handle after the window has opened
    window_before = driver.window_handles[0]

    window_before_title = driver.title
    print(window_before_title)

    #open  new window
    driver.execute_script("window.open('http://www.twitter.com', 'new window')")

    #get the window handle after a new window has opened
    window_after = driver.window_handles[1]


    #switch on to new window
    driver.switch_to.window(window_after)

    window_after_title = driver.title
    print(window_after_title)

    #compare and verify that main window and child window title
    if window_before_title != window_after_title:
      print("Context swtiched to Twitter, so the title did not match")
    else:
      print("Control dod not switch to new window")

    driver.switch_to.window(window_before)

    #Verify that the title now match
    if window_before_title == driver.title:
        print("Context returned to parent window. Title now matches")

    print(driver.title)





