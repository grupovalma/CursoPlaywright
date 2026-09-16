import time
from shlex import split

from playwright.sync_api import Page, Playwright, expect


def test_libre(page: Page):
    page.goto("https://demo.aduanas.gob.do/")
    contentFrame = page.frame_locator("#contentFrame")
    leftFrame = page.frame_locator("#leftFrame")
    contentFrame.locator("#ctl00_ContentsHolder_txtAccount").fill("00000293")
    contentFrame.locator("#ctl00_ContentsHolder_txtPassword").fill("00")
    contentFrame.locator(".btnLoginC").click()

    contentFrame.locator("#ctl00_ContentsHolder_lstSelector").filter(has_text="Agente de Aduanas").click()
    contentFrame.locator("#ctl00_ContentsHolder_btnOK").click()
    leftFrame.get_by_text("Carga de Importación").click()
    leftFrame.locator("")
    time.sleep(5)











