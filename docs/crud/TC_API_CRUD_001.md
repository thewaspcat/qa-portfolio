# TC_API_GET_PRODUCTS_001 --- Retrieve Products List (Valid Request, Contract-Compliant)

## 1. Objective

Verify that the `GET /products` endpoint returns a
**contract-compliant**, **deterministic**, and **validated** response,
including: - Correct HTTP semantics - Header compliance - Schema
validation - Data integrity and consistency

------------------------------------------------------------------------

## 2. Test Classification

  -----------------------------------------------------------------------
  Attribute                                    Value
  -------------------------------------------- --------------------------
  Test Type                                    Functional (Positive)

  Test Level                                   API / Integration

  Test Design Technique                        Specification-based
                                               (Black-box), Contract
                                               Testing

  Priority                                     High

  Severity                                     Critical
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Traceability

  Artifact           Reference
  ------------------ --------------------------
  Requirement ID     API-PROD-GET-001
  Endpoint           `/api/products`
  API Contract       OpenAPI v3 / JSON Schema
  Contract Version   v1.0

------------------------------------------------------------------------

## 4. Environment & Configuration

  Parameter        Value
  ---------------- --------------------------------------------------
  Base URL         https://automationexercise.com/api
  Endpoint         /products
  Method           GET
  Protocol         HTTPS
  Authentication   Not required
  Tooling          Automated test framework + JSON Schema validator

------------------------------------------------------------------------

## 5. Preconditions

One must be satisfied: - Mocked dataset (preferred) - Controlled test
environment with stable data - Contract-stable environment

Additionally: - API reachable - TLS handshake succeeds

------------------------------------------------------------------------

## 6. Test Data

  Attribute   Value
  ----------- --------------------------
  Method      GET
  Headers     Accept: application/json
  Body        None

------------------------------------------------------------------------

## 7. Test Steps

1.  Send GET request to `/products`
2.  Capture:
    -   Status code
    -   Headers
    -   Body
    -   Response time

------------------------------------------------------------------------

## 8. Expected Results

### 8.1 HTTP Status

-   MUST be `200 OK`

### 8.2 Response Time

-   SHOULD meet SLA: p95 ≤ 1000 ms (environment-dependent)

### 8.3 Headers

-   `Content-Type` MUST match: `application/json(; charset=UTF-8)?`

### 8.4 Body Format

-   Valid JSON
-   UTF-8 encoded
-   Root object present

------------------------------------------------------------------------

## 8.5 Schema Validation

``` json
{
  "type": "object",
  "required": ["products"],
  "properties": {
    "products": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "name", "price", "brand"],
        "properties": {
          "id": {
            "type": "integer",
            "minimum": 1
          },
          "name": {
            "type": "string",
            "minLength": 1
          },
          "price": {
            "oneOf": [
              {
                "type": "string",
                "pattern": "^[0-9]+(\.[0-9]{1,2})?$"
              },
              {
                "type": "number",
                "minimum": 0
              }
            ]
          },
          "brand": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```

------------------------------------------------------------------------

## 8.6 Data Integrity

For each product: - All required fields present - No null values - `id`
unique within response - Strings trimmed and non-empty - `price` valid
per schema

------------------------------------------------------------------------

## 8.7 Determinism

Under controlled dataset: - Repeated calls return identical responses

------------------------------------------------------------------------

## 8.8 Negative Assertions

-   No malformed objects
-   No empty objects
-   No structural violations

------------------------------------------------------------------------

## 9. Actual Results

(To be filled during execution)

------------------------------------------------------------------------

## 10. Status

Pass / Fail

------------------------------------------------------------------------

## 11. Postconditions

-   No system state change

------------------------------------------------------------------------

## 12. Notes

-   Designed for automation
-   Supports forward-compatible schema evolution
-   Performance and security covered separately
