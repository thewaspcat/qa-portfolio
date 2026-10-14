# TC_API_CRUD_002 — Duplicate User Account Creation Prevented: Manual Execution Result

## 1. Execution summary

| Field | Value |
|---|---|
| Test case | [TC_API_CRUD_002](../../crud/TC_API_CRUD_002_Duplicate_Prevented.md) |
| Environment | Public Automation Exercise API |
| Result | **Passed** — duplicate registration was rejected, and the original account details remained unchanged. |

## 2. Postman execution

| Field | Value |
|---|---|
| Test account | `user_test_1791973321842@example.com` |
| Retrieved user ID | `3040585` |
| Execution time | Not captured in the Postman evidence |
| Evidence | [Postman execution screenshots](../evidence/TC_API_CRUD_2026-10-14_postman.md) |

| Step | Actual result | Outcome |
|---|---|---|
| Capture original details | Retrieved the registered account with HTTP `200` and `responseCode: 200`. The valid user details were captured as the baseline; all 5 Postman assertions passed. | **Passed** |
| Reject duplicate registration | Submitted a second registration using the same email and different account details. The API returned HTTP `200`, `responseCode: 400`, and `message: "Email already exists!"`; all 6 Postman assertions passed. | **Passed** |
| Verify original details | Retrieved the account again with HTTP `200` and `responseCode: 200`. The complete returned user object matched the baseline; all 6 Postman assertions passed. | **Passed** |

## 3. PowerShell execution

| Field | Value |
|---|---|
| Execution time | 2026-10-14 06:08:22–06:08:23 UTC |
| Test account | `user_test_1791958100619@example.com` |
| Retrieved user ID | `3038560` |
| Evidence | [API response transcript](../evidence/TC_API_CRUD_2026-10-14_responses.md), `002` baseline, duplicate, and after |

| Step | Actual result | Outcome |
|---|---|---|
| Capture original details | Baseline GET returned HTTP `200`, `responseCode: 200`, and the original user object. | **Passed** |
| Reject duplicate registration | Duplicate POST returned HTTP `200`, `responseCode: 400`, and `message: "Email already exists!"`. | **Passed** |
| Verify original details | Final GET returned HTTP `200` and `responseCode: 200`. The complete user object, including ID `3038560`, matched the baseline. | **Passed** |
