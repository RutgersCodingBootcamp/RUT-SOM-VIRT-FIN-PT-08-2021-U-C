# Trading Log

In this activity, you will use lists to create a trading log that tracks profits and losses for each market day of the month. You will iterate over the list to calculate the highest and lowest profit and loss days. The goal of this activity is to use for loops and lists in order to track metrics related to trading performance.

## Background

Karen, an equity trader, has been tracking her profits and losses over the course of the last 20 business days. She wants to quickly analyze her ongoing performance as she continues to log her profits and losses every day. Understanding her profits and losses each day will allow Karen to evaluate her performance for all trades monthly, weekly, and over time. Help Karen create a program to analyze her results.

## Instructions

Using the [starter file](Unsolved/trading_log.py), complete the following:

* Create a for loop over the `trading_pnl` list object, and cumulatively sum up the `total` profits/losses and the `count` of actual trading days.

* Use an if-else statement to calculate the `maximum` and `minimum` profit/loss values. In other words, find the numerical value of the best and worst trading days.

* Create additional lists `profitable_days` and `unprofitable_days` and use if-else statements to group daily trading values into each corresponding list.

* Determine the following:

  * Number of total trading days

  * Total profits and losses

  * Daily average profit and loss

  * Worst loss

  * Best gain

  * Number of profitable days

  * Number of unprofitable days

  * Percentage of profitable days

  * Percentage of unprofitable days

  * Print the values of only profitable days.

  * Print the values of only unprofitable days.

## Hints

Use the below formulas:

* Number of total trading days = length of `trading_pnl`

* Profit = `trading_pnl` value is greater than 0

* Loss = `trading_pnl` value is less than 0

* Total profits/losses = sum of `trading_pnl`

* Daily average profit/loss = total profits/losses divided by number of total trading days

* Worst loss = smallest number in `unprofitable_days`

* Best gain = largest number in `profitable_days`

* Percentage of profitable days = number of profitable days divided by number of total trading days, multiplied by 100

Your results should look similar to the following:

```
---------Summary Statistics----------
Number of Total Days: 20
Number of Profitable Days: 13
Number of Unprofitable Days: 7
Percentage of Profitable Days: 65.0%
Percentage of Unprofitable Days: 35.0%
-------------------------------------
Profitable Days: [352, 252, 354, 56, 123, 254, 325, 47, 321, 123, 133, 613, 232]
Unprofitable Days: [-224, -544, -650, -43, -123, -151, -311]
-------------------------------------
Total Profits/Losses: 1139
Daily Average: 56.95
Worst Loss: -650
Best Gain: 613
```

Refer to this [article](https://www.investopedia.com/terms/p/plstatement.asp) for more information regarding profit and loss statements.

---

© 2019 Trilogy Education Services
