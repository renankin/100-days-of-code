from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

events_time = driver.find_elements(by=By.CSS_SELECTOR,
                                   value=".event-widget time")

events_name = driver.find_elements(by=By.CSS_SELECTOR,
                                   value=".event-widget ul a")

events = {
    num: {"time": events_time[num].text, "name": events_name[num].text} for num
    in range(len(events_time))
}

driver.quit()
