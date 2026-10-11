import json
import pytest
from playwright.sync_api import Playwright, expect
from pageObjects import dashboard
from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

# Json File -> util -> acces into test.
with open('data\\credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credential_list = test_data['user_credentials']

@pytest.mark.regression
@pytest.mark.parametrize('user_credentials', user_credential_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, page, user_credentials):
    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    #Create Order -> Order ID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userEmail, userPassword)

    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)
    ordersDetailsPage.VerifyOrderMessage()






