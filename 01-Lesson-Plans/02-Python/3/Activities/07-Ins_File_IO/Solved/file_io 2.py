# -*- coding: utf-8 -*-
"""Instructor Demo: File IO.

This script will use the Pathlib library to set the file path
and Python's built-in open() function to read in a text file. Then
write the contents to an output file.
"""

# Import from the pathlib library, the main class Path
from pathlib import Path

# Check the current directory where the Python program is executing from
print(f"Current Working Directory: {Path.cwd()}")

# Set the path normally (Windows)
# Set string raw literal due to backslashes acting as escape characters for
# the Windows file = r'..\Resources\input.txt'

# Set the path normally (Unix)
#file = '../Resources/input.txt'

# Set the input file path irregardless of OS
filepath = Path("../Resources/input.txt")

# Open the file in "read" mode ('r') and store the
# contents in the variable "text"
with open(filepath, 'r') as file:
    # Store all of the text from the file inside a variable called "text"
    # and print the contexts of the text file
    text = file.read()
    print(text)

    # Parse and print the file line by line. The print statement adds an
    # extra line break to each line in the output.
    line_num = 1
    for line in file:
        print(f"line {line_num}: {line}")
        line_num += 1

# Set the output file path
output_path = Path("output.txt")

# Open the output_path as a file object in "write" mode ('w')
# Write a header line and write the contents of 'text' to the file
with open(output_path, 'w') as file:
    file.write("This is an output file.\n")
    file.write(text)
