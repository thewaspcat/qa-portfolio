# Homepage UI: Structure and Elements

## 1. Test Case Information
- **Test Case ID:** TC_UI_HOME_001  
- **Title:** Homepage UI: Structure and Elements  
- **Test Objective:** Validate that the homepage UI loads correctly with logo, navigation bar, main sections, and footer as per page source.  
- **Requirement Reference:** REQ-WEB-HOME-004  
- **Test Type:** Manual / Functional
- **Test Level:** System (UI)  
- **Priority:** High  
- **Severity:** Medium  
- **Module:** Homepage  
- **Created By:** Marta Czarnecka  
- **Created on::** 08.09.2025  
- **Last Updated:** 14.09.2025  

---

## 2. Environment & Dependencies
**Environment:**  
- **Browser:** Chrome (latest stable version)  
- **OS:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com  

**Dependencies:**  
- Stable internet connection.  
- Application environment accessible and online.  
- User is logged out (no active session).  

---

## 3. Preconditions
- Chrome browser (latest stable version) is installed and functional.  
- Browser cache and cookies are cleared prior to execution.  
- Application server is up and responding to requests (homepage reachable).  
- User is logged out (no active session).  

---

## 4. Test Data

| Data Field       | Value |
|------------------|------------------------------------------------------------------------|
| Test URL         | https://www.automationexercise.com |
| Page Title       | Automation Exercise |
| Navigation Links | Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact us |

---

## 5. Test Steps

| Step # | Action | Locator / Selector | Expected Result |
|--------|--------|--------------------|-----------------|
| 1 | Open homepage | N/A | Page loads successfully; title is exactly "Automation Exercise". |
| 2 | Verify logo presence | `div.logo.pull-left a img` | Logo is visible in header with non-empty `src` and `alt` attributes. |
| 3 | Verify navigation bar visibility | `ul.nav.navbar-nav` | Navigation bar is rendered correctly below the logo. |
| 4 | Verify navigation link texts | `ul.nav.navbar-nav > li > a` | Link texts match exactly: Home, Products, Cart, Signup / Login, Test Cases, API Testing, Video Tutorials, Contact us. |
| 5 | Verify navigation link hrefs | `ul.nav.navbar-nav > li > a` | Each link has a valid, non-empty `href` attribute. |
| 6 | Verify “Features Items” section | `div.features_items` | Section is visible with header "Features Items". |
| 7 | Verify “Recommended Items” section | `div.recommended_items` | Section is visible with header "Recommended Items" (may require scrolling). |
| 8 | Verify footer presence | `footer#footer` | Footer is visible at the bottom with branding and social icons. |
| 9 | Open page source and confirm required HTML elements exist | Browser → Right Click → View Page Source | Elements listed in Appendix are present in the source. |

---

## 6. Expected Results
- Homepage title is exactly "Automation Exercise".  
- Logo is displayed correctly with valid `src` and `alt` attributes.  
- Navigation bar displays all 8 links with correct texts and working `href` attributes.  
- Sections "Features Items" and "Recommended Items" are present in the correct order.  
- Footer is displayed at the bottom of the page with relevant site information and social icons.  
- Page source contains required elements as listed in Appendix.  

---

## 7. Actual Results
(To be completed after execution.)  

---

## 8. Status
- **Pass:** All homepage UI components load and render correctly as specified.  
- **Fail:** Any homepage UI element is missing, mislabeled, or misaligned.  

---

## 9. Postconditions
- No changes to browser session or application state (user remains logged out, homepage unchanged).  
- Homepage remains accessible and unchanged after verification.  

---

## 10. Notes
- Validation of link texts and section headers is case-sensitive as per UI design specifications.  
- The "Recommended Items" section may require scrolling; adjust viewport if necessary.  
- Functional checks (e.g., clicking links, redirects, logo navigation) are covered in separate test cases.  
- Performance metrics and console log validation are out of scope and will be tested separately.  
- If navigation bar structure or labels change, this test case must be updated accordingly.  

---

## Appendix – Page Source Verification

**Logo element:**  
```html
<div class="logo pull-left">
  <a href="/"><img src="..." alt="Automation Exercise"></a>
</div>
```

**Navigation bar:**  
```html
<ul class="nav navbar-nav">
  <li><a href="/">Home</a></li>
  <li><a href="/products">Products</a></li>
  <li><a href="/view_cart">Cart</a></li>
  <li><a href="/login">Signup / Login</a></li>
  <li><a href="/test_cases">Test Cases</a></li>
  <li><a href="/api_testing">API Testing</a></li>
  <li><a href="/video_tutorials">Video Tutorials</a></li>
  <li><a href="/contact_us">Contact us</a></li>
</ul>
```

**Features Items section:**  
```html
<div class="features_items">...</div>
```

**Recommended Items section:**  
```html
<div class="recommended_items">...</div>
```

**Footer:**  
```html
<footer id="footer">...</footer>
```

---
