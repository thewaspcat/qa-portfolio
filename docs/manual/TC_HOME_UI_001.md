# **Homepage UI Layout and Components Display**

## 1. Test Case Information
- **Test Case ID:** TC_UI_HOME_001  
- **Title:** Homepage UI Layout and Components Display 
- **Objective:** Validate that the homepage UI loads correctly with logo, navigation bar, main sections, and footer as per page structure.  
- **Requirement Reference:** REQ-WEB-HOME-004  
- **Test Type:** Functional  
- **Execution Type:** Manual  
- **Test Level:** System (UI)  
- **Priority:** High  
- **Severity:** Medium  
- **Module:** Homepage  
- **Created by:** Marta Czarnecka  
- **Created on:** 08.09.2025  
- **Last Updated:** 17.10.2025  

---

## 2. Environment & Dependencies
**Test Environment:**  
- **Browser:** Google Chrome (latest stable)  
- **Operating System:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com  

**Dependencies:**  
- Stable internet connection  
- Application environment accessible and online  
- User is logged out (no active session)  

---

## 3. Preconditions
- Chrome browser (latest stable version) is installed and functional.  
- Browser cache and cookies are cleared prior to test execution.  
- Application server is online and reachable.  
- User is logged out (no active session).  

---

## 4. Test Data

| Data Field | Value |
|-------------|-------|
| Test URL | https://www.automationexercise.com |
| Page Title | Automation Exercise |
| Navigation Links | Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact us |

---

## 5. Test Steps

| Step # | Action | Locator / Selector | Expected Result |
|--------|--------|--------------------|-----------------|
| 1 | Navigate to the homepage | N/A | Homepage loads successfully with the title **“Automation Exercise.”** |
| 2 | Verify logo presence | `div.logo.pull-left a img` | Logo is visible in the header and has valid `src` and `alt` attributes. |
| 3 | Verify navigation bar visibility | `ul.nav.navbar-nav` | Navigation bar is rendered correctly below the logo. |
| 4 | Verify navigation link texts | `ul.nav.navbar-nav > li > a` | Navigation links display correct texts: Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact us. |
| 5 | Verify navigation link hrefs | `ul.nav.navbar-nav > li > a` | Each link has a valid, non-empty `href` attribute. |
| 6 | Verify “Features Items” section | `div.features_items` | Section is visible with the header “Features Items.” |
| 7 | Verify “Recommended Items” section | `div.recommended_items` | Section is visible with the header “Recommended Items.” (May require scrolling.) |
| 8 | Verify footer presence | `footer#footer` | Footer is visible at the bottom, containing branding and social icons. |

---

## 6. Expected Results
- Homepage title is exactly **“Automation Exercise.”**  
- Logo is displayed correctly with valid attributes.  
- Navigation bar displays all 8 links with correct texts and valid `href` values.  
- “Features Items” and “Recommended Items” sections appear in the correct order.  
- Footer is displayed at the bottom with expected branding and social elements.  
- All required elements exist and are visible in the DOM.  

---

## 7. Actual Results
*(To be filled after execution.)*  

---

## 8. Status
- **Pass:** All homepage UI components load and render correctly as specified.  
- **Fail:** One or more homepage UI components are missing, mislabeled, or incorrectly rendered.  

---

## 9. Postconditions
- No changes to browser session or application state.  
- User remains logged out and homepage remains accessible after test execution.  

---

## 10. Notes
- Verification of link texts and section headers is **case-sensitive** as per design specifications.  
- The “Recommended Items” section may require scrolling to view.  
- Functional behavior of navigation links and logo redirects is covered in separate test cases.  
- Performance and console log validation are out of scope for this test.    

---

## 11. Automation Readiness
- **Automation Candidate:** Yes  
- **Target Framework:** Playwright / Selenium (as per team standard)  
- **Automation Priority:** Medium  
- **Automated Step Reference:** Step 2–8 – DOM element validation  
- **Script Reference:** `test_tc_home_ui.py`  
- **Automation Notes:** Element existence and attributes are validated through DOM-based checks using automated assertions on defined locators.  

---

## Appendix: Element Locator Reference

| Element | Purpose | Locator Type | Locator / Selector |
|----------|----------|---------------|--------------------|
| Logo | Verifies brand visibility | CSS | `div.logo.pull-left a img` |
| Navigation bar | Contains main site links | CSS | `ul.nav.navbar-nav` |
| Navigation links | Text and href validation | CSS | `ul.nav.navbar-nav > li > a` |
| Features Items section | Displays main product highlights | CSS | `div.features_items` |
| Recommended Items section | Displays suggested products | CSS | `div.recommended_items` |
| Footer | Displays site branding and social icons | CSS | `footer#footer` |

---
