import time

from playwright.sync_api import Page, expect, Playwright


def test_API01(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    time.sleep(15)