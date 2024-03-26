import numpy as np
import pandas as pd

def gen_toy_returns(n_assets, n_periods, ret_pd=False):
    array = np.random.randn(n_assets, n_periods)
    if ret_pd:
        df = pd.DataFrame(array, columns=['t_'+str(i) for i, e in enumerate(array[0])])
        return df
    else:
        return array

def gen_toy_weights(n):
    k = np.random.rand(n)
    return k/sum(k)

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
