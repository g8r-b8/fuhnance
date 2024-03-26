import matplotlib.pyplot as plt

'''
import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
'''

import numpy as np
import argparse

from fuhnance.utils.toys.gen_toy_portfolio import gen_toy_returns, gen_toy_portfolio_returns
from fuhnance.utils.portfolio_theory.markowitz_optimal_portfolio import markowitz_optimal_portfolio

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-pr', '--plot_returns', dest='plot_returns', action='store_true')
    parser.add_argument('-pmb', '--plot_markowitz_bullet', dest='plot_markowitz_bullet', action='store_true')
    parser.add_argument('-pmop', '--plot_markowitz_optimal_portfolio', dest='plot_markowitz_optimal_portfolio', action='store_true')
    parser.add_argument('-a', '--assets', dest='assets', type=int, default=4)
    parser.add_argument('-p', '--portfolios', dest='portfolios', type=int, default=500)
    parser.add_argument('-o', '--observations', dest='observations', type=int, default=1000)
    args = parser.parse_args()
    return args

def plot_returns(returns):
    fig, ax = plt.subplots()
    plt.plot(returns.T, alpha=.4)
    plt.xlabel('time')
    plt.ylabel('returns')
    plt.show()

def plot_markowitz_bullet(means, stds):
    fig, ax = plt.subplots()
    plt.plot(stds, means, 'o', markersize=5)
    plt.xlabel('std')
    plt.ylabel('mean')
    plt.title('Mean and standard deviation of returns of randomly generated portfolios')
    plt.show()

def plot_markowitz_optimal_portfolio(means, stds, risks, returns):
    fig, ax = plt.subplots()
    plt.plot(stds, means, 'o')
    plt.ylabel('mean')
    plt.xlabel('std')
    plt.plot(risks, returns, 'y-o')
    plt.show()

def main():
    args = parse_args()
    portfolio_returns = gen_toy_returns(args.assets, args.observations)
    if args.plot_returns:
        plot_returns(portfolio_returns)
    n_portfolios = args.portfolios
    means, stds = np.column_stack([gen_toy_portfolio_returns(portfolio_returns) for _ in range(n_portfolios)])
    if args.plot_markowitz_bullet:
        plot_markowitz_bullet(means, stds)
    weights, returns, risks = markowitz_optimal_portfolio(portfolio_returns)
    if args.plot_markowitz_optimal_portfolio:
        plot_markowitz_optimal_portfolio(means, stds, risks, returns)

if __name__ == "__main__":
    main()
