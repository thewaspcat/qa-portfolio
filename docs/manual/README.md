# Manual Test Documentation

Manual documentation is split into two artifact types:

## Test case specifications

The files in this directory define reusable web UI test cases. The account API cases in `docs/crud/` use the same specification structure:

- preconditions;
- inputs and test data;
- actions;
- expected results;
- postconditions.

They should not contain execution-specific pass/fail results.

## Execution results

The files in `docs/manual/results/` record web UI manual execution results:

- actual result;
- pass, fail, skip, or expected-failure status;
- environment and timestamp;
- evidence.

Cross-artifact relationships between requirements, test cases, automated tests, page objects, test data, execution records, and defects are maintained only in `docs/automation/TRACEABILITY.md`.

This separation follows the ISO-style distinction between a reusable test specification and the result of executing a test case. The result record may be replaced or extended for each test run without rewriting the test case definition.
