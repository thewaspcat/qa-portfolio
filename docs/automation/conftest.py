import json
import os
import re
from pathlib import Path
from typing import Any, Iterator

import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage


DATA_DIR = Path(__file__).parent / "data"
EVIDENCE_DIR = Path(__file__).parent / "test-results" / "screenshots"


def load_json(filename: str) -> dict[str, Any]:
    """Load one JSON object from the automation data directory."""
    with (DATA_DIR / filename).open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise TypeError(f"Expected a JSON object in {filename}")
    return data


@pytest.fixture
def homepage_data() -> dict[str, Any]:
    """Provide homepage test data."""
    return load_json("test_homepage_data.json")


@pytest.fixture
def navigation_data() -> dict[str, Any]:
    """Provide homepage navigation expectations."""
    return load_json("test_navigation_data.json")


@pytest.fixture
def home_page(page: Page, homepage_data: dict[str, Any]) -> HomePage:
    """Provide a HomePage configured with the test homepage URL."""
    return HomePage(page, homepage_data["home_url"])


@pytest.fixture
def login_page(page: Page, login_data: dict[str, Any]) -> LoginPage:
    """Provide a LoginPage configured with the login URL."""
    return LoginPage(page, login_data["login_url"])


@pytest.fixture
def login_session(login_page: LoginPage) -> Iterator[LoginPage]:
    """Provide a login page and end an authenticated session during teardown."""
    yield login_page

    if login_page.is_authenticated():
        login_page.logout()
        login_page.assert_logged_out()


@pytest.fixture
def login_data() -> dict[str, Any]:
    """Provide login data without storing credentials in source control."""
    data = load_json("test_login_data.json")
    email = os.getenv(data["email_env"])
    password = os.getenv(data["password_env"])

    if not email or not password:
        pytest.skip(
            "Set AUTOMATION_EXERCISE_EMAIL and "
            "AUTOMATION_EXERCISE_PASSWORD to run the login test."
        )

    data["email"] = email
    data["password"] = password
    username_env = data.get("username_env")
    if username_env:
        data["username"] = os.getenv(username_env)
    return data


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]):
    """Capture evidence immediately after each test body completes."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return

    page = getattr(item, "_evidence_page", None)
    if page is None or page.is_closed():
        return

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid).strip("_")
    page.screenshot(path=EVIDENCE_DIR / f"{filename}.png", full_page=True)


@pytest.fixture(autouse=True)
def capture_screenshot_evidence(request: pytest.FixtureRequest, page: Page) -> Iterator[None]:
    """Make the test page available to the execution-report hook."""
    request.node._evidence_page = page
    yield
