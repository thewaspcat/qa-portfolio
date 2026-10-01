# TC_API_CRUD_003 — Delete User Account

| Field | Value |
|---|---|
| Test case ID | `TC_API_CRUD_003` |
| Requirement reference | `REQ-API-USER-004` |
| Objective | Verify that an existing disposable account is deleted and can no longer be retrieved by email. |
| Priority | High |
| Test type | Functional, positive |
| Test level | Integration |
| Test object / interface | REST API |

## Environment

- System under test: [Automation Exercise API](https://automationexercise.com/api_list)
- Execution tool: Postman
- Base URL: `https://automationexercise.com`

## Preconditions

- `TC_API_CRUD_001` has created a disposable account that remains available.
- The account's `registeredEmail` and `registeredPassword` values are stored as Postman collection variables.
- The account can be retrieved with `GET /api/getUserDetailByEmail` before deletion.
- This case also serves as cleanup when `TC_API_CRUD_002` cannot complete after account creation.

## Test Data

| Field | Value |
|---|---|
| email | `{{registeredEmail}}` |
| password | `{{registeredPassword}}` |

Both values refer to the account created by `TC_API_CRUD_001`. No separate account or hard-coded credentials are used.

## Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Send `GET https://automationexercise.com/api/getUserDetailByEmail` with query parameter `email={{registeredEmail}}`. | HTTP status is `200`. The JSON body has `responseCode = 200` and identifies the account to delete. |
| 2 | Send `DELETE https://automationexercise.com/api/deleteAccount` with the Test Data fields as an `x-www-form-urlencoded` body. | HTTP status is `200`. The JSON body has `responseCode = 200` and `message = "Account deleted!"`. |
| 3 | Repeat the GET request from step 1. | HTTP status is `200`. The JSON body has `responseCode = 404` and does not contain the deleted account's `user` object. |

## Postconditions

The disposable account is no longer retrievable by email. If deletion does not succeed, the account remains a cleanup obligation for the test run.

## Automation Readiness

- **Automation candidate:** Yes
- **Current execution mode:** Manual execution in Postman
- **Shared test data:** `registeredEmail` and `registeredPassword` collection variables from `TC_API_CRUD_001`
