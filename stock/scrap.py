from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

os.environ['PATH'] += r"C:/Users/kamil/OneDrive/Pulpit/Stock"

driver = webdriver.Chrome()

driver.get('https://www.londonstockexchange.com')

wait = WebDriverWait(driver, 10)

def search(ticker):
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ccc-notify-buttons')))
    searchEL = driver.find_element_by_id('ccc-notify-accept')
    searchEL.send_keys(Keys.ENTER)
    searchEL = driver.find_element_by_id('quick-search-input')
    searchEL.send_keys(ticker)
    searchEL.send_keys(Keys.DOWN)
    searchEL.send_keys(Keys.ENTER)
    searchEL = driver.find_element_by_link_text('Explore more about this Instrument')
    searchEL.send_keys(Keys.ENTER)

search('UU')

time.sleep(15)
driver.quit()
