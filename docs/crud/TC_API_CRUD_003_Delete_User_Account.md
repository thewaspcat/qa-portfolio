# TC_API_CRUD_003 — Delete User Account

## 1. Test Case Information

- **Test Case ID:** TC_API_CRUD_004
- **Title:** Delete User Account
- **Requirement Reference:** REQ-API-USER-004
- **API Endpoint:** `/api/deleteAccount`
- **HTTP Method:** `DELETE`
- **Base URL:** `https://automationexercise.com`
- **Priority:** High
- **Test Type:** Functional (Positive)
- **Test Level:** API / Integration
- **Automation Status:** Automated
- **Automation Tool:** Postman / Newman

---

## 2. Objective

Validate that the `DELETE /api/deleteAccount` endpoint successfully deletes an existing user account when valid credentials are supplied, and that the account is no longer available afterward.

---

## 3. Preconditions

- API server is reachable
- The endpoint is available
- A valid user account exists
- The email and password for that account are known
- The account can be retrieved successfully before the delete request is executed
- Cleanup activity is available through `TC_API_CRUD_003`

---

## 4. Request Details

### Request URL

`https://automationexercise.com/api/deleteAccount`

### Headers

| Key | Value |
|---|---|
| Accept | application/json |
| Content-Type | application/x-www-form-urlencoded |

### Query Parameters / Path Parameters

None

### Pre-request Script

```javascript id="epkiop"
// Set the credentials for the existing account to be deleted
pm.collectionVariables.set("deleteEmail", "testuser@example.com");
pm.collectionVariables.set("deletePassword", "Test123!");

console.log("Prepared delete credentials for:", pm.collectionVariables.get("deleteEmail"));
```

### Request Body

```json id="44w5oy"
{
  "email": "{{deleteEmail}}",
  "password": "{{deletePassword}}"
}
```

---

## 5. Test Steps

| Step # | Action |
|---|---|
| 1 | Send a `GET` request to `https://automationexercise.com/api/getUserDetailByEmail?email={{deleteEmail}}` and capture the returned user data as the baseline result. |
| 2 | Validate that the baseline response returns the expected existing account information. |
| 3 | Send a `DELETE` request to `https://automationexercise.com/api/deleteAccount` using the valid account credentials. |
| 4 | Capture the HTTP status code, response headers, response time, and response body. |
| 5 | Validate that the delete request is accepted successfully. |
| 6 | Validate that the response header contains `Content-Type: application/json`. |
| 7 | Validate that the response body is valid JSON. |
| 8 | Validate that the response body contains `responseCode = 200`. |
| 9 | Validate that the response body contains `message = "Account deleted!"`. |
| 10 | Send another `GET` request to `https://automationexercise.com/api/getUserDetailByEmail?email={{deleteEmail}}`. |
| 11 | Compare the pre-delete and post-delete retrieval results. |
| 12 | Confirm that the account is no longer available after deletion. |

---

## 6. Expected Results

- The endpoint deletes the specified existing account successfully
- The delete request is accepted successfully
- HTTP status code returned is `200 OK`
- Response header contains:
  - `Content-Type: application/json`
- Response body is valid JSON
- The root response object contains:
  - `responseCode = 200`
  - `message = "Account deleted!"`
- The user account is no longer retrievable after deletion
- The account cannot be used for login or further account-based actions

---

## 7. Postconditions

- The user account is deleted from the system
- The deleted account is no longer available for authentication
- API state is changed by removal of the user record
- Test account cleanup is performed using `TC_API_CRUD_003 — Delete Existing User Account` only if a separate cleanup account is used for setup

---

## 8. Cleanup Dependency

| Type | Reference |
|---|---|
| Cleanup Test Case | TC_API_CRUD_003 — Delete Existing User Account |

---

## 9. Test Data Management

| Item | Strategy |
|---|---|
| Test Account Naming | Pre-created valid test account |
| Variable Storage | Postman collection variables |
| Cleanup Method | API-based account deletion |
| Cleanup Reference | TC_API_CRUD_003 |
| Environment Scope | QA / Test environments only |

---

## 10. Actual Results

- HTTP status code returned: `200 OK`
- Response header contained:
  - `Content-Type: application/json`
- Response body received:

```json id="k7x12l"
{
  "responseCode": 200,
  "message": "Account deleted!"
}
```

- The delete request was accepted successfully
- The user account was deleted
- The user detail response retrieved after deletion no longer returned the account data
- The account could no longer be used for login

---

## 11. Status

Pass
