from .base_page import BasePage
from locators.register_locators import RegisterLocators
from selenium.webdriver.common.by import By
import time


class RegisterPage(BasePage):
    def register_user(self, email, password):
        self.find_element(By.ID, RegisterLocators.REG_EMAIL).send_keys(email)
        self.find_element(By.ID, RegisterLocators.REG_PASSWORD).send_keys(password)
        self.find_element(By.NAME, RegisterLocators.REGISTER_BUTTON).click()

    def evaluate_password_strength(self, email, password):
        self.find_element(By.ID, RegisterLocators.REG_EMAIL).send_keys(email)
        self.find_element(By.ID, RegisterLocators.REG_PASSWORD).send_keys(password)

    def get_welcome_message(self):
        self.wait_until_visible(By.XPATH, RegisterLocators.WELCOME_PARAGRAPH)
        return self.find_element(By.XPATH, RegisterLocators.WELCOME_PARAGRAPH).text

    def get_registration_error_message(self):
        return self.find_element(By.XPATH, RegisterLocators.REGISTRATION_ERROR_MESSAGE).text

    def get_password_error_message(self):
        return self.find_element(By.XPATH, RegisterLocators.PASSWORD_ERROR_MESSAGE).text
