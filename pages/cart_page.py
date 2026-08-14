from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    # Locators
    CART_TOTAL = "#cart-total"

    # Methods
    def verify_cart_total_updated(self, timeout: int = 15000):
        """Verify cart total is not empty"""
        expect(self.page.locator(self.CART_TOTAL)).not_to_have_text("0 item(s) - $0.00", timeout=timeout)

    def navigate_to_checkout(self):
        """Navigate to checkout page"""
        self.navigate_to("index.php?route=checkout/checkout")