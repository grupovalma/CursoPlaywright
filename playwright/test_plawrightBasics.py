from playwright.sync_api import Page


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
