from lib2to3.pgen2 import driver
from locale import currency
from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

os.environ['PATH'] += r"D:/Users/kk/Pulpit/Stock/Scrapper"
driver = webdriver.Chrome()


financial_asset = ['BTC', 'ETH']
chosen_currency = ['EUR', 'USD', 'PLN']


driver.get('https://www.google.com/search?q=' + financial_asset[0] + chosen_currency[0] + 'price')

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
    print(get_last_price())

def get_last_price():
    return driver.find_element_by_xpath('/html/body/app-root/app-handshake/div/app-page-content/app-tab-nav/app-company-ticker/div/div/section/div[1]/div[2]/span[1]/div/span[1]/span').text


search('UU')


time.sleep(300)
driver.quit()
