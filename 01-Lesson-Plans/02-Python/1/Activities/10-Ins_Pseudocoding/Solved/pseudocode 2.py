"""
  Pseudocode for a cheer-leading program:

  1. Initialize "cheer" variable to a string to be cheered
  2. Create a for loop and iterate through each character in "cheer" variable
      2.1 Print each letter to screen with a cheer
  3. Print exclamations to screen ("Woohoo!!!")
"""

# Create a variable named cheer
cheer = "Python"

# Below strings can be used to add fun
cheer_symbol = "*\O/*"
cheer_symbol_2 = "ヘ( ^o^)ノ＼(^_^ )"

# Loop through string
for x in cheer:
    #Print each letter with a cheer
    print("Give me a " + x + "!")
    print(x + "!")

# Print excitement to screen
print("\nWhat does that spell?!")
print(cheer + "!\nWoohoo! Go " + cheer + "!")
print(cheer_symbol * 3)
print(cheer_symbol_2)

"""
Pseudocode for calculating simple interest:

  1. Initialize "principal", "interest_rate", and "time_period" variables to a float
  2. Compute "simple_interest" by multiplying principal, interest_rate, and time_period
  3. Print(simple_interest)
"""

# Declare floats for principal, interest_rate, and time_period
principal = 20000.00
interest_rate = 0.02
time_period = 4.0

# Compute simple interest
simple_interest = principal * interest_rate * time_period

# Print Results
print(f"Simple interest for this purchase would be: {simple_interest}.")

"""
Pseudocode for determining if credit should be acquired based off of simple interest:

1. Initialize "principal" and "interest_rate" variables to a float
2. Initialize "time_period" variable to an integer
3. Compute "simple_interest" by multiplying "principal", "interest_rate", and "time_period"
4. Determine if credit should be accepted
    IF "simple_interest" is less than or equal to 2000
        THEN print("We highly recommend you get this line of credit. Total simple interest paid is less than $2,000")
    ELSE If "simple_interest" is greater than 2000 but less than or equal to 4000
        THEN print("This is an okay deal. You might find better. Total simple interest paid will between $2,000 and $4,000")
    ELSE print("Total simple interest paid will be over $4,000. Do not accept this line of credit")
"""

# Declare floats for principal, interest_rate, and time_period
principal = 20000.00
interest_rate = 0.02
time_period = 4.0

# Compute simple interest
simple_interest = principal * interest_rate * time_period

# Print Results
print(f"Simple interest for this purchase would be: {simple_interest}.")

# Determine if credit should be accepted
if simple_interest <= 2000.0:
    print("I highly recommend you get this line of credit. Total simple interest paid is less than $2,000.")
elif simple_interest > 2000.0 <= 4000.0:
    print("This is an okay deal. You might find better. Total simple interest paid will between $2,000 and $4,000.")
else:
    print("Total simple interest paid will be over $4,000. Do not accept this line of credit.")
