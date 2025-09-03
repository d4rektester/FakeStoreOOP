import pytest
from selenium import webdriver
from pages.store_page import StorePage
from pages.register_page import RegisterPage
from locators.register_locators import RegisterLocators
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://fakestore.testelka.pl/")
    yield driver
    driver.quit()



def test_register_user_weak_password(setup):
    store_page = StorePage(setup)
    register_page = RegisterPage(setup)

    # Go to register page
    store_page.go_to_register()

    user = 'newuser98'
    email = f'{user}@domena.pl'
    password = '4545'

    # Evaluate password strength
    register_page.evaluate_password_strength(email, password)

    # Assert existing user registration failure
    error_message = register_page.get_password_error_message()
    expected_message = 'Bardzo słabe - Proszę wpisać mocniejsze hasło.'
    print(error_message)
    assert error_message == expected_message


def test_register_user(setup):
    store_page = StorePage(setup)
    register_page = RegisterPage(setup)

    # Go to register page
    store_page.go_to_register()

    user = 'newuser98'
    email = f'{user}@domena.pl'
    password = '4545p4$$w0rD!#'

    # Register user
    register_page.register_user(email, password)

    # Assert registration success
    welcome_paragraph = register_page.get_welcome_message()
    expected_message = f'Witaj {user} (nie jesteś {user}? Wyloguj się)'
    print(expected_message)
    assert welcome_paragraph == expected_message


def test_register_existing_user(setup):
    store_page = StorePage(setup)
    register_page = RegisterPage(setup)

    # Go to register page
    store_page.go_to_register()

    user = 'newuser98'
    email = f'{user}@domena.pl'
    password = '4545p4$$w0rD!#'

    # Register user
    register_page.register_user(email, password)

    # Assert existing user registration failure
    error_message = register_page.get_registration_error_message()
    expected_message = f'Błąd: Konto jest już zarejestrowane w {email}. Zaloguj się lub użyj innego adresu e-mail.'
    print(error_message)
    assert error_message == expected_message


#zmienne do wyciagniecia do zewnetrznego pliku z danymi testowymi:
# user = 'nowyuserucx5'
# email = f'{user}@domena.pl'
# password = '4545p4$$w0rD!#'
