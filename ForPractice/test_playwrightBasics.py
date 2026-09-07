

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)   #Para que el browser no sea
    context = browser.new_context()                        # Nuevo tab privado
    page = context.new_page()                              # Objeto para colocar pagina web
    page.goto("https://rahulshettyacademy.com/")

#chromium headless mode, 1 single context (Resumido lo de arriba pero solo chromium, 90% veces)
def test_playwrightShortcut(page):
    page.goto("https://rahulshettyacademy.com/")

