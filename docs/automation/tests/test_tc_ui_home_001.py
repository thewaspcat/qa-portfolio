from typing import Any

import pytest

from pages.home_page import HomePage


def test_tc_ui_home_001_homepage_layout(
    home_page: HomePage,
    homepage_data: dict[str, Any],
) -> None:
    """TC_UI_HOME_001: verify the homepage shell and key components."""
    home_page.open()
    home_page.assert_loaded(homepage_data["expected_title"])
    home_page.assert_logo_visible()
    home_page.assert_navigation_visible()
    for section_name in homepage_data["sections"]:
        home_page.assert_section_visible(section_name)
    home_page.assert_section_heading_visible("Recommended Items")
    home_page.assert_section_follows("Featured Items", "Recommended Items")
    home_page.assert_footer_visible()


@pytest.mark.xfail(
    reason="Known defect BR_TC_UI_HOME_001: application displays 'Features Items'.",
    strict=True,
)
def test_tc_ui_home_001_featured_items_heading(home_page: HomePage) -> None:
    """TC_UI_HOME_001: verify the Featured Items heading."""
    home_page.open()
    home_page.assert_section_heading_visible("Featured Items")
