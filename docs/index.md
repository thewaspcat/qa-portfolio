# QA Portfolio by Marta Czarnecka

<style>
.markdown-body h2 {
  font-size: 1.25em;
}
</style>


Welcome to my Quality Assurance Portfolio.

This portfolio presents selected manual web UI and REST API test cases, plus automated web UI testing work, for [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website.  It demonstrates how test design, execution, defect reporting, and automation contribute to a traceable quality assurance process.

The selected deliverables use a Jira/Xray-style structure and draw on ISO/IEC/IEEE 29119-3 and ISTQB® testing principles.

The portfolio showcases:

* **Manual testing:** Structured web UI and REST API test cases with defined scope, steps, and expected results.
* **API testing:** Postman-ready account API scenarios cover creation, duplicate-registration prevention, retrieval, and deletion.
* **Defect reporting:** A documented finding with reproduction steps, expected and actual results, severity, and impact.
* **Automation:** Python, pytest, and Playwright checks mapped to the manual test cases for traceability.
* **Git version control:** Portfolio artifacts maintained and published through a GitHub repository.
* **Continuous integration:** Automated test execution through GitHub Actions on pushes and pull requests.


## Software Under Test

Automation Exercise serves as the test environment for the featured work.  The selected scope covers core homepage content, valid user authentication, website navigation, and account API creation, duplicate registration, retrieval, and deletion.


## Featured Test Coverage

* **Homepage:** Evaluates the presentation and availability of key page components against defined expectations.
* **Authentication:** Validates access with approved credentials and continuity of the authenticated session.
* **Navigation:** Verifies the structure and behavior of the main menu across its configured destinations.
* **Account API:** Specifies a create → duplicate-registration check → delete sequence, with account retrieval used to verify the resulting state.

The [Traceability Matrix](automation/TRACEABILITY.md) records the available relationships between requirements, test cases, test data, automation, execution records, and defects.


## Web UI Automation Approach

The automated suite uses the Page Object Model to organize UI locators and interactions in dedicated page classes.  Tests focus on the scenarios and expected outcomes, with explicit Playwright assertions used for verification.

**Data-driven testing** supplies URLs and expected values from JSON files.  Pytest parameterization runs the internal navigation check for each configured link.  Reusable fixtures load test data, provide page objects, obtain login credentials from environment variables, and clean up the authenticated session.

GitHub Actions runs the web UI suite with Chromium.  The test setup captures screenshots, and the workflow uploads the test results as evidence.


## Supporting Artifacts

<details>
<summary>Manual Test Cases</summary>
<ul>
  <li><a href="manual/TC_UI_HOME_001.html">TC_UI_HOME_001 — Homepage UI layout and components</a></li>
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
<summary>Continuous Integration Workflow</summary>
<ul>
  <li><a href="https://github.com/thewaspcat/qa-portfolio/blob/main/.github/workflows/tests.yml">GitHub Actions test workflow</a></li>
</ul>
</details>

<details>
<summary>Account API Test Cases</summary>
<p>These specifications are designed for manual execution in Postman.  They are automation candidates and are not part of the current GitHub Actions suite.</p>
<ul>
  <li><a href="crud/TC_API_CRUD_001_Create_Register_User_Account.html">TC_API_CRUD_001 — Create/Register User Account</a></li>
  <li><a href="crud/TC_API_CRUD_002_Duplicate_Prevented.html">TC_API_CRUD_002 — Duplicate User Account Creation Prevented</a></li>
  <li><a href="crud/TC_API_CRUD_003_Delete_User_Account.html">TC_API_CRUD_003 — Delete User Account</a></li>
</ul>
</details>


## Contact Details

For inquiries, feel free to reach out via:

* **LinkedIn:** [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* **Email:** [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)
