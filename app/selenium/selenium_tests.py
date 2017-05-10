import unittest
from django.test import TestCase
from selenium import webdriver 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class SeleniumTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Remote(
           command_executor='http://selenium-chrome:4444/wd/hub/',
           desired_capabilities=DesiredCapabilities.CHROME
        )

	def test_frontend(self):
		driver = self.driver
		driver.get("http://192.168.99.100:8000/home/")
		assert "Welcome to Student Housing!" in driver.page_source

	#test register
	def register(self):
		username = "test11"
		password = "password"
		email = "test1@gmail.com"
		phone_num = "1234567890"
		driver.get("http://192.168.99.100:8000/register/")
		driver.find_element_by_id("id_username").send_keys(username)
		driver.find_element_by_id("id_password").send_keys(password)
		driver.find_element_by_id("id_phone_num").send_keys(phone_num)
		driver.find_element_by_css_selector("button.btn").click()
		# driver.get("http://192.168.99.100:8000/home/")
		# print(driver.page_source)
		assert "successfully created" in driver.page_source

	#test login
	def login(self):
		username = "test11"
		password = "password"
		driver.get("http://192.168.99.100:8000/login/")
		driver.find_element_by_id("id_username").send_keys(username)
		driver.find_element_by_id("id_password").send_keys(password)
		driver.find_element_by_class_name("btn").click()
		# print(driver.page_source)
		# driver.find_element_by_link_text("Student Housing").click()
		assert "You are logged in." in driver.page_source

    # def test_create_listing(self):

    # def test_search(self):

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()