# -*- coding: utf-8 -*-
"""
Student Activity: Weekly Gains.

This script showcases how to use nested list/dict objects to
calculate weekly gains of stock tickers.
"""

# Dictionary of List of Lists
# Key: Stock Ticker | Value: List of Records
# Record: Date, Open, High, Low, Close
historical_stock_data = {
    "AAPL": [
        ["04-17-2019", 199.54, 203.38, 198.61, 203.13],
        ["04-18-2019", 199.46, 201.37, 198.56, 199.25],
        ["04-19-2019", 198.58, 199.85, 198.01, 199.23],
        ["04-20-2019", 199.20, 200.14, 196.21, 198.87],

    ],
    "MU": [
        ["04-17-2019", 43.20, 43.53, 42.79, 43.40],
        ["04-18-2019", 43.36, 44.05, 42.76, 43.15],
        ["04-19-2019", 42.26, 42.93, 42.08, 42.76],
        ["04-20-2019", 42.17, 42.23, 41.20, 41.82],

    ],
    "AMD": [
        ["04-17-2019", 27.60, 27.88, 27.34, 27.68],
        ["04-18-2019", 28.21, 28.27, 27.22, 27.49],
        ["04-19-2019", 27.72, 28.18, 27.49, 27.93],
        ["04-20-2019", 27.80, 27.84, 26.96, 27.33],

    ],
    "TWTR": [
        ["04-17-2019", 34.67, 34.86, 34.32, 34.40],
        ["04-18-2019", 34.73, 34.90, 34.20, 34.48],
        ["04-19-2019", 34.84, 34.99, 34.23, 34.46],
        ["04-20-2019", 34.38, 35.03, 34.34, 34.71],

    ]
}

# Dictionary of Dictionary
# Key: Stock Ticker | Value: Dictionary
new_records = {
    "AAPL": {
        "date": "04-21-2019",
        "open": 200.85,
        "high": 201.00,
        "low": 198.44,
        "close": 198.95
    },
    "MU": {
        "date": "04-21-2019",
        "open": 42.85,
        "high": 43.20,
        "low": 41.81,
        "close": 42.01
    },
    "AMD": {
        "date": "04-21-2019",
        "open": 28.21,
        "high": 28.38,
        "low": 27.66,
        "close": 27.85
    },
    "TWTR": {
        "date": "04-21-2019",
        "open": 34.67,
        "high": 34.83,
        "low": 34.11,
        "close": 34.37
    }
}

# Set each ticker's new record: date, open, high, low, close
new_aapl_record = [new_records['AAPL']['date'], new_records['AAPL']['open'], new_records['AAPL']['high'], new_records['AAPL']['low'], new_records['AAPL']['close']]
new_mu_record = [new_records['MU']['date'], new_records['MU']['open'], new_records['MU']['high'], new_records['MU']['low'], new_records['MU']['close']]
new_amd_record = [new_records['AMD']['date'], new_records['AMD']['open'], new_records['AMD']['high'], new_records['AMD']['low'], new_records['AMD']['close']]
new_twtr_record = [new_records['TWTR']['date'], new_records['TWTR']['open'], new_records['TWTR']['high'], new_records['TWTR']['low'], new_records['TWTR']['close']]

# Choice 1: Add a new round of entries to the 'historical_stock_data' dictionary
historical_stock_data['AAPL'].append(new_aapl_record)
historical_stock_data['MU'].append(new_mu_record)
historical_stock_data['AMD'].append(new_amd_record)
historical_stock_data['TWTR'].append(new_twtr_record)
#print(historical_stock_data)

# Choice 2: Add a new round of entries via for loop to the 'historical_stock_data' dictionary
for ticker, ticker_data in new_records.items():
    # Set the new record to be added in list format
    record = [ticker_data['date'], ticker_data['open'], ticker_data['high'], ticker_data['low'], ticker_data['close']]
    # Append the new record to the historical_stock_data dictionary
    historical_stock_data[ticker].append(record)

# Print out the modified 'historical_stock_data' dictionary
print(historical_stock_data)
