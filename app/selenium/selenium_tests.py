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

	def test_home_page(self):
		driver = self.driver
		driver.get("http://192.168.99.100:8000/home/")
		assert "Welcome to Student Housing!" in driver.page_source

	def test_view_all_listings(self):
		driver = self.driver
		driver.get("http://192.168.99.100:8000/home/")
		driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/p/a").click()
		assert "Listings:" in driver.page_source

	def test_click_register(self):
		driver = self.driver
		driver.get("http://192.168.99.100:8000/home/")
		driver.find_element_by_xpath("/html/body/nav/div/div[2]/p[2]/a").click()
		assert "Register" in driver.page_source

	def test_click_login(self):
		driver = self.driver
		driver.get("http://192.168.99.100:8000/home/")
		driver.find_element_by_xpath("/html/body/nav/div/div[2]/p[3]/a").click()
		assert "Login" in driver.page_source

	# def test_register(self):
	# 	username = "test20"
	# 	password = "password"
	# 	email = "test@gmail.com"
	# 	phone_num = "1234567890"

	# 	driver = self.driver
	# 	driver.get("http://192.168.99.100:8000/register/")
	# 	driver.find_element_by_id("id_username").send_keys(username)
	# 	driver.find_element_by_id("id_password").send_keys(password)
	# 	driver.find_element_by_id("id_phone_num").send_keys(phone_num)
	# 	driver.find_element_by_id("id_phone_num").submit()
	# 	print(driver.page_source)
	# 	register_status = driver.find_element_by_class_name("info")
	# 	self.assertEqual("successfully created", register_status)

	# def test_login(self):
	# 	username = "test20"
	# 	password = "password"

	# 	driver = self.driver
	# 	driver.get("http://192.168.99.100:8000/login/")
	# 	driver.find_element_by_id("id_username").send_keys(username)
	# 	driver.find_element_by_id("id_password").send_keys(password)
	# 	driver.find_element_by_id("id_password").submit()
	# 	login_status = driver.find_element_by_xpath("//*[@id='logged_in_status']/span").text
	# 	self.assertEqual("You are logged in.", login_status)

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()