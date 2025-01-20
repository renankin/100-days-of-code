from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start webdriver with Chrome and access Cookie website
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Define times
timeout = time.perf_counter() + 300
stores_stopwatch = time.perf_counter() + 5

while time.perf_counter() < timeout:
    # Find elements
    cookie = driver.find_element(By.ID, value="cookie")
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    money = driver.find_element(By.ID, value="money")

    # Click on Cookie and store current money
    cookie.click()
    current_money = int(money.text)

    # Buy most expensive upgrade in stores
    if time.perf_counter() > stores_stopwatch:
        for element in reversed(store):
            if element.text is not element.text:
                price_string = element.text.replace(" ", "").split("-")[1]
                price_integer = int(price_string.replace(",", ""))

                if current_money > price_integer:
                    element.click()
                    stores_stopwatch += 5
                    break
