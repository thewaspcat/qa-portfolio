# Case Study: Homepage UI Testing (Automation Exercise)

## Project overview
This case study documents end-to-end QA for the homepage of the Automation Exercise demo e-commerce site. It consolidates manual test design, execution evidence, defect reporting, and automation mapping into a single, traceable workflow.

## Product under test
- **Application:** Automation Exercise (public demo e-commerce)
- **Area:** Homepage UI
- **Requirement:** REQ-WEB-HOME-004 (Homepage renders correctly with primary navigation and key sections)
- **Test case:** [TC_UI_HOME_001](https://thewaspcat.github.io/qa-portfolio/manual/TC_UI_HOME_001.html)
- **Test type:** Functional (UI)
- **Execution:** Manual + Automated (Playwright)

## Objective
Verify that the homepage loads successfully and displays all critical UI components with correct labels, structure, and visibility.

## Scope
### In scope
- Page load and title
- Logo presence and attributes
- Main navigation visibility and links
- Featured Items section
- Recommended Items section
- Footer visibility

### Out of scope
- Navigation click-through behavior
- Authentication flows
- Product detail flows
- API behavior
- Performance and security testing

## Risk-based focus
Highest-risk checks prioritized:
- Page load failure (blocks all usage)
- Missing navigation (blocks user movement)
- Missing core sections (breaks usability)

Lower-risk but relevant:
- Text accuracy and UI labeling

## Test design
The test case uses DOM-based verification points that are stable and automation-friendly:
- Page title assertion
- Logo visibility and attributes
- Navigation container and link validation
- Section headers (Featured, Recommended)
- Footer presence

Each step is mapped to a clear expected outcome, enabling both manual verification and automated assertions.

## Traceability
| Requirement | Test Case | Result | Defect |
|------------|----------|--------|--------|
| Homepage loads correctly | [TC_UI_HOME_001](https://thewaspcat.github.io/qa-portfolio/manual/TC_UI_HOME_001.html) | PASS | — |
| Featured section label correct | [TC_UI_HOME_001](https://thewaspcat.github.io/qa-portfolio/manual/TC_UI_HOME_001.html) | FAIL | [BUG-001](https://thewaspcat.github.io/qa-portfolio/defects/) |

## Manual execution
**Environment:**
- Browser: Chrome 121
- OS: Windows 11
- Resolution: 1920x1080
- Network: Standard broadband

**Execution date:** 2026-03-30

### Steps and results
1. Open homepage URL  
   → Page loads successfully

2. Verify page title  
   → "Automation Exercise" displayed (PASS)

3. Verify logo  
   → Logo visible, correct alt text (PASS)

4. Verify navigation bar  
   → Navigation visible with expected links (PASS)

5. Validate navigation links (text + href)  
   → All links present and correctly labeled (PASS)

6. Verify Featured Items section  
   → Section visible but label incorrect (FAIL)

7. Verify Recommended Items section  
   → Section visible and correctly labeled (PASS)

8. Verify footer  
   → Footer visible (PASS)

## Execution summary
- Total checks: 8
- Passed: 7
- Failed: 1

## Defect report
**ID:** [BUG-001](https://thewaspcat.github.io/qa-portfolio/defects/)  
**Title:** Incorrect headline text in Featured Items section

### Steps to reproduce
1. Open homepage
2. Locate Featured Items section

### Expected result
Section title displays: **Featured Items**

### Actual result
Section title displays: **Features Items**

### Severity
Low

### Priority
Medium

### Impact
Does not block functionality but reduces UI quality and professionalism.

## Automation mapping
The test case is implemented in Playwright and mirrors the manual flow:

- Page load assertion  
- Locator-based UI checks  
- Text validation  

**Implementation:** https://github.com/thewaspcat/qa-portfolio (Playwright tests directory)

## QA outcome
This test confirms that:
- Core homepage functionality is stable
- UI structure is intact
- Minor content defects are present

## Key takeaways
- Manual test design successfully identified a real UI issue
- The same test can be reused for automation with minimal changes
- Even simple UI validation provides value when executed systematically

## Final assessment
The homepage is functionally stable and usable. One minor UI defect was identified that should be corrected to improve presentation quality. The test case is suitable for inclusion in a regression suite and demonstrates a complete QA workflow from requirement to defect.
