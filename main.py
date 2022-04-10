import pandas as pd
import numpy as np
from pandas_datareader import data
from sklearn import svm
from sklearn import model_selection
from datetime import datetime
from Data_preprocess import read_data
from SVM_2 import model_svm
from Back_test import Backtest


if __name__ == "__main__":

    # Read data

    start_date = datetime(2015, 1, 1)
    end_date = datetime(2020, 12, 31)
    read_data('AAPL', start_date, end_date, 'AAPL.csv')
    read_data('^GSPC', start_date, end_date, 'SP500.csv')

    # Model Prediction
    m = 20
    n1 = 20
    n2 = 20
    index_data = pd.read_csv('./SP500.csv', index_col='Date')
    stock_data = pd.read_csv('./AAPL.csv', index_col='Date')
    index_price = pd.DataFrame(index_data.iloc[:, -1])
    stock_price = pd.DataFrame(stock_data.iloc[:, -1])
    label = model_svm(index_price, stock_price, m, n1, n2)

    # Model Back_test
    stock_data = stock_data.iloc[max(n1, n2):-m, :]
    df = pd.concat([stock_data, label], axis=1)
    df = df.dropna(axis=0)
    df = df.rename(columns={0: 'Predicted'})
    backtest1 = Backtest(df, m)
    backtest1.run()



