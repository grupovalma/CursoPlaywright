import time
from os import name
from zoneinfo import reset_tzpath

import pytest
from playwright.sync_api import Page, Playwright, expect

def test_Siga(page:Page):
    contentFrame = page.frame_locator("#contentFrame")
    leftFrame = page.frame_locator("#leftFrame")
    popupFrame1 = contentFrame.frame_locator("#popupFrame1")
    popupFrame2 = popupFrame1.frame_locator("#popupFrame2")

    page.goto("https://demo.aduanas.gob.do/")

    contentFrame.locator("#ctl00_ContentsHolder_txtAccount").fill("00000293")
    contentFrame.locator("#ctl00_ContentsHolder_txtPassword").fill("00")
    contentFrame.locator("#ctl00_ContentsHolder_btnLogin").click()

    contentFrame.locator("#jqxScrollBtnDownverticalScrollBarctl00_ContentsHolder_lstSelector").click()
    contentFrame.locator("#jqxScrollBtnDownverticalScrollBarctl00_ContentsHolder_lstSelector").click()
    contentFrame.locator("#jqxScrollBtnDownverticalScrollBarctl00_ContentsHolder_lstSelector").click()
    contentFrame.locator("#jqxScrollBtnDownverticalScrollBarctl00_ContentsHolder_lstSelector").click()
    contentFrame.locator("#jqxScrollBtnDownverticalScrollBarctl00_ContentsHolder_lstSelector").click()

    contentFrame.get_by_role("option", name="Empresa Naviera").click()
    contentFrame.locator("#ctl00_ContentsHolder_btnOK").click()

    leftFrame.get_by_role("link", name="Carga de Importación", exact=True).click()
    leftFrame.get_by_role("link", name="Manifiesto General", exact=True).click()

    contentFrame.get_by_role("button", name="Nuevo").click()
    contentFrame.locator("#ctl00_ContentsHolder_txtVoyageNo").fill("4321")
    contentFrame.locator("#ctl00_ContentsHolder_cboTransportType").select_option("IG1007-S")
    contentFrame.locator("img[onclick=\"SearchPopup('ViaEntrance', 'Destination');\"]").click()

    popupFrame1.locator("#cboAreaCode").select_option(value="10030")

    popupFrame1.locator("img[onclick=\"fn_country();\"]").click()

    field1 = popupFrame2.locator("#txtCountryCode")
    field1.click()
    field1.fill("214")
    popupFrame2.locator(".listTd").click()


    time.sleep(2)


