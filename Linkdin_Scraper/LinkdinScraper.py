from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup Firefox
options = Options()
# options.add_argument("--headless")  # Uncomment to run in background
options.add_argument("--disable-gpu")

service = Service("/snap/bin/geckodriver") # Path to GeckoDriver (adjust if necessary)
driver = webdriver.Firefox(service=service, options=options)

# Login to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("your_email_here")
driver.find_element(By.ID, "password").send_keys("your_password_here")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Load profile URLs
with open("profiles.txt", "r") as f:
    urls = [line.strip() for line in f.readlines()]

data = [] # and empty list to hold scraped data

# Scrape each profile
for url in urls:
    driver.get(url)
    time.sleep(5)

    name = driver.find_element(By.TAG_NAME, "h1").text
    headline = driver.find_element(By.CLASS_NAME, "text-body-medium").text

    data.append({
        "Name": name,
        "Headline": headline,
        "URL": url
    })

driver.quit()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
print("Scraping complete.")
