import backtrader as bt
import pandas as pd
from datetime import datetime


# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' 提供记录功能'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 引用到输入数据的close价格
        self.dataclose = self.datas[0].close

    def next(self):
        # 目前的策略就是简单显示下收盘价。
        self.log('Close, %.2f' % self.dataclose[0])


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    # 增加一个策略
    cerebro.addstrategy(TestStrategy)

    # 获取数据
    stock_hfq_df = pd.read_csv('./AAPL.csv', index_col='Date', parse_dates=True)
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2020, 12, 31)
    data = bt.feeds.PandasData(dataname=stock_hfq_df, fromdate=start_date, todate=end_date)  # 加载数据
    cerebro.adddata(data)  # 将数据传入回测系统

    cerebro.broker.setcash(100000.0)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())