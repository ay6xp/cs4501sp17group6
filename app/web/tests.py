from django.test import TestCase
from selenium import webdriver 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumTests(TestCase):
	def setUp(self):
	   self.driver = webdriver.Remote(
	       command_executor='http://selenium-chrome:4444/wd/hub/',
	       desired_capabilities=DesiredCapabilities.CHROME
		)

	def test_test(self):
		driver = self.driver
		#driver.get("http://192.168.99.100:8000/")
		driver.get("http://www.google.com")
		assert "google" in driver.page_source