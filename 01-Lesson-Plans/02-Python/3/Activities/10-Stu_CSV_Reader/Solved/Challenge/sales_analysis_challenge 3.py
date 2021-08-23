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
csvpath = Path("../../Resources/sales.csv")

# Initialize dictionary
analysis = {}

# Open the csv file as an object
with open(csvpath, "r") as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Print the header
    print(csv_header)

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

        # If name is not already in the analysis dict, initialize the dictionary
        # Else continue to add to the existing key and nested key-value pairs
        if name not in analysis.keys():
            analysis[name] = {"count": count, "revenue": revenue}
        else:
            analysis[name]["count"] += count
            analysis[name]["revenue"] += revenue

# Set the header for aggregate.csv
header = ["Name", "Count", "Revenue", "Average"]

# Set the path for the aggregate.csv
aggregate_path = Path("aggregate.csv")

# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','
with open(aggregate_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header as the first row
    csvwriter.writerow(header)

    # Loop over every key in analysis and write the associated key (name) and
    # nested key-value pairs (metrics)
    for name in analysis:
        csvwriter.writerow(
            [
                name,
                analysis[name]["count"],
                analysis[name]["revenue"],
                round(analysis[name]["revenue"] / analysis[name]["count"], 2),
            ]
        )
