import requests

from fuhnance.utils.api.common.format_response import format_kraken_response

def get_server_time():
    res = requests.get('https://api.kraken.com/0/public/Time')
    return format_kraken_response(res)

def get_asset_info():
    res = requests.get('https://api.kraken.com/0/public/Assets')
    return format_kraken_response(res)

def get_pairs_info(pairs: str):
    res = requests.get(f'https://api.kraken.com/0/public/AssetPairs?pair={pairs}')
    return format_kraken_response(res)

def get_ticker_info(pair: str):
    ''' 
    a: Ask [<price>, <whole lot volume>, <lot volume>]
    b: Bid [<price>, <whole lot volume>, <lot volume>]
    c: Last trade closed [<price>, <lot volume>]
    v: Volume [<today>, <last 24 hours>]
    p: Volume weighted average price [<today>, <last 24 hours>]
    t: Number of trades [<today>, <last 24 hours>]
    l: Low [<today>, <last 24 hours>]
    h: High [<today>, <last 24 hours>]
    o: Today's opening price
    '''
    res = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={pair}')
    return format_kraken_response(res)

def get_current_price(pair: str):
    assert len(pair.split(',')) == 1
    res = get_ticker_info(pair)
    symbols = list(res.keys())
    assert len(symbols) == 1
    symbol = symbols[0]
    prices = res[symbol]
    return {'bid': float(prices['b'][0]),
            'ask': float(prices['a'][0]),
            'time': str(get_server_time()['unixtime']),
            'exchange':'kraken'}

def get_ohlc_info(pair: str):
    res = requests.get(f'https://api.kraken.com/0/public/OHLC?pair={pair}')
    return format_kraken_response(res)

def get_order_book(pair: str):
    res = requests.get(f'https://api.kraken.com/0/public/Depth?pair={pair}')
    return format_kraken_response(res)

def get_recent_trades(pair: str):
    res = requests.get(f'https://api.kraken.com/0/public/Trades?pair={pair}')
    return format_kraken_response(res)

def get_recent_spreads(pair: str):
    res = requests.get(f'https://api.kraken.com/0/public/Spread?pair={pair}')
    return format_kraken_response(res)
