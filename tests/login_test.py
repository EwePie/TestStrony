# tests/login_test.py
from tests.base_test import BaseTest
from tests.test_data import TestData


class LoginTests(BaseTest):
    """Testy logowania"""

    def setUp(self):
        # Expand base setup for test
        # with test data
        # 1. First i invoke base setup
        super().setUp()
        # 2. generate test data
        self.test_data = TestData()
        # 3. Click my account
        self.login_page = self.home_page.click_log_in()

    def test_invalid_username_and_password(self):
        """ TC1: User enters invalid username and password"""
        # 1. Type wrong username
        self.login_page.enter_username(self.test_data.user_name)
        # 2. Type wrong password
        self.login_page.enter_password(self.test_data.password)
        # 3. Click Log In
        self.login_page.click_log_in()
        # Expected result: we get alert "The password you entered for the username abcd is incorrect."
        self.assertEqual("Error: The password you entered for the username abcd is incorrect. Lost your password?",
                         self.login_page.error_wrong_usr())

    def test_no_name_and_password_entered(self):
        """ TC2: User does not enter username and password"""
        # Click my account button
        self.login_page.click_log_in()
        # Expected result: we get alert "Error: Username is required."
        self.assertEqual("Error: Username is required.", self.login_page.error_usr())

    def test_valid_username_and_password(self):
        """ TC3: User enters valid username and password"""
        # 1. Type valid username
        self.login_page.enter_username(self.test_data.email_reg)
        # 2. Type valid password
        self.login_page.enter_password(self.test_data.password_reg)
        # 3. Click Log In
        self.login_page.click_log_in()
        # Expected result: successfully logged
        self.assertEqual("Hello lolwowheh (not lolwowheh? Log out)", self.login_page.hello_msg())

    def test_no_name_and_password_entered_to_reg(self):
        """ TC4: User does not enter username and password in registration field"""
        self.login_page.click_reg()
        # Expected result: we get alert "Error:  Please provide a valid email address."
        self.assertEqual("Error: Please provide a valid email address.", self.login_page.error_reg())
