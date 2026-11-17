# Requirements

This document defines the expected behavior and acceptance criteria for the homepage, authentication, navigation, and account API functions covered by this portfolio. The existing requirement IDs are retained.

Each entry identifies its source or specification basis. Verification relationships are maintained in the [Traceability Matrix](TRACEABILITY.md).

## REQ-WEB-HOME-004

**Title:** Homepage shell and key components

**Requirement:** The homepage shall load with the expected identity and display its navigation, product sections, and footer.

**Source or basis:** [Homepage specification, test data and expected results](test-cases/ui/TC_UI_HOME_001.md#4-test-data).

**Acceptance criteria:**

1. The homepage loads at `https://www.automationexercise.com/` with the title `Automation Exercise`.
2. The logo is visible, its `alt` value is `Website for automation practice`, and its `src` value is non-empty.
3. The navigation bar is visible.
4. The Featured Items section is visible and its heading reads `Featured Items`.
5. The Recommended Items section is visible, its heading reads `Recommended Items`, and it follows the Featured Items section in page order.
6. The footer is visible.

## REQ-AUTH-001

**Title:** Valid login and session persistence

**Requirement:** A registered user shall be able to authenticate with valid credentials and remain authenticated after a page reload.

**Source or basis:** [Automation Exercise Test Case 2](https://automationexercise.com/test_cases) describes valid login and the authenticated indicator. The [login specification](test-cases/ui/TC_UI_LOGIN_001.md#5-test-steps-and-expected-results) defines the input, Logout control, and reload-persistence criteria.

**Acceptance criteria:**

1. The login page is available at `https://www.automationexercise.com/login` and displays `Login to your account`.
2. The email field displays the supplied address, and the password field masks the entered password.
3. Submitting valid credentials displays `Logged in as` and the Logout control.
4. After a page reload, `Logged in as` and the Logout control remain visible.

## REQ-UI-NAV-001

**Title:** Main navigation structure and destinations

**Requirement:** The navigation menu shall present the specified links in order and allow a logged-out user to reach their configured destinations.

**Source or basis:** [Navigation specification, link data and expected results](test-cases/ui/TC_UI_NAV_001.md#4-test-data).

**Acceptance criteria:**

1. Exactly eight visible links appear in the following order, with the listed labels and `href` values.

   | Label | href |
   |---|---|
   | Home | `/` |
   | Products | `/products` |
   | Cart | `/view_cart` |
   | Signup / Login | `/login` |
   | Test Cases | `/test_cases` |
   | API Testing | `/api_list` |
   | Video Tutorials | `https://www.youtube.com/c/AutomationExercise` |
   | Contact us | `/contact_us` |

2. Selecting an internal link reaches its listed path on the `https://www.automationexercise.com` origin.
3. Selecting Video Tutorials navigates the current tab to the listed YouTube channel or its YouTube consent URL for that channel.

## REQ-API-USER-001

**Title:** Account creation and retrieval

**Requirement:** The account API shall create an account from valid registration data using an unused email address and allow its persisted details to be retrieved by that address.

**Source or basis:** [Automation Exercise APIs 11 and 14](https://automationexercise.com/api_list) document the creation and retrieval operations and application response codes. The [account-creation specification](test-cases/api/TC_API_CRUD_001_Create_Register_User_Account.md#5-test-steps-and-expected-results) defines HTTP status, field comparisons, and request encoding.

**Acceptance criteria:**

1. A valid form-encoded request to `POST /api/createAccount` returns HTTP `200` with a JSON body containing `responseCode: 201` and `message: "User created!"`.
2. `GET /api/getUserDetailByEmail` for the new email returns HTTP `200`, a JSON `responseCode` of `200`, and the created account's `user` object.
3. The returned `name`, `email`, `title`, birth date, first and last names, company, address lines, country, zipcode, state, and city match the submitted values. Field mappings are `birth_date` to `birth_day`, `firstname` to `first_name`, and `lastname` to `last_name`; the birth date includes day, month, and year.

The persisted-field criteria cover the 15 fields retrievable through this interface. Password and mobile-number persistence are outside these retrieval criteria.

## REQ-API-USER-002

**Title:** Duplicate-registration prevention

**Requirement:** Registration with an existing account's email shall be rejected, and the existing account's retrievable details shall remain unchanged.

**Source or basis:** [Duplicate-registration specification, baseline and expected results](test-cases/api/TC_API_CRUD_002_Duplicate_Prevented.md#5-test-steps-and-expected-results).

**Acceptance criteria:**

1. Before the duplicate request, retrieval by email returns HTTP `200`, a JSON `responseCode` of `200`, and a `user` object whose email matches the existing account.
2. A form-encoded `POST /api/createAccount` request using that email and different account details returns HTTP `200` with a JSON body containing `responseCode: 400` and `message: "Email already exists!"`.
3. Retrieval after the duplicate request returns HTTP `200` and a JSON `responseCode` of `200`. The complete `user` object is deeply equal to its pre-request value.

## REQ-API-USER-004

**Title:** Account deletion

**Requirement:** The account API shall delete an existing account when supplied with its valid email and password, after which the account shall no longer be retrievable by email.

**Source or basis:** [Automation Exercise APIs 12 and 14](https://automationexercise.com/api_list) document deletion and retrieval. The [account-deletion specification](test-cases/api/TC_API_CRUD_003_Delete_User_Account.md#5-test-steps-and-expected-results) defines the before-and-after retrieval checks and HTTP status expectations.

**Acceptance criteria:**

1. Before deletion, retrieval by email returns HTTP `200`, a JSON `responseCode` of `200`, and the account's `user` object.
2. A form-encoded `DELETE /api/deleteAccount` request containing that account's valid email and password returns HTTP `200` with a JSON body containing `responseCode: 200` and `message: "Account deleted!"`.
3. Retrieval by the same email after deletion returns HTTP `200` and a JSON `responseCode` of `404`, without a `user` object for the deleted account.
