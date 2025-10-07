# **Valid Login with Correct Credentials**

## 1. Test Case Information
- **Test Case ID:** TC_UI_LOGIN_001  
- **Title:** Valid Login with Correct Credentials  
- **Objective:** Ensure that a user can successfully log in with valid credentials.  
- **Requirement Reference:** REQ-AUTH-001  
- **Test Type:** Functional  
- **Execution Type:** Manual  
- **Test Level:** System (UI)  
- **Priority:** High  
- **Severity:** Critical  
- **Module:** Login / Authentication
- **Created by**: Marta Czarnecka
- **Created on**: 08.09.2025
- **Last Updated**: 14.09.2025

---

## 2. Environment & Dependencies
**Test Environment:**  
- **Browser:** Google Chrome (latest stable)  
- **Operating System:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com/login  

**Dependencies:**  
- Stable internet connection  
- Application environment online and accessible  

---

## 3. Preconditions
- Browser is installed and functional  
- Cache and cookies are cleared  
- Application server is running  
- User is logged out (no active session)  
- Valid user account exists in the system  

---

## 4. Test Data

| Data Field       | Value                          |
|------------------|--------------------------------|
| Test URL         | https://www.automationexercise.com/login |
| Valid Email      | valid_user@example.com         |
| Valid Password   | CorrectPassword123!            |

---

## 5. Test Steps

| Step # | Action | Locator / Selector | Expected Result |
|--------|--------|--------------------|-----------------|
| 1 | Navigate to the login page | N/A | Login page loads successfully with the heading **“Login to your account.”** |
| 2 | Enter valid email in the **Email Address** field | `input[data-qa="login-email"]` | Email is entered successfully. |
| 3 | Enter valid password in the **Password** field | `input[data-qa="login-password"]` | Password is entered successfully. |
| 4 | Click the **Login** button | `button[data-qa="login-button"]` | User is redirected to the dashboard. |
| 5 | Verify dashboard UI elements are displayed | N/A | Dashboard displays navigation menu, “Logged in as [username]” label, and logout button. |
| 6 | Confirm that required HTML elements exist in the page source (see Appendix) | Browser → View Page Source | Expected elements are present. |

---

## 6. Expected Results
- User is successfully logged in with valid credentials.  
- System redirects to the dashboard.  
- Dashboard displays essential UI elements: navigation, “Logged in as [username]”, and logout button.  
- A valid user session is created and maintained.  

---

## 7. Actual Results
*(To be filled after execution.)*  

---

## 8. Status
- **Pass:** User is redirected to dashboard, logged-in state confirmed, UI elements visible.  
- **Fail:** User is not redirected, dashboard does not display correctly, or session is not created.  

---

## 9. Postconditions
- User remains logged in with an active session.  

---

## 10. Notes
- Test can be repeated with multiple valid user accounts.  
- Logout functionality is validated in a separate test case.  

---

## 11. Automation Readiness
- **Automation Candidate:** Yes  
- **Target Framework:** Playwright / Selenium (as per team standard)  
- **Automation Priority:** High  
- **Automated Step Reference:** Step 6 – HTML element validation  
- **Script Reference:** `test_login_valid_credentials.py` (or equivalent)  
- **Automation Notes:** Step 6 can be automated using assertions that verify presence of defined locators.  

---

## Appendix: Element Locator Reference

| Element                    | Purpose                                  | Locator Type | Locator / Selector |
|----------------------------|------------------------------------------|---------------|--------------------|
| Email field                | Input for user’s login email             | CSS           | `input[data-qa="login-email"]` |
| Password field             | Input for user’s login password          | CSS           | `input[data-qa="login-password"]` |
| Login button               | Button to submit login credentials       | CSS           | `button[data-qa="login-button"]` |
| Navigation menu            | Main navigation after login               | CSS           | `div[class="navbar"]` |
| Logged-in username label   | Displays “Logged in as [username]”       | CSS           | ``a[href="/profile"]` |
| Logout button              | Button to log out of the session          | CSS           | `a[href="/logout"]` |

