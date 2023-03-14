import ccxt
import time

exchange = ccxt.binance()
symbol = 'ETH/USDT' # указываем символ торговли ETH/USDT

pastPrice = None # предыдущая цена

while True: # цикл, в котором запрашиваем актуальную цену каждую минуту, а затем проводим анализ
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']
