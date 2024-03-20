import numpy as np

def adjust_columns(df):
    df.columns = [e.lower().replace(' ', '_') for e in df.columns]
    return df

def add_change(df):
    df['change'] = df['close']-df['open']
    return df

def add_percent_change(df):
    df['percent_change'] = 100*((df['close']-df['open'])/df['open'])
    return df

def add_log_ret(df):
    df['log_ret'] = np.log(df.close)-np.log(df.open)
    return df

def enhance_ticker_history(df):
    df = adjust_columns(df)
    df = add_change(df)
    df = add_percent_change(df)
    return df
