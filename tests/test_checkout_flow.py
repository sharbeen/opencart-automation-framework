import pytest

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_confirmation_page import OrderConfirmationPage
from conftest import load_test_data


TEST_CASES = load_test_data()["test_cases"]


@pytest.mark.parametrize("test_case", TEST_CASES, ids=lambda tc: tc["name"])
def test_end_to_end_checkout(page, test_case):
    """End-to-end checkout flow using POM and data-driven approach"""

    category = test_case["category"]
    subcategory = test_case.get("subcategory")
    product_name = test_case["product_name"]
    quantity = test_case["quantity"]
    address = test_case["shipping_address"]
    comments = test_case["comments"]

    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    confirmation_page = OrderConfirmationPage(page)

    product_page.navigate_home()
    assert product_page.get_page_title() == "Your Store"
    product_page.click_category(category, subcategory)
    product_page.select_product(product_name)
    product_page.set_quantity(str(quantity))
    product_page.add_to_cart()

    cart_page.verify_cart_total_updated()
    cart_page.navigate_to_checkout()

    checkout_page.select_guest_checkout()
    checkout_page.click_account_button()
    checkout_page.fill_shipping_address(
        first_name=address["first_name"],
        last_name=address["last_name"],
        email=address["email"],
        telephone=address["telephone"],
        address=address["address_1"],
        city=address["city"],
        post_code=address["post_code"],
    )
    checkout_page.select_country(address["country"])
    checkout_page.select_zone(address["zone"])
    checkout_page.continue_as_guest()

    payment_page.fill_shipping_comment(comments["shipping_comment"])
    payment_page.click_shipping_method()
    payment_page.select_payment_method()
    payment_page.fill_payment_comment(comments["payment_comment"])
    payment_page.agree_to_terms()
    payment_page.verify_agree_checked()
    payment_page.click_payment_method()

    confirmation_page.wait_for_confirm_button()
    confirmation_page.click_confirm_order()
    confirmation_page.verify_order_success()