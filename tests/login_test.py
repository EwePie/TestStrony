# tests/login_test.py
from tests.base_test import BaseTest
from tests.test_data import TestData


class LoginTests(BaseTest):
    """Testy logowania"""

    def setUp(self):
        # Rozszerzam bazowy setup testu
        # o wygenerowanie danych testowych
        # 1. Najpierw wywołuję bazowy setup
        super().setUp()
        # 2. Generuję dane testowe
        self.test_data = TestData()
        # 3. Kliknij moje konto
        self.login_page = self.home_page.click_log_in()

    def test_invalid_username_and_password(self):
        """ TC1: User enters invalid username and password"""
        # 1. Wpisz niepoprawny username
        self.login_page.enter_username(self.test_data.user_name)
        # 2. Wpisz niepoprawne hasło
        self.login_page.enter_password(self.test_data.password)
        # 3. Kliknij Log In
        self.login_page.click_log_in()
        # Oczekiwany rezultat: Wyskakuje komunikat "The password you entered for the username abcd is incorrect."
        self.assertEqual("Error: The password you entered for the username abcd is incorrect. Lost your password?",
                         self.login_page.error_wrong_usr())

    def test_no_name_and_password_entered(self):
        """ TC2: User does not enter username and password"""
        self.login_page.click_log_in()
        # Oczekiwany rezultat: Wyskakuje komunikat "Error: Username is required."
        self.assertEqual("Error: Username is required.", self.login_page.error_usr())

    def test_valid_username_and_password(self):
        """ TC3: User enters valid username and password"""
        # 1. Wpisz poprawny username
        self.login_page.enter_username(self.test_data.email_reg)
        # 2. Wpisz poprawne hasło
        self.login_page.enter_password(self.test_data.password_reg)
        # 3. Kliknij Log In
        self.login_page.click_log_in()
        # Oczekiwany rezultat: poprawnie zalogowano
        self.assertEqual("Hello lolwowheh (not lolwowheh? Log out)", self.login_page.hello_msg())

    def test_no_name_and_password_entered_to_reg(self):
        """ TC4: User does not enter username and password in registration field"""
        self.login_page.click_reg()
        # Oczekiwany rezultat: Wyskakuje komunikat "Error:  Please provide a valid email address."
        self.assertEqual("Error: Please provide a valid email address.", self.login_page.error_reg())
