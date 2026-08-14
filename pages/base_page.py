from playwright.sync_api import Page
import json

from conftest import BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

    def navigate_to(self, path: str = ""):
        """Navigate to a URL"""
        url = self.base_url + path if path else self.base_url
        self.page.goto(url)

    def get_page_title(self) -> str:
        """Get page title"""
        return self.page.title()

    def click_by_text(self, text: str, exact: bool = False):
        """Click element by text content"""
        self.page.get_by_text(text, exact=exact).click()

    def fill_by_placeholder(self, placeholder: str, text: str):
        """Fill input by placeholder text"""
        self.page.get_by_placeholder(placeholder).fill(text)

    def fill_by_locator(self, locator: str, text: str):
        """Fill input by CSS locator"""
        self.page.locator(locator).fill(text)

    def click_by_locator(self, locator: str):
        """Click element by CSS locator"""
        self.page.locator(locator).click()

    def select_by_locator(self, locator: str, label: str):
        """Select option by label in dropdown"""
        self.page.locator(locator).select_option(label=label)

    def check_checkbox(self, locator: str, force: bool = False):
        """Check a checkbox"""
        self.page.locator(locator).check(force=force)

    def wait_for_element(self, locator: str, timeout: int = 15000):
        """Wait for element to be visible"""
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def check_element_text(self, locator: str, text: str, timeout: int = 15000):
        """Wait for element to have specific text"""
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        assert text not in self.page.locator(locator).text_content() or text in self.page.locator(locator).text_content()

