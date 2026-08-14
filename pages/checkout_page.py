from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators
    GUEST_CHECKOUT_RADIO = 'input[type="radio"][name="account"]'
    ACCOUNT_BUTTON = "#button-account"
    FIRST_NAME_INPUT = 'input[placeholder="First Name"]'
    LAST_NAME_INPUT = 'input[placeholder="Last Name"]'
    EMAIL_INPUT = "#input-payment-email"
    TELEPHONE_INPUT = 'input[placeholder="Telephone"]'
    ADDRESS_INPUT = 'input[placeholder="Address 1"]'
    CITY_INPUT = 'input[placeholder="City"]'
    POST_CODE_INPUT = 'input[placeholder="Post Code"]'
    COUNTRY_DROPDOWN = "#input-payment-country"
    ZONE_DROPDOWN = "#input-payment-zone"
    GUEST_CONTINUE_BUTTON = "#button-guest"

    # Methods
    def select_guest_checkout(self):
        """Select Guest Checkout option"""
        self.page.get_by_role("radio", name="Guest Checkout").check()

    def click_account_button(self):
        """Click Account button"""
        self.click_by_locator(self.ACCOUNT_BUTTON)

    def fill_shipping_address(self, first_name: str, last_name: str, email: str,
                              telephone: str, address: str, city: str, post_code: str):
        """Fill complete shipping address"""
        self.fill_by_placeholder("First Name", first_name)
        self.fill_by_placeholder("Last Name", last_name)
        self.fill_by_locator(self.EMAIL_INPUT, email)
        self.fill_by_placeholder("Telephone", telephone)
        self.fill_by_placeholder("Address 1", address)
        self.fill_by_placeholder("City", city)
        self.fill_by_placeholder("Post Code", post_code)

    def select_country(self, country: str):
        """Select country from dropdown"""
        self.select_by_locator(self.COUNTRY_DROPDOWN, country)

    def select_zone(self, zone: str):
        """Select zone/state from dropdown"""
        self.select_by_locator(self.ZONE_DROPDOWN, zone)

    def continue_as_guest(self):
        """Click Continue as Guest button"""
        self.click_by_locator(self.GUEST_CONTINUE_BUTTON)