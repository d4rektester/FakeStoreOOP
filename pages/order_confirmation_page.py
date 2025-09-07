from .base_page import BasePage
from locators.order_confirmation_locators import OrderConfirmationLocators
from selenium.webdriver.common.by import By

class OrderConfirmationPage(BasePage):
    def get_order_confirmation_message(self):
        self.wait_until_visible(By.CSS_SELECTOR, OrderConfirmationLocators.ORDER_CONFIRMATION_MESSAGE)
        return self.driver.find_element(By.CSS_SELECTOR, OrderConfirmationLocators.ORDER_CONFIRMATION_MESSAGE).text
