# tests/cart_test.py
from tests.base_test import BaseTest
from time import sleep
from pages.cart_page import CartPage


class CartTest(BaseTest):
    """Cart tests"""

    def setUp(self):
        # Expand base setup for test
        # 1. First i invoke base setup
        super().setUp()
        # 2.Create object (instance) class CartPage
        self.cart_page = CartPage(self.driver)
        # 3. Click shop site
        self.home_page.click_shop_page()

    def test_add_item_to_cart(self):
        """ TC5: User adds items to cart"""
        # Add items to cart
        self.home_page.item_1()
        sleep(3)
        self.home_page.item_2()
        sleep(3)
        self.home_page.item_3()
        sleep(3)
        # Go to cart
        self.home_page.click_cart()
        # Expected result -3 things in cart:"Little Black Top","Amari Shirt,"Magnolia Dress"
        self.assertEqual(self.cart_page.cart_val(), "Little Black Top")
        self.assertEqual(self.cart_page.cart_val1(), "Amari Shirt")
        self.assertEqual(self.cart_page.cart_val2(), "Magnolia Dress")

    def test_delete_item_from_cart(self):
        """ TC6: User deletes item from cart"""
        # Add item to cart
        self.home_page.item_1()
        sleep(3)
        # Go to cart
        self.home_page.click_cart()
        sleep(3)
        # delete item from cart
        self.cart_page.delete_item()
        sleep(3)
        # update cart
        self.cart_page.update_cart()
        sleep(3)
        # Expected result: empty cart message - "Your cart is currently empty."
        self.assertEqual("Your cart is currently empty.", self.cart_page.empty_cart_msg())

    def test_make_order(self):
        """ TC7: User adds item to cart and place an order"""
        # Add item to cart
        self.home_page.item_1()
        sleep(5)
        # Go to cart
        self.home_page.click_cart()
        sleep(2)
        # go to checkout
        self.cart_page.check_out_btn()
        sleep(2)
        # type name
        self.cart_page.billing_name()
        # type last name
        self.cart_page.billing_last_name()
        # pick country
        self.cart_page.country_btn()
        self.cart_page.select_country()
        # type street name
        self.cart_page.address_str()
        # type zip code
        self.cart_page.zip_code()
        # type city
        self.cart_page.town()
        # type phone number
        self.cart_page.phone()
        # type email
        self.cart_page.email_billing()
        sleep(8)
        # click place order button
        self.cart_page.place_order_btn()
        sleep(7)
        # Expected result - order has been made, we get info "Thank you. Your order has been received."
        self.assertEqual("Thank you. Your order has been received.", self.cart_page.order_msg())
