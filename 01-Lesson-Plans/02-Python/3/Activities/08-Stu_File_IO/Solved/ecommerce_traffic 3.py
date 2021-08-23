# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# From the pathlib library, import the main class Path
from pathlib import Path

# Check the current directory where the Python program is executing from
print(f"Current Working Directory: {Path.cwd()}")

# Set the path using Pathlib
file = Path('../Resources/customer_traffic.txt')

# Initialize variables
customer_total = 0
day_count = 0

# Open the file in "read" mode ('r') and
# store the contents in the variable 'file'
with open(file, 'r') as file:
    # Parse the file line by line
    for line in file:

        # Convert the number in the text file from string to int
        number = int(line)

        # Sum the total and count of the numbers in the text file
        customer_total += number
        day_count += 1

# Print out customer_total and day_count
print(f"customer_total: {customer_total}")
print(f"day_count: {day_count}")
print("-----------------------")

# Calculate the average
daily_average = customer_total / day_count
print(f"daily_average: {daily_average}")

# Set output file name
output_path = 'output.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    # Write daily_average to the output file, convert to string
    file.write(f"There were {customer_total} customers over the course of {day_count} days.\n")
    file.write(f"The average daily customer traffic is {daily_average} customers per day.")
