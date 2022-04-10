from pandas_datareader import data
from datetime import datetime


#  Read data
def read_data(stock_name, start, end, file_name):
    df = data.DataReader(stock_name, 'yahoo', start, end)
    df.to_csv(file_name, sep=',', header=True, index=True)






