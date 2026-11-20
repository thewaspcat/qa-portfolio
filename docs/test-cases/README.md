# Test Case Specifications

## 1. Overview

This directory contains reusable test case specifications for the Automation Exercise website and account API.

The specifications define what to verify and the expected behavior. Execution outcomes are recorded separately.

## 2. Directory Contents

- `ui/` contains homepage, valid-login, and navigation specifications for manual execution and corresponding web UI automation.
- `api/` contains account creation, duplicate-registration prevention, and account deletion specifications designed for manual API testing. Execution evidence includes Postman and PowerShell runs.

## 3. Specification Contents

Each specification describes:

- the test objective and priority;
- the environment and preconditions;
- inputs and test data;
- actions and expected results;
- postconditions;
- automation readiness.

The API specifications also describe the account data passed between dependent cases.

## 4. Related Documentation

[Execution result records](../index.md#4-text-execution) contain actual results, statuses, execution context, and evidence links.

The [Traceability Matrix](../TRACEABILITY.md) maintains the relationships between requirements and portfolio artifacts.
