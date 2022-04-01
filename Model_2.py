import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import model_selection


def target_data(d, m):
    y = []
    for i in range(m, d.shape[0]):
        if d.iloc[i, -1] > d.iloc[i-m, -1]:
            y.append(1)
        else:
            y.append(-1)
    y = pd.DataFrame(y)
    return y

# Hyperparameter
N1 = 5
N2 = 5
M = 5

#  Preprocess data
index_data = pd.read_csv('./SP500.csv', index_col='Date')
stock_data = pd.read_csv('./AAPL.csv', index_col='Date')
index_price = pd.DataFrame(index_data.iloc[:, -1])
stock_price = pd.DataFrame(stock_data.iloc[:, -1])


# Technical indicator
def price_volatility(price, n):
    index = []
    for t in range(n, price.shape[0]):
        percentage_change = 0
        for i in range(t-n+1, t+1):
            percentage_change += (price.iloc[i, 0]/price.iloc[i-1, 0]-1)
        index.append(percentage_change/n)
    index = pd.DataFrame(index)
    return index


def momentum(price, n):
    index = []
    label = target_data(price, 1)
    for t in range(n, price.shape[0]):
        volume = 0
        for i in range(t-n, t):
            volume += label.iloc[i, 0]
        index.append(volume/n)
    index = pd.DataFrame(index)
    return index


y = target_data(stock_data, M).iloc[1:, :]
df1 = price_volatility(stock_price, N1)
df2 = momentum(stock_price, N1)
df3 = price_volatility(index_price, N2)
df4 = momentum(index_price, N2)
x = pd.concat([df1, df2, df3, df4], axis=1)
x = x.iloc[:-1, :]
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, train_size=0.7)

# Model
# clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
clf.fit(x_train, y_train)

# Result
print(clf.score(x_train, y_train))  # 精度
print(clf.score(x_test, y_test))
