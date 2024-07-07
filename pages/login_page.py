# pages/login_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    """Lokators on login page"""
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOG_IN_BTN = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
    EMAIL_INPUT_REG = (By.ID, "reg_email")
    PASSWORD_INPUT_REG = (By.ID, "reg_password")
    REG_BTN = (By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
    ERROR_USR = (By.XPATH, '//*[contains(text(),"Username is required")]')
    ERROR_WRONG_USR = (By.XPATH, '//*[contains(text()," The password you entered for the username")]')
    ERROR_REG = (By.XPATH, '//*[contains(text()," Please provide a valid email address.")]')
    HELLO_MSG = (By.XPATH, '//*[contains(text(),"Hello " )]')


class LoginPage(BasePage):
    def enter_username(self, username):
        """ Enters username """
        el = self.driver.find_element(*Locators.USERNAME_INPUT)
        el.send_keys(username)

    def enter_password(self, password):
        """ Enters password """
        el = self.driver.find_element(*Locators.PASSWORD_INPUT)
        el.send_keys(password)

    def click_log_in(self):
        """ Clicks Log In"""
        self.driver.find_element(*Locators.LOG_IN_BTN).click()

    def click_reg(self):
        """ Clicks Register"""
        self.driver.find_element(*Locators.REG_BTN).click()

    def error_usr(self):
        """Returns error message - no user"""
        return self.driver.find_element(*Locators.ERROR_USR).text

    def error_wrong_usr(self):
        """Returns error message - wrong user"""
        return self.driver.find_element(*Locators.ERROR_WRONG_USR).text

    def error_reg(self):
        """Returns error message in register - no user"""
        return self.driver.find_element(*Locators.ERROR_REG).text

    def hello_msg(self):
        """Returns hello message"""
        return self.driver.find_element(*Locators.HELLO_MSG).text
