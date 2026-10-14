# TC_API_CRUD_003 — Delete User Account: Manual Execution Result

## 1. Execution summary

| Field | Value |
|---|---|
| Test case | [TC_API_CRUD_003](../../crud/TC_API_CRUD_003_Delete_User_Account.md) |
| Environment | Public Automation Exercise API |
| Result | **Passed** — the disposable account was deleted and could no longer be retrieved by email. |

## 2. PowerShell execution

| Field | Value |
|---|---|
| Execution time | 2026-10-14 06:08:23–06:08:24 UTC |
| Test account | `user_test_1791958100619@example.com` |
| User ID before deletion | `3038560` |
| Evidence | [API response transcript](../evidence/TC_API_CRUD_2026-10-14_responses.md), `003` before, delete, and after |

| Step | Actual result | Outcome |
|---|---|---|
| Verify account before deletion | Retrieved the account with HTTP `200`, `responseCode: 200`, and user ID `3038560`. | **Passed** |
| Delete account | Submitted the registered email and password. The API returned HTTP `200`, `responseCode: 200`, and `message: "Account deleted!"`. | **Passed** |
| Verify account after deletion | Repeated the GET by email. The API returned HTTP `200`, `responseCode: 404`, and no `user` object. | **Passed** |
