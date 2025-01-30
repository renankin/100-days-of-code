from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.keys import Keys

load_dotenv()

FACEBOOK_USERNAME = os.environ.get("FACEBOOK_USERNAME")
FACEBOOK_PASSWORD = os.environ.get("FACEBOOK_PASSWORD")

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# start webdriver with Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://tinder.com/")

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# accept cookies and log in
driver.find_element(By.CSS_SELECTOR, ".D\\(f\\)--ml button").click()
driver.find_element(By.LINK_TEXT, "Log in").click()

# login to facebook
driver.find_element(By.CSS_SELECTOR,
                    "button[aria-label='Login with Facebook']").click()

# changing the handles to access login page
time.sleep(2)
for handle in driver.window_handles:
    if handle != main_page:
        # change the control to signin page
        login_page = handle
        driver.switch_to.window(login_page)

# Sign in on the pop-up page
print(f"switching to {driver.title} window..")
driver.find_element(By.ID, "email").send_keys(FACEBOOK_USERNAME)
password = driver.find_element(By.ID, "pass")
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR,
                    "div[aria-label='Continue as Roger'").click()

# Move back to main page and accept conditions
driver.switch_to.window(main_page)
print(f"switching to {driver.title} window..")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[aria-label='Allow'").click()
driver.find_element(By.CSS_SELECTOR,
                    "button[aria-label='I’ll give it a miss'").click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        action_buttons = driver.find_elements(
            By.CSS_SELECTOR,
            ".gamepad-button-wrapper .Lts\\(\\$ls-s\\)"
        )
        # Click Nope Button
        action_buttons[1].click()

    except ElementClickInterceptedException:
        print("element blocked by pop-up")
        try:
            favourites_popup = driver.find_element(By.CSS_SELECTOR,
                                                   ".c1p6lbu0.D\\(b\\).Mx\\("
                                                   "a\\)")
            favourites_popup.click()

        except NoSuchElementException:
            time.sleep(2)
