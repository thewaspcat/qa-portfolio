# test_tc_ui_home_001 — Automated Execution Result

## 1. Execution metadata

| Field | Value |
|---|---|
| Test script | [`test_tc_ui_home_001.py`](../tests/test_tc_ui_home_001.py) |
| Manual test case | [`TC_UI_HOME_001`](../../manual/TC_UI_HOME_001.md) |
| Defect | [`BR_TC_UI_HOME_001`](../../manual/bugs/BR_TC_UI_HOME_001.md) |
| Execution date | 2026-09-25 |
| Environment/build | Public Automation Exercise environment |
| Browser | Playwright Chromium |
| Operating system | Windows |
| Evidence | `test-results/screenshots/docs_automation_tests_test_tc_ui_home_001.py_test_tc_ui_home_001_homepage_layout_chromium.png`; `test-results/screenshots/docs_automation_tests_test_tc_ui_home_001.py_test_tc_ui_home_001_featured_items_heading_chromium.png`. GitHub Actions uploads them as `playwright-evidence`. |

## 2. Actual result

The homepage layout checks, including the Recommended Items heading and DOM-order checks, passed. The application displayed `Features Items` instead of `Featured Items`.

## 3. Status

**Completed with expected failure:** `1 passed, 1 xfailed`.
