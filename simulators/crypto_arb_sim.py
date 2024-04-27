import time

import fuhnance.utils.api.kraken.get_asset_info as kraken
import fuhnance.utils.api.binance.get_asset_info as binance

class Wallet:

    def __init__(self,
             usd,
             asset_a,
             asset_b,
             asset_a_exposure=0,
             asset_b_exposure=0):
        self.usd = usd
        self.asset_a = asset_a
        self.asset_b = asset_b
        self.asset_a_exposure = asset_a_exposure
        self.asset_b_exposure = asset_b_exposure

class Exchange:

    def __init__(self):
        pass

    def convert_currency(self, wallet: Wallet, amount: float, source_currency: str, destination_currency: str):
        pass

    def asset_price(source_currency: str, destination_currency: str):
        pass


class Kraken(Exchange):

    def __init__(self):
        pass

class Binance(Exchange):

    def __init__(self):
        pass


def main():
    run_sim()

def run_sim(initial_equity=10_000, inverse=False):
    equity = initial_equity
    initial_buy_in(equity, pair='LTCUSD')
    while True:
        print('Running')
        kraken_btc, binance_btc = get_price_info()
        time.sleep(1)

def initial_buy_in(equity, pair):
    pass

def get_price_info():
    kraken_btc = kraken.get_current_price('LTCXBT')
    binance_btc = binance.get_current_price('LTCBTC')
    return kraken_btc, binance_btc

if __name__ == "__main__":
    main()
