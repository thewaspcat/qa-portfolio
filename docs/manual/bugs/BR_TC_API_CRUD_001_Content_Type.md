# Bug Report: Create Account Response Uses an Incorrect Media Type

## 1. Bug Information

| Field | Value |
|---|---|
| Bug ID | `BR_TC_API_CRUD_001` |
| Test case | [`TC_API_CRUD_001`](../../crud/TC_API_CRUD_001_Create_Register_User_Account.md) |
| Execution record | [`TC_API_CRUD_001_result.md`](../results/TC_API_CRUD_001_result.md) |
| Type | API response contract discrepancy |
| Environment | Public Automation Exercise API |
| Endpoint | `POST https://automationexercise.com/api/createAccount` |
| Evidence | [Postman creation result](../evidence/TC_API_CRUD_001_create_results_postman.png); [API response transcript](../evidence/TC_API_CRUD_2026-10-14_responses.md), `001` create |

## 2. Description

The create-account endpoint returns a JSON response body with `Content-Type: text/html; charset=utf-8`.  
The declared media type does not describe the returned JSON representation.

## 3. Steps to Reproduce

1. Submit a valid `x-www-form-urlencoded` create-account request using a unique email address.
2. Inspect the successful response body and its `Content-Type` header.

## 4. Expected Result

The JSON response body is identified with the `application/json` media type. [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.3) defines `Content-Type` as the representation's media type; [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html#section-11) registers `application/json` for JSON text.

## 5. Actual Result

The response body is valid JSON with `responseCode: 201` and `message: "User created!"`, but the response header is `Content-Type: text/html; charset=utf-8`.  
The Postman media-type assertion failed; the account was created and its stored details were retrievable.

## 6. Impact

Clients that select a parser or enforce response contracts using `Content-Type` may treat the JSON response as HTML.  
Account creation itself succeeded in the recorded executions.
