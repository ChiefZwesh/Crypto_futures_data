import pandas as pd
from binance.client import Client
import datetime as dt

# Get binance futures symbol data for different timeframe
# pip install for pandas, python-binance, datetime
# Uses the simple k-line usd m futures data for futures trading
# only default timeframes are available, and usually data before 1 Jan 2020 is not available, so
# confirm from binance before putting the date before 2020

api_key = 'API'
api_secret = 'YOURSECRET'
client = Client(api_key, api_secret)


symbol = input('\nType Symbol name, like BTCUSDT : ')
interval = input('\nType Timeframe, like 15m or 1m : ')
since = input('\nType How much time of Data you want, like since 1 Jan, 2020 : ')

print("\nDownloading Data")

klines = client.futures_historical_klines(symbol, interval, since)

print("Converting to CSV")
data = pd.DataFrame(klines)
data.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                'taker_base_vol', 'taker_quote_vol', 'ignore']
data.index = [dt.datetime.fromtimestamp(x / 1000.0).astimezone(dt.timezone(dt.timedelta(hours=2))) for x in
            data.close_time]  # Convert to Africa/Johannesburg timezone (UTC+2)
data.to_csv(symbol + '.csv', index=None, header=True)

print("Data saved to " + symbol + ".csv")
