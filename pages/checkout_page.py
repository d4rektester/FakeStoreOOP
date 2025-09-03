from .base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class CheckoutPage(BasePage):
    def switch_to_iframe(self):
        iframe = self.wait_until_element_present(By.CSS_SELECTOR, CheckoutLocators.PAYMENT_FRAME)
        self.js_scroll_into_view_block(iframe)
        self.wait_until_frame_available_and_switch_to_it(By.CSS_SELECTOR,CheckoutLocators.PAYMENT_FRAME)

    def switch_to_main_window(self):
        self.switch_to_default_content()
        self.hide_element_by(By.CLASS_NAME, CheckoutLocators.BANNER)

    def fill_card_number(self, card_number):
        self.wait_until_visible(By.ID, CheckoutLocators.CARD_NUMBER_INPUT)
        card_input = self.find_element(By.ID, CheckoutLocators.CARD_NUMBER_INPUT)
        # card_input.send_keys(card_number).click()
        card_input.send_keys(card_number)
        card_input.send_keys(Keys.TAB)

    def fill_card_expiry_date(self, expiry_date):
        expiry_input = self.find_element(By.ID, CheckoutLocators.CARD_EXPIRY_DATE_INPUT)
        expiry_input.send_keys(expiry_date)
        expiry_input.send_keys(Keys.TAB)

    def fill_card_cvc_code(self, cvc):
        cvc_input = self.find_element(By.ID, CheckoutLocators.CARD_CVC_CODE_INPUT)
        cvc_input.send_keys(cvc)
        cvc_input.send_keys(Keys.TAB)

    def get_error_message(self, expected_message_locator, expected_message):
        if expected_message_locator == 'card_number':
            self.wait_until_text_present(By.ID, CheckoutLocators.CARD_NUMBER_ERROR_MESSAGE, expected_message)
            return self.find_element(By.ID ,CheckoutLocators.CARD_NUMBER_ERROR_MESSAGE).text
        elif expected_message_locator == 'card_expiry_date':
            self.wait_until_text_present(By.ID, CheckoutLocators.CARD_EXPIRY_DATE_ERROR_MESSAGE, expected_message)
            return self.find_element(By.ID, CheckoutLocators.CARD_EXPIRY_DATE_ERROR_MESSAGE).text
        elif expected_message_locator == 'card_cvc_code':
            self.wait_until_text_present(By.ID, CheckoutLocators.CARD_CVC_CODE_ERROR_MESSAGE, expected_message)
            return self.find_element(By.ID, CheckoutLocators.CARD_CVC_CODE_ERROR_MESSAGE).text
        else:
            pass

    def login_existing_user_in(self, email, password):
        self.hide_element_by(By.CLASS_NAME, CheckoutLocators.BANNER)
        self.wait_until_element_present(By.XPATH, CheckoutLocators.EXISTING_ACCOUNT_BUTTON).click()
        self.wait_until_clickable(By.ID, CheckoutLocators.USERNAME_INPUT)
        self.wait_until_visible(By.ID, CheckoutLocators.USERNAME_INPUT)
        username_input = self.find_element(By.ID, CheckoutLocators.USERNAME_INPUT)
        username_input.click()
        username_input.send_keys(email)
        self.find_element(By.ID, CheckoutLocators.PASSWORD_INPUT).send_keys(password)
        self.find_element(By.NAME, CheckoutLocators.LOGIN_BUTTON).click()

    def select_terms_and_condition_checkbox(self):
        self.hide_element_by(By.CLASS_NAME, CheckoutLocators.BANNER)
        wait_for_checkbox = self.wait_until_element_present(By.ID, CheckoutLocators.TERMS_CHECKBOX)
        self.js_scroll_into_view_block(wait_for_checkbox)
        self.find_element(By.ID, CheckoutLocators.TERMS_CHECKBOX).click()

    # def select_terms_and_condition_checkbox(self):
    #     self.switch_to_default_content()
    #     self.hide_element_by(By.CLASS_NAME, CheckoutLocators.BANNER)
    #     wait_for_checkbox = self.wait_until_element_present(By.ID, CheckoutLocators.TERMS_CHECKBOX)
    #     self.js_scroll_into_view_block(wait_for_checkbox)
    #     self.find_element(By.ID, CheckoutLocators.TERMS_CHECKBOX).click()

    def place_order(self):
        self.find_element(By.ID, CheckoutLocators.PLACE_ORDER_BUTTON).click()

    def get_checkout_error_message(self, expected_message):
        self.wait_until_text_present(By.CSS_SELECTOR, CheckoutLocators.CHECKBOX_ERROR_MESSAGE,expected_message)
        return self.find_element(By.CSS_SELECTOR, CheckoutLocators.CHECKBOX_ERROR_MESSAGE).text

    def get_order_confirmation(self):
        # return self.find_element(By.CSS_SELECTOR, CheckoutLocators.ORDER_CONFIRMATION).text
        pass
