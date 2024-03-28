import datetime as dt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def decompose(data, model='multiplicative'):
    '''
    https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/
    https://towardsdatascience.com/finding-seasonal-trends-in-time-series-data-with-python-ce10c37aa861
    '''
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data, columns=['Price'])
        start = dt.datetime.now()
        end = start - dt.timedelta(days=len(data)-1)
        daterange = pd.to_datetime(pd.date_range(start, end, periods=len(data)))
        data['date'] = daterange.date
    data = data.set_index('date').asfreq('D')
    data.index = pd.to_datetime(data.index)
    decomposition = seasonal_decompose(data['Price'], model=model, period=5)
    return decomposition.trend, decomposition.seasonal, decomposition.resid, decomposition


