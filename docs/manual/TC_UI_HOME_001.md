# Homepage UI Layout and Components Display

| Field | Value |
|---|---|
| Test case ID | `TC_UI_HOME_001` |
| Title | Homepage UI layout and components |
| Objective | Verify that the homepage loads and displays its key UI components. |
| Priority | High |
| Severity | Medium |
| Module | Homepage |

## Environment

- Browser: Google Chrome, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible

## Preconditions

- Start with a clean browser context and no active user session.

## Test Data

| Field | Value |
|---|---|
| Expected title | `Automation Exercise` |
| Expected navigation links | Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact us |
| Expected sections | Featured Items, Recommended Items |

## Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the homepage. | The page loads with title `Automation Exercise`. |
| 2 | Verify the logo. | The logo is visible and has the expected `alt` value and a non-empty `src`. |
| 3 | Verify the navigation bar. | The navigation bar is visible as part of the homepage shell. |
| 4 | Verify the navigation links. | All expected links are present in the configured order with the expected visible labels and `href` values. |
| 5 | Verify the Featured Items section. | The section container is visible and its heading reads `Featured Items`. |
| 6 | Verify the Recommended Items section. | The section container is visible below Featured Items and its heading reads `Recommended Items`. |
| 7 | Verify the footer. | The footer is visible. |

## Postconditions

The browser session remains logged out and no application data is changed.

## Automation Readiness

- **Automation Candidate:** Yes
- **Framework:** pytest with Playwright
- **Test Data Source:** `test_homepage_data.json` and `test_navigation_data.json`
- **Automation Priority:** High
- **Script Reference:** `test_tc_ui_home_001.py`
- **Automation Notes:**
  - Uses `HomePage` locators for homepage component validation.
  - Verifies title, logo attributes, section visibility, the Recommended Items heading and DOM order, and footer visibility.
  - The Featured Items heading check is an expected failure for the documented defect.
