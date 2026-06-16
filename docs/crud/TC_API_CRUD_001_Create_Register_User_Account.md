# TC_API_CRUD_001 — POST To Create/Register User Account

## 1. Test Case Information

- **Test Case ID:** TC_API_CRUD_001
- **Title:** POST To Create/Register User Account
- **Requirement Reference:** REQ-API-USER-001
- **API Endpoint:** `/api/createAccount`
- **HTTP Method:** `POST`
- **Base URL:** `https://automationexercise.com`
- **Priority:** High
- **Test Type:** Functional (Positive)
- **Test Level:** API / Integration
- **Automation Status:** Automated
- **Automation Tool:** Postman

---

## 2. Objective

Validate that the `POST /api/createAccount` endpoint successfully creates a new user account and returns the expected success response.

---

## 3. Preconditions

- API server is reachable
- The endpoint is available
- A valid request payload is prepared
- A unique email address is generated before request execution to avoid duplicate account creation errors
- The generated email address is stored in a Postman collection variable named `registeredEmail`
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
// Generate a unique email address using timestamp
var timestamp = Date.now();
var uniqueEmail = "qa_user_" + timestamp + "@mailtest.com";

pm.collectionVariables.set("registeredEmail", uniqueEmail);

console.log("Generated unique email:", uniqueEmail);
```

### Request Body

```json
{
  "name": "John Doe",
  "email": "{{registeredEmail}}",
  "password": "P@ssw0rd123",
  "title": "Mr",
  "birth_date": "15",
  "birth_month": "08",
  "birth_year": "1995",
  "firstname": "John",
  "lastname": "Doe",
  "company": "Example Ltd",
  "address1": "123 Main Street",
  "address2": "Apartment 4B",
  "country": "United States",
  "zipcode": "10001",
  "state": "New York",
  "city": "New York",
  "mobile_number": "1234567890"
}
```

---

## 5. Test Steps

| Step # | Action |
|---|---|
| 1 | Send a `POST` request to `https://automationexercise.com/api/createAccount` with the required headers and request body. |
| 2 | Capture the HTTP status code, response headers, response time, and response body. |
| 3 | Validate that the response indicates successful user creation. |
| 4 | Send a `GET` request to `https://automationexercise.com/api/getUserDetailByEmail?email={{registeredEmail}}`. |
| 5 | Validate that the returned user details match the submitted account data. |

---

## 6. Expected Results

- The endpoint returns **HTTP 201 Created** if the API uses transport-level success codes for account creation; otherwise the observed HTTP status is captured and validated as part of execution evidence
- The response body is valid JSON
- The root object contains:
  - `responseCode = 201`
  - `message = "User created!"`
- The created account is retrievable using `GET /api/getUserDetailByEmail?email={{registeredEmail}}`
- The returned user details match the submitted data for the persisted fields

---

## 7. Postconditions

- A new user account is created in the system
- API state is changed by the creation of the new user record
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

- HTTP status code returned: 201 Created
- Response body received:
  - `responseCode = 201`
  - `message = "User created!"`
- The request completed successfully
- A new user account was created using the submitted data
- The created account was retrievable using `GET /api/getUserDetailByEmail?email={{registeredEmail}}`
- No errors were returned by the API

---

## 11. Status

Pass
