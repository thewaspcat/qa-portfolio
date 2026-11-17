# QA Portfolio by Marta Czarnecka

<style>
.markdown-body h2 {
  font-size: 1.25em;
}

details > summary {
  color: #0969da;
}
</style>

## 1. Portfolio Overview

Welcome to my Quality Assurance Portfolio.


This portfolio documents a traceable quality assurance process for [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website.


The portfolio showcases:

* **Manual web UI testing:** Homepage, login, and navigation test cases with automation-readiness notes and a separate manual execution record for each.
* **API testing:** Account API test cases for manual execution in Postman, each with an automation-readiness section.
* **Defect reporting:** Documented findings with reproduction steps, expected and actual results, and impact.
* **Automation:** Web UI tests written in Python, run with pytest, and using Playwright for browser interaction, with links to the corresponding manual test cases.
* **Git version control:** Portfolio artifacts maintained and published through a GitHub repository.
* **Continuous Integration:** Automated test execution through GitHub Actions on pushes and pull requests.  GitHub Actions runs the suite with Chromium and uploads screenshot evidence captured after test execution.

The test cases draw on ISO/IEC/IEEE 29119-3 and ISTQB® testing principles, and their structured format can be adapted for test management tools such as Jira with Xray or TestRail.

### Featured Test Coverage

* **Homepage:** Verifies page loading and the visibility of key UI components.
* **Authentication:** Verifies login with valid credentials and persistence of the authenticated session.
* **Navigation:** Verifies the structure and behavior of the main menu across its configured destinations.
* **Account API:** Specifies a create → duplicate-registration check → delete sequence, with account retrieval used to verify the resulting state.

## 2. Requirements and Traceability

The [Requirements](requirements.md) define the expected behavior and acceptance criteria for the covered homepage, authentication, navigation, and account API functions.

The [Traceability Matrix](TRACEABILITY.md) provides a central view of test coverage. For each requirement ID, it links to the corresponding test specification, execution records, documented defects, and available automation, including page objects and test data.
Use the matrix to follow a test from its specification through execution results and supporting evidence.

## 3. Test Design and Test Specifications

Each UI and API test specification defines the test objective, preconditions, test data, and expected results. It also documents automation readiness. The [Test Case Specifications](test-cases/README.md) overview explains how the UI and API cases are organised.

<details>
<summary>Web UI Test Case Specifications</summary>
<ul>
  <li><a href="test-cases/ui/TC_UI_HOME_001.html">TC_UI_HOME_001 — Homepage shell and key components</a></li>
  <li><a href="test-cases/ui/TC_UI_LOGIN_001.html">TC_UI_LOGIN_001 — Valid user login</a></li>
  <li><a href="test-cases/ui/TC_UI_NAV_001.html">TC_UI_NAV_001 — Main navigation</a></li>
</ul>
</details>

<details>
<summary>Account API Test Case Specifications</summary>
<p>These specifications describe manual execution in Postman and include automation-readiness information.</p>
<ul>
  <li><a href="test-cases/api/TC_API_CRUD_001_Create_Register_User_Account.html">TC_API_CRUD_001 — Create/Register User Account</a></li>
  <li><a href="test-cases/api/TC_API_CRUD_002_Duplicate_Prevented.html">TC_API_CRUD_002 — Duplicate User Account Creation Prevented</a></li>
  <li><a href="test-cases/api/TC_API_CRUD_003_Delete_User_Account.html">TC_API_CRUD_003 — Delete User Account</a></li>
</ul>
</details>

## 4. Test Execution and Evidence

Execution records document actual results, statuses, execution context, and supporting evidence.

<details>
<summary>Manual Execution Records</summary>
<ul>
  <li><a href="results/manual/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Homepage execution result</a></li>
  <li><a href="results/manual/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Login execution result</a></li>
  <li><a href="results/manual/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Navigation execution result</a></li>
  <li><a href="results/manual/TC_API_CRUD_001_result.html">TC_API_CRUD_001 — Account creation execution result</a></li>
  <li><a href="results/manual/TC_API_CRUD_002_result.html">TC_API_CRUD_002 — Duplicate-registration prevention execution result</a></li>
  <li><a href="results/manual/TC_API_CRUD_003_result.html">TC_API_CRUD_003 — Account deletion execution result</a></li>
</ul>

</details>

<details>
<summary>Automated Execution Records</summary>
<ul>
  <li><a href="results/automated/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Homepage execution result</a></li>
  <li><a href="results/automated/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Login execution result</a></li>
  <li><a href="results/automated/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Navigation execution result</a></li>
</ul>
</details>

<details>
<summary>Account API Execution Evidence</summary>
<ul>
  <li><a href="evidence/api/TC_API_CRUD_2026-10-14_postman.html">Postman execution screenshots</a></li>
  <li><a href="evidence/api/TC_API_CRUD_2026-10-14_responses.html">PowerShell API response transcript</a></li>
</ul>
</details>

## 5. Defect Management

Each defect report documents the finding and links to its originating test case, execution record, and evidence.

<details>
<summary>Defect Reports</summary>
<ul>
  <li><a href="defects/BR_TC_UI_HOME_001.html">BR_TC_UI_HOME_001 — Featured Items heading</a></li>
  <li><a href="defects/BR_TC_API_CRUD_001_Content_Type.html">BR_TC_API_CRUD_001 — JSON response media type</a></li>
</ul>
</details>

## 6. Test Automation Implementation

The automated suite uses Python, pytest, and Playwright. Page objects organise UI locators and interactions, while tests verify expected outcomes with Playwright assertions.

JSON files provide URLs and expected values. Pytest parameterization runs the internal navigation check for each configured link. Reusable fixtures load test data, provide page objects, obtain login credentials from environment variables, and clean up authenticated sessions.

A pytest hook captures a screenshot after each test body.

<details>
<summary>Automated Test Scripts</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/tests/test_tc_ui_home_001.py">TC_UI_HOME_001 — Homepage checks</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/tests/test_tc_ui_login_001.py">TC_UI_LOGIN_001 — Login checks</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/tests/test_tc_ui_nav_001.py">TC_UI_NAV_001 — Navigation checks</a></li>
</ul>
</details>

<details>
<summary>Web UI Test Data and Page Objects</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/data/test_homepage_data.json">Homepage test data</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/data/test_login_data.json">Login test data</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/data/test_navigation_data.json">Navigation test data</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/pages/home_page.py">Home page object</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/pages/login_page.py">Login page object</a></li>
</ul>
</details>

<details>
<summary>Configuration and Fixtures</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/automation/conftest.py">Fixtures and screenshot evidence hook</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/pyproject.toml">Project dependencies and pytest configuration</a></li>
</ul>
</details>

## 7. Continuous Integration

The GitHub Actions workflow runs on pushes and pull requests. It sets up Python 3.13, installs dependencies with uv, installs Chromium, and runs the automated tests with pytest.

The login test is skipped when the required credential environment variables are unavailable. Screenshot evidence is captured after test bodies; tests skipped during setup do not produce screenshots through this hook.

The workflow attempts to upload the test-results directory as an artifact even when test execution fails.

<details>
<summary>Continuous Integration Workflow</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/.github/workflows/tests.yml">GitHub Actions test workflow</a></li>
</ul>
</details>

## 8. Contact Details

For inquiries, feel free to reach out via:

* **LinkedIn:** [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* **Email:** [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)
