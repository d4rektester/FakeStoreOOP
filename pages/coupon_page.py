from .base_page import BasePage
from locators.coupon_locators import CouponLocators
from selenium.webdriver.common.by import By


class CouponPage(BasePage):
    def coupon_apply(self, coupon_code):
        self.find_element(By.ID, CouponLocators.COUPON_INPUT).send_keys(coupon_code)
        self.find_element(By.NAME, CouponLocators.COUPON_APPLY_BUTTON).click()

    def coupon_remove(self):
        self.hide_element_by(By.CLASS_NAME, CouponLocators.BANNER)
        self.wait_until_clickable(By.XPATH, CouponLocators.REMOVE_COUPON_BUTTON)
        self.find_element(By.XPATH, CouponLocators.REMOVE_COUPON_BUTTON).click()

    def get_coupon_message(self, expected_message):
        self.wait_until_text_present(By.XPATH, CouponLocators.COUPON_MESSAGE, expected_message)
        return self.find_element(By.XPATH, CouponLocators.COUPON_MESSAGE).text
