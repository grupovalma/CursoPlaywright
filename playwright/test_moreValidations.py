import time

from playwright.sync_api import Playwright, Page, expect


def test_UIChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    #al Inspeccionar, aparece una opcion se llama placeholder, esta vacio
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    #pulsando el boton Hide, tomamos la opcion boton de playwright y el value para el nombre
    page.get_by_role("button", name="Hide").click()
    #que lo busque si, ya esta hidden?
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #2da Parte: Alert Boxes
    #El lambda, es una funcion sin nombre anonima, y todas las alertas que encuentra, va a decir aceptar.
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

def test_UIChecksIFrame(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    #El iframe tiene id: por esp se le puso el numeral # a courses-iframe
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    #Assertion
    expect(pageFrame.locator("body")).to_contain_text(" Happy Subscibers!")








