# Manual Test Documentation

## 1. Documentation Overview

Manual documentation is split into two artifact types:

## 2. Test Case Specifications

The files in this directory define reusable web UI test cases.  
The account API cases ([`001`](../crud/TC_API_CRUD_001_Create_Register_User_Account.md), [`002`](../crud/TC_API_CRUD_002_Duplicate_Prevented.md), and [`003`](../crud/TC_API_CRUD_003_Delete_User_Account.md)) use the same specification structure:

- preconditions;
- inputs and test data;
- actions;
- expected results;
- postconditions.

They should not contain execution-specific pass/fail results.

## 3. Execution Results

The [execution result records](../index.md#4-supporting-artifacts) cover web UI and account API executions:

- actual result;
- pass, fail, skip, or expected-failure status;
- environment and timestamp;
- evidence.

Cross-artifact relationships between requirements, test cases, automated tests, page objects, test data, execution records, and defects are maintained in the [Traceability Matrix](../automation/TRACEABILITY.md).

This separation follows the ISO-style distinction between a reusable test specification and the result of executing a test case.  
The result record may be replaced or extended for each test run without rewriting the test case definition.
