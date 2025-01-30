from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

load_dotenv()

LINKEDIN_USERNAME = os.environ.get("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start webdriver with Chrome and access Cookie website
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4137431681"
           "&f_AL=true&geoId=90009497&keywords=data%20scientist&origin"
           "=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Locate Sign in button and use ActionChains to avoid "element not
# interactable" exception
sign_in = driver.find_element(By.CSS_SELECTOR, "div.sign-in-modal button")
ActionChains(driver).move_to_element(sign_in).click(sign_in).perform()

# Fill out username
email_field = driver.find_element(By.NAME, value="session_key")
ActionChains(driver).move_to_element(email_field).click(
    email_field).send_keys(LINKEDIN_USERNAME).perform()

# Fill out password and log in
password_field = driver.find_element(By.NAME, value="session_password")
ActionChains(driver).move_to_element(password_field).click(
    password_field).send_keys(LINKEDIN_PASSWORD).perform()
ActionChains(driver).move_to_element(password_field).click(
    password_field).send_keys(Keys.ENTER).perform()

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
all_listings = driver.find_elements(by=By.CLASS_NAME,
                                    value="job-card-container--clickable")

# Save Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Save job
        save_button = driver.find_element(By.CLASS_NAME,
                                          value="jobs-save-button")
        save_button.click()

        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME,
                                           value="artdeco-toast-item__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()
