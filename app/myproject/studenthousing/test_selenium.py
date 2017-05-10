from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Listing, User
import json
import os
import hmac
from django.conf import settings
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
        #driver.get("http://web1:8000/home/")
        driver.get("http://107.170.92.232:8000/home/")
        assert "Welcome to Student Housing!" in driver.page_source