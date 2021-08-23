# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# Initialize the metric variables
count = 0
total = 0
average = 0
minimum = 0
maximum = 0

# Initialize lists to hold profitable and unprofitable day profits/losses
profitable_days = []
unprofitable_days = []

# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# Iterate over each element of the list
for day_pnl in trading_pnl:

    # Cumulatively sum up the total profits/losses and count of trading days
    total += day_pnl
    count += 1

    # Logic to determine minimum and maximum values
    if minimum == 0:
        minimum = day_pnl
    elif day_pnl < minimum:
        minimum = day_pnl
    elif day_pnl > maximum:
        maximum = day_pnl

    # Logic to determine profitable vs. unprofitable days
    if day_pnl > 0:
        profitable_days.append(day_pnl)
    elif day_pnl <= 0:
        unprofitable_days.append(day_pnl)

# Calculate the average
average = round(total / count, 2)

# Count metrics
profitable_count = len(profitable_days)
unprofitable_count = len(unprofitable_days)

# Percentage metrics
percent_profitable = profitable_count / count * 100
percent_unprofitable = unprofitable_count / count * 100

# Print out the summary statistics
print("---------Summary Statistics----------")
print(f"Number of Total Days: {count}")
print(f"Number of Profitable Days: {profitable_count}")
print(f"Number of Unprofitable Days: {unprofitable_count}")
print(f"Percentage of Profitable Days: {percent_profitable}%")
print(f"Percentage of Unprofitable Days: {percent_unprofitable}%")
print("-------------------------------------")
print(f"Profitable Days: {profitable_days}")
print(f"Unprofitable Days: {unprofitable_days}")
print("-------------------------------------")
print(f"Total Profits/Losses: {total}")
print(f"Daily Average: {average}")
print(f"Worst Loss: {minimum}")
print(f"Best Gain: {maximum}")
