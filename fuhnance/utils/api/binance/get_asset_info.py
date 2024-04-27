import requests

from fuhnance.utils.api.common.format_response import format_response

BASE_URL = 'https://api.binance.us/api/v3/'

def get_ticker_info(pair: str):
    endpoint = f'ticker/price?symbol={pair}'
    response = requests.get(BASE_URL+endpoint)
    return format_response(response)

def get_book_ticker_info(pair: str):
    endpoint = f'ticker/bookTicker?symbol={pair}'
    response = requests.get(BASE_URL+endpoint)
    return format_response(response)

def get_current_price(pair: str):
    res = get_book_ticker_info(pair)
    return {
        'bid':float(res['bidPrice']),
        'ask':float(res['askPrice']),
        #'time':,
        'exchange':'binance'
            }
