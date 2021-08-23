# -*- coding: utf-8 -*-
"""
Student Do: Iterate Lists.

This script demonstrates how to iterate over lists to calculate common summary statistics/metrics.
"""

# Initialize the metric variables
count = 0
total = 0
average = 0
minimum = 0
maximum = 0

# List of daily tips
cash_tips = [22, 10, 30, 45, 54, 60, 56]

# Showcase every tip in the list
for tip in cash_tips:
    print(tip)

# Iterate over each element of the list to determine metrics
for tip in cash_tips:

    # Cumulatively sum up the total and count of tips
    total += tip
    count += 1

    # Logic to determine minimum values
    if minimum == 0:
        minimum = tip
    elif tip < minimum:
        minimum = tip
        
    # Logic to determine maximum values        
    if tip > maximum:
        maximum = tip

# Calculate the average
average = round(total / count, 2)

# Print out the summary statistics
print("---------Summary Statistics----------")
print(f"Number of Days: {count}")
print(f"Total Tips: {total}")
print(f"Daily Average: {average}")
print(f"Least Amount of Tips: {minimum}")
print(f"Maximum Amount of Tips: {maximum}")


