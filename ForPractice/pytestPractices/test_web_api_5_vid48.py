from playwright.sync_api import Playwright

from ForPractice.pytestPractices.utils.apiBase import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Create Order
    api_utils = APIUtils()

    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("grupovalma@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("NewPassword01")
    page.get_by_role("button", name="login").click()

    #Orders History Page -> order is present


