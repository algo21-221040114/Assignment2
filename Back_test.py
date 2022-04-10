import numpy as np
import pandas as pd


class Backtest:

    def __init__(self, dataset, hold_period):
        self.ret = []
        self.cumulative_ret = [1]
        self.position = 0
        self.cost = 0
        self.close = list(dataset['Close'])
        self.signal = pd.DataFrame(dataset['Predicted'])
        self.test_length = self.signal.shape[0]
        self.hold_length = hold_period

    def first_day_trade(self):
        self.position = self.signal.iloc[0, 0]
        self.cost = self.close[1] * self.position
        self.cumulative_ret.append(1)
        if self.signal.iloc[0, 0] == 1:
            print(self.signal.index[0] + ' Buy order')
        else:
            print(self.signal.index[0] + ' Sell order')
        print('Exe price: ' + str(self.close[1]))

    def trade(self):
        for i in range(0, self.test_length-1, self.hold_length):
            if self.position == 1:
                self.ret.append(self.close[i]/self.cost-1)
                self.cumulative_ret.append(self.cumulative_ret[-1] * self.close[i]/self.cost)
                print(self.signal.index[i] + ' Sell order')
                print('Exe price: ' + str(self.close[i]))
            else:
                self.ret.append(abs(self.cost) / self.close[i] - 1)
                self.cumulative_ret.append(self.cumulative_ret[-1] * abs(self.cost) / self.close[i])
                print(self.signal.index[i] + ' Buy order')
                print('Exe price: ' + str(self.close[i]))
            if self.signal.iloc[i, 0] == 1:
                print(self.signal.index[i] + ' Buy order')
                print('Exe price: ' + str(self.close[i+1]))
                self.position = 1
                self.cost = self.close[i+1] * self.signal.iloc[i, 0]
            else:
                print(self.signal.index[i] + ' Sell order')
                print('Exe price: ' + str(self.close[i+1]))
                self.position = -1
                self.cost = self.close[i+1] * self.signal.iloc[i, 0]

    def annulized(self):
        a = self.cumulative_ret[-1]
        print(a)
        annualized_ret = a**(252/self.test_length)
        print('Annualized return is ' + str(annualized_ret))

    def sharpe(self):
        a = self.cumulative_ret[-1]
        mu = a ** (252 / self.test_length)-1 - 0.035
        sigma = np.std(self.ret)*np.sqrt(252/self.hold_length)
        print('Sharpe ratio is ' + str(mu/sigma))

    def maxdrawdown(self):
        mdd = -1
        for i in range(len(self.cumulative_ret)-1):
            for j in range(i+1, len(self.cumulative_ret)):
                if self.cumulative_ret[j] < self.cumulative_ret[i]:
                    mdd = max(mdd, 1-self.cumulative_ret[j]/self.cumulative_ret[i])
                else:
                    break
        print('Max Drawdown is ' + str(mdd))

    def run(self):
        Backtest.first_day_trade(self)
        Backtest.trade(self)
        Backtest.annulized(self)
        Backtest.sharpe(self)
        Backtest.maxdrawdown(self)








