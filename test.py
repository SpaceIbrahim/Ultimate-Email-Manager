from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
import dotenv

dotenv.load_dotenv()
GMAIL = os.getenv('GMAIL')
PASSWORD = os.getenv('PASSWORD')

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service("chrome webdriver/chromedriver"), options=options)

driver.get("https://www.gmail.com")
driver.implicitly_wait(3)


loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
loginBox.send_keys(GMAIL)

