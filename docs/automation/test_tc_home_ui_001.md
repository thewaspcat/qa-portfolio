```python

import pytest
from playwright.sync_api import Page, expect


def test_homepage_ui(page: Page):
    # Navigate to the Automation Exercise homepage
    page.goto("https://www.automationexercise.com/")
    page.wait_for_load_state("domcontentloaded")  # Ensure DOM is fully loaded
    print("✅ Navigated to homepage.")

    # Verify page title
    title = page.title()
    assert title == "Automation Exercise", f"Unexpected page title: '{title}'."
    print("✅ Page title verified.")

    # Verify logo is visible with correct attributes
    logo = page.locator("div.logo.pull-left a img")
    expect(logo).to_be_visible()
    src = logo.get_attribute("src")
    alt = logo.get_attribute("alt")
    assert src and src.strip() != "", "Logo 'src' attribute is missing or empty."
    assert alt == "Automation Exercise", f"Logo 'alt' attribute mismatch: '{alt}'."
    print("✅ Logo verified with correct src and alt attributes.")

    # Verify navigation bar visibility
    nav_bar = page.locator("ul.nav.navbar-nav")
    expect(nav_bar).to_be_visible()
    print("✅ Navigation bar is visible.")

    # Verify navigation link texts and hrefs
    nav_links = page.locator("ul.nav.navbar-nav > li > a")
    expected_links = {
        "Home": "/",
        "Products": "/products",
        "Cart": "/view_cart",
        "Signup / Login": "/login",
        "Test Cases": "/test_cases",
        "API Testing": "/api_testing",
        "Video Tutorials": "/video_tutorials",
        "Contact us": "/contact_us",
    }
    assert nav_links.count() == len(expected_links), (
        f"Expected {len(expected_links)} navigation links, "
        f"but found {nav_links.count()}."
    )
    for text, href in expected_links.items():
        link = page.locator(f'ul.nav.navbar-nav > li > a[href="{href}"]')
        expect(link).to_be_visible()
        assert link.inner_text() == text, f"Link text mismatch: expected '{text}', got '{link.inner_text()}'."
    print(f"✅ Verified {len(expected_links)} navigation links with correct text and href.")

    # Verify “Features Items” section
    features_items = page.locator("div.features_items")
    expect(features_items).to_be_visible()
    header_features = features_items.locator("h2")
    assert header_features.inner_text() == "Features Items", (
        f"Expected header 'Features Items', got '{header_features.inner_text()}'."
    )
    print("✅ 'Features Items' section verified.")

    # Verify “Recommended Items” section
    recommended_items = page.locator("div.recommended_items")
    recommended_items.scroll_into_view_if_needed()
    expect(recommended_items).to_be_visible()
    header_recommended = recommended_items.locator("h2")
    assert header_recommended.inner_text() == "Recommended Items", (
        f"Expected header 'Recommended Items', got '{header_recommended.inner_text()}'."
    )
    print("✅ 'Recommended Items' section verified.")

    # Verify footer presence
    footer = page.locator("footer#footer")
    footer.scroll_into_view_if_needed()
    expect(footer).to_be_visible()
    print("✅ Footer is visible.")

    # Verify required elements exist in page source
    page_source = page.content()
    required_elements = [
        'alt="Automation Exercise"',                # Logo alt attribute
        '<ul class="nav navbar-nav">',              # Navigation bar
        '<div class="features_items"',              # Features Items section
        '<div class="recommended_items"',           # Recommended Items section
        '<footer id="footer"',                      # Footer section
    ]
    for element in required_elements:
        assert element in page_source, f"Expected element '{element}' not found in page source."
    print("✅ Required elements confirmed in page source.")

