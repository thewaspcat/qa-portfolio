**QA coverage**


  | Requirement | Test case ID | Test scenario | Verification scope | Method |
  |---|---|---|---|---|
  | `REQ-WEB-HOME-004` | `TC_UI_HOME_001` | Homepage | Page title, logo attributes, navigation, section visibility and DOM order, footer | Manual UI + Playwright | 
  | `REQ-AUTH-001` | `TC_UI_LOGIN_001` | Valid login | Credential handling, authenticated state and session persistence after reload | Manual UI + Playwright | 
  | `REQ-UI-NAV-001` | `TC_UI_NAV_001` | Main navigation | Eight links, exact labels, order, `href` attributes and destination behavior | Manual UI + Playwright | 
  | `REQ-API-USER-001` | `TC_API_CRUD_001` | Account creation | Request validation, creation response and persistence of 15 retrievable fields | Postman | 
  | `REQ-API-USER-002` | `TC_API_CRUD_002` | Duplicate registration | Existing-account retrieval, duplicate rejection and deep equality of the original account data | Postman | 
  | `REQ-API-USER-004` | `TC_API_CRUD_003*` | Account deletion | Account existence, deletion response and unsuccessful retrieval after deletion | Postman |