#Video 41 - 43, em test_Tables video 44 y 45
import time

from playwright.sync_api import Page, expect, Playwright



def test_UiChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # Tipo de almacenamiento al inspeccionar
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    #Con ID:
    #page.locator("#hide-textbox").click()
    #Ejemplo expuesto:
    page.get_by_role("button", name="Hide").click() #name = value, recordar.
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Reload").click()
    time.sleep(5)

    #Alerts Boxes Vide 42
    page.locator("#name").fill("Americo")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    # time.sleep(5)

    #Frame Handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    #Body, es para verificar toda la pagina
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")


def test_Tables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index;
            print(f"Price Column valye is {priceColValue}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")






