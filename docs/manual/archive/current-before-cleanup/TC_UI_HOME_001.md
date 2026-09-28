# Homepage UI Layout and Components Display

## Document Control

| Field | Value |
|---|---|
| Document version | 1.2 |
| Last updated | 2026-09-23 |
| Document owner | TBD |
| Requirement owner | TBD |
| Defect reference | [`BR_TC_UI_HOME_001`](https://thewaspcat.github.io/qa-portfolio/bugs/BR_TC_UI_HOME_001.html) |

## Test Case Information

- **Test Case ID:** TC_UI_HOME_001
- **Title:** Homepage UI Layout and Components Display
- **Objective:** Validate that the homepage loads and displays the key UI components, structure, attributes, and content.
- **Requirement Reference:** REQ-WEB-HOME-004
- **Test Type:** Functional
- **Execution Type:** Manual / Automated
- **Test Level:** System (UI)
- **Priority:** High
- **Severity:** Medium
- **Module:** Homepage

## 2. Environment & Dependencies

**Test Environment:**

- Browser: Google Chrome, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible
- Browser automation runtime and Playwright browser available for automated execution
- No active user session

## 3. Preconditions

- Browser is installed and functional.
- Cache and cookies are cleared prior to manual execution, or a fresh browser context is used for automated execution.
- Application server is online and reachable.
- User is logged out with no active session.

## 4. Test Data

| Field | Value |
|---|---|
| `home_url` | `https://www.automationexercise.com/` |
| `expected_title` | `Automation Exercise` |
| Expected sections | Featured Items, Recommended Items |

Source: `docs/automation/data/test_homepage_data.json`. Navigation data is owned by `TC_UI_NAV_001`.

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the homepage. | The page loads with title `Automation Exercise`. |
| 2 | Verify the logo. | The logo is visible and has the expected `alt` value and a non-empty `src`. |
| 3 | Verify the navigation bar. | The navigation bar is visible as part of the homepage shell. |
| 4 | Verify the Featured Items container. | The section container is visible. The exact heading is validated separately because the known heading defect is independently reportable. |
| 5 | Verify the Recommended Items section. | The section container is visible. |
| 6 | Verify the footer. | The footer is visible. |

Navigation link count, order, labels, `href` values, and navigation behavior are covered by `TC_UI_NAV_001`.

## 6. Automation Mapping

- Implementation: `docs/automation/tests/test_home.py`
- Test: `test_tc_ui_home_001_homepage_layout`
- POM: `docs/automation/pages/home_page.py`
- Data: `docs/automation/data/test_homepage_data.json`
- Related test case: `TC_UI_HOME_002`
- Related automation defect test: `test_tc_ui_home_002_featured_items_heading`

## 7. Postconditions

The browser session remains logged out and no application data is changed.

Execution outcomes are recorded separately in `docs/manual/results/TC_UI_HOME_001_result.md`.
