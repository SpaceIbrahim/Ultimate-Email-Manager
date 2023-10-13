from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service("chrome webdriver/chromedriver"), options=options)

driver.get("https://www.google.com")