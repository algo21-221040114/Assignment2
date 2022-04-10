import pandas as pd
from sklearn import svm
from sklearn import model_selection


# The following model is conducted with stock and indices data,
# providing a better performance in prediction.


# Label
def target_data(d, m):
    y = []
    for i in range(d.shape[0]-m):
        if d.iloc[i, -1] < d.iloc[i+m, -1]:
            y.append(1)
        else:
            y.append(-1)
    y = pd.DataFrame(y)
    return y


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


# Model
def model_svm(index_price, stock_price, M, N1, N2):

    max_N = max(N1, N2)

    # Preprocess data
    y = target_data(stock_price, M).iloc[max_N:, :]
    df1 = price_volatility(stock_price, N1)
    df2 = momentum(stock_price, N1)
    df3 = price_volatility(index_price, N2)
    df4 = momentum(index_price, N2)
    x = pd.concat([df1, df2, df3, df4], axis=1)
    x = x.dropna(axis=0)
    x = x.iloc[:-M, :]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, train_size=0.7)

    # Model
    # clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
    clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
    clf.fit(x_train, y_train)
    # print(clf.predict(x))
    # print(clf.score(x_train, y_train))
    # print(clf.score(x_test, y_test))
    data_label = pd.DataFrame(clf.predict(x))
    data_label.index = stock_price.index[max_N:-M]
    return data_label

