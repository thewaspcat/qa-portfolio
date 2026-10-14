# TC_API_CRUD_001 — Create/Register User Account: Manual Execution Result

## 1. Execution summary

| Field | Value |
|---|---|
| Test case | [TC_API_CRUD_001](../../crud/TC_API_CRUD_001_Create_Register_User_Account.md) |
| Environment | Public Automation Exercise API |
| Functional result | **Passed** — the account was created and all 15 retrievable details matched the submitted data. |
| Contract observation | The JSON creation response was labelled `text/html; charset=utf-8`; the separate Postman media-type assertion failed. See [`BR_TC_API_CRUD_001`](../bugs/BR_TC_API_CRUD_001_Content_Type.md). |

## 2. Postman execution

| Field | Value |
|---|---|
| Test account | `user_test_1791973321842@example.com` |
| Retrieved user ID | `3040585` |
| Execution time | Not captured in the Postman evidence |
| Evidence | [Postman execution screenshots](../evidence/TC_API_CRUD_2026-10-14_postman.md) |

| Step | Actual result | Functional outcome |
|---|---|---|
| Create account | Submitted the account data as `x-www-form-urlencoded`. The API returned HTTP `200`, `responseCode: 201`, and `message: "User created!"`. Six of seven Postman assertions passed; the `Content-Type` assertion failed on `text/html; charset=utf-8`. | **Passed** |
| Verify persisted details | Retrieved the new account by email. The API returned HTTP `200`, `responseCode: 200`, and user ID `3040585`. All 20 Postman assertions passed, including the 15 persisted-field checks. | **Passed** |

## 3. PowerShell execution

| Field | Value |
|---|---|
| Execution time | 2026-10-14 06:08:21–06:08:22 UTC |
| Test account | `user_test_1791958100619@example.com` |
| Retrieved user ID | `3038560` |
| Evidence | [API response transcript](../evidence/TC_API_CRUD_2026-10-14_responses.md), `001` create and detail |

| Step | Actual result | Functional outcome |
|---|---|---|
| Create account | The API returned HTTP `200`, `responseCode: 201`, and `message: "User created!"`. The response body was JSON; its `Content-Type` header was `text/html; charset=utf-8`. | **Passed** |
| Verify persisted details | The API returned HTTP `200`, `responseCode: 200`, and user ID `3038560`. All 15 retrievable fields matched the submitted data. | **Passed** |

The PowerShell account was retained for the next case and deleted during the recorded [`TC_API_CRUD_003` execution](TC_API_CRUD_003_result.md).
