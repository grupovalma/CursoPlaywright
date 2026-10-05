import json
import pytest
from playwright.sync_api import Playwright, expect
from ForPractice.PytestandPlaywright.pageObjects import dashboard
from ForPractice.PytestandPlaywright.pageObjects.dashboard import DashboardPage
from ForPractice.PytestandPlaywright.pageObjects.login import LoginPage
from utils.apiBase import APIUtils

# Json File -> util -> acces into test.
with open('ForPractice/PytestandPlaywright/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credential_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credential_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    #Create Order -> Order ID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    #Login
    loginPage = LoginPage(page)
    loginPage.navigate()
    dashboardPage = loginPage.login(userEmail, userPassword)
    #Dashboard Page
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)

    ordersDetailsPage.VerifyOrderMessage()






