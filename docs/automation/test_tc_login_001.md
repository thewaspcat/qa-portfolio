```python

import pytest
import json
from pathlib import Path
from playwright.sync_api import Page, expect


def load_test_data():
    data_path = Path(__file__).parent / "test_login_data.json"
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("credentials", load_test_data())
def test_tc_ui_login_001_valid_login(page: Page, credentials):
    """
    Test Case ID: TC_UI_LOGIN_001
    Title: Login Page Functionality – Valid Credentials
    Objective: Confirm that users with valid credentials can log in successfully and session persists after reload.
    Requirement Reference: REQ-AUTH-001
    """
    email = credentials["email"]
    password = credentials["password"]
    username = credentials["username"]

    # Step 1: Navigate to login page
    page.goto("https://www.automationexercise.com/login")
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()

    # Step 2–3: Fill credentials
    page.get_by_label("Email Address").or_(page.get_by_placeholder("Email Address")).fill(email)
    page.get_by_label("Password").or_(page.get_by_placeholder("Password")).fill(password)

    # Step 4: Click login
    page.get_by_role("button", name="Login").or_(page.get_by_text("Login")).click()

    # Step 5: Verify UI elements after login
    expect(page.get_by_role("navigation")).to_be_visible()
    expect(page.get_by_text(f"Logged in as {username}", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()

    # Step 6: Ensure session persists
    page.reload()
    expect(page.get_by_text(f"Logged in as {username}", exact=True)).to_be_visible()
