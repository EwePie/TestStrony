# pages/home_page.py
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.cart_page import CartPage


class Locators:
    """Lokatory na stronie głównej"""
    LOGIN_LINK = (By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a')
    ITEM_1 = (By.XPATH, '//*[@id="tyche_products-1"]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/a')
    ITEM_2 = (By.XPATH, '//*[@id="tyche_products-2"]/div/div[3]/div/div[1]/div/div[1]/div/div/div[2]/a')
    ITEM_3 = (By.XPATH, '//*[@id="tyche_products-3"]/div/div/div[2]/div/div[2]/div/a')
    CART = (By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]')
    SHOP_PAGE = (By.XPATH, '//*[@id="menu-item-142"]/a')


class HomePage(BasePage):
    """Strona główna"""

    def click_log_in(self):
        """Clicks Log in and returns LoginPage"""
        el = self.driver.find_element(*Locators.LOGIN_LINK)
        el.click()
        return LoginPage(self.driver)

    def item_1(self):
        """Adds item 1 to cart"""
        element = self.driver.find_element(*Locators.ITEM_1)
        element.click()

    def item_2(self):
        """Adds item 2 to cart"""
        self.driver.find_element(*Locators.ITEM_2).click()

    def item_3(self):
        """Adds item 3 to cart"""
        self.driver.find_element(*Locators.ITEM_3).click()

    def click_cart(self):
        """Clicks cart button and returns Cart Page"""
        element = self.driver.find_element(*Locators.CART)
        element.click()
        return CartPage(self.driver)

    def click_shop_page(self):
        """Clicks shop page"""
        self.driver.find_element(*Locators.SHOP_PAGE).click()
