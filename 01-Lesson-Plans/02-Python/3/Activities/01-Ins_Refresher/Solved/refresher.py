# -*- coding: utf-8 -*-
"""
Python refresher activity.

This script showcases basic operations in Python such as variables,
conditionals, lists, dicts, for loops, and functions.
"""

# Variables
# Creates a variable with a string "Frankfurter"
title = "Frankfurter"
years = 23
hourly_wage = 65.40
expert_status = True


# Conditionals
# Declare variables and values for evaluation
x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
  print("x is equal to 1")

# Lists
# Create a list of Pokemon
print("Creating a list of Pokemon...")
pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Garydos", "Dragonite", "Onyx"]
print(pokemon)

# Loop over list
# Loop through a range of numbers (0 through 4)
for x in range(5):
  print(x)

# Dicts
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

# Traverse/access nested objects
# List of Dicts
ceo_nested_dict = [
  {
      "name": "Warren Buffet",
      "age": 88,
      "occupation": "CEO of Berkshire Hathaway"
  },
  {
      "name": "Jeff Bezos",
      "age": 55,
      "occupation": "CEO of Amazon"
  },
  {
      "name": "Harry Markowitz",
      "age": 91,
      "occupation": "Professor of Finance"
  }
]

# Define a function
# Define a main function that accepts a string argument
def main(stock_ticker):
  print(stock_ticker + " is booming right now!")

stock_ticker = "SBUX"
main(stock_ticker)
