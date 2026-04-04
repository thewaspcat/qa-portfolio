# QA Portfolio by Marta Czarnecka <br>

---

Welcome to my Quality Assurance portfolio, which presents a collection of manual and automated testing artifacts across frontend and backend scenarios, compliant with international QA standards (ISO/IEC/IEEE 29119-3 and ISTQB®).

The selected deliverables include UI test cases, REST API checks, defect reporting, and automation scripts, to showcase a comprehensive approach to testing, with clear test structure, traceability, and reproducible execution.

The test artifacts are organized in a Jira/Xray-style format and can be directly linked or imported to Xray work items.

---

## Software Under Test

The software under test is [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website used here as a stable environment for demonstrating QA workflows.

---

## Section 1: Featured Case Study

[Homepage Functional Testing](case_studies/case_study_1.md) <- click to view

This case study presents a focused functional QA workflow for the Automation Exercise demo site.  
It addresses homepage UI validation, navigation behavior, and basic login page verification, integrating manual execution, defect reporting, and Playwright automation into a single traceable flow.

It demonstrates how a defined requirement can be translated into targeted test scenarios while maintaining traceability across testing stages.

---

## Section 2: Skills Demonstrated

🔹 Manual Testing: Frontend UI verification and backend testing using Postman (CRUD API: GET, POST, PUT, DELETE)

🔹 Automation (Python + Pytest + Playwright): Automated test scripts mapped 1:1 to manual test cases for traceability

🔹 Defect Reporting: Bug documentation with reproduction steps, expected vs. actual results, severity, and impact

---

## Section 3: Supporting Artifacts

### Manual Test Cases:

#### Frontend (Web UI):

- [Homepage UI Layout and Components Display](manual/TC_UI_HOME_001.md) <- click to view
 
- [Login Page Functionality – Valid Credentials](manual/TC_UI_LOGIN_001.md) <- click to view
  
- [Homepage Navigation Menu Functionality](manual/TC_UI_NAV_001.md) <- click to view


#### Backend (REST API):

These API test cases are designed for manual test execution in Postman against the public Automation Exercise API.

- [GET All Products List](crud/TC_API_CRUD_001.md) <- click to view
  
- [POST a new Product to All Products List](crud/TC_API_CRUD_002.md) <- click to view
 
- [PUT an update to All Brands List](crud/TC_API_CRUD_003.md) <- click to view
 
- [DELETE User Account](crud/TC_API_CRUD_004.md) <- click to view

---

### Automated Test Scripts (Python + Pytest + Playwright):

> Click the links to view the scripts on GitHub with syntax highlighting.

- [Homepage UI Layout and Components Display](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_home_001.md)

- [Login Page Functionality – Valid Credentials](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_login_001.md)

- [Homepage Navigation Menu Functionality part 1](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_nav_001.md)

- [Homepage Navigation Menu Functionality part 2 (Video Tutorials)](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_nav_001_video_tutorials.md)  

---

### Defect reporting

- [BUG-001: Homepage - Incorrect Headline Text in Featured Items Section](bugs/BR_TC_UI_HOME_001.md) <- click to view
  
---

## Next Steps

Explore the QA workflow in a clear sequence: start with the featured case study , then review the manual test cases, the defect report, and finally the automation scripts.

You can navigate the portfolio in this order:

Featured Case Study → Manual Test Cases → Defect Reports → Automation Scripts

This sequence shows the full story—from the workflow overview to the detailed test cases, the defect uncovered, and the automation that reinforces manual testing.

---

## 📩 Contact details

For inquiries, feel free to reach out via:  

- **LinkedIn**: www.linkedin.com/in/marta-czarnecka-
- **Email**: martaczarneckaqa@gmail.com
