from pages.base_page import BasePage
from playwright.sync_api import expect


class PaymentPage(BasePage):
    # Locators
    SHIPPING_COMMENT = 'textarea[name="comment"]'
    SHIPPING_METHOD_BUTTON = "#button-shipping-method"
    PAYMENT_COMMENT = 'textarea[name="comment"]'
    AGREE_CHECKBOX = 'input[name="agree"]'
    PAYMENT_METHOD_RADIO = 'input[name="payment_method"]'
    PAYMENT_METHOD_BUTTON = "#button-payment-method"
    PAYMENT_METHOD_PANEL = "#collapse-payment-method"

    # Methods
    def fill_shipping_comment(self, comment: str):
        """Fill shipping comment (first textarea)"""
        self.page.locator(self.SHIPPING_COMMENT).nth(0).fill(comment)

    def click_shipping_method(self):
        """Click Shipping Method button and wait for Payment step to be fully rendered"""
        self.click_by_locator(self.SHIPPING_METHOD_BUTTON)
        expect(self.page.locator(self.PAYMENT_METHOD_RADIO).first).to_be_visible(timeout=15000)
        expect(self.page.locator(self.AGREE_CHECKBOX)).to_be_visible(timeout=15000)
        expect(self.page.locator(self.PAYMENT_METHOD_BUTTON)).to_be_visible(timeout=15000)

    def fill_payment_comment(self, comment: str):
        """Fill payment comment (second textarea)"""
        self.page.locator(self.PAYMENT_COMMENT).nth(1).fill(comment)

    def agree_to_terms(self):
        """Check the agree checkbox"""
        self.check_checkbox(self.AGREE_CHECKBOX, force=True)

    def verify_agree_checked(self):
        """Verify agree checkbox is checked"""
        expect(self.page.locator(self.AGREE_CHECKBOX)).to_be_checked()

    def select_payment_method(self):
        """Ensure a payment method radio is selected"""
        radio = self.page.locator(self.PAYMENT_METHOD_RADIO).first
        radio.check(force=True)
        expect(radio).to_be_checked()

    def click_payment_method(self):
        """Click Payment Method button; retry once if Confirm step doesn't open"""
        confirm = self.page.locator("#button-confirm")
        self.click_by_locator(self.PAYMENT_METHOD_BUTTON)
        try:
            expect(confirm).to_be_visible(timeout=10000)
        except Exception:
            self.click_by_locator(self.PAYMENT_METHOD_BUTTON)
            expect(confirm).to_be_visible(timeout=15000)