from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the Automation Exercise login page."""

    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url

        self.email_input = page.locator('[data-qa="login-email"]')
        self.password_input = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.logout_link = page.locator('a[href="/logout"]')

    def open(self) -> None:
        """Navigate to the login page."""
        self.page.goto(self.url)

    def assert_loaded(self, expected_url: str) -> None:
        """Verify that the login page is loaded."""
        expect(self.page).to_have_url(expected_url)
        expect(
            self.page.get_by_role("heading", name="Login to your account", exact=True)
        ).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()

    def login(self, email: str, password: str) -> None:
        """Log in with the supplied credentials."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_logged_in(
        self,
        expected_text: str,
        username: str | None = None,
    ) -> None:
        """Verify that the user is authenticated."""
        expect(
            self.page.get_by_text(expected_text, exact=False)
        ).to_be_visible()

        expect(self.logout_link).to_be_visible()

        if username:
            expect(
                self.page.get_by_text(username, exact=True)
            ).to_be_visible()

    def reload_and_assert_authenticated(
        self,
        expected_text: str,
        username: str | None = None,
    ) -> None:
        self.page.reload()
        self.assert_logged_in(expected_text, username)

    def is_authenticated(self) -> bool:
        """Return whether the authenticated Logout control is visible."""
        return self.logout_link.is_visible()

    def logout(self) -> None:
        """End the authenticated session."""
        self.logout_link.click()

    def assert_logged_out(self) -> None:
        """Verify that logout returns the user to the login page."""
        self.assert_loaded(self.url)
