# Traceability Matrix

This matrix is the single source of truth for relationships between requirements, manual test cases, automated tests, page objects, test data, execution records, and defects.

An em dash means no linked artifact is recorded. N/A means a page object does not apply to the API case.

| Requirement | Manual test case | Manual execution record | Automated execution record | Defect | Automated coverage | Page object | Test data |
|---|---|---|---|---|---|---|---|
| `REQ-WEB-HOME-004` | [`TC_UI_HOME_001`](../manual/TC_UI_HOME_001.md) | [`TC_UI_HOME_001_result.md`](../manual/results/TC_UI_HOME_001_result.md) | [`TC_UI_HOME_001_result.md`](results/TC_UI_HOME_001_result.md) | [`BR_TC_UI_HOME_001`](../manual/bugs/BR_TC_UI_HOME_001.md) | `tests/test_tc_ui_home_001.py::test_tc_ui_home_001_homepage_layout`; `tests/test_tc_ui_home_001.py::test_tc_ui_home_001_featured_items_heading` (xfail); `tests/test_tc_ui_nav_001.py::test_tc_ui_nav_001_navigation_order_and_attributes` | `pages/home_page.py` | `data/test_homepage_data.json`; `data/test_navigation_data.json` |
| `REQ-AUTH-001` | [`TC_UI_LOGIN_001`](../manual/TC_UI_LOGIN_001.md) | [`TC_UI_LOGIN_001_result.md`](../manual/results/TC_UI_LOGIN_001_result.md) | [`TC_UI_LOGIN_001_result.md`](results/TC_UI_LOGIN_001_result.md) | — | `tests/test_tc_ui_login_001.py::test_tc_ui_login_001_valid_credentials` | `pages/login_page.py` | `data/test_login_data.json` and approved credential variables |
| `REQ-UI-NAV-001` | [`TC_UI_NAV_001`](../manual/TC_UI_NAV_001.md) | [`TC_UI_NAV_001_result.md`](../manual/results/TC_UI_NAV_001_result.md) | [`TC_UI_NAV_001_result.md`](results/TC_UI_NAV_001_result.md) | — | `tests/test_tc_ui_nav_001.py::test_tc_ui_nav_001_navigation_order_and_attributes`; `tests/test_tc_ui_nav_001.py::test_tc_ui_nav_001_internal_navigation`; `tests/test_tc_ui_nav_001.py::test_tc_ui_nav_001_video_tutorials_same_tab` | `pages/home_page.py` | `data/test_navigation_data.json` |
| `REQ-API-USER-001` | [`TC_API_CRUD_001`](../crud/TC_API_CRUD_001_Create_Register_User_Account.md) | — | — | — | — | N/A | [Case test data](../crud/TC_API_CRUD_001_Create_Register_User_Account.md#test-data); `registeredEmail`, `registeredPassword` collection variables |
| `REQ-API-USER-002` | [`TC_API_CRUD_002`](../crud/TC_API_CRUD_002_Duplicate_Prevented.md) | — | — | — | — | N/A | [Case test data](../crud/TC_API_CRUD_002_Duplicate_Prevented.md#test-data); `registeredEmail` collection variable |
| `REQ-API-USER-004` | [`TC_API_CRUD_003`](../crud/TC_API_CRUD_003_Delete_User_Account.md) | — | — | — | — | N/A | [Case test data](../crud/TC_API_CRUD_003_Delete_User_Account.md#test-data); `registeredEmail`, `registeredPassword` collection variables |
