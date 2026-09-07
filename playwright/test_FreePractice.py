import time

from playwright.sync_api import Page, Playwright, expect

def test_personal(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.aduanas.gob.do/")
    contentFrame = page.frame_locator("#contentFrame")
    contentFrame.get_by_role("textbox", name="#ctl00_ContentsHolder_txtAccount").fill("00000293")
    time.sleep(10)