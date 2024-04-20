import requests

from fuhnance.utils.api.common.format_response import format_response

def get_ohlc_info(market, pair, period, price_type, from_date, to_date):
    '''
    market:
        The market type. Acceptable values: Spot, Mt.
    pair:
        The asset pair Id.
    period:
        The time period. Acceptable values: Min5, Min15, Min30, Hour, Hour4, Hour6, Hour12, Day, Week, Month.
    price_type:
        The price type. Acceptable values: Bid, Ask, Mid, Trades.
    from_date:
        The request's starting date and time.
    to_date:
        The request's finishing date and time.
    '''
    print(market, pair, period, price_type, from_date, to_date)
    # TODO

def get_ticker_info(pair: str):
    res = requests.get(f'https://hft-apiv2.lykke.com/api/prices?assetPairIds={pair}')
    return format_response(res)

def get_current_price(pair: str):
    res = get_ticker_info(pair)
    prices = res['payload']
    assert len(prices) == 1
    prices = prices[0]
    return {'bid': prices['bid'],
            'ask': prices['ask'],
            'time': str(prices['timestamp'])[:10],
            'exchange': 'lykke'}
