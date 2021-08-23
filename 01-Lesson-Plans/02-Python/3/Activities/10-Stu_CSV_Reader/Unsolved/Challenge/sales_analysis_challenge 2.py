# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# @TODO: Import the pathlib and csv library



# @TODO: Set the file path


# @TODO: Initialize dictionary


# @TODO: Open the csv file as an object

    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object


    # @TODO: Read the header row first (skip this step if there is no header)

    # @TODO: Print the header


    # @TODO: Read each row of data after the header

        # @TODO: Print the row

        # @TODO:
        # Set the 'name', 'count', and 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations




        # @TODO: Calculate the average and round to the nearest 2 decimal places

        # @TODO:
        # If name is not already in the analysis dict, initialize the dictionary
        # Else continue to add to the existing key and nested key-value pairs






# @TODO: Set the header for aggregate.csv


# @TODO: Set the path for the aggregate.csv

# @TODO:
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','



    # @TODO: Write the header as the first row

    # @TODO:
    # Loop over every key in analysis and write the associated key (name) and
    # nested key-value pairs (metrics)
