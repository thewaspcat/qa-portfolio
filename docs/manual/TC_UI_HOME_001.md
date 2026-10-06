# TC_UI_HOME_001 — Homepage shell and key components

## 1. Test Case Information

- **Test case ID:** `TC_UI_HOME_001`
- **Title:** Homepage shell and key components
- **Objective:** Verify that the homepage loads and displays its key UI components.
- **Priority:** High
- **Severity:** Medium
- **Module:** Homepage

## 2. Environment & Dependencies

- **Browser:** Google Chrome, latest stable
- **Operating system:** Windows / macOS / Linux
- **Test URL:** `https://www.automationexercise.com/`

- Stable internet connection
- Application environment online and accessible

## 3. Preconditions

- Start with a clean browser context and no active user session.

## 4. Test Data

| Field | Value |
|---|---|
| Expected title | `Automation Exercise` |
| Expected logo `alt` | `Website for automation practice` |
| Expected sections | Featured Items, Recommended Items |

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the homepage. | The page loads with title `Automation Exercise`. |
| 2 | Verify the logo. | The logo is visible, its `alt` matches the Test Data value, and its `src` is non-empty. |
| 3 | Verify the navigation bar. | The navigation bar is visible as part of the homepage shell. |
| 4 | Verify the Featured Items section. | The section container is visible and its heading reads `Featured Items`. |
| 5 | Verify the Recommended Items section. | The section container is visible below Featured Items and its heading reads `Recommended Items`. |
| 6 | Verify the footer. | The footer is visible. |

## 6. Postconditions

The browser session remains logged out and no application data is changed.

## 7. Automation Readiness

- **Automation Candidate:** Yes
- **Framework:** pytest with Playwright
- **Test Data Source:** `test_homepage_data.json`
- **Automation Priority:** High
- **Script Reference:** `test_tc_ui_home_001.py`
- **Automation Notes:**
  - Uses `HomePage` locators for homepage component validation.
  - Verifies title, logo attributes, section visibility, the Recommended Items heading and DOM order, and footer visibility.
