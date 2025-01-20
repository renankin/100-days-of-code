from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create driver and navigate to Wikipedia
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find element by CSS selector
article_count = driver.find_element(By.CSS_SELECTOR,
                                    value="#articlecount a")

# Find element by link and click on it
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
# driver.quit()
