# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# @TODO: Import the pathlib and csv library



# @TODO: Set the file path


# Initialize list of records
records = []

# @TODO: Open the csv file as an object


    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object

    # @TODO: Read the header row

    # @TODO: Print the header


    # @TODO: Append the column 'Average' to the header

    # @TODO: Append the header to the list of records


    # @TODO: Read each row of data after the header

        # @TODO: Print the row

        # @TODO:
        # Set the 'name', 'count', 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations




        # @TODO: Calculate the average (round to the nearest 2 decimal places)


        # @TODO: Append the average to the row

        # @TODO: Append the row to the list of records


# @TODO: Set the path for the output.csv

# @TODO:
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','


    # @TODO:
    # Loop through the list of records and write every record to the
    # output csv file
