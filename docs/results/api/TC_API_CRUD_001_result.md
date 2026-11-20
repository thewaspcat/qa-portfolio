# TC_API_CRUD_001 — Create/Register User Account: Manual Execution Result

## 1. Execution summary

| Field | Value |
|---|---|
| Test case | [TC_API_CRUD_001](../../test-cases/api/TC_API_CRUD_001_Create_Register_User_Account.md) |
| Environment | Public Automation Exercise API |

| Verification | Result |
|---|---|
| Account creation | **Passed** |
| Persisted account data | **Passed** |
| Content-Type validation | **Discrepancy identified** |
| Overall functional test case | **Passed** |

All 15 retrievable account fields matched the submitted values. Six of seven Postman assertions for account creation passed. The `Content-Type` assertion failed because the JSON response was labelled `text/html; charset=utf-8`. See [`BR_TC_API_CRUD_001`](../../defects/BR_TC_API_CRUD_001_Content_Type.md).

## 2. Postman execution

| Field | Value |
|---|---|
| Test account | `user_test_1791973321842@example.com` |
| Retrieved user ID | `3040585` |
| Execution time | Not captured in the Postman evidence |
| Evidence | [Create response](../../evidence/api/TC_API_CRUD_001_create_response_postman.png) · [Create test results](../../evidence/api/TC_API_CRUD_001_create_results_postman.png) · [Account-detail response](../../evidence/api/TC_API_CRUD_001_detail_response_postman.png) · [Account-detail test results](../../evidence/api/TC_API_CRUD_001_detail_results_postman.png) |

| Step | Actual result | Functional outcome |
|---|---|---|
| Create account | Submitted the account data as `x-www-form-urlencoded`. The API returned HTTP `200`, `responseCode: 201`, and `message: "User created!"`. Six of seven Postman assertions passed; the `Content-Type` assertion failed on `text/html; charset=utf-8`. | **Passed** |
| Verify persisted details | Retrieved the new account by email. The API returned HTTP `200`, `responseCode: 200`, and user ID `3040585`. All 20 Postman assertions passed, including the 15 persisted-field checks. | **Passed** |