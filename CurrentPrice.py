import ccxt
import time

exchange = ccxt.binance()
symbol = 'ETH/USDT' # указываем символ торговли ETH/USDT

pastPrice = None # предыдущая цена

while True: # цикл, в котором запрашиваем актуальную цену каждую минуту, а затем проводим анализ
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']

    if pastPrice: 
        changePrice = (price - pastPrice) / pastPrice * 100
        if abs(changePrice) >= 1: # Если процент изменения цены >= 1%, выводим сообщение в консоль.
            print(f'Price change: {changePrice}')

    pastPrice = price
    time.sleep(60)