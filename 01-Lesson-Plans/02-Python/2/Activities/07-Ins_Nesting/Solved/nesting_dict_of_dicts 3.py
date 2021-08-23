# -*- coding: utf-8 -*-
"""
Instructor Demo: Nesting.

This script showcases how to traverse dictionary of dicts.
"""

# Dictionary of Dicts
stocks_nested_dict = {
    "APPL": {
        "name": "Apple",
        "exchange": "NASDAQ",
        "market_cap": 937.7
    },
    "MU": {
        "name": "Micron Technology",
        "exchange": "NASDAQ",
        "market_cap": 48.03
    },
    "AMD": {
        "name": "Advanced Micro Devices",
        "exchange": "NASDAQ",
        "market_cap": 29.94
    },
    "TWTR": {
        "name": "Twitter",
        "exchange": "NASDAQ",
        "market_cap": 26.42
    }
}

# Retrieve Twitter entry
twitter_entry = stocks_nested_dict["TWTR"]

# Retrieve TWTR name, exchange, and market_cap
twitter_name = stocks_nested_dict["TWTR"]["name"]
twitter_exchange = stocks_nested_dict["TWTR"]["exchange"]
twitter_market_cap = stocks_nested_dict["TWTR"]["market_cap"]

# Print results to screen
print(f"Name of TWTR ticker is {twitter_name}. TWTR is available on {twitter_exchange}, and it currently has a market capitalization of {twitter_market_cap}.")
