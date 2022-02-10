# pip install alpha_vantage
# pip install openpyxl
# pip3 install openpyxl
# pip install pandas

from importlib.metadata import metadata
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import openpyxl
from openpyxl import Workbook, load_workbook



api_key = 'JZ1M5CMS2JI0RMF8'
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
print(data)

# i = 1
# while i==1:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#    data.to_excel(r'C:\Users\kamil\OneDrive\Pulpit\Stock\StockPrices\stock\output.xlsx', index = False, header=True)
#    time.sleep(15)

close_data = data['4. close']
percentage_change = close_data.pct_change()

print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.0004:
    print("MSFT Alert:" + str(last_change))