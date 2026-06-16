# TC_API_CRUD_004 — Delete User Account

## 1. Test Case Information

- **Test Case ID:** TC_API_CRUD_004
- **Title:** Delete User Account
- **Requirement Reference:** REQ-API-USER-004
- **API Endpoint:** /api/deleteAccount
- **HTTP Method:** DELETE
- **Base URL:** https://automationexercise.com
- **Priority:** High
- **Test Type:** Functional (Positive)
- **Test Level:** API / Integration

## 2. Objective

Validate that an existing user account can be deleted successfully using the `DELETE /api/deleteAccount` endpoint with valid credentials.

## 3. Preconditions

- API server is reachable
- No authentication is required for this endpoint
- A valid user account exists
- The email and password of that user account are known

## 4. Request Details

### Request URL

https://automationexercise.com/api/deleteAccount

### Headers

| Key | Value |
|---|---|
| Accept | application/json |
| Content-Type | application/x-www-form-urlencoded |

### Query Parameters / Path Parameters

- None

### Request Body

```json
{
  "email": "testuser@example.com",
  "password": "Test123!"
}
```

## 5. Test Steps

| Step # | Action |
|---|---|
| 1 | Send a `DELETE` request to `https://automationexercise.com/api/deleteAccount` with valid credentials |
| 2 | Capture the HTTP status code, response headers, and response body |
| 3 | Validate the response body and confirm that the account is deleted successfully |

## 6. Expected Results

- The endpoint returns **HTTP 200 OK**
- The response body is valid JSON
- The root object contains:
  - `responseCode` = `200`
  - `message` = `"Account deleted!"`
- The user account is permanently removed and can no longer be used for login

## 7. Postconditions

- The user account is deleted
- The deleted account cannot be used for login

## 8. Actual Results

(To be filled during execution)

## 9. Status

Pass / Fail
