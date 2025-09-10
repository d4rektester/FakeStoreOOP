from pages.store_page import StorePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time


def test_card_message_incomplete_number(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add item to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Go to checkout
    cart_page.go_to_checkout()
    # Switch to payment iFrame
    checkout_page.switch_to_iframe()
    # Go to payment section and fill card number
    checkout_page.fill_card_number('44458')
    # Get error message and assert with expected message
    expected_message = 'Numer karty jest niepełny.'
    card_number_message = checkout_page.get_error_message('card_number', expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + card_number_message)
    assert card_number_message in expected_message

def test_card_message_wrong_card_number(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add item to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Go to checkout
    cart_page.go_to_checkout()
    # Switch to payment iFrame
    checkout_page.switch_to_iframe()
    # Go to payment section and fill card number
    checkout_page.fill_card_number('4325 4354 3345 5435')
    # Get error message and assert with expected message
    expected_message = 'Numer karty jest nieprawidłowy.'
    card_number_message = checkout_page.get_error_message('card_number', expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + card_number_message)
    assert card_number_message in expected_message

def test_card_message_incomplete_expiry_date(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add item to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Go to checkout
    cart_page.go_to_checkout()
    # Switch to payment iFrame
    checkout_page.switch_to_iframe()
    # Go to payment section and fill card expiry date
    checkout_page.fill_card_expiry_date('06')
    # Get error message and assert with expected message
    expected_message = 'Data ważności karty jest niepełna.'
    card_expiry_date_message = checkout_page.get_error_message('card_expiry_date', expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + card_expiry_date_message)
    assert card_expiry_date_message in expected_message

def test_card_message_expired_card(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add item to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Go to checkout
    cart_page.go_to_checkout()
    # Switch to payment iFrame
    checkout_page.switch_to_iframe()
    # Go to payment section and fill card expiry date
    checkout_page.fill_card_expiry_date('0525')
    # Get error message and assert with expected message
    expected_message = 'Termin ważności karty znajduje się w przeszłości.'
    card_expiry_date_message = checkout_page.get_error_message('card_expiry_date', expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + card_expiry_date_message)
    assert card_expiry_date_message in expected_message

def test_card_message_cvc_code_incomplete(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add item to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Go to checkout
    cart_page.go_to_checkout()
    # Switch to payment iFrame
    checkout_page.switch_to_iframe()
    # Go to payment section and fill card cvc code
    checkout_page.fill_card_cvc_code('06')
    # Get error message and assert with expected message
    expected_message = 'Kod zabezpieczający karty jest niekompletny.'
    card_cvc_message = checkout_page.get_error_message('card_cvc_code', expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + card_cvc_message)
    assert card_cvc_message in expected_message

def test_terms_checkbox_not_selected(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)
    email = 'testcheckbox@domena.pl'
    password = 'testcheckbox@domena.pl'

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add item to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Go to checkout
    cart_page.go_to_checkout()
    # Existing user log in
    checkout_page.login_existing_user_in(email, password)
    # Switch to payment iFrame
    checkout_page.switch_to_iframe()
    # Fill card details
    checkout_page.fill_card_number('4242424242424242')
    checkout_page.fill_card_expiry_date('0626')
    checkout_page.fill_card_cvc_code('666')
    # Switch to main content
    checkout_page.switch_to_main_window()
    # Place order
    checkout_page.place_order()
    # Get error message and assert with expected message
    expected_message = 'Proszę przeczytać i zaakceptować regulamin sklepu aby móc sfinalizować zamówienie.'
    checkout_error_message = checkout_page.get_checkout_error_message(expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + checkout_error_message)
    assert checkout_error_message in expected_message
