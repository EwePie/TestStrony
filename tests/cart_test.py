# tests/cart_test.py
from tests.base_test import BaseTest
from time import sleep
from pages.cart_page import CartPage


class CartTest(BaseTest):
    """Testy koszyka"""

    def setUp(self):
        # Rozszerzam bazowy setup testu
        # o wygenerowanie danych testowych
        # 1. Najpierw wywołuję bazowy setup
        super().setUp()
        # 2.Tworzę obiekt (instancję) klasy CartPage
        self.cart_page = CartPage(self.driver)

    def test_add_item_to_cart(self):
        """ TC5: User adds items to cart"""
        # klikamy stronę zakupową
        self.home_page.click_shop_page()
        # dodajemy rzeczy do koszyka
        self.home_page.item_1()
        sleep(3)
        self.home_page.item_2()
        sleep(3)
        self.home_page.item_3()
        sleep(3)
        # przechodzimy do koszyka
        self.home_page.click_cart()
        # Oczekiwany rezultat-3 rzeczy w koszyku:"Little Black Top","Amari Shirt,"Magnolia Dress"
        self.assertEqual(self.cart_page.cart_val(), "Little Black Top")
        self.assertEqual(self.cart_page.cart_val1(), "Amari Shirt")
        self.assertEqual(self.cart_page.cart_val2(), "Magnolia Dress")
        sleep(3)

    def test_delete_item_from_cart(self):
        """ TC6: User deletes item from cart"""
        self.home_page.click_shop_page()
        # dodajemy rzeczy do koszyka
        self.home_page.item_1()
        sleep(3)
        # przechodzimy do koszyka
        self.home_page.click_cart()
        sleep(3)
        # usuwamy przedmiot
        self.cart_page.delete_item()
        sleep(3)
        # aktualizujemy koszyk
        self.cart_page.update_cart()
        sleep(3)
        # Oczekiwany rezultat: wiadomość o pustym koszyku - "Your cart is currently empty."
        self.assertEqual("Your cart is currently empty.", self.cart_page.empty_cart_msg())

    def test_make_order(self):
        """ TC7: User adds item to cart and place an order"""
        self.home_page.click_shop_page()
        # dodajemy rzeczy do koszyka
        self.home_page.item_1()
        sleep(5)
        # przechodzimy do koszyka
        self.home_page.click_cart()
        sleep(2)
        # przechodzimy do składania zamówienia
        self.cart_page.check_out_btn()
        sleep(2)
        # wpisujemy imię
        self.cart_page.billing_name()
        sleep(1)
        # wpisujemy nazwisko
        self.cart_page.billing_last_name()
        sleep(1)
        # wybieramy kraj
        self.cart_page.country_btn()
        sleep(2)
        self.cart_page.select_country()
        sleep(2)
        # wpisujemy ulicę
        self.cart_page.address_str()
        sleep(2)
        # wpisujemy kod pocztowy
        self.cart_page.zip_code()
        sleep(2)
        # wpisujemy miasto
        self.cart_page.town()
        sleep(2)
        # wpisujemy nr telefonu
        self.cart_page.phone()
        sleep(2)
        # wpisujemy email
        self.cart_page.email_billing()
        sleep(10)
        # Klikamy przycisk składania zamówienia
        self.cart_page.place_order_btn()
        sleep(10)
        # Oczekiwany rezultat - zamówienie zostało złożone, dostajemy info "Thank you. Your order has been received."
        self.assertEqual("Thank you. Your order has been received.", self.cart_page.order_msg())
