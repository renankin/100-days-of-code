from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium.common import (ElementClickInterceptedException,
                             NoSuchElementException)
import time

load_dotenv()
SIMILAR_ACCOUNT = "chefsteps"
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # input credentials and log in
        self.driver.find_element(
            By.CSS_SELECTOR,
            "input[aria-label='Phone number, username or email address']"
        ).send_keys(INSTAGRAM_USERNAME)
        self.driver.find_element(
            By.CSS_SELECTOR, "input[aria-label='Password']"
        ).send_keys(INSTAGRAM_PASSWORD)
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # click pop-up
        pop_up = self.driver.find_element(By.XPATH, "//div[text()='Not now']")
        if pop_up:
            pop_up.click()

    def follow(self):
        follow_buttons = self.driver.find_elements(
            By.XPATH, "//button[.//div[text()='Follow']]")

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                try:
                    self.driver.find_element(By.XPATH,
                                             "//button[text()='OK']").click()
                except (ElementClickInterceptedException,
                        NoSuchElementException):
                    continue

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        self.driver.find_element(By.XPATH,
                                 "//a[contains(text(), 'followers')]").click()

        time.sleep(2)
        modal = self.driver.find_element(
            By.XPATH,
            "/html/body/div[5]/div[2]/div/div/div[1]"
            "/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        for _ in range(10):
            # execute JavaScript to scroll down pop-up
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
