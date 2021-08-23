"""
Conditionally Yours

Pseudocode:
1. Initialize variables original_price, current_price, increase, percent_increase, recommendation, threshold_to_buy, and threshold_to_sell
2. Compoute increase
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
"""
