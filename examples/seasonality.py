import matplotlib.pyplot as plt
from fuhnance.utils.toys import gen_toy_portfolio as f
from fuhnance.utils.seasonality.decompose import decompose as g

def main():
    x = f.gen_multiplicative_seasonality(100)
    trend, seasonal, residual, decomposition = g(x)
    breakpoint()

if __name__ == "__main__":
    main()
