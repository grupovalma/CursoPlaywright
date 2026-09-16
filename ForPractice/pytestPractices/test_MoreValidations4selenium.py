#Para estudiar Selenium muy importante.


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Obtener índice de la columna Price
    headers = driver.find_elements(By.XPATH, "//th")
    price_col_index = next(
        i for i, h in enumerate(headers)
        if h.text.strip() == "Price"
    )

    # Obtener fila de Rice
    rice_row = driver.find_element(
        By.XPATH,
        "//tr[td[contains(text(),'Rice')]]"
    )

    price = rice_row.find_elements(By.TAG_NAME, "td")[price_col_index].text

    assert price == "37"
    print("Test Passed!")

finally:
    driver.quit()