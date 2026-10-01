# TC_API_CRUD_001 — Create/Register User Account

| Field | Value |
|---|---|
| Test case ID | `TC_API_CRUD_001` |
| Requirement reference | `REQ-API-USER-001` |
| Objective | Verify that a new user account can be created and its persisted details can be retrieved. |
| Priority | High |
| Test type | Functional, positive |
| Test level | Integration |
| Test object / interface | REST API |

## Environment

- System under test: [Automation Exercise API](https://automationexercise.com/api_list)
- Execution tool: Postman
- Base URL: `https://automationexercise.com`

## Preconditions

- The API is reachable.
- `registeredEmail` is generated uniquely for the run, stored as a Postman collection variable, and does not identify an existing account.
- `registeredPassword` is the password for the disposable account and is stored as a Postman collection variable.
- The test is executed as part of the account API sequence `TC_API_CRUD_001` → `TC_API_CRUD_002` → `TC_API_CRUD_003`.

## Test Data

Before step 1, a unique email address with a timestamp in its local part is assigned to the `registeredEmail` Postman collection variable. A disposable account password is assigned to `registeredPassword`. Both values remain available to `TC_API_CRUD_002` and `TC_API_CRUD_003`.

| Field | Value |
|---|---|
| name | John Doe |
| email | `{{registeredEmail}}` |
| password | `{{registeredPassword}}` |
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

## Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Send `POST https://automationexercise.com/api/createAccount` with the Test Data fields as an `x-www-form-urlencoded` body. | HTTP status is `200`. The JSON response body contains `responseCode = 201` and `message = "User created!"`. |
| 2 | Send `GET https://automationexercise.com/api/getUserDetailByEmail` with query parameter `email={{registeredEmail}}`. | HTTP status is `200`. The JSON response body contains `responseCode = 200` and a `user` object containing the persisted account details. Returned values match the submitted data according to the API field mapping: `birth_date` → `birth_day`, `firstname` → `first_name`, and `lastname` → `last_name`. |

The retrieval assertion covers the following persisted fields:

`name`, `email`, `title`, `birth_day`, `birth_month`, `birth_year`, `first_name`, `last_name`, `company`, `address1`, `address2`, `country`, `zipcode`, `state`, and `city`.

The detail response does not expose the password or mobile number; therefore, persistence of those two values is not asserted by this test case.

## Postconditions

A disposable account exists and is retained for `TC_API_CRUD_002` and `TC_API_CRUD_003`.

`TC_API_CRUD_003` performs final cleanup of the disposable account.

## Automation Readiness

- **Automation candidate:** Yes
- **Current execution mode:** Manual execution in Postman
- **Shared test data:** `registeredEmail` and `registeredPassword` collection variables
- **Sequence dependency:** `TC_API_CRUD_002` and `TC_API_CRUD_003` consume the account created by this test case
