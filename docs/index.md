# QA Portfolio | Marta Czarnecka

<style>
.markdown-body h2 {
  font-size: 1.25em;
}

details > summary {
  color: #0969da;
}
</style>

**MANUAL QA · REST API TESTING · TEST AUTOMATION · CONTINUOUS INTEGRATION**  
**Python · pytest · Playwright · Postman · PowerShell · uv · Git · GitHub · GitHub Actions**


## Portfolio Overview

This portfolio presents a structured QA process for [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website. 

The QA process maintains traceability throughout all stages and includes following sections:

1. Test Basis and Traceability Matrix
2. Test Coverage
3. Test Case Specifications and Test Cases
4. Test Execution and Evidence
5. Defect Management
6. Test Automation
7. Continuous Integration


## QA Process

### 1. Test Basis and Traceability Matrix

<details markdown="1">
<summary markdown="span">Test basis</summary>

The [test basis](requirements.md) defines the rewuirements, expected behavior and acceptance criteria for the selected testing scope.
</details>

<details markdown="1">
<summary markdown="span">Traceability Matrix</summary>

The [Traceability Matrix](TRACEABILITY.md) provides a central view of test coverage.
For each requirement ID, it links to the corresponding test specification, execution records, documented defects, and available automation, including page objects and test data.
Use the matrix to follow a test from its specification through execution results and supporting evidence.
</details>


### 2. Test Coverage

| Area | Test coverage | Execution |
|---|---|---|
| Homepage | Page loading, logo, key components, footer | Manual + Playwright |
| Authentication | Valid login, authenticated state, session persistence | Manual + Playwright |
| Navigation | Eight links, order, destinations, same-tab navigation | Manual + Playwright |
| Account API | Account creation and persisted data | Postman |
| Duplicate registration | Duplicate prevention and data integrity | Postman |
| Account deletion | Deletion and post-deletion retrieval | Postman |


### 3. Test Case Specifications and Test Cases

The [Test Case Specifications](test-cases/README.md) overview explains how the UI and API cases are organised.

Each UI and API test case defines the test objective, preconditions, test data, and expected results. It also documents automation readiness.

<details>
<summary>Web UI Test Cases</summary>
<ul>
  <li><a href="test-cases/ui/TC_UI_HOME_001.html">TC_UI_HOME_001 — Homepage shell and key components</a></li>
  <li><a href="test-cases/ui/TC_UI_LOGIN_001.html">TC_UI_LOGIN_001 — Valid user login</a></li>
  <li><a href="test-cases/ui/TC_UI_NAV_001.html">TC_UI_NAV_001 — Main navigation</a></li>
</ul>
</details>

<details>
<summary>Account API Test Cases</summary>
<p>These specifications describe manual execution in Postman and include automation-readiness information.</p>
<ul>
  <li><a href="test-cases/api/TC_API_CRUD_001_Create_Register_User_Account.html">TC_API_CRUD_001 — Create/Register User Account</a></li>
  <li><a href="test-cases/api/TC_API_CRUD_002_Duplicate_Prevented.html">TC_API_CRUD_002 — Duplicate User Account Creation Prevented</a></li>
  <li><a href="test-cases/api/TC_API_CRUD_003_Delete_User_Account.html">TC_API_CRUD_003 — Delete User Account</a></li>
</ul>
</details>


### 4. Text Execution 

Execution records document actual results, statuses, execution context, and supporting evidence.

<details>
<summary>Manual Execution Records</summary>
<ul>
  <li><a href="results/ui/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Homepage execution result</a></li>
  <li><a href="results/ui/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Login execution result</a></li>
  <li><a href="results/ui/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Navigation execution result</a></li>
</ul>

</details>

<details>
<summary>REST API Execution Records</summary>
<ul>
 <li><a href="results/api/TC_API_CRUD_001_result.html">TC_API_CRUD_001 — Account creation execution result</a></li>
  <li><a href="results/api/TC_API_CRUD_002_result.html">TC_API_CRUD_002 — Duplicate-registration prevention execution result</a></li>
  <li><a href="results/api/TC_API_CRUD_003_result.html">TC_API_CRUD_003 — Account deletion execution result</a></li>
  <li><a href="results/api/TC_API_CRUD_001_result.html#2-postman-execution">Account creation Postman evidence</a></li>
  <li><a href="results/api/TC_API_CRUD_002_result.html#2-postman-execution">Duplicate-registration Postman evidence</a></li>
</ul>
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
  <li><a href="../automation/results/TC_UI_HOME_001_result.md">TC_UI_HOME_001 — Homepage execution result</a></li>
  <li><a href="../automation/results/TC_UI_LOGIN_001_result.md">TC_UI_LOGIN_001 — Login execution result</a></li>
  <li><a href="../automation/results/TC_UI_NAV_001_result.md">TC_UI_NAV_001 — Navigation execution result</a></li>
</ul>
</details>

### 7. Continuous Integration

The [GitHub Actions workflow](https://raw.githubusercontent.com/thewaspcat/qa-portfolio/refs/heads/main/.github/workflows/tests.yml) runs on pushes and pull requests. It sets up Python 3.13, installs dependencies with uv, installs Chromium, and runs the automated tests with pytest.

GitHub Actions runs the suite with Chromium and uploads screenshot evidence captured after test execution.
The login test is skipped when the required credential environment variables are unavailable. Tests skipped during setup do not produce screenshots through this hook.                      
           


## Contact Details

* **LinkedIn:** [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* **Email:** [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)
