from pages.store_page import StorePage
from pages.register_page import RegisterPage
import time


def test_register_user_success(setup):
    store_page = StorePage(setup)
    register_page = RegisterPage(setup)
    user = 'successfulregistration50'
    email = f'{user}@domena.pl'
    password = 'successfulregistration@domena.pl'

    # Go to register page
    store_page.go_to_myaccount()
    # Register user
    register_page.register_user(email, password)
    # Assert registration success
    expected_message = f'Witaj {user} (nie jesteś {user}? Wyloguj się)'
    welcome_paragraph = register_page.get_welcome_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + welcome_paragraph)
    assert welcome_paragraph == expected_message

def test_register_existing_user(setup):
    store_page = StorePage(setup)
    register_page = RegisterPage(setup)
    user = 'ExistingUser'
    email = f'{user}@testy.pl'
    password = 'ExistingUser@testy.pl'

    # Go to register page
    store_page.go_to_myaccount()
    # Register user
    register_page.register_user(email, password)
    # Assert existing user registration failure
    expected_message = f'Błąd: Konto jest już zarejestrowane w {email}. Zaloguj się lub użyj innego adresu e-mail.'
    error_message = register_page.get_registration_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message == expected_message

def test_register_user_weak_password(setup):
    store_page = StorePage(setup)
    register_page = RegisterPage(setup)
    user = 'WeakPassword'
    email = f'{user}@domena.pl'
    password = '4545'

    # Go to register page
    store_page.go_to_myaccount()
    # Evaluate password strength
    register_page.evaluate_password_strength(email, password)
    # Assert existing user registration failure
    expected_message = 'Bardzo słabe - Proszę wpisać mocniejsze hasło.'
    error_message = register_page.get_password_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message == expected_message
