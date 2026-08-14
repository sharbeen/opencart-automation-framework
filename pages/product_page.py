from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    QUANTITY_INPUT = "#input-quantity"
    ADD_TO_CART_BUTTON = "#button-cart"

    # Methods
    def navigate_home(self):
        """Navigate to home page"""
        self.navigate_to()

    def click_category(self, category_name, subcategory: str = None):
        """Click category from top navigation; optionally click subcategory"""
        self.page.get_by_role("link", name=category_name, exact=True).click()
        if subcategory:
            self.page.get_by_role("link", name=subcategory, exact=True).click()

    def select_product(self, product_name: str):
        """Click product tile title from category listing and wait for product page"""
        product_link = self.page.get_by_role("link", name=product_name, exact=True).first
        product_link.wait_for(state="visible", timeout=15000)
        product_link.click()
        self.page.locator(self.QUANTITY_INPUT).wait_for(state="visible", timeout=15000)

    def set_quantity(self, quantity: str):
        """Set product quantity"""
        self.fill_by_locator(self.QUANTITY_INPUT, quantity)

    def add_to_cart(self):
        """Click Add to Cart button; caller verifies cart total updates."""
        self.click_by_locator(self.ADD_TO_CART_BUTTON)