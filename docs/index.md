# QA Portfolio | Marta Czarnecka

<style>
.markdown-body h2 {
  font-size: 1.25em;
}

details > summary {
  color: #0969da;
}
</style>

**Scope**: Manual Testing · REST API Testing · Test Automation · Continuous Integration  
**Technology stack**: Python · JavaScript · Markdown · pytest · Playwright · Postman · PowerShell · uv · Git · GitHub · GitHub Actions

<details><summary>Contact Details</summary>

* LinkedIn: [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* Email: [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)</details>

<details><summary>Credentials</summary>
ISTQB certification</details>

## Project Overview

This project presents a structured QA process applied to [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website.   
The portfolio showcases a traceable workflow from requirements analysis and test design through manual execution, defect reporting, test automation and continuous integration.  
The [GitHub repository](https://github.com/thewaspcat/qa-portfolio) comprises three web UI areas (homepage functionality, user authentication, main navigation) and three account management API scenarios, alongside their associated requirements, test data, execution records, automation artifacts and CI architecture. 

## QA stages and deliverables

- **Requirements analysis:** Defined testable requirements, acceptance criteria and coverage for the selected application functionality.  
  <details><summary>Deliverables</summary>

  * [Test Basis](requirements.md)
  * [QA Coverage](qa_coverage.md)
</details> 

- **Test design:** Created structured test specifications and test cases, including preconditions, test data, execution steps, expected results and automation readiness.
  <details><summary>Deliverables</summary>

  * [Test Case Specifications](test-cases/README.md)  
  * <details><summary>Web UI Test Cases</summary>
    <ul>
    <li><a href="test-cases/ui/TC_UI_HOME_001.html">TC_UI_HOME_001 — Homepage shell and key components</a></li>
    <li><a href="test-cases/ui/TC_UI_LOGIN_001.html">TC_UI_LOGIN_001 — Valid user login</a></li>
    <li><a href="test-cases/ui/TC_UI_NAV_001.html">TC_UI_NAV_001 — Main navigation</a></li>
    </ul>
    </details>  
  * <details><summary>Account API Test Cases</summary>
    <ul>
    <li><a href="test-cases/api/TC_API_CRUD_001_Create_Register_User_Account.html">TC_API_CRUD_001 — Create/Register User Account</a></li>
    <li><a href="test-cases/api/TC_API_CRUD_002_Duplicate_Prevented.html">TC_API_CRUD_002 — Duplicate User Account Creation Prevented</a></li>
    <li><a href="test-cases/api/TC_API_CRUD_003_Delete_User_Account.html">TC_API_CRUD_003 — Delete User Account</a></li>
    </ul>
  </details>
</details>

- **Traceability:** Created a traceability matrix which provides a central view of relationships between requirements, manual test cases, automated tests, page objects, test data, execution records, and defects.  

  <details><summary>Deliverables</summary>  
  * [Traceability Matrix](TRACEABILITY.md)  
</details>

- **Manual test execution** Executed web UI test cases, and REST API tests using Postman.   
Execution records document actual results, statuses, execution context, and supporting evidence.
  <details><summary>Deliverables</summary> 

  * <details><summary>Manual Execution Records</summary>
    <ul>
    <li><a href="results/ui/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Homepage execution result</a></li>
    <li><a href="results/ui/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Login execution result</a></li>
    <li><a href="results/ui/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Navigation execution result</a></li>
    </ul>
  </details>  

  * <details><summary>REST API Execution Records</summary>
    <ul>
    <li><a href="results/api/TC_API_CRUD_001_result.html">TC_API_CRUD_001 — Account creation execution result</a></li>
    <li><a href="results/api/TC_API_CRUD_002_result.html">TC_API_CRUD_002 — Duplicate-registration prevention execution result</a></li>
    <li><a href="results/api/TC_API_CRUD_003_result.html">TC_API_CRUD_003 — Account deletion execution result</a></li>
    <li><a href="results/api/TC_API_CRUD_001_result.html#2-postman-execution">Account creation Postman evidence</a></li>
    <li><a href="results/api/TC_API_CRUD_002_result.html#2-postman-execution">Duplicate-registration Postman evidence</a></li>
    <li><a href="results/api/TC_API_CRUD_003_result.html#2-postman-execution">Account deletion Postman evidence</a></li>
    </ul>
</details>
</details>

### 5. Defect Management

Each defect report documents the finding and links to its originating test case, execution record, and evidence.

<details>
<summary>Defect Reports</summary>
<ul>
  <li><a href="defects/BR_TC_UI_HOME_001.html">BR_TC_UI_HOME_001 — Featured Items heading</a></li>
  <li><a href="defects/BR_TC_API_CRUD_001_Content_Type.html">BR_TC_API_CRUD_001 — JSON response media type</a></li>
</ul>
</details>


### 6. Test Automation

The automated suite uses Python, pytest, and Playwright. Page objects organise UI locators and interactions, while tests verify expected outcomes with Playwright assertions.

JSON files provide URLs and expected values. Pytest parameterization runs the internal navigation check for each configured link. Reusable fixtures load test data, provide page objects, obtain login credentials from environment variables, and clean up authenticated sessions.

A pytest hook captures a screenshot after each test body, also when a test has failed.

<details>
<summary>Configuration and Fixtures</summary>
<ul>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/conftest.py">Fixtures and screenshot evidence hook</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/pyproject.toml">Project dependencies and pytest configuration</a></li>
</ul>
</details>

<details>
<summary>Web UI Test Data and Page Objects</summary>
<ul>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/data/test_homepage_data.json">Homepage test data</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/data/test_login_data.json">Login test data</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/data/test_navigation_data.json">Navigation test data</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/pages/home_page.py">Home page object</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/pages/login_page.py">Login page object</a></li>
</ul>
</details>

<details>
<summary>Automated Test Scripts</summary>
<ul>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/tests/test_tc_ui_home_001.py">TC_UI_HOME_001 — Homepage checks</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/tests/test_tc_ui_login_001.py">TC_UI_LOGIN_001 — Login checks</a></li>
  <li><a href="https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/automation/tests/test_tc_ui_nav_001.py">TC_UI_NAV_001 — Navigation checks</a></li>
</ul>
</details>

<details>
<summary>Automated Execution Records</summary>
<ul>
  <li><a href="https://thewaspcat.github.io/qa-portfolio/results/automated/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Homepage execution result</a></li>
  <li><a href="https://thewaspcat.github.io/qa-portfolio/results/automated/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Login execution result</a></li>
  <li><a href="https://thewaspcat.github.io/qa-portfolio/results/automated/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Navigation execution result</a></li>
</ul>
</details>

### 7. Continuous Integration

The [GitHub Actions workflow](https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/.github/workflows/tests.yml) runs on pushes and pull requests. It sets up Python 3.13, installs dependencies with uv, installs Chromium, and runs the automated tests with pytest.

GitHub Actions runs the suite with Chromium and uploads screenshot evidence captured after test execution.
The login test is skipped when the required credential environment variables are unavailable. Tests skipped during setup do not produce screenshots through this hook.                      
           


## Contact Details

* **LinkedIn:** [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* **Email:** [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)
