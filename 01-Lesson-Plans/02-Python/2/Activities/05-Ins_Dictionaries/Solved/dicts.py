# -*- coding: utf-8 -*-
"""
Instructor Demo: Dicts.
This script showcases basic operations of Python Dicts.
"""

  # Initialize a dictionary containing top traders for each month in 2019
top_traders_2019 = {
    "january" : "Karen",
    "february" : "Harold",
    "march" : "Sam"
}

print()
print(f"Dictionary: {top_traders_2019}")
print()

# Initialize a dictionary
trading_pnl = {
    "title": "Trading Log",
    "03-18-2019": -224,
    "03-19-2019": 352,
    "03-20-2019": 252,
    "03-21-2019": 354,
    "03-22-2019": -544,
    "03-23-2019": -650,
    "03-24-2019": 56,
    "03-25-2019": 123,
    "03-26-2019": -43,
    "03-27-2019": 254,
    "03-28-2019": 325,
    "03-29-2019": -123,
    "03-30-2019": 47,
    "03-31-2019": 321,
    "04-01-2019": 123,
    "04-02-2019": 133,
    "04-03-2019": -151,
    "04-04-2019": 613,
    "04-05-2019": 232,
    "04-06-2019": -311
}

# Print out dictionary, initial print() to serve as spacing between command line input
print()
print(f"Dictionary: {trading_pnl}")
print()

# Print out specific value of a key
print(f"03-31-2019: {trading_pnl['03-31-2019']}")
print()

# Add a new key-value pair
trading_pnl["04-07-2019"] = 413
print(trading_pnl)
print()

# Modify a key value
trading_pnl["04-07-2019"] = 542
print(trading_pnl)
print()

# Delete a key-value pair
del trading_pnl["04-07-2019"]
print(trading_pnl)
print()

# Check if key exists
if "04-03-2019" in trading_pnl:
    print("Yes, '04-03-2019' is one of the keys in the trading_pnl dictionary")
print()

# Print out dict keys via a for loop
for key in trading_pnl:
    print(f"Key: {key}")
print()

# Print out dict values
for key in trading_pnl:
    print(f"Value: {trading_pnl[key]}")
print()

# Print out dict key-value pairs
for key, value in trading_pnl.items():
    print(f"Key: {key} Value: {value}")
print()
