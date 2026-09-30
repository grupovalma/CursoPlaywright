#Video 54, Mouy importante se trata de MOCKING o interceptar la respuesta antes de tiempo con algo falso.
#-> api call from browser -> api call contact server return back response to browser

import time

from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}   #Mensaje que devuelve el API en menu Orders, cuando no hay ordenes. Fijado aqui para que lo devuelva falsamente.

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("#userEmail").fill("grupovalma@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("NewPassword01")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    order_text = page.locator(".mt-4").text_content()
    print(order_text)

