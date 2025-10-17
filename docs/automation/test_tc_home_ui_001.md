```python

import pytest
import json
from pathlib import Path
from playwright.sync_api import Page, expect


def load_homepage_data():
    """Load homepage verification data from JSON file."""
    data_path = Path(__file__).parent / "test_homepage_data.json"
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("test_data", load_homepage_data())
def test_TC_UI_HOME_001_homepage_ui_verification(page: Page, test_data):
    """
    Test Case ID: TC_UI_HOME_001
    Title: Homepage UI Validation (Data-Driven)
    Objective: Validate that all key UI components and navigation links are displayed correctly on the homepage.
    Requirement Reference: REQ-UI-001
    """

    base_url = test_data["base_url"]
    expected_title = test_data["expected_title"]
    expected_links = test_data["expected_links"]
    sections = test_data["sections"]

    # Step 1: Navigate to the homepage
    page.goto(base_url)
    expect(page).to_have_title(expected_title)

    # Step 2: Verify logo visibility and attributes
    logo = page.get_by_role("img", name="Automation Exercise").or_(
        page.locator("div.logo.pull-left a img")
    )
    expect(logo).to_be_visible()
    expect(logo).to_have_attribute("alt", "Automation Exercise")
    expect(logo).to_have_attribute("src", lambda v: v and v.strip() != "")

    # Step 3: Verify navigation bar and main links
    nav_bar = page.get_by_role("navigation")
    expect(nav_bar).to_be_visible()

    for link_text, href in expected_links.items():
        link = page.get_by_role("link", name=link_text).or_(
            page.locator(f'ul.nav.navbar-nav > li > a[href="{href}"]')
        )
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", pytest.approx(href))

    # Step 4: Verify homepage sections
    for section_name in sections:
        section_header = page.get_by_role("heading", name=section_name).or_(
            page.locator(f"div:has(h2:text('{section_name}')) h2")
        )
        section_header.scroll_into_view_if_needed()
        expect(section_header).to_be_visible()

    # Step 5: Verify footer visibility
    footer = page.get_by_role("contentinfo").or_(page.locator("footer#footer"))
    footer.scroll_into_view_if_needed()
    expect(footer).to_be_visible()


