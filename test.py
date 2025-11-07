from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service("/snap/bin/geckodriver") 
driver = webdriver.Firefox(service=service)
driver.get("https://example.com")
print(driver.title)
driver.quit()