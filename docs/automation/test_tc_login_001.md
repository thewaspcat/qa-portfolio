```python

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("email, password, username", [
    ("valid_user@example.com", "CorrectPassword123!", "valid_user")
])
def test_successful_login(page: Page, email: str, password: str, username: str):
    # Step 1: Navigate to login page
    page.goto("https://www.automationexercise.com/login")
    expect(page.locator("h2:has-text('Login to your account')")).to_be_visible()

    # Step 2 & 3: Enter valid credentials
    page.fill("input[type='email'][data-qa='login-email']", email)
    page.fill("input[type='password'][data-qa='login-password']", password)

    # Step 4: Click Login button
    page.click("button[data-qa='login-button']")

    # Step 5: Verify homepage UI elements
    expect(page.locator("ul.nav.navbar-nav")).to_be_visible()
    expect(page.locator(f"//a[contains(text(),'Logged in as {username}')]")).to_be_visible()
    expect(page.locator("a[href='/logout']")).to_be_visible()

    # Step 6: Confirm page source contains required HTML elements
    page_source = page.content()
    assert 'input type="email" data-qa="login-email"' in page_source, "Email field not found in page source"
    assert 'input type="password" data-qa="login-password"' in page_source, "Password field not found in page source"
    assert 'button data-qa="login-button"' in page_source, "Login button not found in page source"
    assert 'Logged in as' in page_source, "'Logged in as' label not found in page source"
    assert 'href="/logout"' in page_source, "Logout button not found in page source"

    # Postcondition: Ensure session persists after reload
    page.reload()
    expect(page.locator(f"//a[contains(text(),'Logged in as {username}')]")).to_be_visible()
