# QA Portfolio by Marta Czarnecka <br>

---

Welcome to my Quality Assurance Portfolio! 

The portfolio presents a collection of manual and automated testing artifacts across frontend and backend scenarios, compliant with international QA standards (ISO/IEC/IEEE 29119-3 and ISTQB®). 
The selected deliverables are organized in a Jira/Xray-style format and can be directly linked or imported to industry-standard test management tools.

The purpose of the portfolio is to showcase skills in the following areas:

🔹 Manual Testing: Frontend UI validation and backend API testing using Postman (CRUD operations: GET, POST, PUT, DELETE)

🔹 Defect Reporting: Bug documentation with reproduction steps, expected vs. actual results, severity, and impact

🔹 Automation (Python + Pytest + Playwright): Automated test scripts mapped one-to-one with manual test cases for traceability

🔹 Git Version Control: Use of command-line interfaces (PowerShell and Bash) to publish and maintain the portfolio repository on GitHub.

---

### Software Under Test

The software under test is [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website used here as a stable environment for demonstrating QA workflows.

---

### Section 1: Featured Test Summary Report

[Homepage Entry Flow Coverage](case_studies/case_study_1.md) <- click to view

This test summary report presents a focused functional QA evaluation of the homepage entry flow for the Automation Exercise demo site.
It covers homepage UI layout and component display, navigation menu functionality, and login page behavior using valid credentials, with execution results and defect tracking consolidated into a single traceable document.

It demonstrates how defined coverage areas are validated through structured test execution while maintaining traceability between scope, test cases, and outcomes.

---

### Section 2: Supporting Artifacts

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

### Defect reporting

- [BUG-001: Homepage - Incorrect Headline Text in Featured Items Section](bugs/BR_TC_UI_HOME_001.md) <- click to view
  
---

### Automated Test Scripts (Python + Pytest + Playwright):

> Click the links to view the scripts on GitHub with syntax highlighting.

- [Homepage UI Layout and Components Display](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_home_001.md)

- [Login Page Functionality – Valid Credentials](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_login_001.md)

- [Homepage Navigation Menu Functionality part 1](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_nav_001.md)

- [Homepage Navigation Menu Functionality part 2 (Video Tutorials)](https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/test_tc_ui_nav_001_video_tutorials.md)  

---

### Next Steps

Navigate the QA artifacts in the following order:

Test Summary Report → Manual Test Cases → Defect Reports → Automation Scripts

This sequence reflects the structure of the documented testing work:

🔹the Test Summary Report defines scope and presents execution results

🔹the Manual Test Cases detail the individual validations performed

🔹the Defect Report captures the identified issue

🔹the Automation Scripts implement repeatable checks for selected scenarios

---

### 📩 Contact details

For inquiries, feel free to reach out via:  

- **LinkedIn**: www.linkedin.com/in/marta-czarnecka-
- **Email**: martaczarneckaqa@gmail.com
