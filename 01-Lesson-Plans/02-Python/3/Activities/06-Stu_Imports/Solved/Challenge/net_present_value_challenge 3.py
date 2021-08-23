# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# Import the NumPy library
import numpy_financial as npf

# Discount Rate
discount_rate = .1

# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# Initialize dictionary to hold NPV return values
npv_dict = {}

# Calculate the NPV for each scenario
npv_dict['conservative'] = npf.npv(discount_rate, cash_flows_conservative)
npv_dict['neutral'] = npf.npv(discount_rate, cash_flows_neutral)
npv_dict['aggressive'] = npf.npv(discount_rate, cash_flows_aggressive)

# Initialize variables
max_value = 0
max_key = 0

# Iterate over the dictionary and find the max key-value pair
for key, value in npv_dict.items():
    print(f"{key} {value}")

    if max_value == 0:
        max_value = value
        max_key = key
    elif value > max_value:
        max_value = value
        max_key = key

# Print out the optimal project scenario with the highest NPV value
print("---------------------------------------------------------")
print(f"The project scenario with the max NPV value is '{max_key}' with a NPV of {max_value}")
