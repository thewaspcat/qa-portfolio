# Case Study: Homepage Functional Testing (Automation Exercise)

## Project Overview.

This case study documents functional QA of the Automation Exercise demo e-commerce site across three scenarios: homepage UI validation, navigation behavior, and login functionality.  
It links manual test cases, execution results, defect reporting, and Playwright automation into a single traceable workflow.

## Product Under Test

- **Application:** Automation Exercise (public demo e-commerce)
- **Areas:** Homepage UI, Navigation, Login
- **Requirement:** REQ-WEB-HOME-004 (Homepage renders correctly with primary navigation and key sections)
- **Execution:** Manual + Automated (Playwright)

---

## Objective
Validate that core user-facing functionality works correctly by verifying UI structure, navigation behavior, and login functionality.

---

## Test Coverage
The application is validated through three complementary test cases:

- **TC_UI_HOME_001 – UI Structure & Visibility**
  - Page load, title, logo, navigation, sections, footer

- **TC_NAV_HOME_002 – Navigation Behavior**
  - Navigation links route correctly and are functional

- **TC_AUTH_LOGIN_003 – Login Functionality**
  - User can access login page and perform authentication-related checks

Each test targets a distinct functional area while contributing to overall system validation.

---

## Scope

### In Scope
- Homepage rendering and structure
- Navigation presence and behavior
- Login page accessibility and functionality
- Core UI components and visibility

### Out of Scope
- Product detail flows
- Backend/API validation
- Performance and security testing

---

## Test Strategy

- **UI integrity risk** → TC_UI_HOME_001  
- **Navigation failure risk** → TC_NAV_HOME_002  
- **Authentication risk** → TC_AUTH_LOGIN_003  

Testing focuses on validating critical entry points and core user actions.

---

## Test Design
All test cases use DOM-based verification points designed for:
- Stability
- Repeatability
- Automation compatibility

Validation includes:
- Page title assertions
- Element visibility checks
- Navigation link validation
- Login form validation
- Section and component verification

---

## Manual Execution

**Environment:**
- Browser: Chrome 121  
- OS: Windows 11  
- Resolution: 1920x1080  
- Network: Standard broadband  

**Execution Date:** 2026-03-30

### Execution Summary

| Test Case | Area | Result |
|----------|------|--------|
| TC_UI_HOME_001 | UI Structure | PASS / 1 FAIL |
| TC_NAV_HOME_002 | Navigation | PASS |
| TC_AUTH_LOGIN_003 | Login | PASS |

---

## Defect Report

**ID:** BUG-001  
**Title:** Incorrect headline text in Featured Items section  

### Steps to Reproduce
1. Open homepage  
2. Locate Featured Items section  

### Expected Result
"Featured Items"

### Actual Result
"Features Items"

### Severity
Low

### Priority
Medium

### Impact
Does not block functionality but reduces UI quality and professionalism.

---

## Traceability

| Requirement | Test Case | Coverage Area | Result | Defect |
|------------|----------|--------------|--------|--------|
| REQ-WEB-HOME-004 | TC_UI_HOME_001 | UI Structure | PASS/FAIL | BUG-001 |
| REQ-WEB-HOME-004 | TC_NAV_HOME_002 | Navigation | PASS | — |
| REQ-WEB-HOME-004 | TC_AUTH_LOGIN_003 | Login | PASS | — |

---

## Automation Mapping
All test cases are implemented in Playwright and mirror manual execution:

- Page load assertions  
- Locator-based UI checks  
- Navigation validation  
- Login form validation  

Automation uses reusable selectors and structured test data to support maintainability.

---

## QA Outcome
- Core homepage functionality is stable  
- Navigation is functional and consistent  
- Login functionality is accessible and working  
- One minor UI defect identified  

---

## Key Takeaways
- Multiple test scenarios improve coverage across functional areas  
- Manual tests translate directly into automation  
- Functional + authentication coverage increases realism  
- Structured traceability strengthens QA credibility  

---

## Final Assessment
The application is functionally stable across homepage, navigation, and login scenarios. The test suite demonstrates structured QA coverage, traceability, and automation alignment, making it suitable for regression testing and portfolio presentation.
