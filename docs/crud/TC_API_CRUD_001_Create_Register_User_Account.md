# TC_API_CRUD_001 — Create/Register User Account

## 1. Test Case Information

| Field | Value |
|---|---|
| Test case ID | `TC_API_CRUD_001` |
| Requirement reference | `REQ-API-USER-001` |
| Objective | Verify that a new user account can be created and its persisted details can be retrieved. |
| Priority | High |
| Test type | Functional, positive |
| Test level | Integration |
| Test object / interface | REST API |

## 2. Environment

- System under test: [Automation Exercise API](https://automationexercise.com/api_list)
- Execution tool: Postman
- Base URL: `https://automationexercise.com` (`baseUrl` Postman collection variable)

## 3. Preconditions

- The API is reachable.
- The `baseUrl` and `accountPassword` Postman collection variables are set to `https://automationexercise.com` and the disposable password `P@ssw0rd123`.
- The pre-request script generates a unique `uniqueEmail` collection variable that does not identify an existing account.
- The test is executed as part of the account API sequence `TC_API_CRUD_001` → [`TC_API_CRUD_002`](TC_API_CRUD_002_Duplicate_Prevented.md) → [`TC_API_CRUD_003`](TC_API_CRUD_003_Delete_User_Account.md).

## 4. Test Data

Before step 1, the Postman pre-request script clears any previous `registeredEmail` and `registeredPassword` values. It creates `user_test_` + `Date.now()` + `@example.com` and assigns that address to `uniqueEmail`. The request body uses `uniqueEmail` and `accountPassword`.

| Field | Value |
|---|---|
| name | John Doe |
| email | `{{uniqueEmail}}` |
| password | `{{accountPassword}}` |
| title | Mr |
| birth_date | 15 |
| birth_month | 08 |
| birth_year | 1995 |
| firstname | John |
| lastname | Doe |
| company | Example Ltd |
| address1 | 123 Main Street |
| address2 | Apartment 4B |
| country | United States |
| zipcode | 10001 |
| state | New York |
| city | New York |
| mobile_number | 1234567890 |

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Send `POST https://automationexercise.com/api/createAccount` with the Test Data fields as an `x-www-form-urlencoded` body. | HTTP status is `200`. The response body is valid JSON containing `responseCode = 201` and `message = "User created!"`. |
| 2 | Send `GET https://automationexercise.com/api/getUserDetailByEmail` with query parameter `email={{registeredEmail}}`. | HTTP status is `200`. The JSON response body contains `responseCode = 200` and a `user` object containing the persisted account details. Returned values match the submitted data according to the API field mapping: `birth_date` → `birth_day`, `firstname` → `first_name`, and `lastname` → `last_name`. |

The retrieval assertion covers the following persisted fields:

`name`, `email`, `title`, `birth_day`, `birth_month`, `birth_year`, `first_name`, `last_name`, `company`, `address1`, `address2`, `country`, `zipcode`, `state`, and `city`.

The detail response does not expose the password or mobile number; therefore, persistence of those two values is not asserted by this test case.

## 6. Postman Handoff

The creation response script checks the HTTP status, JSON parsing, and the presence and values of `responseCode` and `message`. Its `Content-Type` assertion checks the response's media-type contract separately from this case's create-and-retrieve objective. The script stores `uniqueEmail` as `registeredEmail` and `accountPassword` as `registeredPassword` only when HTTP status is `200`, `responseCode` is `201`, and the message is `User created!`. Otherwise it clears both registered credential variables. The detail request is skipped when `registeredEmail` is unavailable.

The detail response script checks the HTTP status, JSON body, response code, and returned `user` object. It compares each of the 15 retrievable fields listed above with its expected value.

## 7. Postconditions

A disposable account exists when the creation handoff conditions are met. The account remains available to `TC_API_CRUD_002` and `TC_API_CRUD_003`.

`TC_API_CRUD_003` performs final cleanup of the disposable account.

## 8. Automation Readiness

- **Automation candidate:** Yes
- **Current execution mode:** Manual execution in Postman
- **Shared test data:** `baseUrl` and `accountPassword` for setup; `uniqueEmail` for the creation request; `registeredEmail` and `registeredPassword` after the creation handoff conditions are met
- **Sequence dependency:** `TC_API_CRUD_002` and `TC_API_CRUD_003` consume the account created by this test case
