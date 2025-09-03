class CheckoutLocators:
    EXISTING_ACCOUNT_BUTTON = '//a[@class="showlogin"]'
    USERNAME_INPUT = 'username' #ID
    PASSWORD_INPUT = 'password' #ID
    LOGIN_BUTTON = 'login' #NAME
    # LOGIN_BUTTON = 'woocommerce-button button woocommerce-form-login__submit' #CSS_SELECTOR
    BILLING_EMAIL_INPUT = 'billing_email' #ID
    BANNER = 'woocommerce-store-notice'

    PAYMENT_FRAME = 'iframe[title="Bezpieczne pole wprowadzania płatności"]' #CSS_SELECTOR
    CARD_NUMBER_INPUT = 'Field-numberInput'
    CARD_NUMBER_ERROR_MESSAGE = 'Field-numberError' #ID
    CARD_EXPIRY_DATE_INPUT = 'Field-expiryInput'
    CARD_EXPIRY_DATE_ERROR_MESSAGE = 'Field-expiryError' #ID
    CARD_CVC_CODE_INPUT = 'Field-cvcInput' #ID
    CARD_CVC_CODE_ERROR_MESSAGE = 'Field-cvcError' #ID

    TERMS_CHECKBOX = 'terms' #ID

    PLACE_ORDER_BUTTON = 'place_order' #ID
    CHECKBOX_ERROR_MESSAGE = 'li[data-id="terms"]' #CSS_SELECTOR



