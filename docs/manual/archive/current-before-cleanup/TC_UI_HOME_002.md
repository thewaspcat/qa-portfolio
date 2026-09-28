# Featured Items Heading Display

## Document Control

| Field | Value |
|---|---|
| Test Case ID | `TC_UI_HOME_002` |
| Document version | 1.1 |
| Last updated | 2026-09-23 |
| Document owner | TBD |
| Requirement owner | TBD |
| Defect reference | [`BR_TC_UI_HOME_001`](https://thewaspcat.github.io/qa-portfolio/bugs/BR_TC_UI_HOME_001.html) |

## Test Case Information

- **Title:** Featured Items Heading Display
- **Objective:** Verify that the homepage displays the exact heading `Featured Items`.
- **Requirement Reference:** REQ-WEB-HOME-004
- **Test Type:** Functional
- **Execution Type:** Manual / Automated
- **Test Level:** System (UI)
- **Priority:** High
- **Severity:** Medium
- **Module:** Homepage

## 2. Environment & Dependencies

- Browser: Google Chrome, latest stable
- Operating system: Windows / macOS / Linux
- Test URL: `https://www.automationexercise.com/`

**Dependencies:**

- Stable internet connection
- Application environment online and accessible
- Browser automation runtime and Playwright browser available for automated execution

## 3. Preconditions

- Browser is installed and functional.
- Cache and cookies are cleared prior to manual execution, or a fresh browser context is used for automated execution.
- Application server is online and reachable.
- User is logged out with no active session.

## 4. Test Data

| Field | Value |
|---|---|
| Homepage URL | `https://www.automationexercise.com/` |
| Expected heading | `Featured Items` |

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Open the homepage. | The homepage loads successfully. |
| 2 | Locate the Featured Items section. | The section container is visible. |
| 3 | Verify the section heading text. | The exact heading is `Featured Items`. |

## 6. Automation Mapping

- Implementation: `docs/automation/tests/test_home.py`
- Test: `test_tc_ui_home_002_featured_items_heading`
- POM: `docs/automation/pages/home_page.py`
- Data: `docs/automation/data/test_homepage_data.json`

Execution outcomes are recorded separately in `docs/manual/results/TC_UI_HOME_002_result.md`.
