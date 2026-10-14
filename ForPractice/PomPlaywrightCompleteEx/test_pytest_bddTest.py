from pytest_bdd import given

from pageObjects.login import LoginPage
from utils.apiBase import APIUtils


@given('place item order with {username} and {password}')       #Esto viene del .feature
def place_item_order(playwright, username, password):
    user_credentials = {}
    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)


@given('the user us on landing page')
def user_on_landing_page(browserInstance):              #Se pone browserInstance aqui, porque esta en conftest y es universal
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()

