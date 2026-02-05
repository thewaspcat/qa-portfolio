# TC_API_CRUD_002 – POST To All Products List (POST /api/productsList)

**Objective:**  
Verify that sending a POST request to `/productsList` returns the correct “Method Not Allowed” response (expected positive behavior).

**Test Type / Level:** Functional / API  
**Priority / Severity:** Medium / Minor  

---

## 1. Environment & Dependencies
- Base URL: `https://automationexercise.com/api`
- Postman environment variable: `{{baseUrl}} = https://automationexercise.com/api`
- Collection: **Automation Exercise – Product API**
- Authorization: None required

---

## 2. Preconditions
- API is online.
- Request method is set to POST.

---

## 3. Test Data
**Request**  
- **Method:** `POST`  
- **Endpoint:** `{{baseUrl}}/productsList`
- **Headers:**  
  - `Content-Type: application/json`  
- **Body:**
```json
{
  "name": "Invalid Product",
  "price": 10
}
```

---

## 4. Test Steps
1. In Postman, open **POST To Products List** request.  
2. Verify that the method is set to POST.  
3. Click **Send** and observe response.

---

## 5. Expected Results
- HTTP **405 Method Not Allowed** returned.  
- Response body includes:
  ```json
  {
    "responseCode": 405,
    "message": "This request method is not supported."
  }
  ```
- This is the correct expected positive result.

---

## 6. Actual Results
*(To be filled after execution; attach Postman response screenshot)*

---

## 7. Status
Pass / Fail

---

## 8. Postconditions
- None (no data created).

---

## 9. Notes
- This test validates proper API method enforcement.
