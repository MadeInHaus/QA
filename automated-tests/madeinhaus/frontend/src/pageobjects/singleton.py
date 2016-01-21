from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://madeinhaus.com")

try:
    element = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="app"]/div/div/div/div/span[3]')))
finally:
    driver.quit()

