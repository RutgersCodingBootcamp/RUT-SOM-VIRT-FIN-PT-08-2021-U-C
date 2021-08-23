# -*- coding: utf-8 -*-
"""
Instructor Demo: Nesting.

This script showcases how to traverse list of dicts.
"""

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

# Retrieve second entry
second_entry = ceo_nested_dict[1]

# Retrieve name, age, and occupation of the second dict entry
second_entry_name = ceo_nested_dict[1]["name"]
second_entry_age = ceo_nested_dict[1]["age"]
second_entry_occupation = ceo_nested_dict[1]["occupation"]

# Print results to the screen
print(f"The second entry in ceo_nested_dict is {second_entry_name}, a {second_entry_age} year old {second_entry_occupation}.")
