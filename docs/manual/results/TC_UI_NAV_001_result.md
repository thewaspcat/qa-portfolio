# TC_UI_NAV_001 — Manual Execution Result

## Execution metadata

| Field | Value |
|---|---|
| Execution date | 2026-09-25 |
| Environment | Public Automation Exercise website |
| Execution source | Manual test execution |
| Execution timestamp | 2026-09-25 11:04:53–11:05:13 |
| Evidence | [Navigation structure](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_navigation_order_and_attributes_chromium.png); [Home](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-Home.png); [Products](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-Products.png); [Cart](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-Cart.png); [Signup / Login](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-Signup_Login.png); [Test Cases](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-Test_Cases.png); [API Testing](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-API_Testing.png); [Contact us](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_internal_navigation_chromium-Contact_us.png); [Video Tutorials](../evidence/TC_UI_NAV_001/docs_automation_tests_test_tc_ui_nav_001.py_test_tc_ui_nav_001_video_tutorials_same_tab_chromium.png). |

## Actual result

All eight links were present in the expected order. Each destination check passed:

| Link | Actual result | Status |
|---|---|---|
| Home | Remained on the homepage. | Passed |
| Products | Reached `/products`. | Passed |
| Cart | Reached `/view_cart`. | Passed |
| Signup / Login | Reached `/login`. | Passed |
| Test Cases | Reached `/test_cases`. | Passed |
| API Testing | Reached `/api_list`. | Passed |
| Video Tutorials | Navigated in the current tab to the YouTube destination, possibly via its consent endpoint. | Passed |
| Contact us | Reached `/contact_us`. | Passed |

## Status

**Passed.**
