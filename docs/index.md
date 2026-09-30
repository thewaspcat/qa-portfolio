# QA Portfolio by Marta Czarnecka

<style>
.markdown-body h2 {
  font-size: 1.25em;
}
</style>


Welcome to my Quality Assurance Portfolio.

This portfolio presents selected manual and automated web UI testing work for [Automation Exercise](https://www.automationexercise.com/), a public demo e-commerce website. It demonstrates how test design, execution, defect reporting, and automation contribute to a traceable quality assurance process.

The deliverables use a Jira/Xray-style structure and draw on ISO/IEC/IEEE 29119-3 and ISTQB® testing principles.

The portfolio showcases:

* **Manual testing:** Structured web UI test cases with defined scope, steps, and expected results.
* **Defect reporting:** A documented finding with reproduction steps, expected and actual results, severity, and impact.
* **Automation:** Python, pytest, and Playwright checks mapped to the manual test cases for traceability.
* **Git version control:** Portfolio artifacts maintained and published through a GitHub repository.
* **Continuous integration:** Automated test execution through GitHub Actions on pushes and pull requests.


## Software Under Test

Automation Exercise serves as the test environment for the featured work. 
The selected scope covers core homepage content, valid user authentication, and website navigation.


## Featured Test Coverage

* **Homepage:** Evaluates the presentation and availability of key page components against defined expectations.
* **Authentication:** Validates access with approved credentials and continuity of the authenticated session.
* **Navigation:** Verifies the structure and behavior of the main menu across its configured destinations.

The [Traceability Matrix](automation/TRACEABILITY.md) connects each requirement with its manual test case, automated checks, test data, execution records, and any related defect.


## Automation Approach

The automated suite uses the Page Object Model to organize UI locators and interactions in dedicated page classes. Tests focus on the scenarios and expected outcomes, with explicit Playwright assertions used for verification.

**Data-driven testing** supplies URLs and expected values from JSON files. Pytest parameterization runs the internal navigation check for each configured link. Reusable fixtures load test data, provide page objects, obtain login credentials from environment variables, and clean up the authenticated session.

GitHub Actions runs the suite with Chromium. The test setup captures screenshots, and the workflow uploads the test results as evidence.


## Supporting Artifacts

* [Manual Test Cases](https://github.com/thewaspcat/qa-portfolio/tree/main/docs/manual)
* [Test-Case Execution Records](https://github.com/thewaspcat/qa-portfolio/tree/main/docs/manual/results)
* [Automated Execution Records](https://github.com/thewaspcat/qa-portfolio/tree/main/docs/automation/results)
* [Defect Reporting](https://github.com/thewaspcat/qa-portfolio/tree/main/docs/manual/bugs)
* [Automated Test Scripts](https://github.com/thewaspcat/qa-portfolio/tree/main/docs/automation/tests)
* [Continuous Integration Workflow](https://github.com/thewaspcat/qa-portfolio/blob/main/.github/workflows/tests.yml)


## Contact Details

For inquiries, feel free to reach out via:

* **LinkedIn:** [Marta Czarnecka](https://www.linkedin.com/in/marta-czarnecka-)
* **Email:** [martaczarneckaqa@gmail.com](mailto:martaczarneckaqa@gmail.com)
