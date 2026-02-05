# TC_API_CRUD_003 – PUT To All Brands List (PUT /api/brandsList)

**Objective:**  
Verify that sending a PUT request to `/brandsList` returns the correct “Method Not Allowed” response (expected positive behavior).

**Test Type / Level:** Functional / API  
**Priority / Severity:** Medium / Minor  

---

## 1. Environment & Dependencies
- Base URL: `https://automationexercise.com/api`
- Postman environment variable: `{{baseUrl}} = https://automationexercise.com/api`
- Collection: **Automation Exercise – Brand API**
- Authorization: None required

---

## 2. Preconditions
- API is online.
- Request method is set to PUT.

---

## 3. Test Data
**Request**  
- **Method:** `PUT`  
- **Endpoint:** `{{baseUrl}}/brandsList`  
- **Headers:**  
  - `Content-Type: application/json`  
- **Body:**
```json
{
  "brand": "SampleBrand"
}
```

---

## 4. Test Steps
1. Open **PUT To Brands List** request in Postman.  
2. Confirm method is PUT.  
3. Click **Send** and review response.

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

---

## 6. Actual Results
*(To be filled after execution; attach screenshot of Postman response)*

---

## 7. Status
Pass / Fail

---

## 8. Postconditions
- None.

---

## 9. Notes
- Confirms API adherence to correct HTTP verb handling.
