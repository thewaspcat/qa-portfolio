# POST /api/createAccount Returns an Incorrect Content-Type Header

## 1. Bug Information

| Field | Value |
|---|---|
| Bug ID | `BR_TC_API_CRUD_001` |
| Test case | [`TC_API_CRUD_001`](../test-cases/api/TC_API_CRUD_001_Create_Register_User_Account.md) |
| Execution record | [`TC_API_CRUD_001_result.md`](../results/manual/TC_API_CRUD_001_result.md) |
| Severity | Medium |
| Priority | Medium |
| Status | Reproduced ([execution record](../results/manual/TC_API_CRUD_001_result.md)) |
| Type | API response contract discrepancy |
| Environment | Public Automation Exercise API |
| Endpoint | `POST https://automationexercise.com/api/createAccount` |
| Evidence | [Postman creation result](../evidence/api/TC_API_CRUD_001_create_results_postman.png); [API response transcript](../evidence/api/TC_API_CRUD_2026-10-14_responses.md), [`001` create](../evidence/api/TC_API_CRUD_2026-10-14_responses.md#tc-api-crud-001-create) |

## 2. Description

The create-account endpoint returns a JSON response body with `Content-Type: text/html; charset=utf-8`.  
The declared media type does not describe the returned JSON representation.

## 3. Steps to Reproduce

1. Submit a valid `x-www-form-urlencoded` create-account request using a unique email address.
2. Inspect the successful response body and its `Content-Type` header.

## 4. Expected Result

The Content-Type response header should accurately identify the media type of the response representation. Since the response body contains JSON, the expected media type is application/json.
[RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.3) defines `Content-Type` as the representation's media type.
[RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html#section-11) registers `application/json` for JSON text.

## 5. Actual Result

The endpoint returns a JSON response body with the Content-Type header set to text/html; charset=utf-8.

## 6. Impact

Clients relying on the Content-Type header to identify and process response representations may handle the response incorrectly. This discrepancy reduces API interoperability and compliance with HTTP representation metadata conventions.
