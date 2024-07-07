# tests/base_test.py
from pages.home_page import HomePage
from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):
    """Base class for every test"""

    def setUp(self):
        """Set up for evey test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        # We are at main page - create instance class HomePage
        # Need to import needed class
        # Create object (instance) class HomePage
        self.home_page = HomePage(self.driver)

    # cleaning up after tests
    def tearDown(self):
        self.driver.quit()
