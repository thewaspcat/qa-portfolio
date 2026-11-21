# TC_API_CRUD_003 — Delete User Account: Manual Execution Result

## 1. Execution summary

| Field | Value |
|---|---|
| Test case | [TC_API_CRUD_003](../../test-cases/api/TC_API_CRUD_003_Delete_User_Account.md) |
| Environment | Public Automation Exercise API |
| Result | **Passed** — the disposable account was deleted and could no longer be retrieved by email. |

## 2. Postman execution

| Field | Value |
|---|---|
| Test account | `user_test_1795267471904@example.com` |
  | Retrieved user ID  | 3040585 |
| Execution date | 2026-11-21 |
| Evidence | [Pre-deletion lookup test results](../../evidence/api/TC_API_CRUD_003_verify_account_exists_results.png) · [Deletion response](../../evidence/api/TC_API_CRUD_003_vdelete_user_account.png) · [Deletion test results and script](../../evidence/api/TC_API_CRUD_003_delete_account_results.png) · [Post-deletion lookup response](../../evidence/api/TC_API_CRUD_003_verify_user_deleted.png) · [Post-deletion lookup test results and script](../../evidence/api/TC_API_CRUD_003_verify_user_deleted_results.png) |

| Step | Actual result | Outcome |
|---|---|---|
| Verify the account exists | Retrieved the account by its registered email. The API returned HTTP `200`, `responseCode: 200`, and a `user` object with the matching email and user ID `3272167`. Both Postman tests passed. | **Passed** |
| Delete the account | Sent the registered email and password as an `x-www-form-urlencoded` body. The API returned HTTP `200`, `responseCode: 200`, and `message: "Account deleted!"`. Both Postman tests passed. | **Passed** |
| Verify the account is no longer retrievable | Repeated the lookup with the same email. The API returned HTTP `200` and `responseCode: 404`. The response body reported that the account could not be found and omitted the `user` object. Both Postman tests passed. | **Passed** |
