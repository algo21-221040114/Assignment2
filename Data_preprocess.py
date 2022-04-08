import pandas as pd
import numpy as np
from pandas_datareader import data
from sklearn import svm
from sklearn import model_selection
import datetime


#  Read data

start_date = datetime.datetime(2015, 1, 1)
end_date = datetime.datetime(2020, 12, 31)

# index indicator

df = data.DataReader('^GSPC', 'yahoo', start_date, end_date)
df.to_csv('SP500.csv', sep=',', header=True, index=True)

# stock indicator

stock = data.DataReader('AAPL', 'yahoo', start_date, end_date)
stock.to_csv('AAPL.csv', sep=',', header=True, index=True)





