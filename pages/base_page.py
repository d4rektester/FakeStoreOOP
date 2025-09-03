from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.5)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def switch_to_default_content(self):
        return self.driver.switch_to.default_content()

    def wait_until_frame_available_and_switch_to_it(self, by, value):
        return self.wait.until(EC.frame_to_be_available_and_switch_to_it((by, value)))

    def wait_until_visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_until_element_present(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_until_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def wait_until_text_present(self, by, value, text):
        return self.wait.until(EC.text_to_be_present_in_element((by, value), text))

    def js_scroll_into_view(self, arguments):
        return self.driver.execute_script("arguments[0].scrollIntoView();", arguments)

    def js_scroll_into_view_block(self, arguments):
        return self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", arguments)

    def js_click(self, arguments):
        return self.driver.execute_script("arguments[0].click();", arguments)

    def js_display_none(self, arguments):
        return self.driver.execute_script("arguments[0].style.display = 'none';", arguments)

    def hide_element_by(self, by, value):
        try:
            element = self.find_element(by, value)
            self.js_display_none(element)
        except:
            pass
