from .base_page import BasePage
from locators.store_locators import StoreLocators
from selenium.webdriver.common.by import By


class StorePage(BasePage):
    def go_to_myaccount(self):
        self.find_element(By.ID, StoreLocators.MENU_MY_ACCOUNT).click()

    def go_to_shop(self):
        self.find_element(By.ID, StoreLocators.MENU_SHOP).click()

    def go_to_category(self):
        self.hide_element_by(By.CLASS_NAME, StoreLocators.BANNER)
        self.wait_until_clickable(By.XPATH, StoreLocators.CATEGORY_WINDSURFING)
        self.find_element(By.XPATH, StoreLocators.CATEGORY_WINDSURFING).click()

    def add_to_cart(self):
        self.hide_element_by(By.CLASS_NAME, StoreLocators.BANNER)
        self.wait_until_clickable(By.XPATH, StoreLocators.WINDSURFING_EGIPT)
        self.find_element(By.XPATH, StoreLocators.WINDSURFING_EGIPT).click()

    def go_to_cart(self):
        self.wait_until_text_present(By.XPATH, StoreLocators.CART_PRODUCT_COUNT, "1 Produkt")
        self.find_element(By.XPATH, StoreLocators.CART_ICON).click()
