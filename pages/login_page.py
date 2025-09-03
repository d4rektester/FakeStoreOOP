from .base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def login_user(self, email, password):
        self.find_element(By.ID, LoginLocators.USERNAME).send_keys(email)
        self.find_element(By.ID, LoginLocators.PASSWORD).send_keys(password)
        self.find_element(By.NAME, LoginLocators.LOGIN_BUTTON).click()

    def login_user_by_username(self, user, password):
        self.find_element(By.ID, LoginLocators.USERNAME).send_keys(user)
        self.find_element(By.ID, LoginLocators.PASSWORD).send_keys(password)
        self.find_element(By.NAME, LoginLocators.LOGIN_BUTTON).click()

    def get_welcome_message(self):
        return self.find_element(By.XPATH, LoginLocators.WELCOME_PARAGRAPH).text

    def get_login_error_message(self):
        return self.find_element(By.XPATH, LoginLocators.LOGIN_ERROR_MESSAGE).text

