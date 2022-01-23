from http import server
from lib2to3.pgen2 import driver
from locale import currency
from multiprocessing.sharedctypes import Value
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


def search_price():
        wait = WebDriverWait(driver, 10)
        driver.get('https://www.google.com/search?q=' + financial_asset[0] + chosen_currency[0] + 'price')
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/span/div/div/div/div[3]/button[2]/div').click()
        value = driver.find_element_by_class_name('pclqee').text
        print(value)

search_price()

time.sleep(2)
driver.quit()



