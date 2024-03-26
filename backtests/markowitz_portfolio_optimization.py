from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
import yfinance as yf

from fuhnance.utils.portfolio_theory.markowitz_optimal_portfolio import markowitz_optimal_portfolio

# Import the backtrader platform
import backtrader as bt


# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.t = 0
        #breakpoint()

    def rebalance_portfolio(self, weights):
        print('='*50)
        print(self.t)
        print('='*50)
        for i, weight in enumerate(weights):
            if i >= len(self.datas):
                #self.close(self.datas[i])
                breakpoint()
                continue
            if self.getposition(self.datas[i]):
                self.close(self.datas[i])
            n_contracts = weight[0] * self.broker.cash * self.datas[i].close[0]
            self.buy(self.datas[i], n_contracts)


    def next(self):
        '''
        if not self.position:
            if self.t > 10:
                datas_results = []
                for i, e in enumerate(self.datas):
                    open = e.open.get(ago=0, size=self.t+1)
                    close = e.close.get(ago=0, size=self.t+1)
                    percent_returns = np.divide(np.subtract(close, open), open)
                    datas_results.append(percent_returns)
                datas_results = np.column_stack(datas_results)
                weights, _, _ = markowitz_optimal_portfolio(datas_results)
                self.rebalance_portfolio(weights)
                breakpoint()
        '''
        datas_results_list = []
        if self.t > 5:
            for i, e in enumerate(self.datas):
                open = e.open.get(ago=0, size=self.t+1)
                close = e.close.get(ago=0, size=self.t+1)
                percent_returns = np.divide(np.subtract(close, open), open)
                datas_results_list.append(percent_returns)
            datas_results = np.column_stack(datas_results_list).T
            weights, _, _ = markowitz_optimal_portfolio(datas_results)
            if self.t > 10:
                self.rebalance_portfolio(weights)
        self.t += 1



if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    stocks = ["AMZN", "MSFT", "INTC", "GOOG", 'TSLA', 'AAPL', 'HOG', 'QQQ', 'AMC', 'GME', 'META']
    #data = bt.feeds.PandasData(dataname=yf.download('SPY', '2015-07-06', '2021-07-01', auto_adjust=True))
    start = '2015-07-01'
    end = '2024-01-01'
    prices = {}
    for ticker in stocks:
        prices.update({ticker:bt.feeds.PandasData(dataname=yf.download(ticker, start, end, auto_adjust=True))})
        data = cerebro.adddata(prices[ticker])

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

