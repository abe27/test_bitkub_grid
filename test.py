import time
import os
from dotenv import load_dotenv
from grid import GridTrader
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

g = GridTrader()

def main():
    # print(g.EXCHANGE.status())
    doc = g.list_ticker()
    for s in doc:
        print(s)

if __name__ == "__main__":
    main()