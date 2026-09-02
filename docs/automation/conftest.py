import json
import os
from pathlib import Path
from typing import Any

import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage


DATA_DIR = Path(__file__).parent / "data"


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
def home_page(page: Page, homepage_data: dict[str, Any]) -> HomePage:
    """Provide a HomePage configured with the test homepage URL."""
    return HomePage(page, homepage_data["home_url"])


@pytest.fixture
def login_page(page: Page, login_data: dict[str, Any]) -> LoginPage:
    """Provide a LoginPage configured with the login URL."""
    return LoginPage(page, login_data["login_url"])


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