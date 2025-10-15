# Homepage – Core Functionalities (Category, Brands & Featured Items)

## 1. Test Case Information
- **Test Case ID:** TC_FUNC_HOME_001  
- **Title:** Homepage – Core Functionalities (Category, Brands & Featured Items)  
- **Test Objective:** Validate that the homepage correctly displays the **Category section** (with categories and subcategories), the **Brands section** (with brand names and product counts), and the **Featured Items** grid including product details.  
- **Requirement Reference:** REQ-WEB-HOME-002  
- **Test Type:** Manual / Functional  
- **Test Level:** System (UI)  
- **Priority:** Critical  
- **Severity:** High  
- **Module:** Homepage  
- **Created By:** Marta Czarnecka  
- **Created On:** 03.09.2025  
- **Last Updated:** 15.10.2025  

---

## 2. Environment & Dependencies
**Environment:**  
- **Browser:** Chrome (latest stable version)  
- **OS:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com  

**Dependencies:**  
- Stable internet connection.  
- Application environment accessible and online.  
- User is logged out (no active session).  

---

## 3. Preconditions
- Chrome browser (latest stable version) is installed and functional.  
- Browser cache and cookies are cleared prior to execution.  
- Application server is up and responding to requests (homepage reachable).  
- User is logged out (no active session).  

---

## 4. Test Data

| Data Field     | Value |
|----------------|-------|
| Test URL       | https://www.automationexercise.com |
| Categories     | Women → Dress, Tops, Saree; Men → Tshirts, Jeans; Kids → Dress, Tops & Shirts |
| Brands         | Polo, H&M, Kookie Kids, Biba, etc. (with product counts) |
| Product Fields | Product Name, Price, Image |

---

## 5. Test Steps

| Step # | Action | Locator / Selector | Expected Result |
|--------|--------|--------------------|-----------------|
| 1 | Open homepage | N/A | Homepage loads successfully; sidebar and Featured Items section are visible without noticeable delay. |
| 2 | Check category section presence | `.left-sidebar` | Category section is visible on the left with heading “CATEGORY”. |
| 3 | Check main categories are listed (Women, Men, Kids) | `.left-sidebar a[href="#Women"]`, `.left-sidebar a[href="#Men"]`, `.left-sidebar a[href="#Kids"]` | Links for Women, Men, and Kids are visible. |
| 4 | Check subcategories under each main category | `.left-sidebar ul li a` | Expected subcategories are visible under Women (Dress, Tops, Saree), Men (Tshirts, Jeans), Kids (Dress, Tops & Shirts). |
| 5 | Check brands section presence | `.brands_products` | Brands section is visible with multiple entries and product counts (e.g., “(6) Polo”). |
| 6 | Check Featured Items grid section presence | `.features_items` | Section heading “FEATURES ITEMS” is visible, followed by a product grid. |
| 7 | Check at least one product is listed | `.features_items .col-sm-4` | At least one product card is displayed. |
| 8 | Check product details in grid | `.features_items h2` (price), `.features_items p` (name), `.features_items img` (image) | Each product card includes: (a) product name text not empty, (b) price displayed in numeric + currency format, (c) image loaded with non-empty `src` and `alt`. |
| 9 | Open page source and confirm required HTML elements exist | Browser → Right Click → View Page Source | Elements `<div class="left-sidebar">`, `<div class="brands_products">`, and `<div class="features_items">` exist in the source. |

---

## 6. Expected Results
- Category section is visible with main categories (Women, Men, Kids) and correct subcategories.  
- Brands section is present with multiple brand entries and product counts.  
- Featured Items section is visible with heading “FEATURES ITEMS.”  
- Product grid contains product cards with:  
  - Product name (non-empty text)  
  - Product price (valid numeric + currency format)  
  - Product image (valid `src` and non-empty `alt`)  
- All required HTML elements are confirmed in the page source.  

---

## 7. Actual Results
(To be completed after execution.)  

---

## 8. Status
- **Pass:** Category and Brands sections are visible with correct details; Featured Items section displays correctly; product cards include name, price, and image; page source elements exist.  
- **Fail:** Any required element missing, misaligned, or non-functional.  

---

## 9. Postconditions
- No changes to browser session or application state (user remains logged out).  
- Homepage remains accessible and unchanged after verification.  

---

## 10. Notes
- This test case validates *structural and content presence* only.  
- Performance validation (e.g., load time ≤5 seconds) is out of scope for manual testing and will be covered by automated performance tests.  
- Functional checks such as “Add to Cart,” “Wishlist,” or navigation to Product Details are covered in separate dedicated test cases.  

---

## Appendix – Element References

| Section | Locator / Selector | Description |
|----------|--------------------|--------------|
| Category Section | `div.left-sidebar` | Container for all category links |
| Brands Section | `div.brands_products` | Container for brand list with counts |
| Featured Items Section | `div.features_items` | Container for product grid |
| Product Name | `.features_items p` | Product title text |
| Product Price | `.features_items h2` | Product price element |
| Product Image | `.features_items img` | Product thumbnail with `src` and `alt` attributes |
