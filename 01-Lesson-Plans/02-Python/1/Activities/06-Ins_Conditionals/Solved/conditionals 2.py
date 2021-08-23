# Demonstrate conditional statement
if True:
    # Do something
else:
    # Do something else

# Demonstrate conditional with print statement
is_raining = True
if is_raining:
    print("Bring an umbrella!")
else:
    print("Leave the umbrella at home!")

# Demonstrate equality
x = 5
if x == 1:
    print("x is equal to 1")

# Demonstrate using variables to store conditions
x = 5
y = 10
if x == y:
    print("x is equal to y")

# Check inequality
y = 9
if y != 1:
    print("y is not equal to 1")

# Declare variables and values for evaluation
x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")

# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")

# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned True")

# Checks for two conditions to be met using and
if x == 1 and y < 10:
    print("Both values returned True")

# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were True")

# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

# Nested if statements with insurance premium predictor
accident = True
at_fault = False
accident_forgiveness = True
elite_status = True

increase_insurance_premium = True

print("Insurance premium will increase. True or False?")

# Nested Conditional Statements
if accident:
    if at_fault and accident_forgiveness:
        increase_insurance_premium = False
    elif at_fault and not accident_forgiveness and not elite_status:
        increase_insurance_premium = True
    else:
        increase_insurance_premium = False
elif not accident and elite_status:
    increase_insurance_premium = False
else:
    increase_insurance_premium = True

print(f"Prediction: {increase_insurance_premium}")
