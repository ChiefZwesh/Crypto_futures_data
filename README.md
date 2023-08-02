# Binance Futures Historical Data Downloader

This Python script downloads historical k-line data for a specific trading symbol from Binance Futures using the Binance API.

## Prerequisites

Before running the script, make sure you have installed the following libraries:

- pandas
- python-binance

You can install these libraries using pip:

```bash
pip install pandas python-binance
```

## Usage

1. Replace `'API'` and `'YOURSECRET'` in the script with your actual Binance API key and secret.

2. Run the script using Python:

```bash
python script.py
```

3. The script will prompt you to provide the symbol name, timeframe, and duration for which you want to download the data.

4. After providing the required input, the script will connect to the Binance API and download the historical k-line data for the specified symbol, timeframe, and duration.

5. The downloaded data will be saved as a CSV file named `symbol.csv` in the script's directory. The file will contain columns such as open time, open price, high price, low price, close price, volume, and more.

## Note

- The script uses the Binance `futures_historical_klines` method to download the data. Note that only default timeframes are available, and usually data before January 1, 2020, is not available. Confirm with Binance if you need data before that date.

- The timestamps in the CSV file will be in South Africa (Africa/Johannesburg) timezone (UTC+2) by default. You can modify the timezone conversion in the script as needed.

## Disclaimer

This script is for educational and informational purposes only. Trading involves risk, and the content provided here does not constitute financial advice. Always conduct thorough research and consider seeking professional advice before making any financial decisions.

## License

This script is open-source and licensed under the [MIT License](LICENSE).

Feel free to modify, distribute, and use the script as per the terms of the MIT License.

---
*Disclaimer: The author and the script contributors are not responsible for any losses or damages incurred while using this script. Use it at your own risk.*
