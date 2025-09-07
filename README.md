Final Project for University Course – Automated Testing of an Online Store Using Python, Selenium, and PyTest
Tested store URL: https://fakestore.testelka.pl/

IMPORTANT!
Before running the test cases from the file test_1register.py, you must manually change the numeric value of the user variable (e.g., successfulregistrationXX), where XX should be a unique number (e.g., "02", than "03" and so on).
Otherwise, the test case test_register_user_success will fail due to a duplicate username.
The user variable is defined on line 9 of the test file.

The project follows the Page Object Model (POM) design pattern.
It uses Selenium and PyTest frameworks, which must be installed for the project to run correctly.

Project Structure
The root directory contains the following folders:
locators – contains locators for individual pages and functionalities
pages – classes with methods used on specific pages/functionality
tests – test files for each page/functionality

The purchase process is divided into separate functionalities, each tested on ts respective page or subpage.
Test Suite Overview:
The test cases are grouped into separate, self-descriptive files:
test_1register.py – tests for new user registration
test_2login.py – tests for user login
test_3cart.py – cart tests: adding a product, removing it, and updating product quantity
test_4coupon.py – applying and removing a discount coupon
test_5checkout.py – tests for credit card payment fields and acceptance of the store's terms and conditions
test_6order_confirmation.py – end-to-end test: adding a product to the cart, proceeding through payment, and confirming the order
In the test case test_6order_confirmation.py, all functionalities are combined into a single flow to simulate a complete end-to-end shopping process from the customer's perspective.