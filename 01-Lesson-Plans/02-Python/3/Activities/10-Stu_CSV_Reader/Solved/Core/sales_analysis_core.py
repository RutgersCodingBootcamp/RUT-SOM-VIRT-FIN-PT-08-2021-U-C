# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('../../Resources/sales.csv')

# Initialize list of records
records = []

# Open the csv file as an object
with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Print the header
    print(csv_header)

    # Append the column 'Average' to the header
    csv_header.append("Average")
    # Append the header to the list of records
    records.append(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)

        # Set the 'name', 'count', and 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations
        name = row[0]
        count = int(row[1])
        revenue = int(row[2])

        # Calculate the average and round to the nearest 2 decimal places
        average = round(revenue / count, 2)

        # Append the average to the row
        row.append(average)
        # Append the row to the list of records
        records.append(row)

# Set the path for the output.csv
output = Path("output.csv")

# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Loop through the list of records and write every record to the
    # output csv file
    for record in records:
        csvwriter.writerow(record)
