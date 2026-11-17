import re

from playwright.sync_api import Locator, Page, expect


class HomePage:
    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url
        self.header = page.locator("header#header")
        self.logo = page.locator("div.logo.pull-left a img")
        self.navigation = page.locator("ul.nav.navbar-nav")
        self.navigation_links = self.navigation.locator(":scope > li > a")
        self.footer = page.locator("footer#footer")
        self.section_containers = {
            "Featured Items": page.locator("div.features_items"),
            "Recommended Items": page.locator("div.recommended_items"),
        }

    def open(self) -> None:
        self.page.goto(self.url)

    def assert_loaded(self, expected_title: str) -> None:
        expect(self.page).to_have_url(self.url)
        expect(self.page).to_have_title(expected_title)

    def assert_logo_visible(self) -> None:
        expect(self.logo).to_be_visible()
        expect(self.logo).to_have_attribute("alt", "Website for automation practice")
        expect(self.logo).to_have_attribute("src", re.compile(r".+"))

    def assert_navigation_visible(self) -> None:
        expect(self.navigation).to_be_visible()

    def assert_navigation_order(self, expected_names: list[str]) -> None:
        for index, expected_name in enumerate(expected_names):
            expect(self.navigation_links.nth(index)).to_contain_text(expected_name)

    def navigation_link(self, name: str) -> Locator:
        return self.navigation_links.filter(
            has_text=re.compile(re.escape(name))
        )

    def assert_navigation_link(self, name: str, expected_href: str) -> None:
        link = self.navigation_link(name)
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", expected_href)

    def open_navigation_link(self, name: str) -> None:
        self.navigation_link(name).click()

    def assert_section_visible(self, name: str) -> None:
        expect(self.section_containers[name]).to_be_visible()

    def assert_section_heading_visible(
        self,
        section_name: str,
        expected_heading: str | None = None,
    ) -> None:
        heading = expected_heading or section_name
        expect(
            self.section_containers[section_name].get_by_role(
                "heading",
                name=re.compile(rf"^{re.escape(heading)}$", re.IGNORECASE),
            )
        ).to_be_visible()

    def assert_section_follows(
        self,
        preceding_section: str,
        following_section: str,
    ) -> None:
        preceding = self.section_containers[preceding_section]
        following = self.section_containers[following_section]
        expect(preceding).to_be_visible()
        expect(following).to_be_visible()

        preceding_handle = preceding.element_handle()
        following_handle = following.element_handle()
        if preceding_handle is None or following_handle is None:
            raise AssertionError("Expected section container was not attached to the DOM.")

        follows = self.page.evaluate(
            """([preceding, following]) => Boolean(
                preceding.compareDocumentPosition(following)
                & Node.DOCUMENT_POSITION_FOLLOWING
            )""",
            [preceding_handle, following_handle],
        )
        assert follows, (
            f"Expected {following_section!r} to follow {preceding_section!r} in DOM order."
        )

    def assert_footer_visible(self) -> None:
        expect(self.footer).to_be_visible()
