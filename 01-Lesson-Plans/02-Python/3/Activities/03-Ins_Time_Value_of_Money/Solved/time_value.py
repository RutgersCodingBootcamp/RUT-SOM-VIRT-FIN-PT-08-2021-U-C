# -*- coding: utf-8 -*-
"""
Instructor Demo: Time Value of Money Functions.
This script contains functions that can calculate future values and present values.
"""

def calculate_future_value(present_value, interest_rate, compounding_periods, years):
    """
    Calculates the future value of money given the present_value, interest rate, compounding period, and number of years.

    Args:
        present_value (float): The present value
        interest_rate (float): The interest rate
        periods (int): The compounding period
        years (int): The number of years

    Returns:
        The future value of money.

    """

    future_value = present_value * ((1 + (interest_rate / compounding_periods))**(compounding_periods * years))
    future_value_formatted = round(future_value, 2)

    return future_value_formatted

# Set the values
present_value = 10000
interest_rate = .1
compounding_periods = 1
years = 3

# Call the calculate_future_value() function
calculated_future_value = calculate_future_value(present_value, interest_rate, compounding_periods, years)

# Print out the future_value result
print(f"The future value of ${present_value} at an interest rate of {interest_rate} compounded {compounding_periods} time(s) every year over {years} years is ${calculated_future_value}")
