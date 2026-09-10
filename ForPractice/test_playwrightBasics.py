import time

from playwright.sync_api import Page   ## Esto es para la segunda resumida def test_playwrightShortcu

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)   #Para que el browser no sea
    context = browser.new_context()                        # Nuevo tab privado
    page = context.new_page()                              # Objeto para colocar pagina web
    page.goto("https://rahulshettyacademy.com/")

#chromium headless mode, 1 single context (Resumido lo de arriba pero solo chromium, 90% veces)
def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")


def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # Label /
    page.get_by_label("Username:").fill("rahulshettyacademy")
    #Label /  para esto el label debe tener for = "ej1" igual al input id = "ej1", o dentro del label debe estar el input
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    #Drop down (Combobox)/  encima te ensana todas las opciones role(combobox), debe ser unico, seleccionamos value del dropdown
    page.get_by_role("combobox").select_option("teach")
    #Links / Tomamos el nombre del xpath
    page.get_by_role("link", name="terms and conditions").click()
    ##CSS Selectors
    # 1) PARA ID = #IDNAME, PARA 2) CLASSName = .Nombredelaclase, 3) tagname
    #Locator / Seleccionamos del punto anterior el ID
    page.locator("#terms").check()
    #Boton / usé el valor de value
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)






