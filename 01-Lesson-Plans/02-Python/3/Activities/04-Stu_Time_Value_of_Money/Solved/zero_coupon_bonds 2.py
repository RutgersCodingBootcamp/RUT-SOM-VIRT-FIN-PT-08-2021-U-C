# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# Function to calculate present value
def calculate_present_value(future_value, discount_rate, compounding_periods, years):
    """
    Calculates the present value of money given the future_value, interest rate, compounding period, and number of years.
    Args:
        future_value (float): The future value
        discount_rate (float): The interest rate
        compounding_periods (int): The compounding period
        time_to_maturity (int): The number of years
    Returns:
        The present value of money.
    """

    present_value = future_value / (
        (1 + (discount_rate / compounding_periods)) ** (compounding_periods * years)
    )
    present_value_formatted = round(present_value, 2)

    return present_value_formatted


# Initialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = 0.1
compounding_periods = 1
years = 5

# Call the calculate_present_value() function
bond_value = calculate_present_value(
    future_value, discount_rate, compounding_periods, years
)

# Determine if the bond is worth it
if bond_value > price:
    discount = round(bond_value - price, 2)
    print(f"The bond is selling at a price of ${price} and is valued at ${bond_value}.")
    print(f"A discount of {discount} exists, therefore you want to buy the bond.")
elif bond_value < price:
    premium = round(price - bond_value, 2)
    print(f"The bond is selling at a price of ${price} and is valued at ${bond_value}.")
    print(f"A premium of {premium} exists, therefore you do not want to buy the bond.")
else:
    print(f"The bond is selling at a price of ${price} and is valued at ${bond_value}.")
    print(f"The bond is selling at its present value, you are neutral.")
