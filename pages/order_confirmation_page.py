from pages.base_page import BasePage
from playwright.sync_api import expect


class OrderConfirmationPage(BasePage):
    # Locators
    CONFIRM_BUTTON = "#button-confirm"
    SUCCESS_MESSAGE = "text=Your order has been successfully processed!"

    # Methods
    def wait_for_confirm_button(self, timeout: int = 15000):
        """Wait for Confirm Order button to be visible"""
        self.wait_for_element(self.CONFIRM_BUTTON, timeout=timeout)

    def click_confirm_order(self):
        """Click Confirm Order button"""
        self.click_by_locator(self.CONFIRM_BUTTON)

    def verify_order_success(self, timeout: int = 30000):
        """Verify order success message is displayed"""
        expect(self.page.get_by_text("Your order has been successfully processed!")).to_be_visible(timeout=timeout)