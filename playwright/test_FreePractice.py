import time

from playwright.sync_api import Page

def test_personal(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.aduanas.gob.do/")
    page.get_by_role("button", name="Entrar").click()
    time.sleep(5)