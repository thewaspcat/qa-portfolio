# TC_API_GET_PRODUCTS_001 — Retrieve Products List

## 1. Objective

Validate that the GET [/api/productsList](https://automationexercise.com/api/productsList) endpoint returns a successful response with a valid JSON structure containing a list of products.

---

## 2. Test Classification

- Test Type: Functional (Positive)
- Test Level: API
- Priority: High

---

## 4. Preconditions

- API server is reachable

---

## 5. Test Data

Base URL: <https://automationexercise.com>

Request:

- Method: GET
- Endpoint: /api/productsList
- Headers: Accept: application/json

---

## 5. Test Steps

1. Send GET request to /api/productsList
2. Capture response:

Status code
Headers
Response body

---

## 6. Expected Results

### 6.1 Status Code

- 200 OK

### 6.2 Response Headers

- Content-Type contains application/json

### 6.3 Response Body

- Response is valid JSON
- Root object contains:
  - responseCode = 200
  - products (array)

### 6.4 Product Object Validation

For each product:

- id is present and numeric
- name is present and non-empty
- price is present (string format allowed)
- brand is present and non-empty

---

## 7. Actual Result

(To be filled during execution)

---

## 8. Status

Pass / Fail
