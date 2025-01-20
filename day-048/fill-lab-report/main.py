from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a configure the Chrome webdriver and navigate to website
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

# Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Renan")
last_name.send_keys("Kindermann")
email.send_keys("renankin@live.com")

# Find "Sign Up" button and click on it
sign_up = driver.find_element(By.CLASS_NAME, value="btn")
sign_up.click()
