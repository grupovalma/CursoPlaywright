#Video 41
import time

from playwright.sync_api import Page, expect, Playwright
from selenium.webdriver.common.fedcm import dialog


def test_UiChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # Tipo de almacenamiento al inspeccionar
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    #Con ID:
    #page.locator("#hide-textbox").click()
    #Ejemplo expuesto:
    page.get_by_role("button", name="Hide").click() #name = value, recordar.
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alerts Boxes Vide 42
    page.locator("#name").fill("Americo")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)



