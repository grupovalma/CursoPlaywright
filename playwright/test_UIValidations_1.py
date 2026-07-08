import time

from playwright.sync_api import Page, expect


#Nokia Edge -- iphone X Verify 2 items are showing in cart
def test_UIVAlidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # Lo mas importante de la leccion
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    time.sleep(2)
    #Assertion dos elementos dentro de media body, porque fue Nokia y Iphone
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(3)



def testchidlWindowHandle(page:Page):
    #Pagina madre
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #Pagina hija
    with page.expect_popup() as newPage_info:
        #page.locator(".blinkingText").click()
        #En el curso solo habia un locator, asi que tuve que usar este para seleccionar el primero. First
        page.locator(".blinkingText").first.click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        #print(text)
        #All text: Please email us at mentor@rahulshettyacademy.com with below template to receive response
        #A partir de at, es como si se convirtiera en una lista
        words = text.split("at")
        email = words[1].strip().split(" ")[0]

        assert email == "mentor@rahulshettyacademy.com"









