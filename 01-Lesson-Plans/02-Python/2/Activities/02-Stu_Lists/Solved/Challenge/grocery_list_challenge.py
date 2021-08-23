# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# Create a list of groceries
print("My list of groceries:")
groceries = ["water", "butter", "eggs", "apples", "cinnamon", "sugar", "milk"]
print(groceries)
print()

# Find the first two items on the list
print("What are my first two items on the list?")
print(groceries[:2])
print()

# Find the last five items on the list
print("What are all my items except for the first two on the list?")
print(groceries[2:])
print()

# Find every other item on the list, starting from the second item
print("What is every other item on the list, starting from the second item?")
print(groceries[1::2])
print()

# Add an element to the end of the list
print("Oops, forgot to add flour...")
groceries.append("flour")
print(groceries)
print()

# Changes a specified element within the list at the given index
print("I should be more specific with what kind of apples I want...")
groceries[3] = "gala apples"
print(groceries)
print()

# Calculate how many items you have in the list
print("How many items do I have on my shopping list?")
print(len(groceries))
print()

# ----------------------Go to the grocery store---------------------------")

# Find the index of the particular element name
print("Where is 'gala apples' in the list index?")
print(groceries)
print(groceries.index("gala apples"))
print()

# Remove an element from the list based on the given element name
print("Picked up some sugar!")
groceries.remove("sugar")
print(groceries)
print()

# Remove an element from the list based on the given index
print("Actually, I don't need water. I have some at home...")
water_index = groceries.index("water")
groceries.pop(water_index)
print(groceries)
print()

# Remove the last element of the list
print("I'm going to pick up the last item on the list...")
groceries.pop(-1)
print(groceries)
print()

print("You continue on your journey purchasing groceries...")
