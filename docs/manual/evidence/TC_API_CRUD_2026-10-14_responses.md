# Account API response transcript — 2026-10-14

## 1. Execution Context

## 2. API Responses

Captured from the PowerShell `Invoke-WebRequest` execution against the public Automation Exercise API on 2026-10-14.  
Request bodies were sent as `application/x-www-form-urlencoded`.  
The disposable account email was `user_test_1791958100619@example.com`; passwords are omitted from this transcript.  
Times are UTC.  
All eight responses had HTTP status `200` and `Content-Type: text/html; charset=utf-8`.

Execution records: [`TC_API_CRUD_001`](../results/TC_API_CRUD_001_result.md), [`TC_API_CRUD_002`](../results/TC_API_CRUD_002_result.md), and [`TC_API_CRUD_003`](../results/TC_API_CRUD_003_result.md).

| Case and step | Time (UTC) | Request | Response body |
|---|---|---|---|
| `001` create | 06:08:21.582 | `POST /api/createAccount` | `{"responseCode":201,"message":"User created!"}` |
| `001` detail | 06:08:22.369 | `GET /api/getUserDetailByEmail?email=user_test_1791958100619%40example.com` | `responseCode: 200`; `user` shown below |
| `002` baseline | 06:08:22.613 | Same GET | `responseCode: 200`; same `user` shown below |
| `002` duplicate | 06:08:23.365 | `POST /api/createAccount` with the case 002 data | `{"responseCode":400,"message":"Email already exists!"}` |
| `002` after | 06:08:23.618 | Same GET | `responseCode: 200`; same `user` shown below |
| `003` before | 06:08:23.835 | Same GET | `responseCode: 200`; same `user` shown below |
| `003` delete | 06:08:24.080 | `DELETE /api/deleteAccount` | `{"responseCode":200,"message":"Account deleted!"}` |
| `003` after | 06:08:24.302 | Same GET | `{"responseCode":404,"message":"Account not found with this email, try another email!"}`; no `user` object |

## 3. Persisted Account Details

The four successful detail responses returned the same `user` object, including `id: 3038560` and these persisted fields:

| Field | Returned value |
|---|---|
| `name` | John Doe |
| `email` | `user_test_1791958100619@example.com` |
| `title` | Mr |
| `birth_day` | 15 |
| `birth_month` | 08 |
| `birth_year` | 1995 |
| `first_name` | John |
| `last_name` | Doe |
| `company` | Example Ltd |
| `address1` | 123 Main Street |
| `address2` | Apartment 4B |
| `country` | United States |
| `zipcode` | 10001 |
| `state` | New York |
| `city` | New York |

## 4. Execution Method

The supplied Postman pre-request and after-response scripts were reference material for the test data and checks.  
This run used PowerShell and carried the generated email and disposable password directly between requests; it did not execute Postman scripts.
