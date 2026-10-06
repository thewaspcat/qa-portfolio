# TC_UI_LOGIN_001 — Login with valid credentials

## 1. Test Case Information

- **Test case ID:** `TC_UI_LOGIN_001`
- **Title:** Login with valid credentials
- **Objective:** Verify authentication and session persistence after reload.
- **Priority:** High
- **Severity:** Critical
- **Module:** Login / Authentication

## 2. Environment & Dependencies

- **Browser:** Google Chrome, latest stable
- **Operating system:** Windows / macOS / Linux
- **Test URL:** `https://www.automationexercise.com/login`

- Stable internet connection
- Application environment online and accessible
- Valid credentials available through the approved secret mechanism

## 3. Preconditions

- Start with a clean browser context and no active user session.

## 4. Test Data

Credentials are supplied through the approved secret mechanism and excluded from source control and execution evidence.

| Field | Source |
|---|---|
| Email | `AUTOMATION_EXERCISE_EMAIL` |
| Password | `AUTOMATION_EXERCISE_PASSWORD` |
| Authenticated indicator | `Logged in as` |

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the login page. | The page loads at the configured URL and displays `Login to your account`. |
| 2 | Enter the valid email address. | The email field displays the supplied address. |
| 3 | Enter the valid password. | The password field displays masked characters. |
| 4 | Select Login. | `Logged in as` and Logout are visible. |
| 5 | Reload the page. | `Logged in as` and Logout remain visible. |

## 6. Postconditions

The authenticated session remains active after reload.

## 7. Automation Readiness

- **Automation Candidate:** Yes
- **Framework:** pytest with Playwright
- **Test Data Source:** `test_login_data.json` with credentials supplied through environment variables
- **Automation Priority:** High
- **Script Reference:** `test_tc_ui_login_001.py`
- **Automation Notes:**
  - Uses `LoginPage` locators for authentication and session validation.
  - Verifies the authenticated UI and session persistence after reload.
