import decimal
import time
import os
from dotenv import load_dotenv
from grid import GridTrader, OwnerBinance
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

g = GridTrader()
binn = OwnerBinance()

def main():
    # print(g.EXCHANGE.status())
    # doc = g.list_ticker()
    # for s in doc:
    #     print(s)

    # binn.get_all_price()
    doc = g.SYMBOLS
    for s in doc['result']:
        t = g.ticker(sym=s['symbol'])
        if len(t) > 0:
            symbol = str(s['symbol']).replace('THB_','')
            print(f"symbol: {symbol}")
            p = binn.get_price(f"{symbol}")
            price = decimal.Decimal(str(t[s['symbol']]['last']))
            # print(f"symbol: {symbol}, price: {price}THB USD: {p}")
            print(f"=============================================")

if __name__ == "__main__":
    main()