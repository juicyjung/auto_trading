import pyupbit
import time
import datetime

def get_target_price():
    df = pyupbit.get_ohlcv("KRW-BTC", count = 30)
    volatility = (df.iloc[-2, 1] - df.iloc[-2, 2]) * 0.6
    target_price = df.iloc[-1, 0] + volatility
    return target_price

def buy_crypto_currency(upbit, price):
    krw = upbit.get_balance("KRW")
    order_krw = krw * 0.9995
    return upbit.buy_market_order("KRW-BTC", order_krw)

def sell_crypto_currency(upbit):
    unit = upbit.get_balance("KRW-BTC")
    return upbit.sell_market_order("KRW-BTC", unit)