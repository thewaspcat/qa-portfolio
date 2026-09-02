from typing import Any

from pages.home_page import HomePage


def test_homepage_loads(home_page: HomePage, homepage_data: dict[str, Any]) -> None:
    """Verify the homepage loads with the expected URL and title."""
    home_page.open()
    home_page.assert_loaded(homepage_data["expected_title"])
