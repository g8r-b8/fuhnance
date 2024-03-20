import yfinance as yf

msft = yf.Ticker("MSFT")

#print(msft.options)
opt = msft.option_chain('2024-04-19')
print(opt.calls)
breakpoint()
