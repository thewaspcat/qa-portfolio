
# Valid Login with Correct Credentials

## 1. Test Case Information
- **Test Case ID:** TC_UI_LOGIN_001  
- **Title:** Valid Login with Correct Credentials  
- **Objective:** Ensure that a user can successfully log in with valid credentials and access the homepage.  
- **Requirement Reference:** REQ-AUTH-001  
- **Test Type:** Manual / Functional
- **Test Level:** System (UI)  
- **Priority:** High  
- **Severity:** Critical  
- **Module:** Login / Authentication  
- **Created By:** Marta Czarnecka  
- **Created Date:** 09.09.2025  
- **Last Updated:** 16.09.2025  

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
| 1 | Navigate to the login page | N/A | Login page loads successfully with the heading **“Login to your account”**. |
| 2 | Enter valid email in the **Email Address** field | `input type="email" data-qa="login-email"` | Email is entered. |
| 3 | Enter valid password in the **Password** field | `input type="password" data-qa="login-password"` | Password is entered. |
| 4 | Click the **Login** button | `button data-qa="login-button"` | User is redirected to the homepage. |
| 5 | Verify homepage UI elements are displayed | N/A | Homepage is visible with navigation menu, “Logged in as [username]” label, and logout button. |
| 6 | Confirm page source contains required HTML elements (see Appendix) | Browser → View Page Source | All expected elements are present. |

---

## 6. Expected Results
- User is successfully logged in with valid credentials  
- System redirects to homepage  
- Homepage displays UI elements: navigation, “Logged in as [username]”, logout button  
- A valid session is created  
- Page source contains required elements as listed in Appendix  

---

## 7. Actual Results
(To be filled after execution.)  

---

## 8. Status
- **Pass:** User is redirected to homepage, logged in state confirmed, UI elements visible  
- **Fail:** User is not redirected, homepage does not display correctly, or session is not created  

---

## 9. Postconditions
- User remains logged in with an active session  

---

## 10. Notes
- Test can be repeated with multiple valid user accounts  
- Logout functionality is validated in a separate test case  

---

## Appendix: Page Source Reference

| Element        | Locator / Selector |
|----------------|---------------------|
| Email field    | `input[data-qa="login-email"]` |
| Password field | `input[data-qa="login-password"]` |
| Login button   | `button[data-qa="login-button"]` |

