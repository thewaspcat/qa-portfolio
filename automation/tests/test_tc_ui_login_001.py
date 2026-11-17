from typing import Any

from pages.login_page import LoginPage


def test_tc_ui_login_001_valid_credentials(
    login_session: LoginPage,
    login_data: dict[str, Any],
) -> None:
    """TC_UI_LOGIN_001: verify valid login and session persistence."""
    login_session.open()
    login_session.assert_loaded(login_data["login_url"])
    login_session.login(login_data["email"], login_data["password"])
    login_session.assert_logged_in(
        login_data["expected_text"],
        login_data.get("username"),
    )
    login_session.reload_and_assert_authenticated(
        login_data["expected_text"],
        login_data.get("username"),
    )
