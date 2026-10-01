# TC_API_CRUD_002 — Duplicate User Account Creation Prevented

| Field | Value |
|---|---|
| Test case ID | `TC_API_CRUD_002` |
| Requirement reference | `REQ-API-USER-002` |
| Objective | Verify that registration with an existing email is rejected and the retrievable account details remain unchanged. |
| Priority | High |
| Test type | Functional, negative |
| Test level | Integration |
| Test object / interface | REST API |

## Environment

- System under test: [Automation Exercise API](https://automationexercise.com/api_list)
- Execution tool: Postman
- Base URL: `https://automationexercise.com`

## Preconditions

- `TC_API_CRUD_001` has created a disposable account that remains available.
- Its `registeredEmail` value is stored as a Postman collection variable.
- The account can be retrieved with `GET /api/getUserDetailByEmail` before the duplicate request.

## Test Data

The second registration uses the existing `registeredEmail` and different account details. The password shown here is a disposable test value; it is not used to authenticate the original account.

| Field | Value |
|---|---|
| name | Jane Smith |
| email | `{{registeredEmail}}` |
| password | DifferentP@ssw0rd123 |
| title | Mrs |
| birth_date | 22 |
| birth_month | 04 |
| birth_year | 1992 |
| firstname | Jane |
| lastname | Smith |
| company | Example Corporation |
| address1 | 456 Park Avenue |
| address2 | Suite 10 |
| country | United States |
| zipcode | 10001 |
| state | New York |
| city | New York |
| mobile_number | 9876543210 |

## Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Send `GET https://automationexercise.com/api/getUserDetailByEmail` with query parameter `email={{registeredEmail}}`; retain the returned `user` object as the baseline. | HTTP status is `200` and the JSON body has `responseCode = 200` and the account created in `TC_API_CRUD_001`. |
| 2 | Send `POST https://automationexercise.com/api/createAccount` with the Test Data fields as an `x-www-form-urlencoded` body. | HTTP status is `200`. The JSON body has `responseCode = 400` and `message = "Email already exists!"`. |
| 3 | Repeat the GET request from step 1 and compare its `user` object with the baseline. | HTTP status is `200`, the JSON body has `responseCode = 200`, and every returned `user` field is unchanged. |

The API does not expose an account-count operation or the stored password through these requests. The rejection response and unchanged retrievable details are the observable checks for this case.

## Postconditions

The original account remains available. `TC_API_CRUD_003` removes it after this check.

## Automation Readiness

- **Automation candidate:** Yes
- **Current execution mode:** Manual execution in Postman
- **Shared test data:** `registeredEmail` collection variable from `TC_API_CRUD_001`
