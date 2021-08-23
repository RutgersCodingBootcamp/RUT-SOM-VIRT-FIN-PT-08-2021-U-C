"""
Conditionally Yours

Pseudocode:
1. Initialize variables original_price, current_price, increase, percent_increase, recommendation, threshold_to_buy, and threshold_to_sell
2. Compute increase
3. Compute percent_increase
4. IF percent_increase is greater than or equal to threshold_to_sell
        THEN Set recommendation to "sell"
    ELSE IF percent_increase is less than or equal to threshold_to_buy
        THEN set recommendation to "buy"
    ELSE IF percent_increase is less than threshold_to_sell and greater than threshold_to_buy
        THEN set recommendation to "hold"
    ELSE
        THEN print("Not enough data to make a decision. Need human input")
5. Print("Recommendation: " + recommendation)
6. Initialize variable balance as float
7. Compute balance_check
8. Print balance
9. IF recommendation equals "buy" and balance_check is greater than current_price
        THEN print(recommendation)
    ELSE IF recommendation equals buy and balance_check is less than current_price
        THEN print("You should buy, but you don't have enough capital")
    ELSE
        print(recommendation)
"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
original_price = 360.35

# Create integer variable for current_price
current_price = 293.33

# Create float for threshold_to_buy
threshold_to_buy = -10.00

# Create float for threshold_to_sell
threshold_to_sell = 20.00

# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase / original_price) * 100

# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price is ${current_price}")

# Print percent increase
print("Netflix's stock price changed by", "{:.2f}%".format(percent_increase))

# Determine if stock should be bought or sold
if percent_increase >= threshold_to_sell:
    recommendation = "sell"
elif percent_increase <= threshold_to_buy:
    recommendation = "buy"
elif percent_increase < threshold_to_sell and percent_increase > threshold_to_buy:
    recommendation = "hold"
else:
    print("Not enough data to make a decision. Need human input.")

print("Recommendation: " + recommendation)
print()
print("But wait a minute... lets check your excess equity first.")

# Challenge

# Create float for portfolio balance
balance = 5000.00

#Create float for balance check
balance_check = balance * 5

# Compare balance to recommendation
print(f"You currently have ${balance} in excess equity available in your portfolio.")

if recommendation == "buy" and balance_check > current_price:
    print("Final Recommendation: " + recommendation)
elif recommendation == "buy" and balance_check < current_price:
    print("Final Recommendation: You should buy. But you don't have enough available capital.")
else:
    print("Final Recommendation: " + recommendation)
