from .base_page import BasePage
from locators.cart_locators import CartLocators
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def remove_item(self):
        self.hide_element_by(By.CLASS_NAME, CartLocators.BANNER)
        self.wait_until_clickable(By.XPATH, CartLocators.REMOVE_ITEM_BUTTON)
        self.find_element(By.XPATH, CartLocators.REMOVE_ITEM_BUTTON).click()

    def update_quantity(self, quantity):
        self.hide_element_by(By.CLASS_NAME, CartLocators.BANNER)
        self.wait_until_clickable(By.XPATH, CartLocators.QUANTITY_INPUT)
        quantity_input = self.find_element(By.XPATH, CartLocators.QUANTITY_INPUT)
        quantity_input.clear()
        quantity_input.send_keys(quantity)
        self.find_element(By.XPATH, CartLocators.UPDATE_CART_BUTTON).click()

    def get_cart_message_remove(self):
        self.wait_until_text_present(By.XPATH, CartLocators.CART_UPDATE_MESSAGE, "Usunięto: „Egipt - El Gouna“. Cofnij?")
        return self.find_element(By.XPATH, CartLocators.CART_UPDATE_MESSAGE).text

    def get_cart_message_update(self):
        self.wait_until_text_present(By.XPATH, CartLocators.CART_UPDATE_MESSAGE, "Koszyk zaktualizowany.")
        return self.find_element(By.XPATH, CartLocators.CART_UPDATE_MESSAGE).text

    def get_cart_empty_message(self):
        return self.find_element(By.XPATH, CartLocators.CART_EMPTY_MESSAGE).text

    def go_to_checkout(self):
        self.hide_element_by(By.CLASS_NAME, CartLocators.BANNER)
        self.find_element(By.XPATH, CartLocators.CHECKOUT_BUTTON).click()