# Homepage Navigation Menu Functionality

## Document Control

| Field | Value |
|---|---|
| Document version | 1.2 |
| Last updated | 2026-09-23 |
| Document owner | TBD |
| Requirement owner | TBD |

## Test Case Information

- **Test Case ID:** TC_UI_NAV_001
- **Title:** Homepage Navigation Menu Functionality
- **Objective:** Validate that the homepage navigation menu displays the expected links in the correct order and that each link reaches its configured destination.
- **Requirement Reference:** REQ-UI-NAV-001
- **Test Type:** Functional
- **Execution Type:** Manual / Automated
- **Test Level:** System (UI)
- **Priority:** Medium
- **Severity:** Major
- **Module:** Homepage → Navigation Bar

## 2. Environment & Dependencies

- Browser: Chrome, Firefox, or Edge, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible
- Consent UI handled if displayed
- Browser automation runtime and Playwright browser available for automated execution

## 3. Preconditions

- Browser is installed and functional.
- Cache and cookies are cleared prior to manual execution, or a fresh browser context is used for automated execution.
- Application server is online and reachable.
- User is logged out with no active session.

## 4. Test Data

The navigation dataset is stored in `docs/automation/data/test_navigation_data.json`.

Expected order:

1. Home
2. Products
3. Cart
4. Signup / Login
5. Test Cases
6. API Testing
7. Video Tutorials
8. Contact us

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the homepage. | The homepage loads and the navigation menu is visible. |
| 2 | Verify the navigation count and order. | Exactly eight links are displayed in the configured order. |
| 3 | Verify link text and `href` values. | Each link has the expected visible label and configured destination. |
| 4 | Select Home. | The user remains on the homepage. |
| 5 | Select Products. | The user is redirected to `/products` and the destination page loads. |
| 6 | Select Cart. | The user is redirected to `/view_cart` and the destination page loads. |
| 7 | Select Signup / Login. | The user is redirected to `/login` and the login page loads. Detailed login validation is covered by `TC_UI_LOGIN_001`. |
| 8 | Select Test Cases. | The user is redirected to `/test_cases` and the destination page loads. |
| 9 | Select API Testing. | The user is redirected to `/api_list` and the destination page loads. |
| 10 | Select Video Tutorials. | The current browser tab navigates to the configured YouTube destination. A YouTube consent redirect may appear before the final destination. |
| 11 | Select Contact us. | The user is redirected to `/contact_us`. |

## 6. Automation Mapping

- Implementation: `docs/automation/tests/test_navigation.py`
- Structure test: `test_tc_ui_nav_001_navigation_order_and_attributes`
- Internal destinations: `test_tc_ui_nav_001_internal_navigation`
- External destination: `test_tc_ui_nav_002_video_tutorials_same_tab`
- POM: `docs/automation/pages/home_page.py`
- Data: `docs/automation/data/test_navigation_data.json`

Execution outcomes are recorded separately in `docs/manual/results/TC_UI_NAV_001_result.md`.

## 7. Postconditions

The user remains logged out and the browser session can be closed safely.
