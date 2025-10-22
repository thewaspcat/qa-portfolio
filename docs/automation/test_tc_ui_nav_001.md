```python

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(("link_text", "expected_url"), [
    ("Home", "https://www.automationexercise.com/"),
    ("Products", "https://www.automationexercise.com/products"),
    ("Cart", "https://www.automationexercise.com/view_cart"),
    ("Signup / Login", "https://www.automationexercise.com/login"),
    ("Test Cases", "https://www.automationexercise.com/test_cases"),
    ("API Testing", "https://www.automationexercise.com/api_list"),
    ("Contact us", "https://www.automationexercise.com/contact_us"),
])
def test_tc_ui_nav_001_navigation_links(page: Page, link_text: str, expected_url: str):
    """
    Test Case ID: TC_UI_NAV_001
    Title: Homepage Navigation Menu Links – Functionality Verification
    Objective: Confirm that each navigation menu link on the homepage redirects to the correct page and displays the corresponding content.
    Requirement Reference: REQ-UI-NAV-001
    """

    # Step 1: Navigate to homepage
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_url("https://www.automationexercise.com/")
    expect(page.locator("nav")).to_be_visible()

    # Step 2: Remove cookie consent overlay if present
    page.evaluate("""
        () => {
            const consent = document.querySelector('.fc-consent-root');
            if (consent) consent.remove();
        }
    """)

    # Step 3: Locate the navigation link by visible text
    locator = page.get_by_role("link", name=link_text)
    expect(locator).to_be_visible()

    # Step 4: Click the link and verify redirection
    locator.click()
    expect(page).to_have_url(expected_url)

    # Step 5: Verify page content loaded successfully
    expect(page.locator("body")).to_be_visible()
