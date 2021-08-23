# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# Initialize a dictionary of banks and market caps (in billions)
banks = {
    "JP Morgan Chase": 327,
    "Bank of America": 302,
    "Citigroup": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "U.S. Bancorp": 83,
    "TD Bank": 108,
    "PNC Financial Services": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "First Hawaiian Bank": 3,
    "Ally Financial": 12,
    "Wachovia": 145,
    "Republic Bancorp": .97
}

# Change the market cap for 'Citigroup'
banks['Citigroup'] = 170

# Add a new bank and market cap pair
banks['American Express'] = 33

# Remove a bank from the dictionary
del banks['Wachovia']

# Initialize metric variables
total_market_cap = 0
bank_count = 0
average = 0

# Initialize minimum key-value pair
minimum_key = ""
minimum_value = 0

# Initialize maximum key-value pair
maximum_key = ""
maximum_value = 0


# Mega Cap: Firms with a market capitalization greater than or equal to $300 billion.
# Large Cap: Firms with a market capitalization greater than or equal to $10 billion and less than $300 billion.
# Mid Cap: A market capitalization greater than or equal to $2 and less than $10 billion.
# Small Cap: A market capitalization greater than or equal to $300 million and less than $2 billion.

# Initialize market cap lists
mega_caps = []
large_caps = []
mid_caps = []
small_caps = []

# Iterate over key-value pairs of the dictionary
print()
for bank_name, market_cap in banks.items():
    print(f"Name: {bank_name} | Market Cap: {market_cap}")

    # Calculate sum of market caps and number of banks in the dictionary
    total_market_cap += int(market_cap)
    bank_count += 1

    # Logic to determine min value and associated key
    if minimum_value == 0:
        minimum_value = market_cap
        minimum_key = bank_name
    elif market_cap < minimum_value:
        minimum_value = market_cap
        minimum_key = bank_name

    # Logic to determine max value and associated key
    if market_cap > maximum_value:
        maximum_value = market_cap
        maximum_key = bank_name

    # Group banks by categories of market caps
    if market_cap >= 300:
        mega_caps.append(bank_name)
    elif market_cap >= 10 and market_cap < 300:
        large_caps.append(bank_name)
    elif market_cap >= 2 and market_cap < 10:
        mid_caps.append(bank_name)
    elif market_cap < 2:
        small_caps.append(bank_name)
print()

# Calculate average market cap of banks in the dictionary
avg_market_cap = round(total_market_cap / bank_count, 2)

# Print the metrics
print(f"Total Market Capitalization: {total_market_cap}")
print(f"Total Numer of Banks: {bank_count}")
print(f"Average Market Capitalization: {avg_market_cap}")
print(f"Largest Bank: {maximum_key}")
print(f"Smallest Bank: {minimum_key}")
print("------------------------------------------------")
print(f"Mega Cap Banks: {mega_caps}")
print(f"Large Cap Banks: {large_caps}")
print(f"Mid Cap Banks: {mid_caps}")
print(f"Small Cap Banks: {small_caps}")
print()
