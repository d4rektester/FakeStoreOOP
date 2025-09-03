import pytest
from selenium import webdriver
from pages.store_page import StorePage
from pages.login_page import LoginPage
from locators.login_locators import LoginLocators
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://fakestore.testelka.pl/")
    yield driver
    driver.quit()


def test_login_empty_username (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    email = ''
    password = ''

    # Login user
    login_page.login_user(email, password)

    # Assert empty username
    error_message = login_page.get_login_error_message()
    expected_message = 'Błąd: Nazwa użytkownika jest wymagana.'
    print(expected_message)
    assert error_message == expected_message


def test_login_empty_password (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    email = 'email@domena.pl'
    password = ''

    # Login user
    login_page.login_user(email, password)

    # Assert empty password
    error_message = login_page.get_login_error_message()
    expected_message = 'Błąd: pole hasła jest puste.'
    print(expected_message)
    assert error_message == expected_message


def test_login_nonexisting_email (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    user = 'nonexisting'
    email = f'{user}@domena.pl'
    password = '4545p4$$w0rD!#'

    # Login user
    login_page.login_user(email, password)

    # Assert nonexisting email
    error_message = login_page.get_login_error_message()
    expected_message = 'Nieznany adres e-mail. Proszę sprawdzić ponownie lub wypróbować swoją nazwę użytkownika.'
    print(expected_message)
    assert error_message == expected_message


def test_login_nonexisting_user (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    user = 'NonexistingUsername'
    password = '4545p4$$w0rD!#'

    # Login user
    login_page.login_user_by_username(user, password)

    # Assert nonexisting user
    error_message = login_page.get_login_error_message()
    expected_message = f'Błąd: brak {user} wśród zarejestrowanych w witrynie użytkowników. Jeśli nie masz pewności co do nazwy użytkownika, użyj adresu e-mail.'
    print(expected_message)
    assert error_message == expected_message


def test_login_by_email_wrong_password (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    user = 'ExistinguserLoginByEmailWrongPassword'
    email = f'{user}@domena.pl'
    password = '1234#'

    # Login user
    login_page.login_user(email, password)

    # Assert wrong password when logging by email
    error_message = login_page.get_login_error_message()
    expected_message = f'Błąd: dla adresu e-mail {email} podano nieprawidłowe hasło. Nie pamiętasz hasła?'
    print(expected_message)
    assert error_message == expected_message


def test_login_by_username_wrong_password (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    user = 'ExistinguserLoginByUsernameWrongPassword'
    password = '1234#'

    # Login user
    login_page.login_user_by_username(user, password)

    # Assert wrong password when logging by username
    error_message = login_page.get_login_error_message()
    expected_message = f'Błąd: wpisano niepoprawne hasło dla użytkownika {user}. Nie pamiętasz hasła?'
    print(expected_message)
    assert error_message == expected_message


def test_login_user(setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)

    # Go to login page
    store_page.go_to_register()

    user = 'loginsuccess'
    email = f'{user}@domena.pl'
    password = '4545p4$$w0rD!#'

    # Login user
    login_page.login_user(email, password)

    # Assert login success
    welcome_message = login_page.get_welcome_message()
    expected_message = f'Witaj {user} (nie jesteś {user}? Wyloguj się)'
    print(expected_message)
    assert welcome_message == expected_message

# 4545p4$$w0rD!#
# ExistinguserLoginByUsernameWrongPassword@domena.pl