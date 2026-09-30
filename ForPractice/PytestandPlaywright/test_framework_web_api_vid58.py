import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

# Json File -> util -> acces into test.
with open('ForPractice/PytestandPlaywright/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credential_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credential_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Create Order - Creamos el producto a traves del API en apiBase.py, tambien se imprime
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    #Login - Entramos a la pagina, para verificar el producto por UI
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("grupovalma@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("NewPassword01")
    page.get_by_role("button", name="login").click()

    #Entramos a las ordenes por UI
    page.get_by_role("button", name="ORDERS").click()

    #Orders History Page -> order is present  , Verificamos por UI si el producto fue insertado por el API, y hacemos un Assertion
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()





