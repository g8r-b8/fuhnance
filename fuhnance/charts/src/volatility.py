import datetime as dt
import pandas as pd
import numpy as np
import math
import scipy
from scipy.interpolate import griddata

import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm


def black_scholes(v, call_put_flag = 'c', S = 100.0, X = 100.0, T = 1.0, r = 0.01):
    N = scipy.stats.norm.cdf
    try:
        d1 = (math.log(S / X) + (r + v * v / 2.0) * T) / (v * math.sqrt(T))
        d2 = d1 - v * math.sqrt(T)
        if call_put_flag=='c':
            return S * N(d1) - X * math.exp(-r * T) * N(d2)
        else:
            res = X * math.exp(-r * T) * N(-d2) - S * N(-d1)
            return res
    except: return 0

def calc_impl_vol(price = 5.0,
                  right = 'c',
                  underlying = 100.0,
                  strike = 100.0,
                  time = 1.0,
                  rf = 0.01,
                  inc = 0.001):
    f = lambda x: black_scholes(x,
                                call_put_flag=right,
                                S=underlying,
                                X=strike,
                                T=time,
                                r=rf) - price
    return scipy.optimize.brentq(f, 0, 5)

def get_surf(df):
    vals = []
    for index, row in df.iterrows():
        underlying = float(row['underlying_price'])
        price = (float(row['ask'])+float(row['bid']))/2.0
        expd = (row['expiry'] - dt.datetime.now()).days
        exps = (row['expiry'] - dt.datetime.now()).seconds
        exp = (expd*24.*3600. + exps) / (365.*24.*3600.)
        try:
            impl = calc_impl_vol(price, 'c', underlying, float(row['strike']), exp)
            vals.append([exp, float(row['strike']), impl])
        except Exception as e:
            print('passing')
            print(e)
            pass
    vals = np.array(vals).T
    plot_vol_surface_optimized(vals)
    # Matplotlib
    fig = plt.figure()#.add_subplot(projection='3d')
    ax = plt.figure().add_subplot(projection='3d')
    #mesh_plot2(vals[0],vals[1],vals[2], fig, ax)
    #plot3D(vals[0], vals[1], vals[2], fig, ax)
    #combine_plots(vals[0],vals[1],vals[2])

def plot3D(X, Y, Z, fig, ax, combined=False):
    ax.plot(X,Y,Z,'o', color = 'pink')
    plt.xlabel("expiry")
    plt.ylabel("strike")
    if not combined:
        plt.show()
   
def mesh_plot2(X, Y, Z, fig, ax, combined=False):
    XX, YY, ZZ = make_surf(X, Y, Z)
    ax.plot_surface(XX, YY, ZZ, color = 'blue')
    ax.contour(XX, YY, ZZ)
    plt.xlabel("expiry")
    plt.ylabel("strike")
    if not combined:
        plt.show()
 
def combine_plots(X, Y, Z):
    fig = plt.figure()
    ax = plt.figure().add_subplot(projection='3d')
    mesh_plot2(X, Y, Z, fig, ax, True)
    plot3D(X, Y, Z, fig, ax, True)
    plt.show()

def make_surf(X, Y, Z):
    XX, YY = np.meshgrid(np.linspace(min(X), max(X), 230), np.linspace(min(Y), max(Y), 230))
    ZZ = griddata(np.array([X, Y]).T, np.array(Z),(XX, YY), method='linear')
    return XX, YY, ZZ

def plot_vol(df):
    df = df.query('contract_type == "calls"')
    get_surf(df)
    #plot_vol_surface(df)
    #plot_vol_dot_plot(df)

def plot_vol_dot_plot(df):
    df['days_til_expiry'] = (pd.to_datetime(df['expiry']) - dt.datetime.today()).dt.days
    fig = px.scatter_3d(df,
        x='days_til_expiry',
        y='strike',
        z='impliedVolatility',
        color='contract_type')
    fig.show()


def plot_vol_surface(df):
    '''
        The volatility surface is a three-dimensional plot where the x-axis 
    is the time to maturity, the z-axis is the strike price, 
    and the y-axis is the implied volatility.
    
    Missing gridspace. Follow the following tutorial:
    https://quantpy.com.au/implied-volatility/intraday-option-vol-surfaces/
    '''
    df['days_til_expiry'] = (df['expiry'] - dt.datetime.today()).dt.days
    #XX, YY, ZZ = make_surf(df['days_til_expiry'], df['impliedVolatility'], df['strike'])
    XX, YY, ZZ = make_surf(df['days_til_expiry'], df['strike'], df['impliedVolatility'])
    fig = go.Figure(data=[go.Surface(x=XX,y=YY,z=ZZ)])
    fig.show()

def plot_vol_surface_optimized(df):
    '''
        The volatility surface is a three-dimensional plot where the x-axis 
    is the time to maturity, the z-axis is the strike price, 
    and the y-axis is the implied volatility.
    
    Missing gridspace. Follow the following tutorial:
    https://quantpy.com.au/implied-volatility/intraday-option-vol-surfaces/
    '''
    XX, YY, ZZ = make_surf(df[0], df[1], df[2])
    fig = go.Figure(data=[go.Surface(x=XX,y=YY,z=ZZ
            )
        ]
    )
    fig.show()
