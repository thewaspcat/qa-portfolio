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

## 2. Featured Test Coverage

* **Homepage:** Verifies page loading and the visibility of key UI components.
* **Authentication:** Verifies login with valid credentials and persistence of the authenticated session.
* **Navigation:** Verifies the structure and behavior of the main menu across its configured destinations.
* **Account API:** Specifies a create → duplicate-registration check → delete sequence, with account retrieval used to verify the resulting state.

The [Traceability Matrix](automation/TRACEABILITY.md) records the available relationships between requirements, test cases, test data, automation, page objects, execution records, and defects.


## 3. Web UI Automation Approach

The automated suite uses the Page Object Model to organize UI locators and interactions in dedicated page classes.  
Tests verify expected outcomes with Playwright assertions.

JSON files supply URLs and expected values.  
Pytest parameterization runs the internal navigation check for each configured link.  
Reusable fixtures load test data, provide page objects, obtain login credentials from environment variables, and clean up the authenticated session.

A pytest hook captures a screenshot after each test body.  
GitHub Actions uploads the screenshots from the test-results directory as an artifact.


## 4. Supporting Artifacts

<details>
<summary>Manual Test Cases</summary>
<ul>
  <li><a href="manual/TC_UI_HOME_001.html">TC_UI_HOME_001 — Homepage shell and key components</a></li>
  <li><a href="manual/TC_UI_LOGIN_001.html">TC_UI_LOGIN_001 — Valid user login</a></li>
  <li><a href="manual/TC_UI_NAV_001.html">TC_UI_NAV_001 — Main navigation</a></li>
</ul>
</details>

<details>
<summary>Test-Case Execution Records</summary>
<ul>
  <li><a href="manual/results/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Manual execution result</a></li>
  <li><a href="manual/results/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Manual execution result</a></li>
  <li><a href="manual/results/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Manual execution result</a></li>
  <li><a href="manual/results/TC_API_CRUD_001_result.html">TC_API_CRUD_001 — Account API execution result (passed)</a></li>
  <li><a href="manual/results/TC_API_CRUD_002_result.html">TC_API_CRUD_002 — Account API execution result (passed)</a></li>
  <li><a href="manual/results/TC_API_CRUD_003_result.html">TC_API_CRUD_003 — Account API execution result (passed)</a></li>
</ul>
</details>

<details>
<summary>Automated Execution Records</summary>
<ul>
  <li><a href="automation/results/TC_UI_HOME_001_result.html">TC_UI_HOME_001 — Automated execution result</a></li>
  <li><a href="automation/results/TC_UI_LOGIN_001_result.html">TC_UI_LOGIN_001 — Automated execution result</a></li>
  <li><a href="automation/results/TC_UI_NAV_001_result.html">TC_UI_NAV_001 — Automated execution result</a></li>
</ul>
</details>

<details>
<summary>Defect Reporting</summary>
<ul>
  <li><a href="manual/bugs/BR_TC_UI_HOME_001.html">BR_TC_UI_HOME_001 — Featured Items heading</a></li>
  <li><a href="manual/bugs/BR_TC_API_CRUD_001_Content_Type.html">BR_TC_API_CRUD_001 — JSON response media type</a></li>
</ul>
</details>

<details>
<summary>Automated Test Scripts</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/tests/test_tc_ui_home_001.py">TC_UI_HOME_001 — Homepage checks</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/tests/test_tc_ui_login_001.py">TC_UI_LOGIN_001 — Login checks</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/tests/test_tc_ui_nav_001.py">TC_UI_NAV_001 — Navigation checks</a></li>
</ul>
</details>

<details>
<summary>Web UI Test Data and Page Objects</summary>
<ul>
  <li><a href="automation/data/test_homepage_data.json">Homepage test data</a></li>
  <li><a href="automation/data/test_login_data.json">Login test data</a></li>
  <li><a href="automation/data/test_navigation_data.json">Navigation test data</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/pages/home_page.py">Home page object</a></li>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/docs/automation/pages/login_page.py">Login page object</a></li>
</ul>
</details>

<details>
<summary>Account API Execution Evidence</summary>
<ul>
  <li><a href="manual/evidence/TC_API_CRUD_2026-10-14_postman.html">Postman execution screenshots</a></li>
  <li><a href="manual/evidence/TC_API_CRUD_2026-10-14_responses.html">API response transcript</a></li>
</ul>
</details>

<details>
<summary>Continuous Integration Workflow</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/.github/workflows/tests.yml">GitHub Actions test workflow</a></li>
</ul>
</details>

<details>
<summary>Account API Test Cases</summary>
<p>These specifications are designed for manual execution in Postman while being automation candidates.</p>
<ul>
  <li><a href="crud/TC_API_CRUD_001_Create_Register_User_Account.html">TC_API_CRUD_001 — Create/Register User Account</a></li>
  <li><a href="crud/TC_API_CRUD_002_Duplicate_Prevented.html">TC_API_CRUD_002 — Duplicate User Account Creation Prevented</a></li>
  <li><a href="crud/TC_API_CRUD_003_Delete_User_Account.html">TC_API_CRUD_003 — Delete User Account</a></li>
</ul>
</details>


## 5. Contact Details

For inquiries, feel free to reach out via:

* **LinkedIn:** [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* **Email:** [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)
