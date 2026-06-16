```python

import re
from playwright.sync_api import Page, expect

def test_tc_ui_nav_001_video_tutorials(page: Page):
    """
    Test Case ID: TC_UI_NAV_001
    Title: Homepage Navigation Menu Functionality - Video Tutorials
    Objective: Validate that the 'Video Tutorials' navigation link opens the correct YouTube channel in a new browser tab.
    Requirement Reference: REQ-UI-NAV-001
    """

    # Set the YouTube consent cookies to bypass consent page
    page.context.add_cookies([
        {
            'name': 'CONSENT',
            'value': 'YES+42',
            'domain': '.youtube.com',
            'path': '/'
        },
        {
            'name': 'SOCS',
            'value': 'CAISEwgDEgk1Njc5NzQ0NjIaAmF0IAEaBgiA7bXvBg',
            'domain': '.youtube.com',
            'path': '/'
        }
    ])

    # Navigate to the Automation Exercise homepage
    page.goto("https://www.automationexercise.com/")

    # Remove the cookie consent overlay if present
    page.evaluate("""
        () => {
            const consent = document.querySelector('.fc-consent-root');
            if (consent) consent.remove();
        }
    """)

    # Click the "Video Tutorials" link in the navbar
    locator = page.get_by_role("link", name="Video Tutorials")
    expect(locator).to_be_visible()
    locator.click()

    # Wait for the page navigation to complete and verify URL
    expect(page).to_have_url(re.compile(r"https://www\.youtube\.com/c/AutomationExercise(\?.*)?"))

    # Optional: Verify page content loaded
    expect(page.locator("body")).to_be_visible()
