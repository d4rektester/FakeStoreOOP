import time
from pages.store_page import StorePage
from pages.coupon_page import CouponPage


def test_coupon_apply(setup):
    store_page = StorePage(setup)
    coupon_page = CouponPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Apply coupon
    coupon_code = '10procent1'
    coupon_page.coupon_apply(coupon_code)
    # Assert coupon applied
    expected_message = 'Kupon został pomyślnie użyty.'
    coupon_message = coupon_page.get_coupon_message(expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + coupon_message)
    assert coupon_message in expected_message

def test_coupon_remove(setup):
    store_page = StorePage(setup)
    coupon_page = CouponPage(setup)

    # Go to shop
    store_page.go_to_shop()
    store_page.go_to_category()
    # Add to cart
    store_page.add_to_cart()
    # Go to cart
    store_page.go_to_cart()
    # Apply coupon
    coupon_code = "10procent1"
    coupon_page.coupon_apply(coupon_code)
    # Remove coupon
    coupon_page.coupon_remove()
    # Assert coupon removed
    expected_message = 'Kupon został usunięty.'
    coupon_message = coupon_page.get_coupon_message(expected_message)
    print(time.strftime("%a, %d %b %Y %H:%M:%S ") + coupon_message)
    assert coupon_message in expected_message
