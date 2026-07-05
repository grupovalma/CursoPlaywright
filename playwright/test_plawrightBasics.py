import time

from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import context


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#Segunda clase, forma simplificada, solo chromium y headless, no tiene comandos para poder aceptar comandos, hay que bajar: from playwright.sync_api import Page
# y ponerle (page:Page), no habre sin headless.

def test_playwrightShortCut(page:Page):
    page.goto("https://rahulshettyacademy.com")

## En la flechita verde, puede darle click derecho seleccionar Modify Run configuration: En additional arguments
## Puedes escribir --headless, y corre abriendo el browser sin headless.
## Desde la consola sin headless ::: pytest .\test_plawrightBasics.py::test_playwrightShortCut --headed

#-- #terms(ID), .text-info(Class, el punto), tagName(x)
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy") #En esta parte seleccionamos el label, encima del campo
    page.get_by_label("Password:").fill("Learning@830$3mK2t")
    page.get_by_role("combobox").select_option("consult") #Combobox verificamos todas las opciones, luego seleccionamos el value. Si hay mas combobox, se elige por indice
    page.get_by_role("link", name="terms and conditions").click()
    #page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check()  #Aqui seleccionamos por I, osea #, y en vez de click, usamos check
    page.get_by_role("button", name="Sign In").click()

    #Assertion example  -- TEXTO -- Incorrect username/password ->
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()


#Este es para abrir despde firefox, tuvimos que igualar Playwright.
def test_firefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2t")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect username/password")).to_be_visible()


