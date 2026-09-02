from typing import Any

from pages.login_page import LoginPage


def test_login(login_page: LoginPage, login_data: dict[str, Any]) -> None:
    """Verify that a configured valid user can log in successfully."""
    login_page.open()
    login_page.assert_loaded(login_data["login_url"])
    login_page.login(login_data["email"], login_data["password"])
    login_page.assert_logged_in(
        login_data["expected_text"],
        login_data.get("username"),
    )