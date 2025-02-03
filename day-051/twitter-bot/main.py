import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CSS_SELECTOR, ".start-button > a").click()

        # Wait for speed test to finish
        time.sleep(60)
        self.down = float(self.driver.find_element(By.CLASS_NAME,
                                                   "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME,
                                                 "upload-speed").text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        # signing in to Twitter
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        username_field = self.driver.find_element(
            By.CSS_SELECTOR,
            "input[autocomplete='username']")
        username_field.send_keys(TWITTER_USERNAME)
        username_field.send_keys(Keys.ENTER)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        # posting the message
        post_field = self.driver.find_element(
            By.CSS_SELECTOR,
            "div[aria-label='Post text'] span")
        tweet = (f"Hey Internet Provider, why is my internet speed "
                 f"{self.down}down/{self.up}up when I pay "
                 f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
        post_field.send_keys(tweet)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[data-testid='tweetButtonInline'").click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
else:
    print("Internet speed within promised values.")
