import time

from playwright.sync_api import Page, expect, Playwright

#Ver el video del video 37

##Lesson : Items: iphone X / Nokia Edge  -> Verify that 2 items are showing in cart.

def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2") #Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button").click()


    #Seleccionamos el TagName, en comun de todos los celulares.
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()

    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()

    page.get_by_text("Checkout").click()

    # Se uso .media-body, porque es un css selector
    # page.locator(".media-body") Este es el locator que vamos a usar en la assertion.

    # Assertion para ver que tenga dos elementos, porque eso es lo que cuenta. count."
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:           #Aqui estamos diciendo que newPage_info es una nueva pagina adentro:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"










