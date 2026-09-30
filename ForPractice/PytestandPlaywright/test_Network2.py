#Video 5, Muy importante se trata de MOCKING 2 parte
#-> api call from browser -> api call contact server return back response to browser
#Prueba donde te redirecciona con un mock que te lleva a una pagina de con un usuario que no es el correcto, y por tanto no te deja ver el producto. Asi que es
#una prueba de Seguridad, cuando intentas entrar a un producto que no te corresponde.
import time

from playwright.sync_api import Page

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/6ab81b962be7a4bc2b712281")

def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.locator("#userEmail").fill("grupovalma@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("NewPassword01")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(2)
    message = page.locator(".blink_me").text_content()
    time.sleep(2)
    print(message)

