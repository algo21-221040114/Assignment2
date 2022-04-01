import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import model_selection


def target_data(d):
    y = []
    for i in range(1, d.shape[0]):
        if d.iloc[i, -1] > d.iloc[i - 1, -1]:
            y.append(1)
        else:
            y.append(-1)
    y = pd.DataFrame(y)
    return y


#  Preprocess data
df = pd.read_csv('./SP500.csv', index_col='Date')
stock_data = pd.read_csv('./AAPL.csv', index_col='Date')
y = target_data(stock_data)
x = stock_data.apply(lambda a: (a-np.min(a))/(np.max(a)-np.min(a)))
x = x.iloc[:-1, :]
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, train_size=0.7)

# Model
clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
# clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
clf.fit(x_train, y_train)

# Result
print(clf.score(x_train, y_train))  # 精度
y_hat = clf.predict(x_train)
print(clf.score(x_test, y_test))
y_hat = clf.predict(x_test)
# only with stock data,
# 0.5606060606060606
# 0.5110132158590308
# rbf
# 0.5852272727272727
# 0.5066079295154186
