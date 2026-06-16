### CI Workflow Overview

The CI workflow demonstrates:

* Automated execution of Pytest + Playwright test suites;
* Dependency management using uv;
* Browser installation and setup in a clean runner environment;
* Automated validation of test scripts after each code change;
* Reproducible test execution independent of local machine configuration;
* Integration of test automation with version control practices.


```html
<h3>CI Workflow Overview</h3>
<pre><code>Git Push
    ↓
GitHub Actions Trigger
    ↓
Ubuntu Runner
    ↓
Python Setup
    ↓
uv Sync
    ↓
Playwright Browser Installation
    ↓
Pytest Execution
    ↓
Test Results</code></pre>

