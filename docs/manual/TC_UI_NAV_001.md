# **Homepage Navigation Menu Functionality**

## 1. Test Case Information  

- **Test Case ID:** TC_UI_NAV_001  
- **Title:** Homepage Navigation Menu Functionality  
- **Objective:** Validate that the homepage navigation menu displays the expected links in the correct order and that each link redirects to the correct destination.  
- **Requirement Reference:** REQ-UI-NAV-001  
- **Test Type:** Functional  
- **Execution Type:** Manual / Automated  
- **Test Level:** System (UI)  
- **Priority:** Medium  
- **Severity:** Major  
- **Module:** Homepage → Navigation Bar  

---

## 2. Environment & Dependencies 

**Test Environment:**  
- **Browser:** Chrome / Firefox / Edge (latest stable versions)  
- **Operating System:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com  

**Dependencies:**  
- Stable internet connection  
- Test environment accessible and responsive  
- Cookie consent banners dismissed, if displayed 

---

## 3. Preconditions  

- Browser is installed and functional.  
- Cache and cookies are cleared.  
- Homepage is accessible and fully loaded. 
- User is logged out with no active session. 

---

## 4. Test Data  

| Field | Description | Value |
|--------|-------------|----------------|
| Test URL | Application homepage | `https://www.automationexercise.com` |
| Navigation Links | Menu items to validate | Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact Us |

---

## 5. Test Steps  

| Step # | Action | Locator / Reference | Expected Result |
|--------|---------|---------------------|-----------------|
| 1 | Navigate to the homepage | `ul.nav.navbar-nav` | Homepage loads at https://www.automationexercise.com/ and the navigation menu is visible. |
| 2 | Verify navigation link count | `ul.nav.navbar-nav > li` | Exactly 8 navigation links are displayed in the following order: Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact Us. |
| 3 | Click **Home** link | `ul.nav.navbar-nav > li > a[href="/"]` | User remains on the homepage and the navigation menu with 8 links remains visible. |
| 4 | Click **Products** link | `ul.nav.navbar-nav > li > a[href="/products"]` | User is redirected to `/products`. |
| 5 | Click **Cart** link | `ul.nav.navbar-nav > li > a[href="/view_cart"]` | User is redirected to `/view_cart`. |
| 6 | Click **Signup / Login** link | `ul.nav.navbar-nav > li > a[href="/login"]` | User is redirected to `/login`. |
| 7 | Click **Test Cases** link | `ul.nav.navbar-nav > li > a[href="/test_cases"]` | User is redirected to `/test_cases`. |
| 8 | Click **API Testing** link | `ul.nav.navbar-nav > li > a[href="/api_list"]` | User is redirected to `/api_list`. |
| 9 | Click **Video Tutorials** link | `ul.nav.navbar-nav > li > a[href="https://www.youtube.com/c/AutomationExercise"]` | External YouTube page opens in a new tab with the correct destination URL. |
| 10 | Click **Contact Us** link | `ul.nav.navbar-nav > li > a[href="/contact_us"]` | User is redirected to `/contact_us`. |

---

## 6. Actual Results  

- The homepage loaded successfully.
- The navigation menu was visible.
- Exactly 8 navigation links were displayed in the expected order.
- Each internal link redirected to the correct page.
- The Video Tutorials link opened the correct external YouTube destination in a new tab.

---

## 7. Status  

- **Pass:** All 8 links present, redirect correctly, and content loads as expected.  


---

## 8. Postconditions  

- User remains logged out.  
- Browser session can be safely closed.  

---

## 9. Notes

- Validate both **link text** and **href attributes** (case-sensitive).  
- Functional testing of forms (login/contact) covered in separate cases.  
- Broken link verification to be repeated during regression testing.  
- **Automation Note**: The automation scripts are split due to differences in behavior for internal versus external links.
  - Script 1: `test_tc_ui_nav_001.py`. It validates the first 7 internal navigation links.
  - Script 2:`test_tc_ui_nav_001_video_tutorials.py`. It validates the external link (Video Tutorials) opening in a new browser tab (YouTube).

---

## 10. Automation Readiness 
 
- **Automation Candidate:** Yes  
- **Framework:** Playwright  
- **Test Data Source:** Inline link definitions or JSON data file  
- **Automation Priority:** Medium  
- **Script Reference:** `test_tc_ui_nav_001.py` and `test_tc_ui_nav_001_video_tutorials.py`  
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
