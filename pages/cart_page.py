# pages/cart_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Locators:
    """Locators on cart page"""
    SHOP_PAGE = (By.XPATH, '//*[@id="menu-item-142"]/a')
    DELETE_ITEM = (By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[5]/div/div/a[1]/span')
    UPDATE_CART = (By.XPATH, '//input[@class="button" and @name="update_cart"]')
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[contains(text(),"Your cart is currently empty")]')
    CHECK_OUT_BTN = (By.XPATH, '//div[@class="wc-proceed-to-checkout"]')
    BILLING_NAME = (By.XPATH, '//*[@id="billing_first_name"]')
    BILLING_LAST_NAME = (By.XPATH, '//*[@id="billing_last_name"]')
    COUNTRY = (By.XPATH, '//*[@id="billing_country"]')
    COUNTRY_BTN = (By.XPATH, '//*[@id="select2-billing_country-container"]')
    COUNTRY_CLICK = (By.XPATH, '//*[@class="select2-results__option select2-results__option--highlighted"]')
    ADDRESS_STR = (By.XPATH, '//*[@id="billing_address_1"]')
    ZIP = (By.XPATH, '//*[@id="billing_postcode"]')
    TOWN = (By.XPATH, '//*[@id="billing_city"]')
    PHONE = (By.XPATH, '//*[@id="billing_phone"]')
    ORDER_BTN = (By.XPATH, '//*[@id="place_order"]')
    BILLING_EMAIL = (By.XPATH, '//*[@id="billing_email"]')
    ORDER_MSG = (By.XPATH, '//*[contains(text(),"Thank you. Your order has been received" )]')
    CART_VAL = (By.XPATH, '//*[contains(text(),"Little Black Top")]')
    CART_VAL1 = (By.XPATH, '//*[contains(text(),"Amari Shirt")]')
    CART_VAL2 = (By.XPATH, '//*[contains(text(),"Magnolia Dress")]')


class CartPage(BasePage):
    def update_cart(self):
        """Clicks on update cart button"""
        element = self.driver.find_element(*Locators.UPDATE_CART)
        element.click()

    def empty_cart_msg(self):
        """Returns empty cart message"""
        return self.driver.find_element(*Locators.EMPTY_CART_MESSAGE).text

    def delete_item(self):
        """Deletes item from cart"""
        self.driver.find_element(*Locators.DELETE_ITEM).click()

    def check_out_btn(self):
        """Clicks check out button"""
        self.driver.find_element(*Locators.CHECK_OUT_BTN).click()

    def billing_name(self):
        """Types billing name"""
        element = self.driver.find_element(*Locators.BILLING_NAME)
        element.send_keys("Ewe")

    def billing_last_name(self):
        """Types billing last name"""
        element = self.driver.find_element(*Locators.BILLING_LAST_NAME)
        element.send_keys("Pie")

    def select_country(self):
        """Selects country from list"""
        country_select = Select(self.driver.find_element(*Locators.COUNTRY))
        country_select.select_by_visible_text("Poland")
        self.driver.find_element(*Locators.COUNTRY_CLICK).click()

    def country_btn(self):
        """Clicks selected country button"""
        self.driver.find_element(*Locators.COUNTRY_BTN).click()

    def address_str(self):
        """Types street"""
        element = self.driver.find_element(*Locators.ADDRESS_STR)
        element.send_keys("Pocztowa 1")

    def zip_code(self):
        """Types zip code"""
        element = self.driver.find_element(*Locators.ZIP)
        element.send_keys("70-360")

    def town(self):
        """Types Town name"""
        element = self.driver.find_element(*Locators.TOWN)
        element.send_keys("Szczecin")

    def phone(self):
        """Types phone number"""
        element = self.driver.find_element(*Locators.PHONE)
        element.send_keys("+48 123 456 789")

    def email_billing(self):
        """Types email"""
        element = self.driver.find_element(*Locators.BILLING_EMAIL)
        element.send_keys("lolwowheh@wp.pl")

    def place_order_btn(self):
        """Clicks place order button"""
        self.driver.find_element(*Locators.ORDER_BTN).click()

    def order_msg(self):
        """Returns order message"""
        return self.driver.find_element(*Locators.ORDER_MSG).text

    def cart_val(self):
        """Returns first item in cart name"""
        return self.driver.find_element(*Locators.CART_VAL).text

    def cart_val1(self):
        """Returns second item in cart name"""
        return self.driver.find_element(*Locators.CART_VAL1).text

    def cart_val2(self):
        """Returns third item in cart name"""
        return self.driver.find_element(*Locators.CART_VAL2).text
