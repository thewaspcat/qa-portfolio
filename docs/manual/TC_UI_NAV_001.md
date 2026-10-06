# TC_UI_NAV_001 — Homepage navigation menu

## 1. Test Case Information

- **Test case ID:** `TC_UI_NAV_001`
- **Title:** Homepage navigation menu
- **Objective:** Verify navigation link order, labels, destinations, and behavior.
- **Priority:** Medium
- **Severity:** Major
- **Module:** Homepage → Navigation Bar

## 2. Environment & Dependencies

- **Browser:** Chrome, Firefox, or Edge, latest stable
- **Operating system:** Windows / macOS / Linux
- **Test URL:** `https://www.automationexercise.com/`

- Stable internet connection
- Application environment online and accessible
- Consent UI handled if displayed

## 3. Preconditions

- Start with a clean browser context and no active user session.

## 4. Test Data

Expected menu links in order:

Internal `href` paths resolve against the origin of the Test URL.

| Label | `href` |
|---|---|
| Home | `/` |
| Products | `/products` |
| Cart | `/view_cart` |
| Signup / Login | `/login` |
| Test Cases | `/test_cases` |
| API Testing | `/api_list` |
| Video Tutorials | `https://www.youtube.com/c/AutomationExercise` |
| Contact us | `/contact_us` |

## 5. Test Steps and Expected Results

For steps 4–11, start each destination check from a fresh browser context at the homepage.

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the homepage. | The homepage loads and the navigation menu is visible. |
| 2 | Verify the navigation count and order. | Exactly eight links are displayed in the configured order. |
| 3 | Verify link text and `href` values. | Each link has the visible label and `href` specified in Test Data. |
| 4 | Select Home. | The browser URL matches the Home destination in Test Data. |
| 5 | Select Products. | The browser URL matches the Products destination in Test Data. |
| 6 | Select Cart. | The browser URL matches the Cart destination in Test Data. |
| 7 | Select Signup / Login. | The browser URL matches the Signup / Login destination in Test Data. |
| 8 | Select Test Cases. | The browser URL matches the Test Cases destination in Test Data. |
| 9 | Select API Testing. | The browser URL matches the API Testing destination in Test Data. |
| 10 | Select Video Tutorials. | The current tab reaches the Video Tutorials URL in Test Data or its YouTube consent URL. |
| 11 | Select Contact us. | The browser URL matches the Contact us destination in Test Data. |

## 6. Postconditions

The user remains logged out and the browser session can be closed safely.

## 7. Automation Readiness

- **Automation Candidate:** Yes
- **Framework:** pytest with Playwright
- **Test Data Source:** `test_navigation_data.json`
- **Automation Priority:** Medium
- **Script Reference:** `test_tc_ui_nav_001.py`
- **Automation Notes:**
  - Uses `HomePage` locators for navigation structure and destination validation.
  - Verifies link count, order, labels, `href` values, internal destinations, and same-tab Video Tutorials navigation.
