# TC_API_CRUD_004 – Delete User Account (DELETE /api/deleteAccount)

**Objective:**  
Verify that an existing user account can be deleted successfully via DELETE request with valid credentials.

**Test Type / Level:** Functional / API  
**Priority / Severity:** High / Major  

---

## 1. Environment & Dependencies
- Base URL: `https://automationexercise.com/api`
- Postman environment variable: `{{baseUrl}} = https://automationexercise.com/api`
- Collection: **Automation Exercise – User API**
- Authorization: None required

---

## 2. Preconditions
- A valid user account exists.
- Email and password of that user are known.

---

## 3. Test Data
**Request**  
- **Method:** `DELETE`  
- **Endpoint:** `{{baseUrl}}/deleteAccount`  
- **Headers:**  
  - `Content-Type: application/x-www-form-urlencoded`  
- **Body (form-data or x-www-form-urlencoded):**
  - `email`: `testuser@example.com`
  - `password`: `Test123!`

---

## 4. Test Steps
1. Open **Delete User Account** request in Postman.  
2. Select method `DELETE`.  
3. Add body parameters (email, password).  
4. Send the request.  
5. Observe the response code and message.

---

## 5. Expected Results
- HTTP **200 OK** returned.  
- Response body:
  ```json
  {
    "responseCode": 200,
    "message": "Account deleted!"
  }
  ```
- Account should be permanently removed.

---

## 6. Actual Results
*(To be filled after execution; attach Postman screenshot)*

---

## 7. Status
Pass / Fail

---

## 8. Postconditions
- Account deleted; cannot be used for login.

---

## 9. Notes
- If rerun, expect “Account not found” message.
