# -*- coding: utf-8 -*-
"""
Instructor Demo: Nesting.

This script showcases how to traverse nested lists of lists.
"""

# List
ceo_list = ["Warren", "Jack", "Harry"]

# List of Lists
ceo_nested_list = [
    ["Warren Buffet", 88, "CEO of Berkshire Hathaway"],
    ["Jeff Bezos", 55, "CEO of Amazon"],
    ["Harry Markowitz", 91, "Professor of Finance"]
]

# Retrieve first entry of ceo_nested_list
first_entry = ceo_nested_list[0]

# Retrieve name of first entry
first_entry_name = ceo_nested_list[0][0]

# Retrieve age of first entry
first_entry_age = ceo_nested_list[0][1]

# Retrieve occupation of first entry
first_entry_occupation = ceo_nested_list[0][2]

# Print results to screen
print("The first entry in employees_nested_list is:", first_entry)
print(f"{first_entry_name} is {first_entry_age} years old, serving as {first_entry_occupation}.")
