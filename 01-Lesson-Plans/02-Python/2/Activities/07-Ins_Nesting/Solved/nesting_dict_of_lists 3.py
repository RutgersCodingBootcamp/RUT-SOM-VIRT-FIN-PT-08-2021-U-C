# -*- coding: utf-8 -*-
"""
Instructor Demo: Nesting.

This script showcases how to traverse dictionary of lists.
"""

# Dict
stocks_dict = {
    "APPL": 101.32,
    "MU": 43.4,
    "AMD": 23.12,
    "TWTR": 25
}

# Dictionary of Lists
stocks_nested_list = {
    "APPL": ["Apple", 101.32, "NASDAQ", 937.7],
    "MU": ["Micron Technology", 32.12, "NASDAQ", 48.03],
    "AMD": ["Advanced Micro Devices", 23.12, "NASDAQ", 29.94],
    "TWTR": ["Twitter", 34.40, "NASDAQ", 26.42]
}

# Retrieve entry for APPL
appl_entry = stocks_nested_list["APPL"]

# Retrieve name, stock_price, and exchange for APPL entry
appl_name = stocks_nested_list["APPL"][0]
appl_stock_price = stocks_nested_list["APPL"][1]
appl_exchange = stocks_nested_list["APPL"][2]

# Print results to screen
print(f"APPL ticker stands for {appl_name}. APPL stock price is currently {appl_stock_price}, and it is available on {appl_exchange}.")
