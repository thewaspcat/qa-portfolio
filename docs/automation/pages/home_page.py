from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url

    def open(self) -> None:
        self.page.goto(self.url)

    def assert_loaded(self, expected_title: str) -> None:
        expect(self.page).to_have_url(self.url)
        expect(self.page).to_have_title(expected_title)