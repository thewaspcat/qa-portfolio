# Login Page Functionality – Valid Credentials

| Field | Value |
|---|---|
| Test case ID | `TC_UI_LOGIN_001` |
| Title | Login with valid credentials |
| Objective | Verify authentication and session persistence after reload. |
| Priority | High |
| Severity | Critical |
| Module | Login / Authentication |

## Environment

- Browser: Google Chrome, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/login`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible
- Valid credentials available through the approved secret mechanism

## Preconditions

- Start with a clean browser context and no active user session.

## Test Data

Credentials are supplied through the approved secret mechanism and excluded from source control and execution evidence.

| Field | Source |
|---|---|
| Email | `AUTOMATION_EXERCISE_EMAIL` |
| Password | `AUTOMATION_EXERCISE_PASSWORD` |
| Username, when validated | `AUTOMATION_EXERCISE_USERNAME` |
| Authenticated indicator | `Logged in as` |

## Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the login page. | The page loads at the configured URL and displays `Login to your account`. |
| 2 | Enter the valid email address. | The email is accepted in the email field. |
| 3 | Enter the valid password. | The password is accepted in the password field. |
| 4 | Select Login. | The user is authenticated. |
| 5 | Verify the authenticated UI. | `Logged in as`, the configured username when available, and Logout are visible. |
| 6 | Reload the page. | The authenticated state remains visible after reload. |

## Postconditions

The authenticated session remains active after reload.

## Automation Readiness

- **Automation Candidate:** Yes
- **Framework:** pytest with Playwright
- **Test Data Source:** `test_login_data.json` with credentials supplied through environment variables
- **Automation Priority:** High
- **Script Reference:** `test_tc_ui_login_001.py`
- **Automation Notes:**
  - Uses `LoginPage` locators for authentication and session validation.
  - Verifies the authenticated UI and session persistence after reload.
