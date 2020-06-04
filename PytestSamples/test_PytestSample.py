from selenium import webdriver
import pytest

class TestSample():

      @pytest.fixture()
      def setup(self):
         global driver
         path = "/Users/bobit/Documents/Drivers/chromedriver"
         driver = webdriver.Chrome(executable_path=path)
         driver.implicitly_wait(10)
         driver.maximize_window()
         yield
         driver.close()
         driver.quit()
         print("Test completed")

      def test_login(self, setup):
         driver.get("https://opensource-demo.orangehrmlive.com/")
         driver.find_element_by_id("txtUsername").send_keys("Admin")
         driver.find_element_by_id("txtPassword").send_keys("admin123")
         driver.find_element_by_id("btnLogin").click()
         title = driver.title
         assert title == "OrangeHRM"



