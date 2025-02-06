from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

# scraping Zillow website with Beautiful Soup
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 "
                  "Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9",
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/",
                        headers=header)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

all_addresses = soup.find_all(name="address")
addresses = [address.text.strip() for address in all_addresses]

# format address
formatted_addresses = []
for address in addresses:
    last_addresses = address.split(",")[-3:]
    formatted_address = ""
    for sub_address in last_addresses:
        if "|" in sub_address:
            sub_address = sub_address.split("|")[1]
        if "CA" not in sub_address:
            sub_address = sub_address.strip() + ", "
        formatted_address += sub_address
    formatted_addresses.append(formatted_address)

all_links = soup.find_all(name="a", class_="property-card-link")
links = [link.get("href") for link in all_links]

all_prices = soup.find_all(name="span",
                           attrs={"data-test": "property-card-price"})
prices = [price.text.split("+")[0].split("/")[0] for price in all_prices]

# filling out google form with Selenium
load_dotenv()
form_link = os.environ.get("GOOGLE_FORM_LINK")

# initialise webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(form_link)
driver.implicitly_wait(3)

# fill out form with property data
for n_property in range(len(formatted_addresses)):
    form_inputs = driver.find_elements(
        By.XPATH,
        value="//div[div/text() = 'Sua resposta']/input"
    )

    time.sleep(5)  # wait page to load to interact
    form_inputs[0].send_keys(formatted_addresses[n_property])
    form_inputs[1].send_keys(prices[n_property])
    form_inputs[2].send_keys(links[n_property])

    driver.find_element(By.CSS_SELECTOR, "div[aria-label='Submit']").click()
    driver.find_element(By.LINK_TEXT, "Enviar outra resposta").click()
