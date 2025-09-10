from pages.store_page import StorePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage
import time


def test_order_placed_correctly(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    checkout_page = CheckoutPage(setup)
    order_confirmation_page = OrderConfirmationPage(setup)
    email = 'testend2end@domena.pl'
    password = 'testend2end@domena.pl'

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
    # Select checkbox
    checkout_page.select_terms_and_condition_checkbox()
    # Place order
    checkout_page.place_order()
    # Get order confirmation message and assert with expected message
    expected_message = 'Dziękujemy. Otrzymaliśmy Twoje zamówienie.'
    message = order_confirmation_page.get_order_confirmation_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + message)
    assert message in expected_message
