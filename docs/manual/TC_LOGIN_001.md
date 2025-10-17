# **Valid Login with Correct Credentials (Data-Driven)**

## 1. Test Case Information
- **Test Case ID:** TC_UI_LOGIN_001  
- **Title:** Login Page Functionality – Valid Credentials  
- **Objective:** Confirm that users with valid credentials can log in successfully and session persists after reload.  
- **Requirement Reference:** REQ-AUTH-001  
- **Test Type:** Functional  
- **Execution Type:** Manual / Automated  
- **Test Level:** System (UI)  
- **Priority:** High  
- **Severity:** Critical  
- **Module:** Login / Authentication  
- **Created by:** Marta Czarnecka  
- **Created on:** 08.09.2025  
- **Last Updated:** 17.10.2025  

---

## 2. Environment & Dependencies
**Test Environment:**  
- **Browser:** Google Chrome (latest stable)  
- **Operating System:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com/login  

**Dependencies:**  
- Stable internet connection  
- Application environment online and accessible  
- JSON data file (`test_login_data.json`) with valid credentials  

---

## 3. Preconditions
- Browser is installed and functional  
- Cache and cookies are cleared  
- Application server is running  
- User is logged out (no active session)  
- Valid user data is available in `test_login_data.json`  

---

## 4. Test Data (from JSON file)

| Field | Description | Example Value |
|--------|-------------|----------------|
| `email` | User’s login email | `valid_user@example.com` |
| `password` | User’s login password | `CorrectPassword123!` |
| `username` | Displayed username after login | `valid_user` |

---

## 5. Test Steps

| Step # | Action | Locator / Reference | Expected Result |
|--------|---------|---------------------|-----------------|
| 1 | Navigate to the login page | `page.goto("https://www.automationexercise.com/login")` | Login page loads successfully with heading **“Login to your account.”** |
| 2 | Enter valid email in **Email Address** field | `page.get_by_label("Email Address")` | Email is entered successfully. |
| 3 | Enter valid password in **Password** field | `page.get_by_label("Password")` | Password is entered successfully. |
| 4 | Click the **Login** button | `page.get_by_role("button", name="Login")` | User is redirected to dashboard. |
| 5 | Verify post-login UI | `page.get_by_text("Logged in as {username}")`, `page.get_by_role("link", name="Logout")` | Dashboard displays navigation, logged-in username, and logout link. |
| 6 | Reload the page to verify session persistence | `page.reload()` | “Logged in as {username}” remains visible, confirming active session. |

---

## 6. Expected Results
- User logs in successfully with valid credentials.  
- Dashboard elements appear: navigation bar, “Logged in as {username}”, and logout link.  
- Session remains valid after page reload.  

---

## 7. Actual Results  
*(To be filled after execution.)*  

---

## 8. Status  
- **Pass:** All expected UI elements visible, and session persists after reload.  
- **Fail:** Any UI element missing or session invalidated after reload.  

---

## 9. Postconditions  
- User stays logged in with an active session.  
- Logout functionality verified separately.  

---

## 10. Notes  
- Data-driven execution allows reuse with multiple valid user credentials.  

---

## 11. Automation Readiness
- **Automation Candidate:** Yes  
- **Framework:** Playwright  
- **Test Data Source:** `test_login_data.json`  
- **Automation Priority:** High  
- **Script Reference:** `test_TC_UI_LOGIN_001_valid_login.py`  
- **Automation Notes:** Uses Playwright locators (`get_by_label`, `get_by_role`, `get_by_text`) for accessibility and maintainability.  

---

## Appendix: Locator Reference

| Element | Purpose | Playwright Locator |
|----------|----------|-------------------|
| Email field | Input for login email | `page.get_by_label("Email Address")` |
| Password field | Input for password | `page.get_by_label("Password")` |
| Login button | Submit credentials | `page.get_by_role("button", name="Login")` |
| Logged-in username | Verify login success | `page.get_by_text("Logged in as {username}")` |
| Logout link | End session | `page.get_by_role("link", name="Logout")` |
| Navigation bar | Verify dashboard UI | `page.get_by_role("navigation")` |

