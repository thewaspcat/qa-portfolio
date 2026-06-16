# TC_API_GET_PRODUCTS_001 — Retrieve Products List

## 1. Test Case Information

- **Test Case ID:** TC_API_GET_PRODUCTS_001
- **Title:** Retrieve Products List
- **Requirement Refrence:** REQ-API-PRODUCTS-001
- **API Endpoint:** /api/productsList
- **HTTP Method:** GET
- **Base URL:** https://automationexercise.com
- **Priority:** High
- **Test Type:** Functional (Positive)
- **Test Level:** API / Integration


## 2. Objective

Validate that the `GET /api/productsList` endpoint returns a successful response with product data in a JSON format.


## 3. Preconditions

- API server is reachable
- No authentication is required for this endpoint


## 4. Request Details

### Request URL

https://automationexercise.com/api/productsList

### Headers

| Key | Value |
|---|---|
| Accept | application/json |

### Query Parameters / Path Parameters

- None

### Request Body

- Not applicable


## 5. Test Steps

| Step # | Action |
|---|---|
| 1 | Send a `GET` request to `https://automationexercise.com/api/productsList` |
| 2 | Capture the HTTP status code, response headers, and response body |
| 3 | Validate the response body structure and product fields |


## 6. Expected Results

- The endpoint returns **HTTP 200 OK**
- The response header `Content-Type` contains `application/json`
- The response body is valid JSON
- The root object contains:
  - `responseCode` = `200`
  - `products` as an array
- Each product object contains valid values for:
  - `id` present and numeric
  - `name` present and non-empty
  - `price` present
  - `brand` present and non-empty


## 7. Postconditions

- No data is modified by this request
- API state remains unchanged


## 8. Actual Results

(To be filled during execution)

## 9. Status

Pass / Fail