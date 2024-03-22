import pandas as pd

def add_breakeven_movement_needed(df, last_price, contract):
    if contract not in ['call', 'put']:
        raise ValueError('Must enter "call" or "put" for positional arg "contract".')
    if contract == 'call':
        df['movement_needed'] = (df['strike'] - last_price) + df['lastPrice']
    if contract == 'put':
        df['movement_needed'] = (last_price - df['strike']) + df['lastPrice']
    return df

def enhance_option_chain(chain, last_price):
    calls = add_breakeven_movement_needed(chain.calls, last_price, 'call')
    puts = add_breakeven_movement_needed(chain.puts, last_price, 'put')
    calls['contract_type'] = 'calls'
    puts['contract_type'] = 'puts'
    df = pd.concat([calls, puts], axis=0)
    df['underlying_price'] = last_price
    # master[master['movement_needed']>0].query('inTheMoney == False').sort_values('movement_needed')
    return df
