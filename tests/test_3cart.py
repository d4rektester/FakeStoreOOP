import time
from pages.store_page import StorePage
from pages.cart_page import CartPage


def test_remove_item_from_cart(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Remove item from cart
    cart_page.remove_item()
    # Assert item is removed
    expected_message = 'Usunięto: „Egipt - El Gouna“. Cofnij?'
    cart_message = cart_page.get_cart_message_remove()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + cart_message)
    assert cart_message in expected_message

def test_update_cart_quantity(setup):
    store_page = StorePage(setup)
    cart_page = CartPage(setup)
    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Update quantity
    cart_page.update_quantity('0')
    # Assert quantity updated & empty cart
    expected_message1 = 'Koszyk zaktualizowany.'
    expected_message2 = 'Twój koszyk jest pusty.'
    cart_message1 = cart_page.get_cart_message_update()
    cart_message2 = cart_page.get_cart_empty_message()
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + f'{cart_message1} & {cart_message2}')
    assert cart_message1 in expected_message1
    assert cart_message2 in expected_message2
