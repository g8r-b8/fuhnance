import yfinance as yf

from fuhnance.utils.history.enhance_ticker_history import enhance_ticker_history

def main():
    tesla = yf.Ticker("TSLA")
    hist = tesla.history(period='1mo', interval='5m')
    hist = enhance_ticker_history(hist)
    print(hist)

if __name__ == "__main__":
    main()
