# -*- coding: utf-8 -*-
"""Instructor Demo: Imports.

This script will showcase the use of imports of both custom code (functions.py)
and standard libraries (NumPy).
"""

# Call the print_hello() function via a reference to
# the imported module functions.py
import functions
functions.print_hello()

# Call the print_hello() function imported directly from functions.py
from functions import print_hello
print_hello()

# Import the NumPy library
import numpy

# Import the NumPy Financial library
import numpy_financial as npf

# Initialize variables
interest_rate = .1
cash_flows = [-1000, 400, 400, 400, 400]

#Call the NPV function from the NumPy Financial library
net_present_value = npf.npv(interest_rate, cash_flows)
print(f"NPV = {net_present_value}")
