# **Homepage UI Layout and Components Display**

## 1. Test Case Information
- **Test Case ID:** TC_UI_HOME_001  
- **Title:** Homepage UI Layout and Components Display 
- **Objective:** Validate that the homepage UI loads correctly and contains key structural components with correct attributes and content.   
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
| 4 | Verify navigation link texts and hrefs| `ul.nav.navbar-nav > li > a` | Each link text and corresponding `href` match test data.|
| 5 | Verify “Featured Items” section | `div.features_items` | Section is visible with the header “Featured Items.” |
| 6 | Verify “Recommended Items” section | `div.recommended_items` | Section is visible with the header “Recommended Items.” (May require scrolling.) |
| 7 | Verify footer presence | `footer#footer` | Footer is visible at the bottom, containing branding and social icons. |

---

## 6. Expected Results
- Homepage title is exactly **“Automation Exercise.”**  
- Logo is displayed correctly with valid attributes.  
- Navigation bar displays all 8 links with correct texts and valid `href` values.  
- “Featured Items” and “Recommended Items” sections appear in the correct order.  .  
- Footer is visible and contains expected branding/social components. 

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
- User remains logged out.  
- No browser session or application state changes occur after execution.  

---

## 10. Notes
- Verification of link texts and section headers is **case-sensitive** as per design specifications.  
- The “Recommended Items” section may require scrolling to become visibile.  
- This test focuses on **UI structure only**; navigation functionality is tested separately.  
- Performance and console checks are out of scope.
- If navigation structure changes, the test data table shall be updated accordingly.  

---

## 11. Automation Readiness
- **Automation Candidate:** Yes  
- **Target Framework:** Playwright (preferred)  
- **Automation Priority:** High  
- **Automated Step Reference:** Step 8 – Page source validation  
- **Script Reference:** `test_tc_ui_home_001.py`  
- **Automation Notes:**  
  - Data-driven implementation uses parameterized test data for link text–href pairs.  
  - Assertions cover visibility, text validation, and attribute checks.  

---

## Appendix: Element Locator Reference

| Element | Purpose | Locator Type | Locator / Selector |
|----------|----------|---------------|--------------------|
| Logo | Brand visibility | Locator | `page.locator("div.logo.pull-left a img")` |
| Navigation bar | Container for main links | Locator | `page.locator("ul.nav.navbar-nav")` |
| Navigation links | Validate link text and href | Locator | `page.locator("ul.nav.navbar-nav > li > a")` |
| Features Items | Verify section presence | Locator | `page.locator("div.features_items")` |
| Recommended Items | Verify section presence | Locator | `page.locator("div.recommended_items")` |
| Footer | Page footer | Locator | `page.locator("footer#footer")` |

---
