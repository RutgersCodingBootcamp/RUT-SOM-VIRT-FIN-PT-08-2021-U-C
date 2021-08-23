# E-Commerce Traffic

In this activity, you will parse a text file. You will also sum the total number of customers and count of days in the text file to calculate the daily average of customer traffic for your e-commerce business. Assume each line is equal to a day's worth of customers.

## Instructions

Using the [starter file](Unsolved/ecommerce_traffic.py), complete the following steps.

1. Import the pathlib library.

2. Set the file path for the `customer_traffic.txt` data file.

3. Initialize the `customer_total` and `day_count` variables that will hold the total and count of the numbers in the text file, respectively.

4. Use the file path pointing to the `customer_traffic.txt` data file to open the file as an object.

5. Iterate over each line in the file and cumulatively add to the `customer_total` and `day_count` variables. You will need to convert the number from the text file as an int to perform numerical calculations.

6. Write the contents of the `customer_total`, `day_count`, and `daily_average` to an `output.txt` file. Your `output.txt` file should look similar to the following code block:

    ```
    The total and count of the numbers in the text file are 4945 and 100, respectively. The average is 49.45.
    ```

## Hint

You already know a lot of the concepts needed to complete this activity, like variables, for loops, and formatted strings. Just take it step by step; don't let file paths and reading and writing to/from a file throw you off!

---

© 2019 Trilogy Education Services
