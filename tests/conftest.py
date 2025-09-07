import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://fakestore.testelka.pl/")
    driver.maximize_window()
    yield driver
    driver.quit()
