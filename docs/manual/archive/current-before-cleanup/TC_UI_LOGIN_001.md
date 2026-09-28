# Login Page Functionality – Valid Credentials

## Document Control

| Field | Value |
|---|---|
| Document version | 1.2 |
| Last updated | 2026-09-23 |
| Document owner | TBD |
| Requirement owner | TBD |

## Test Case Information

- **Test Case ID:** TC_UI_LOGIN_001
- **Title:** Login Page Functionality – Valid Credentials
- **Objective:** Confirm that valid credentials authenticate a user and that the session persists after reload.
- **Requirement Reference:** REQ-AUTH-001
- **Test Type:** Functional
- **Execution Type:** Manual / Automated
- **Test Level:** System (UI)
- **Priority:** High
- **Severity:** Critical
- **Module:** Login / Authentication

## 2. Environment & Dependencies

- Browser: Google Chrome, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/login`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible
- Valid credentials available through the approved secret mechanism
- Browser automation runtime and Playwright browser available for automated execution

## 3. Preconditions

- Browser is installed and functional.
- Cache and cookies are cleared prior to manual execution, or a fresh browser context is used for automated execution.
- Application server is online and reachable.
- User is logged out with no active session.

## Test Data

## 4. Test Data

Credentials must not be stored in source control. Automation reads the following environment variables named by `docs/automation/data/test_login_data.json`.

Credentials must also be excluded from logs, screenshots, traces, reports, and defect attachments.

| Field | Source |
|---|---|
| Email | `AUTOMATION_EXERCISE_EMAIL` |
| Password | `AUTOMATION_EXERCISE_PASSWORD` |
| Username, when validated | `AUTOMATION_EXERCISE_USERNAME` |
| Authenticated indicator | `Logged in as` |

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Navigate to the login page. | The page loads at the configured URL and displays `Login to your account.` |
| 2 | Enter the valid email address. | The email is accepted in the email field. |
| 3 | Enter the valid password. | The password is accepted in the password field. |
| 4 | Select Login. | The user is authenticated. |
| 5 | Verify the authenticated UI. | `Logged in as`, the configured username when available, and Logout are visible. |
| 6 | Reload the page. | The authenticated state remains visible after reload. |

## 6. Automation Mapping

- Implementation: `docs/automation/tests/test_login.py`
- Test: `test_tc_ui_login_001_valid_credentials`
- POM: `docs/automation/pages/login_page.py`
- Data: `docs/automation/data/test_login_data.json`

Execution outcomes are recorded separately in `docs/manual/results/TC_UI_LOGIN_001_result.md`.

## 7. Postconditions

The test should log out during cleanup when required by the test environment.
