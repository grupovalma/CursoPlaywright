import time

from playwright.sync_api import Page, expect, Playwright

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v151.fed_cm import click_dialog_button
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.common.keys import Keys
#Waits
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_free(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    username = page.get_by_label("Username:").fill("rahulshettyacademy")
    password = page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.locator( "#signInBtn").click()

    iphonePproduct = page.locator("app-card").filter(has_text="iphone X")
    iphonePproduct.get_by_role("button").click()

    blackberryProduct = page.locator("app-card").filter(has_text="Blackberry")
    blackberryProduct.get_by_role("button").click()

    checkOutButton = page.get_by_text("Checkout").click()

    #Recordar que es una clase
    expect(page.locator(".media-body")).to_have_count(2)




def test_selenium_free():

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 50)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    username = wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("rahulshettyacademy")
    password = wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Learning@830$3mK2")

    comboBox1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@class='form-control']")))
    intracombo = Select(comboBox1)
    intracombo.select_by_value("consult")

    I_AgreeCheck = wait.until(EC.element_to_be_clickable((By.ID, "terms"))).click()
    terms_and_cont = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='text-white termsText']"))).click()
    singInButton = wait.until(EC.element_to_be_clickable((By.ID, "signInBtn"))).click()


    phone_selection = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//app-card[@class='col-lg-3 col-md-6 mb-3']")))

    for i in phone_selection:
        phone_brand = i.find_element(By.XPATH, ".//h4/a").text
        #print(phone_brand)

        if phone_brand == "iphone X":
            add_button = i.find_element(By.XPATH, ".//button[text()='Add ']")
            add_button.click()

        if phone_brand == "Blackberry":
            add_button = i.find_element(By.XPATH, ".//button[text()='Add ']")
            add_button.click()
            time.sleep(5)
            break

    checkOutButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link btn btn-primary']"))).click()

    totalProducts = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='media-body']")))

    assert len(totalProducts) >= 2

