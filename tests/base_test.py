# tests/base_test.py
from pages.home_page import HomePage
from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):
    """Klasa bazowa każdego testu"""

    def setUp(self):
        """Warunki wstępne każdego testu"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        # Jesteśmy na stronie głównej - tworzę instancję klasy HomePage
        # Muszę zaimportować niezbędną klasę
        # Tworzę obiekt (instancję) klasy HomePage
        self.home_page = HomePage(self.driver)

    # sprzątanie po testach
    def tearDown(self):
        self.driver.quit()
