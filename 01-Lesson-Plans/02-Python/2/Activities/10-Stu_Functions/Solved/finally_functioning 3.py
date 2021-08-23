"""
Determine the Compound Annual Growth Rate for an investment
"""

# Declare a variable beginning_balance as a float
beginning_balance = 29000.00

# Declare a variable ending_balance as float
ending_balance = 45000.10

# Declare a variable years as an int
years = 1.0

# Define a function called calculate_compound_growth_rate with three arguments: beginning_balance, ending_balance, years. Function should output growth_rate.
def calculate_compound_growth_rate(beginning_balance, ending_balance, years):
    growth_rate = (ending_balance / beginning_balance)**(1/years) - 1
    return growth_rate

# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_one_growth.
year_one_growth = calculate_compound_growth_rate(beginning_balance, ending_balance, years)

# Update beginning_balance and ending balance for year two, and then execute calculate_compound_growth_rate and capture as year_two_growth.
beginning_balance = 45000.10
ending_balance = 47000.00
year_two_growth = calculate_compound_growth_rate(beginning_balance, ending_balance, years)

# Update beginning_balance and ending balance for year three, and then execute calculate_compound_growth_rate and capture as year_three_growth.
beginning_balance = 47000.00
ending_balance = 48930.00
year_three_growth = calculate_compound_growth_rate(beginning_balance, ending_balance, years)

# Use round function to round variables
year_one_growth_rnd = round(year_one_growth,2)
year_two_growth_rnd = round(year_two_growth,2)
year_three_growth_rnd = round(year_three_growth,2)

print(f"Compound Annual Growth Rate for 2016: {year_one_growth_rnd}%")
print(f"Compound Annual Growth Rate for 2016: {year_two_growth_rnd}%")
print(f"Compound Annual Growth Rate for 2016: {year_three_growth_rnd}%")

# Challenge

# Create a global, empty list
growth_rates = list()

# Define a function called
def calculate_compound_growth_rate_list(beginning_balance, ending_balance, years):
    growth_rate = (ending_balance / beginning_balance)**(1/years) - 1

    # Populate growth_rates
    growth_rates.append(growth_rate)

# Populate growth_rates list with 2016 values by calling calculate_compound_growth_rate_list.
beginning_balance = 29000.00
ending_balance = 45000.10
calculate_compound_growth_rate_list(beginning_balance, ending_balance, years)

# Populate growth_rates list with 2017 values by calling calculate_compound_growth_rate_list.
beginning_balance = 45000.10
ending_balance = 47000.00
calculate_compound_growth_rate_list(beginning_balance, ending_balance, years)

# Populate growth_rates list with 2018 values by calling calculate_compound_growth_rate_list.
beginning_balance = 47000.00
ending_balance = 48930.00
calculate_compound_growth_rate_list(beginning_balance, ending_balance, years)

# Print growth_rates list
print("Growth rates: ", growth_rates)
