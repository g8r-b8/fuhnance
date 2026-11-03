import yfinance as yf

msft = yf.Ticker("MSFT")

#print(msft.options)
opt = msft.option_chain('2027-01-15')
print(opt.calls)
breakpoint()
