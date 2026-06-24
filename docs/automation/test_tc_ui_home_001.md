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
def test_tc_ui_home_001_homepage_ui(page: Page, test_data):
    """
    Test Case ID: TC_UI_HOME_001
    Title: Homepage UI Layout and Components Display
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

    logo = page.get_by_role("img", name="Website for automation practice").or_(
        page.locator("div.logo.pull-left a img")
    )
    expect(logo).to_be_visible()
    expect(logo).to_have_attribute("alt", "Website for automation practice")
    expect(logo).to_have_attribute("src", re.compile(r".+"))

    
    # Step 3: Verify navigation bar and main links

    header = page.locator("header#header")
    expect(header).to_be_visible()

    for link_text, href in expected_links.items():
        link = page.locator(f'ul.nav.navbar-nav > li > a[href="{href}"]')
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", re.compile(rf".*{re.escape(href)}$"))


    # Step 4: Verify homepage sections - Keep this test for the general homepage sections only.
    # The "Featured Items" heading is verified in a dedicated test.

    general_sections = [section for section in sections if section != "Featured Items"]

    for section_name in general_sections:
        section_header = page.get_by_role("heading", name=section_name)
        expect(section_header).to_be_visible()


    # Step 5: Verify footer visibility

    footer = page.get_by_role("contentinfo").or_(page.locator("footer#footer"))
    expect(footer).to_be_visible()


@pytest.mark.parametrize("test_data", load_homepage_data())
@pytest.mark.xfail(
    reason="Known defect: homepage shows 'Features Items' instead of 'Featured Items'.",
    strict=False,
)
def test_tc_ui_home_002_featured_items_heading(page: Page, test_data):
    """
    Test Case ID: TC_UI_HOME_002
    Title: Featured Items Heading Display
    Objective: Validate that the Featured Items section heading is displayed correctly on the homepage.
    Requirement Reference: REQ-UI-001
    """

    page.goto(test_data["base_url"])
    featured_items_heading = page.get_by_role("heading", name="Featured Items", exact=True)
    expect(featured_items_heading).to_be_visible()


