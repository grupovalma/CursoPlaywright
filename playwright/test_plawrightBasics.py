import time

from playwright.sync_api import Page, expect


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

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy") #En esta parte seleccionamos el label, encima del campo
    page.get_by_label("Password:").fill("Learning@830$3mK2t")
    page.get_by_role("combobox").select_option("consult") #Combobox verificamos todas las opciones, luego seleccionamos el value. Si hay mas combobox, se elige por indice
    page.get_by_role("link", name="terms and conditions").click()
    #page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check()  #Aqui seleccionamos por I, osea #, y en vez de click, usamos check
    page.get_by_role("button", name="Sign In").click()

    #Incorrect username/password. Assertion example
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()

    #time.sleep(5)
