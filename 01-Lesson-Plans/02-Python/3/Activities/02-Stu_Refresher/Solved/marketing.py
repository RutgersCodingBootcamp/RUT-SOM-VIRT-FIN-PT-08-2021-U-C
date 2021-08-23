# -*- coding: utf-8 -*-
"""Refresher activity.

This script will use variables, conditionals, lists, dicts, and functions
to print out different greetings for customers based on their
business tier (determined by revenue).
"""

# List of dicts
customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]

# Define a function that accepts a customer first_name, last_name,
# and revenue and returns a custom greeting using the full name.
# Use these ranges to determine the business tier (and corresponding message)
# for each customer.
#   Platinum = 3001+
#   Gold = 2001-3000
#   Silver = 1001-2000
#   Bronze = 0-1000
def create_greeting(first_name, last_name, revenue):
    """Creates a customer greeting based on revenue status.

    Args:
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        revenue (int): The revenue of the customer.

    Returns:
        A customized greeting string.
    """

    if revenue > 3000:
        greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a platinum member."
    elif (revenue > 2000 and revenue <= 3000):
        greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a gold member."
    elif (revenue > 1000 and revenue <= 2000):
        greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a silver member."
    elif (revenue >= 0  and revenue <= 1000):
        greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a bronze member."

    return greeting

# Loop through the list of customers and use your function to print custom greetings for each customer.
for customer in customers:
    greeting = create_greeting(customer['first_name'], customer['last_name'], customer['revenue'])
    print(greeting)
