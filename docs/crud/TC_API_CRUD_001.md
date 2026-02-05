# TC_API_CRUD_001 – GET All Products List (GET /api/productsList)

**Objective:**  
Validate that the API returns the complete list of products with correct structure and status code.

**Test Type / Level:** Functional / API  
**Priority / Severity:** High / Major  

---

## 1. Environment & Dependencies
- Base URL: `https://automationexercise.com/api`
- Postman environment variable: `{{baseUrl}} = https://automationexercise.com/api`
- Collection: **Automation Exercise – Product API**
- Authorization: None required

---

## 2. Preconditions
- The server is online and accessible.
- Product data is available in the backend database.

---

## 3. Test Data
**Request**  
- **Method:** `GET`  
- **Endpoint:** `{{baseUrl}}/productsList`

**Headers:**  
- `Content-Type: application/json`

---

## 4. Test Steps
1. Open **Get All Products List** request in Postman.  
2. Ensure the environment variable `{{baseUrl}}` is set.  
3. Click **Send** to perform the GET request.  
4. Observe the response code and body.

---

## 5. Expected Results
- HTTP **200 OK** returned.  
- Response body includes:
  - `responseCode: 200`
  - `products` array containing multiple product objects.
- Each product object includes `id`, `name`, `price`, and `brand`.

---

## 6. Actual Results
*(To be filled after execution; attach Postman screenshot)*

---

## 7. Status
Pass / Fail

---

## 8. Postconditions
- None.

---

## 9. Notes
- This endpoint is read-only.
- Ensure the API response time is under 1s for optimal performance.
