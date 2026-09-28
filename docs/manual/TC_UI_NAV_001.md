# Homepage Navigation Menu Functionality

| Field | Value |
|---|---|
| Test case ID | `TC_UI_NAV_001` |
| Title | Homepage navigation menu |
| Objective | Verify navigation link order, labels, destinations, and behavior. |
| Priority | Medium |
| Severity | Major |
| Module | Homepage → Navigation Bar |

## Environment

- Browser: Chrome, Firefox, or Edge, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible
- Consent UI handled if displayed

## Preconditions

- Start with a clean browser context and no active user session.

## Test Data

Expected order:

1. Home
2. Products
3. Cart
4. Signup / Login
5. Test Cases
6. API Testing
7. Video Tutorials
8. Contact us

## Test Steps and Expected Results

For steps 4–11, start each destination check from a fresh browser context at the homepage.

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the homepage. | The homepage loads and the navigation menu is visible. |
| 2 | Verify the navigation count and order. | Exactly eight links are displayed in the configured order. |
| 3 | Verify link text and `href` values. | Each link has the expected visible label and configured destination. |
| 4 | Select Home. | The user remains on the homepage. |
| 5 | Select Products. | The user is redirected to `/products` and the destination page loads. |
| 6 | Select Cart. | The user is redirected to `/view_cart` and the destination page loads. |
| 7 | Select Signup / Login. | The user is redirected to `/login` and the login page loads. |
| 8 | Select Test Cases. | The user is redirected to `/test_cases` and the destination page loads. |
| 9 | Select API Testing. | The user is redirected to `/api_list` and the destination page loads. |
| 10 | Select Video Tutorials. | The current browser tab navigates to the configured YouTube destination. A YouTube consent redirect may appear before the final destination. |
| 11 | Select Contact us. | The user is redirected to `/contact_us`. |

## Postconditions

The user remains logged out and the browser session can be closed safely.

## Automation Readiness

- **Automation Candidate:** Yes
- **Framework:** pytest with Playwright
- **Test Data Source:** `test_navigation_data.json`
- **Automation Priority:** Medium
- **Script Reference:** `test_tc_ui_nav_001.py`
- **Automation Notes:**
  - Uses `HomePage` locators for navigation structure and destination validation.
  - Verifies link count, order, labels, `href` values, internal destinations, and same-tab Video Tutorials navigation.
