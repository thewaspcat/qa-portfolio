# Homepage – Core Functionalities (Category, Brands & Featured Items)

## 1. Test Case Information
- **Test Case ID:** TC_FUNC_HOME_001  
- **Title:** Homepage – Core Functionalities (Category, Brands & Featured Items)  
- **Test Objective:** Ensure that the homepage loads correctly and displays the **Category section** (with categories and subcategories), the **Brands section** (with brand names and product counts), and the **Featured Items** grid with expected elements.  
- **Requirement Reference:** REQ-WEB-HOME-002  
- **Test Type:** Manual / Functional  
- **Test Level:** System (UI)
- **Priority:** Critical  
- **Severity:** High  
- **Module:** Homepage  
- **Created By:** Marta Czarnecka  
- **Created Date:** 03.09.2025  
- **Last Updated:** 13.09.2025  

---

## 2. Environment & Dependencies
**Environment:**  
- **Browser:** Chrome (latest stable version)  
- **OS:** Windows / macOS / Linux  
- **Test URL:** https://www.automationexercise.com  

**Dependencies:**  
- Stable internet connection  
- Test environment accessible and online  
- User is logged out (no active session)  

---

## 3. Preconditions
- Chrome browser (latest stable version) is installed and functional  
- Browser cache and cookies are cleared prior to execution  
- Application server is up and responding to requests (homepage reachable)  
- User is logged out (no active session)  

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
| 2 | Verify category section presence | `.left-sidebar` | Category section is visible on the left with “CATEGORY” heading. |
| 3 | Verify main categories are listed (Women, Men, Kids) | `.left-sidebar a[href="#Women"]`, `.left-sidebar a[href="#Men"]`, `.left-sidebar a[href="#Kids"]` | Links for Women, Men, and Kids are visible. |
| 4 | Verify subcategories under each main category | `.left-sidebar ul li a` | Expected subcategories are visible under Women (Dress, Tops, Saree), Men (Tshirts, Jeans), Kids (Dress, Tops & Shirts). |
| 5 | Verify brands section presence | `.brands_products` | Brands section is visible with multiple entries and product counts (e.g., “(6) Polo”). |
| 6 | Verify Featured Items grid section presence | `.features_items` | “FEATURES ITEMS” heading is visible, followed by a product grid. |
| 7 | Verify at least one product is listed | `.features_items .col-sm-4` | At least one product card is displayed. |
| 8 | Verify product details in grid | `.features_items h2` (price), `.features_items p` (name), `.features_items img` (image) | Each product card includes: (a) product name text not empty, (b) price displayed in numeric + currency format, (c) image loaded with non-empty `src` and `alt`. |
| 9 | Validate page source contains required elements | Browser → Right Click → View Page Source | Elements `<div class="left-sidebar">`, `<div class="brands_products">`, and `<div class="features_items">` exist in the source. |

---

## 6. Expected Results
- Category section is visible with main categories (Women, Men, Kids) and correct subcategories.  
- Brands section is present with multiple brand entries and product counts.  
- Featured Items section is visible with heading “FEATURES ITEMS.”  
- Product grid contains product cards with:  
  - Product name (non-empty text)  
  - Product price (valid format)  
  - Product image (with valid `src` and non-empty `alt`)  
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
- This test case covers *structural and content presence* only.  
- Performance validation (e.g., load time ≤5 seconds) is out of scope for manual testing and should be covered by automated performance tests.  
- Functional checks such as “Add to Cart,” “Wishlist,” or navigation to Product Details are covered in separate dedicated test cases.  

---

## Appendix – Page Source Verification

**Category Section:**  
```html
<div class="left-sidebar">
  <h2>Category</h2>
  <a href="#Women">Women</a>
  <ul class="nav nav-stacked">...</ul>
</div>
```

**Brands Section:**  
```html
<div class="brands_products">
  <h2>Brands</h2>
  <ul class="nav nav-pills nav-stacked">
    <li><a href=""> <span class="pull-right">(6)</span>Polo</a></li>
    ...
  </ul>
</div>
```

**Featured Items Grid:**  
```html
<div class="features_items">
  <h2 class="title text-center">Features Items</h2>
  <div class="col-sm-4">
    <div class="product-image-wrapper">
      <img src="blue-top.jpg" alt="Blue Top">
      <h2>$50</h2>
      <p>Blue Top</p>
    </div>
  </div>
</div>
```
