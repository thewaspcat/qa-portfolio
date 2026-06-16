# TC_API_CRUD_002 — Duplicate User Account Creation Prevented

## 1. Test Case Information

- **Test Case ID:** TC_API_CRUD_002
- **Title:** Duplicate User Account Creation Prevented
- **Requirement Reference:** REQ-API-USER-002
- **API Endpoint:** `/api/createAccount`
- **HTTP Method:** `POST`
- **Base URL:** `https://automationexercise.com`
- **Priority:** High
- **Test Type:** Functional (Negative)
- **Test Level:** API / Integration
- **Automation Status:** Automated
- **Automation Tool:** Postman / Newman

---

## 2. Objective

Validate that the `POST /api/createAccount` endpoint rejects a request that uses an email address already associated with an existing user account, does not create a duplicate account, and does not modify the existing account data.

---

## 3. Preconditions

- API server is reachable
- The endpoint is available
- `TC_API_CRUD_001` completed successfully
- A user account was created during execution of `TC_API_CRUD_001`
- The generated email address from `TC_API_CRUD_001` is stored in a Postman collection variable named `registeredEmail`
- The existing account can be retrieved successfully before and after the duplicate registration attempt
- Cleanup activity is available through `TC_API_CRUD_003`

---

## 4. Request Details

### Request URL

`https://automationexercise.com/api/createAccount`

### Headers

| Key | Value |
|---|---|
| Accept | application/json |
| Content-Type | application/json |

### Query Parameters / Path Parameters

None

### Pre-request Script

```javascript
// Retrieve the email generated during TC_API_CRUD_001
var existingEmail = pm.collectionVariables.get("registeredEmail");

console.log("Using existing email:", existingEmail);
```

### Request Body

```json
{
  "name": "Jane Smith",
  "email": "{{registeredEmail}}",
  "password": "P@ssw0rd123",
  "title": "Mrs",
  "birth_date": "22",
  "birth_month": "04",
  "birth_year": "1992",
  "firstname": "Jane",
  "lastname": "Smith",
  "company": "Example Corporation",
  "address1": "456 Park Avenue",
  "address2": "Suite 10",
  "country": "United States",
  "zipcode": "10001",
  "state": "New York",
  "city": "New York",
  "mobile_number": "9876543210"
}
```

---

## 5. Test Steps

| Step # | Action |
|---|---|
| 1 | Send a `GET` request to `https://automationexercise.com/api/getUserDetailByEmail?email={{registeredEmail}}` and capture the returned user data as the baseline result. |
| 2 | Validate that the baseline response returns the expected existing account information. |
| 3 | Send a `POST` request to `https://automationexercise.com/api/createAccount` using the existing email address created during `TC_API_CRUD_001`. |
| 4 | Capture the HTTP status code, response headers, response time, and response body. |
| 5 | Validate that the duplicate account creation request is rejected. |
| 6 | Validate that the response header contains `Content-Type: application/json`. |
| 7 | Validate that the response body is valid JSON. |
| 8 | Validate that the response body contains `responseCode = 400`. |
| 9 | Validate that the response body contains `message = "Email already exists!"`. |
| 10 | Send another `GET` request to `https://automationexercise.com/api/getUserDetailByEmail?email={{registeredEmail}}`. |
| 11 | Compare all persisted user fields between the baseline and post-attempt responses. |
| 12 | Confirm that no existing account data was modified after the duplicate registration attempt. |

---

## 6. Expected Results

- The endpoint does not create a second account using the same email address
- The duplicate registration request is rejected successfully
- HTTP status code returned is `400 Bad Request`
- Response header contains:
  - `Content-Type: application/json`
- Response body is valid JSON
- The root response object contains:
  - `responseCode = 400`
  - `message = "Email already exists!"`
- The existing account data returned before and after the duplicate registration attempt remains identical
- No evidence of additional accessible account creation is observable through available API responses
- No existing user data is modified

---

## 7. Postconditions

- No duplicate user account is added to the system
- The existing account remains unchanged
- API state is not modified by the duplicate registration attempt
- Test account cleanup is performed using `TC_API_CRUD_003 — Delete Existing User Account`

---

## 8. Cleanup Dependency

| Type | Reference |
|---|---|
| Cleanup Test Case | TC_API_CRUD_003 — Delete Existing User Account |

---

## 9. Test Data Management

| Item | Strategy |
|---|---|
| Test Account Naming | Timestamp-generated unique email address |
| Variable Storage | Postman collection variables |
| Cleanup Method | API-based account deletion |
| Cleanup Reference | TC_API_CRUD_003 |
| Environment Scope | QA / Test environments only |

---

## 10. Actual Results

- HTTP status code returned: `400 Bad Request`
- Response header contained:
  - `Content-Type: application/json`
- Response body received:

```json
{
  "responseCode": 400,
  "message": "Email already exists!"
}
```

- The duplicate registration request was rejected successfully
- No duplicate account was created
- User detail responses retrieved before and after the duplicate registration attempt were identical
- The existing account data remained unchanged

---

## 11. Status

Pass
