import re
import json
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage


def _internal_links(navigation_data: dict[str, Any]) -> list[dict[str, Any]]:
    return [link for link in navigation_data["links"] if not link["external"]]


def _link_id(link_data: dict[str, Any]) -> str:
    return link_data["name"]


def _load_navigation_data() -> dict[str, Any]:
    data_path = Path(__file__).parents[1] / "data" / "test_navigation_data.json"
    with data_path.open(encoding="utf-8") as file:
        return json.load(file)


INTERNAL_NAVIGATION_LINKS = _internal_links(_load_navigation_data())


def test_tc_ui_nav_001_navigation_order_and_attributes(
    home_page: HomePage,
    navigation_data: dict[str, Any],
) -> None:
    """TC_UI_NAV_001: verify navigation count, order, text, and hrefs."""
    home_page.open()
    links = navigation_data["links"]
    expected_names = [link["name"] for link in links]

    expect(home_page.navigation_links).to_have_count(len(links))
    home_page.assert_navigation_order(expected_names)

    for link in links:
        expected_href = link["href"]
        home_page.assert_navigation_link(link["name"], expected_href)


@pytest.mark.parametrize(
    "link_data",
    INTERNAL_NAVIGATION_LINKS,
    ids=_link_id,
)
def test_tc_ui_nav_001_internal_navigation(
    page: Page,
    home_page: HomePage,
    link_data: dict[str, Any],
) -> None:
    """TC_UI_NAV_001: verify each internal navigation destination."""
    home_page.open()
    home_page.open_navigation_link(link_data["name"])
    expect(page).to_have_url(urljoin(home_page.url, link_data["href"]))


def test_tc_ui_nav_001_video_tutorials_same_tab(
    home_page: HomePage,
    navigation_data: dict[str, Any],
) -> None:
    """TC_UI_NAV_001: verify Video Tutorials opens in the current tab."""
    home_page.open()
    video_link = next(
        link for link in navigation_data["links"] if link["external"]
    )
    home_page.assert_navigation_link(video_link["name"], video_link["href"])

    home_page.open_navigation_link(video_link["name"])
    expect(home_page.page).to_have_url(
        re.compile(
            r"https://(?:www\.youtube\.com/c/AutomationExercise"
            r"|consent\.youtube\.com/.*AutomationExercise)"
        )
    )
