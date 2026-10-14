# TC_API_CRUD_002 — Duplicate User Account Creation Prevented

## 1. Test Case Information

| Field | Value |
|---|---|
| Test case ID | `TC_API_CRUD_002` |
| Requirement reference | `REQ-API-USER-002` |
| Objective | Verify that registration with an existing email is rejected and the retrievable account details remain unchanged. |
| Priority | High |
| Test type | Functional, negative |
| Test level | Integration |
| Test object / interface | REST API |

## 2. Environment

- System under test: [Automation Exercise API](https://automationexercise.com/api_list)
- Execution tool: Postman
- Base URL: `https://automationexercise.com` (`baseUrl` Postman collection variable)

## 3. Preconditions

- [`TC_API_CRUD_001`](TC_API_CRUD_001_Create_Register_User_Account.md) has created a disposable account that remains available.
- The submitted `uniqueEmail` from a successful `TC_API_CRUD_001` creation is available as the `registeredEmail` Postman collection variable.
- The account can be retrieved with `GET /api/getUserDetailByEmail` before the duplicate request.

## 4. Test Data

The second registration uses the `registeredEmail` from the creation response handoff and different account details. The password shown here is a disposable test value; it is not used to authenticate the original account. The baseline GET stores the complete returned `user` object as JSON in the `crud002BaselineUser` collection variable.

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

## 5. Test Steps and Expected Results

| Step | Action | Expected result |
|---|---|---|
| 1 | Send `GET https://automationexercise.com/api/getUserDetailByEmail` with query parameter `email={{registeredEmail}}`; retain the returned `user` object as the baseline. | HTTP status is `200`, the JSON body has `responseCode = 200`, and the returned `user.email` equals `registeredEmail`. A valid baseline is stored in `crud002BaselineUser`. |
| 2 | Send `POST https://automationexercise.com/api/createAccount` with the Test Data fields as an `x-www-form-urlencoded` body. | HTTP status is `200`. The JSON body has `responseCode = 400` and `message = "Email already exists!"`. |
| 3 | Repeat the GET request from step 1 and compare its `user` object with the saved baseline. | HTTP status is `200`, the JSON body has `responseCode = 200`, and the complete returned `user` object is deeply equal to `crud002BaselineUser`. |

The API does not expose an account-count operation or the stored password through these requests. The rejection response and unchanged retrievable details are the observable checks for this case.

## 6. Postman Handoff

Before the baseline GET, the pre-request script clears any stale `crud002BaselineUser`. The response script stores a new baseline only when HTTP status is `200`, the JSON body has `responseCode = 200`, and a valid `user` object has an email equal to `registeredEmail`.

The duplicate POST is skipped when `registeredEmail` or `crud002BaselineUser` is missing. Its response script checks the HTTP status, JSON body, response code, and message. The final GET is skipped when `registeredEmail` or the saved baseline is invalid; its response script parses the baseline and checks deep equality with the complete returned `user` object. The final comparison can still run when the duplicate-response assertion fails, provided the baseline remains valid.

## 7. Postconditions

The original account is expected to remain available. [`TC_API_CRUD_003`](TC_API_CRUD_003_Delete_User_Account.md) removes it after this check, including when a duplicate-response assertion fails.

## 8. Automation Readiness

- **Automation candidate:** Yes
- **Current execution mode:** Manual execution in Postman
- **Shared test data:** `registeredEmail` from `TC_API_CRUD_001`; `crud002BaselineUser` captured before the duplicate request
