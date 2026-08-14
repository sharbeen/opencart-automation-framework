import json
import os

import pytest
from playwright.sync_api import sync_playwright
BASE_URL = "https://opencart.abstracta.us/"
@pytest.fixture
def browser(playwright):
    """Start browser before test, close after test"""
   # p = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser, request):
    """Create a new page (tab) for each test"""
    context = browser.new_context()
    context.clear_cookies()
    page = context.new_page()
    yield page
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        page.screenshot(path=f"failure_{request.node.name}.png", full_page=True)
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())

def load_test_data(file_name: str = "test_data.json"):
    """Load test data"""
    file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
    with open(file_path, "r") as file:
        return json.load(file)

