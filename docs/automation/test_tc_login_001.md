```python

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("email, password, username", [
    ("valid_user@example.com", "CorrectPassword123!", "valid_user")
])

def test_TC_UI_LOGIN_001_valid_login(page: Page, email: str, password: str, username: str):
    """
    Test Case ID: TC_UI_LOGIN_001
    Title: Valid Login with Correct Credentials
    Objective: Ensure that a user can successfully log in with valid credentials.
    Requirement Reference: REQ-AUTH-001
    """

    # Step 1: Navigate to login page
    page.goto("https://www.automationexercise.com/login")
    expect(page.locator("h2:has-text('Login to your account')")).to_be_visible()

    # Step 2: Enter valid email
    page.fill("input[data-qa='login-email']", email)

    # Step 3: Enter valid password
    page.fill("input[data-qa='login-password']", password)

    # Step 4: Click the Login button
    page.click("button[data-qa='login-button']")

    # Step 5: Verify dashboard UI elements are displayed
    expect(page.locator("ul.nav.navbar-nav")).to_be_visible()
    expect(page.locator("a[href='/profile']")).to_have_text(f"Logged in as {username}")
    expect(page.locator("a[href='/logout']")).to_be_visible()

    # Step 6: Confirm required HTML elements exist in the page source
    page_source = page.content()
    assert 'data-qa="login-email"' in page_source, "Email field not found in page source"
    assert 'data-qa="login-password"' in page_source, "Password field not found in page source"
    assert 'data-qa="login-button"' in page_source, "Login button not found in page source"
    assert f"Logged in as {username}" in page_source, "'Logged in as' label not found in page source"
    assert 'href="/logout"' in page_source, "Logout button not found in page source"

    # Postcondition: Ensure session persists after reload
    page.reload()
    expect(page.locator("a[href='/profile']")).to_have_text(f"Logged in as {username}")
