from playwright.sync_api import expect


class OrdersDetailsPage:
    def __init__(self, page):
        self.page = page

    def VerifyOrderMessage(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
