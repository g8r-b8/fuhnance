import pandas as pd
import yfinance as yf

from fuhnance.utils.history.enhance_ticker_history import enhance_ticker_history
from fuhnance.utils.options.enhance_option_chain import enhance_option_chain
from fuhnance.charts.src.volatility import plot_vol

def gen_history(ticker_obj):
    hist = ticker_obj.history(period='1mo', interval='5m')
    hist = enhance_ticker_history(hist)
    return ticker_obj

def gen_options(ticker_obj, ticker):
    option_dates = ticker_obj.options
    last_price = ticker_obj.history(period='1d', interval='1d')['Close'].values[0]
    master = pd.DataFrame()
    for expiration_date in option_dates:
        chain = ticker_obj.option_chain(expiration_date)
        chain = enhance_option_chain(chain, last_price)
        chain['expiry'] = expiration_date
        chain['expiry'] = pd.to_datetime(chain['expiry'])
        master = pd.concat([master, chain], axis=0)
    plot_vol(master)


def main():
    ticker = 'TSLA'
    tesla = yf.Ticker(ticker)
    hist = gen_history(tesla)
    options = gen_options(tesla, ticker)

if __name__ == "__main__":
    main()
