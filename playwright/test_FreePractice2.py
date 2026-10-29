import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.aduanas.gob.do/")
    page.locator("#contentFrame").content_frame.locator("#ctl00_ContentsHolder_txtAccount").click()
    page.locator("#contentFrame").content_frame.locator("#ctl00_ContentsHolder_txtAccount").fill("00000293")
    page.locator("#contentFrame").content_frame.locator("#ctl00_ContentsHolder_txtPassword").fill("11")
    page.locator("#contentFrame").content_frame.locator(".jqx-reset.jqx-reset-custom-scheme.jqx-icon-arrow-down").click()
    page.locator("#contentFrame").content_frame.locator(".jqx-reset.jqx-reset-custom-scheme.jqx-icon-arrow-down").click()
    page.locator("#contentFrame").content_frame.locator(".jqx-reset.jqx-reset-custom-scheme.jqx-icon-arrow-down").click()
    page.locator("#contentFrame").content_frame.locator(".jqx-reset.jqx-reset-custom-scheme.jqx-icon-arrow-down").click()
    page.locator("#contentFrame").content_frame.get_by_role("option", name="Empresa Naviera").locator("span").click()
    page.locator("#contentFrame").content_frame.get_by_role("link", name="OK").click()
    page.locator("#leftFrame").content_frame.get_by_role("link", name="Carga de Importación", exact=True).click()
    page.locator("#leftFrame").content_frame.get_by_role("link", name="Manifiesto General", exact=True).click()
    page.locator("#contentFrame").content_frame.get_by_role("button", name="Nuevo").click()
    page.locator("#contentFrame").content_frame.locator("#ctl00_ContentsHolder_cboTransportType").select_option("IG1007-S")
    page.locator("#contentFrame").content_frame.locator("#ctl00_ContentsHolder_txtVoyageNo").click()
    page.locator("#contentFrame").content_frame.locator("#ctl00_ContentsHolder_txtVoyageNo").fill("123456")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
