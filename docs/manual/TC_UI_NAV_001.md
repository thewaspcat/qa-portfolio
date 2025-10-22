# **Homepage Navigation Menu Functionality**

## 1. Test Case Information  
- **Test Case ID:** TC_UI_NAV_001  
- **Title:** Homepage Navigation Menu Functionality  
- **Objective:** Validate that each navigation menu link on the homepage redirects to the correct page and displays the corresponding content.  
- **Requirement Reference:** REQ-UI-NAV-001  
- **Test Type:** Functional  
- **Execution Type:** Manual / Automated  
- **Test Level:** System (UI)  
- **Priority:** Medium  
- **Severity:** Major  
- **Module:** Homepage → Navigation Bar  
- **Created by:** Marta Czarnecka  
- **Created on:** 09.09.2025  
- **Last Updated:** 22.10.2025  

---

## 2. Environment & Dependencies  
**Test Environment:**  
- **Browser:** Chrome / Firefox / Edge (latest stable versions)  
- **Operating System:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com  

**Dependencies:**  
- Stable internet connection  
- Test environment accessible and responsive  
- Cookie consent banners dismissed  

---

## 3. Preconditions  
- Browser is installed and functional  
- Cache and cookies are cleared  
- Homepage is accessible and fully loaded  
- User is logged out (no active session)  

---

## 4. Test Data  

| Field | Description | Example Value |
|--------|-------------|----------------|
| Test URL | Application homepage | `https://www.automationexercise.com` |
| Navigation Links | Menu items to validate | Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact Us |

---

## 5. Test Steps  

| Step # | Action | Locator / Reference | Expected Result |
|--------|---------|---------------------|-----------------|
| 1 | Navigate to homepage | `ul.nav.navbar-nav` | Homepage loads; navigation menu is visible. |
| 2 | Verify navigation link count | `ul.nav.navbar-nav > li` | Exactly 8 links are displayed in correct order. |
| 3 | Click **Home** link | `ul.nav.navbar-nav > li > a[href="/"]` | User remains on homepage (`/`); sections like **Featured Items** and **Recommended Items** visible. |
| 4 | Click **Products** link | `ul.nav.navbar-nav > li > a[href="/products"]` | Redirects to `/products`; product grid loads with items, names, prices. |
| 5 | Click **Cart** link | `ul.nav.navbar-nav > li > a[href="/view_cart"]` | Redirects to `/view_cart`; cart table and totals visible. |
| 6 | Click **Signup / Login** link | `ul.nav.navbar-nav > li > a[href="/login"]` | Redirects to `/login`; email and password fields visible. |
| 7 | Click **Test Cases** link | `ul.nav.navbar-nav > li > a[href="/test_cases"]` | Redirects to `/test_cases`; list of test cases visible. |
| 8 | Click **API Testing** link | `ul.nav.navbar-nav > li > a[href="/api_list"]` | Redirects to `/api_list`; API endpoint list visible. |
| 9 | Click **Video Tutorials** link | `ul.nav.navbar-nav > li > a[href="https://www.youtube.com/c/AutomationExercise"]` | Opens YouTube channel in new tab, validated in separate automation script. |
| 10 | Click **Contact Us** link | `ul.nav.navbar-nav > li > a[href="/contact_us"]` | Redirects to `/contact_us`; form with fields Name, Email, Subject, Message, Submit visible. |

---

## 6. Expected Results  
- Navigation menu is visible and lists 8 links in correct order.  
- Each link redirects to the intended page or external URL.  
- All target pages load without errors and display key content elements.  

---

## 7. Actual Results  
*(To be filled after execution.)*  

---

## 8. Status  
- **Pass:** All 8 links present, redirect correctly, and content loads as expected.  
- **Fail:** Any link is missing, broken, mislabeled, or redirects incorrectly.  

---

## 9. Postconditions  
- User remains logged out.  
- Browser session can be safely closed.  

---

## 10. Notes  
- Validate both **link text** and **href attributes** (case-sensitive).  
- Functional testing of forms (login/contact) covered in separate cases.  
- Broken link verification to be repeated during regression testing.  
- **Automation Note**: The automation scripts are split due to differences in behavior for internal versus external links.
-   Script 1: Validates the first 7 internal navigation links (Home → Contact us).
-   Script 2: Validates the external link (Video Tutorials) opening in a new browser tab (YouTube).

---

## 11. Automation Readiness  
- **Automation Candidate:** Yes  
- **Framework:** Playwright  
- **Test Data Source:** Inline link definitions or JSON data file  
- **Automation Priority:** Medium  
- **Script Reference:** `test_tc_ui_nav_001.py and test_tc_ui_nav_001_video_tutorials.py`  
- **Automation Notes:** Each link click and redirection validated using Playwright’s `page.url()` and `expect(page).to_have_url()` assertions.  

---

## Appendix: Locator Reference  

| Element | Purpose | Playwright Locator |
|----------|----------|-------------------|
| Navigation bar | Container for all menu items | `ul.nav.navbar-nav` |
| Home link | Homepage redirect | `a[href="/"]` |
| Products link | Product listing page | `a[href="/products"]` |
| Cart link | Cart page | `a[href="/view_cart"]` |
| Signup / Login link | Login/registration page | `a[href="/login"]` |
| Test Cases link | Test case list | `a[href="/test_cases"]` |
| API Testing link | API list page | `a[href="/api_list"]` |
| Video Tutorials link | YouTube channel | `a[href*="youtube.com"]` |
| Contact Us link | Contact form page | `a[href="/contact_us"]` |
