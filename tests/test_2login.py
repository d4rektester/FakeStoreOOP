import time
from pages.store_page import StorePage
from pages.login_page import LoginPage


def test_login_empty_username (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    email = ''
    password = ''

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user(email, password)
    # Assert empty username
    expected_message = 'Błąd: Nazwa użytkownika jest wymagana.'
    error_message = login_page.get_login_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message in expected_message

def test_login_empty_password (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    email = 'email@domena.pl'
    password = ''

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user(email, password)
    # Assert empty password
    expected_message = 'Błąd: pole hasła jest puste.'
    error_message = login_page.get_login_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message in expected_message

def test_login_nonexisting_email (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    user = 'nonexisting'
    email = f'{user}@domena.pl'
    password = '4545879974Af'

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user(email, password)
    # Assert nonexisting email
    expected_message = 'Nieznany adres e-mail. Proszę sprawdzić ponownie lub wypróbować swoją nazwę użytkownika.'
    error_message = login_page.get_login_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message in expected_message

def test_login_nonexisting_user (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    user = 'NonexistingUsername'
    password = '4545879974Af'

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user_by_username(user, password)
    # Assert nonexisting user
    expected_message = f'Błąd: brak {user} wśród zarejestrowanych w witrynie użytkowników. Jeśli nie masz pewności co do nazwy użytkownika, użyj adresu e-mail.'
    error_message = login_page.get_login_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message in expected_message

def test_login_by_email_wrong_password (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    user = 'ExistinguserLoginByEmailWrongPassword'
    email = f'{user}@domena.pl'
    password = '1234#'

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user(email, password)
    # Assert wrong password when logging by email
    error_message = login_page.get_login_error_message()
    expected_message = f'Błąd: dla adresu e-mail {email} podano nieprawidłowe hasło. Nie pamiętasz hasła?'
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message in expected_message

def test_login_by_username_wrong_password (setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    user = 'ExistinguserLoginByUsernameWrongPassword'
    password = '1234#'

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user_by_username(user, password)
    # Assert wrong password when logging by username
    expected_message = f'Błąd: wpisano niepoprawne hasło dla użytkownika {user}. Nie pamiętasz hasła?'
    error_message = login_page.get_login_error_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + error_message)
    assert error_message in expected_message

def test_login_user(setup):
    store_page = StorePage(setup)
    login_page = LoginPage(setup)
    user = 'LoginSuccess'
    email = f'{user}@domena.pl'
    password = 'LoginSuccess@domena.pl'

    # Go to login page
    store_page.go_to_myaccount()
    # Login user
    login_page.login_user(email, password)
    # Assert login success
    expected_message = f'Witaj {user} (nie jesteś {user}? Wyloguj się)'
    welcome_message = login_page.get_welcome_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + welcome_message)
    assert welcome_message in expected_message
