import os
import requests
import json
from bitkub import Bitkub
from binance.client import Client

class OwnerBinance:
    def __init__(self):
        self.BINANCE_API_KEY = os.environ.get('BINANCE_API_KEY')
        self.BINANCE_SECRET_KEY = os.environ.get('BINANCE_SECRET_KEY')
        self.OWNER_BINANCE = Client(self.BINANCE_API_KEY, self.BINANCE_SECRET_KEY)
        pass

    def get_all_price(self):
        list = self.OWNER_BINANCE.get_all_tickers()
        for i in list:
            print(i)
        pass
    def get_price(self, symbol="BTC"):
        pair = ["USD","BUSD", "USDT", "EUR", "AUD","NGN","RUB", "GBP","TRY"]
        for i in pair:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}{i}"
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers)
            if response.ok:
                price = response.json()
                print(price)
                # return float(price["price"]) * 37.5154

        return 0

class GridTrader:
    order_list = []

    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.API_SECRET_KEY = os.getenv("API_SECRET_KEY")
        self.SYMBOL = os.getenv("SYMBOL")
        self.GRID_LEVEL = round(int(os.getenv("GRID_LEVEL"))/2)
        self.LOWER_PRICE = float(os.getenv("LOWER_PRICE"))
        self.UPPER_PRICE = float(os.getenv("UPPER_PRICE"))
        self.COST = float(os.getenv("COST"))
        self.AMOUNT = float(self.COST/(self.GRID_LEVEL*2))
        self.EXCHANGE = Bitkub(api_key=self.API_KEY, api_secret=self.API_SECRET_KEY)
        self.SERVER_TIME = self.EXCHANGE.servertime()
        self.SYMBOLS = self.EXCHANGE.symbols()
        self.TICKER = self.EXCHANGE.ticker(sym=f"THB_{self.SYMBOL}")
        pass

    def ticker(self, sym=None):
        return self.EXCHANGE.ticker(sym=sym)

    def list_ticker(self):
        lst = []
        for s in self.SYMBOLS['result']:
            symbol = s['symbol']
            p = self.ticker(sym=symbol)
            if len(p) > 0:
                if p[symbol]["last"] >= 1:
                    price = p[symbol]["last"]
                    cost = round(price * self.GRID_LEVEL, 2)
                    baseVolume = p[symbol]['baseVolume']
                    quoteVolume = p[symbol]['quoteVolume']
                    if cost <= self.COST and baseVolume > 100000:
                        sellVolume = []
                        for r in range(round(self.GRID_LEVEL)):
                            sellVolume.append(round(price+(self.UPPER_PRICE * (r + 1)), 2))

                        openVolume = []
                        for r in range(round(self.GRID_LEVEL)):
                            openVolume.append(round(price-(self.LOWER_PRICE * (r + 1)), 2))

                        lst.append({
                            'symbol': str(symbol).replace("THB_", ""),
                            'price': price,
                            'cost': cost,
                            'base': baseVolume,
                            'quote': quoteVolume,
                            'open': openVolume,
                            'sell': sellVolume
                        })
        return lst

    def place_order(self):
        pass

    def loop_jobs(self):
        pass

    def send_request(self):
        pass

    def logs(self, path=None, msg=None):
        pass