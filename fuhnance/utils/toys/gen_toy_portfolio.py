import math
import numpy as np
import pandas as pd

def gen_toy_returns(n_assets, n_periods, ret_pd=False):
    array = np.random.randn(n_assets, n_periods)
    if len(array) == 1:
        return array[0]
    if ret_pd:
        df = pd.DataFrame(array, columns=['t_'+str(i) for i, e in enumerate(array[0])])
        return df
    else:
        return array

def gen_toy_weights(n):
    k = np.random.rand(n)
    return k/sum(k)

def gen_seasonality(n):
    # Sin wave
    samples = np.linspace(0, math.pi, int(n*math.pi), endpoint=False)
    signal = np.sin(2 * np.pi * samples)
    return signal

def gen_multiplicative_seasonality(n):
    seasonality = gen_seasonality(n) + 1
    random_ts = np.absolute(gen_toy_returns(1, len(seasonality)))
    return random_ts * seasonality

def gen_additive_seasonality(n):
    seasonality = gen_seasonality(n) + 1
    random_ts = np.absolute(gen_toy_returns(1, len(seasonality)))
    return random_ts + seasonality

def gen_toy_portfolio_returns(returns):
    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(gen_toy_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))
    # Mean and StdDev
    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)
    # This recursion reduces outliers to keep plots pretty
    if sigma > 2:
        return gen_toy_portfolio_returns(returns)
    return mu, sigma
