import fuhnance.utils.api.kraken.get_asset_info as kraken
import fuhnance.utils.api.lykke.get_asset_info as lykke 
import fuhnance.utils.api.binance.get_asset_info as binance

def main():
    '''
    kraken_btc = kraken.get_current_price('XBTUSD')
    lykke_btc = lykke.get_current_price('BTCUSD')
    print(compare_prices(kraken_btc, lykke_btc))
    '''
    kraken_btc = kraken.get_current_price('LTCXBT')
    binance_btc = binance.get_current_price('LTCBTC')
    breakpoint()
    print(compare_prices(kraken_btc, binance_btc))

def compare_prices(exchange_a, exchange_b):
    results = []
    #price_diff_a_b = exchange_a['ask'] - exchange_b['bid'] > 0
    price_diff = exchange_a['ask'] - exchange_b['bid']
    if price_diff > 0:
        results.append(f'buy {exchange_b["exchange"]}: {price_diff}')
    price_diff = exchange_b['ask'] - exchange_a['bid']
    #price_diff_b_a = exchange_b['ask'] - exchange_a['bid'] > 0
    if price_diff > 0:
        results.append(f'buy {exchange_a["exchange"]}: {price_diff}')
    return results

if __name__ == "__main__":
    main()
