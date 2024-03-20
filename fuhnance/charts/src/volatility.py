import datetime as dt
import pandas as pd
import plotly.graph_objects as go

def plot_vol(df):
    '''
        The volatility surface is a three-dimensional plot where the x-axis 
    is the time to maturity, the z-axis is the strike price, 
    and the y-axis is the implied volatility.
    
    Missing gridspace. Follow the following tutorial:
    https://quantpy.com.au/implied-volatility/intraday-option-vol-surfaces/
    '''

    df['days_til_expiry'] = (pd.to_datetime(df['expiry']) - dt.datetime.today()).dt.days
    fig = go.Figure(data=[go.Surface(
        x=df['days_til_expiry'], 
        y=df['impliedVolatility'], z=df['strike'])])
    fig.show()
    breakpoint()
