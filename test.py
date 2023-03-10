import decimal
import time
import os
from dotenv import load_dotenv
from grid import GridTrader
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

g = GridTrader()

def main():
    # print(g.EXCHANGE.status())
    # doc = g.list_ticker()
    # for s in doc:
    #     print(s)
    doc = g.SYMBOLS
    for s in doc['result']:
        t = g.ticker(sym=s['symbol'])
        if len(t) > 0:
            symbol = str(s['symbol']).replace('THB_','')
            price = decimal.Decimal(str(t[s['symbol']]['last']))
            digit = float(str(g.LOWER_PRICE).zfill(abs(price.as_tuple().exponent)))
            if abs(price.as_tuple().exponent) > 0:
                digit = float("0." + str(g.LOWER_PRICE).zfill(abs(price.as_tuple().exponent)))

            pipBuy = []
            pipSell = []
            for p in range(g.GRID_LEVEL):
                pipBuy.append(round(float(price) - (digit * (p+1)), abs(price.as_tuple().exponent)))
                pipSell.append(round(float(price) + (digit * (p+1)), abs(price.as_tuple().exponent)))

            print(f"{symbol}:::{price}\nbuy: {sorted(pipBuy)}\nsell: {sorted(pipSell)}\n\n")

if __name__ == "__main__":
    main()