# **Homepage UI Layout and Components Display**

## 1. Test Case Information
- **Test Case ID:** TC_UI_HOME_001  
- **Title:** Homepage UI Layout and Components Display 
- **Objective:** Validate that the homepage UI loads correctly and displays all key UI components with correct structure, attributes, and content.   
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
- Application environment online and accessible  
- No active user session  

---

## 3. Preconditions
- Browser installed and functional  
- Cache and cookies cleared prior to execution  
- Application server online and reachable  
- User logged out (no active session)  

---

## 4. Test Data

| Field | Description | Value |
|--------|-------------|---------------|
| `test_url` | Target homepage URL | `https://www.automationexercise.com` |
| `page_title` | Expected browser title | `Automation Exercise` |
| `navigation_links` | Expected navigation items | Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact us |

---

## 5. Test Steps

| Step # | Action | Locator / Reference | Expected Result |
|--------|---------|---------------------|-----------------|
| 1 | Navigate to the homepage | `page.goto("https://www.automationexercise.com")` | Homepage loads successfully with title **“Automation Exercise.”** |
| 2 | Verify logo visibility and attributes | `page.locator("div.logo.pull-left a img")` | Logo is visible with valid `src` and `alt` attributes. |
| 3 | Verify navigation bar visibility | `page.locator("ul.nav.navbar-nav")` | Navigation bar is displayed correctly below the logo. |
| 4 | Validate navigation link texts and hrefs | `page.locator("ul.nav.navbar-nav > li > a")` | Each navigation link displays expected text and valid `href` value. |
| 5 | Verify **Featured Items** section presence | `page.locator("div.features_items")` | Section visible with heading **“Featured Items.”** |
| 6 | Verify **Recommended Items** section presence | `page.locator("div.recommended_items")` | Section visible with heading **“Recommended Items.”** (Scrolling may be required.) |
| 7 | Verify footer visibility | `page.locator("footer#footer")` | Footer displayed at bottom of page with branding and social icons. |

---

## 6. Expected Results
- Homepage title matches **“Automation Exercise.”**  
- Logo and navigation bar displayed correctly with valid attributes.  
- Navigation bar includes all expected links with correct text and URLs.  
- “Featured Items” and “Recommended Items” sections appear in correct order.  
- Footer visible and contains branding and social icons.  

---

## 7. Actual Results  
*(To be completed after execution.)*  

---

## 8. Status  
- **Pass:** All homepage UI components load and render as expected.  
- **Fail:** Any homepage component missing, mislabeled, or incorrectly rendered.  

---

## 9. Postconditions  
- Browser session and application state unchanged.  
- User remains logged out after test completion.  

---

## 10. Notes  
- Verification of link texts and section headers is **case-sensitive** per design.  
- “Recommended Items” may require scrolling to be visible.  
- Test focuses on **UI layout and structural validation only**; navigation functionality tested separately.  
- Update test data table if navigation structure changes.  

---

## 11. Automation Readiness
- **Automation Candidate:** Yes  
- **Framework:** Playwright  
- **Test Data Source:** Parameterized navigation dataset  
- **Automation Priority:** High  
- **Script Reference:** `test_tc_ui_home_001.py`  
- **Automation Notes:**  
  - Uses Playwright locators (`page.locator`) for component validation.  
  - Validates visibility, inner text, and attribute integrity.  
  - Element existence is validated through DOM-based checks in automation.  

---

## Appendix: Locator Reference

| Element | Purpose | Playwright Locator |
|----------|----------|-------------------|
| Logo | Brand identity check | `page.locator("div.logo.pull-left a img")` |
| Navigation bar | Container for main links | `page.locator("ul.nav.navbar-nav")` |
| Navigation links | Verify link text and `href` values | `page.locator("ul.nav.navbar-nav > li > a")` |
| Featured Items | Validate section presence | `page.locator("div.features_items")` |
| Recommended Items | Validate section presence | `page.locator("div.recommended_items")` |
| Footer | Confirm footer visibility and content | `page.locator("footer#footer")` |

---
