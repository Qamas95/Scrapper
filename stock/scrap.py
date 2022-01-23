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


def search_price():
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.google.com/search?q=' + financial_asset[0] + chosen_currency[0] + 'price')
    # def get_price():
    #     return driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/span[1]').text

    # print(get_price())


search_price()

time.sleep(2)
driver.quit()



# # os.environ['PATH'] += r"C:/Users/kamil/OneDrive/Pulpit/Stock"

# os.environ['PATH'] += r"D:/Users/kk/Pulpit/Stock/Scrapper"

# driver = webdriver.Chrome()

# driver.get('https://www.londonstockexchange.com')

# wait = WebDriverWait(driver, 10)

# def search(ticker):
#     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ccc-notify-buttons')))
#     searchEL = driver.find_element_by_id('ccc-notify-accept')
#     searchEL.send_keys(Keys.ENTER)
#     searchEL = driver.find_element_by_id('quick-search-input')
#     searchEL.send_keys(ticker)
#     searchEL.send_keys(Keys.DOWN)
#     searchEL.send_keys(Keys.ENTER)
#     searchEL = driver.find_element_by_link_text('Explore more about this Instrument')
#     searchEL.send_keys(Keys.ENTER)
#     print(get_last_price())

# def get_last_price():
#     return driver.find_element_by_xpath('/html/body/app-root/app-handshake/div/app-page-content/app-tab-nav/app-company-ticker/div/div/section/div[1]/div[2]/span[1]/div/span[1]/span').text


# search('UU')


# time.sleep(300)
# driver.quit()
