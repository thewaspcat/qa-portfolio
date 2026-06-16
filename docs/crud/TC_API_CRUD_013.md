# TC_API_CRUD_003 — PUT To Brands List

## 1. Test Case Information

- **Test Case ID:** TC_API_CRUD_003
- **Title:** PUT To Brands List
- **Requirement Reference:** REQ-API-BRANDS-003
- **API Endpoint:** /api/brandsList
- **HTTP Method:** PUT
- **Base URL:** https://automationexercise.com
- **Priority:** Medium
- **Test Type:** Functional (Negative)
- **Test Level:** API / Integration

## 2. Objective

Validate that the `PUT /api/brandsList` endpoint returns the expected method-not-allowed response when the PUT method is used.

## 3. Preconditions

- API server is reachable
- No authentication is required for this endpoint
- The request method is set to `PUT`

## 4. Request Details

### Request URL

https://automationexercise.com/api/brandsList

### Headers

| Key | Value |
|---|---|
| Accept | application/json |
| Content-Type | application/json |

### Query Parameters / Path Parameters

- None

### Request Body

```json
{
  "brand": "SampleBrand"
}
```

## 5. Test Steps

| Step # | Action |
|---|---|
| 1 | Send a `PUT` request to `https://automationexercise.com/api/brandsList` |
| 2 | Capture the HTTP status code, response headers, and response body |
| 3 | Validate the response body and confirm that the method is not supported |

## 6. Expected Results

- The endpoint returns **HTTP 405 Method Not Allowed**
- The response body is valid JSON
- The root object contains:
  - `responseCode` = `405`
  - `message` = `"This request method is not supported."`

## 7. Postconditions

- No data is created or modified
- API state remains unchanged

## 8. Actual Results

(To be filled during execution)

## 9. Status

Pass / Fail
