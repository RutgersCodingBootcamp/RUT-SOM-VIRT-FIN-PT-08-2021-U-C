# Market Capitalization

In this activity, you will create a dictionary, and then update, remove, and extract values in/from the dictionary.

## Background

Sam wants to categorize banks by their market capitalizations, which is the total dollar market value of a company's outstanding shares. Because she wants to know the relationship between a certain bank and its market capitalization, Sam uses a dictionary to index bank names to the value of its market cap.

Sam needs to make a few changes to her dictionary of bank market caps because she noticed a few errors and omissions. Help Sam fix her dictionary of bank market caps, and even better, help her group the banks by their corresponding market capitalization tier.

## Instructions

Using the [starter file](Unsolved/Core/market_cap_core.py), complete the following:

- Initialize the dictionary of `banks`. Add the following key-value pairs:

  - JP Morgan Chase: 327
  - Bank of America: 302
  - Citigroup: 173
  - Wells Fargo: 273
  - Goldman Sachs: 87
  - Morgan Stanley: 72
  - U.S. Bancorp: 83
  - TD Bank: 108
  - PNC Financial Services: 67
  - Capital One: 47
  - FNB Corporation: 4
  - First Hawaiian Bank: 3
  - Ally Financial: 12
  - Wachovia: 145
  - Republic Bancorp: .97

- Change the market cap for `Citigroup` to `170`.

- Add a new bank `American Express` to the dictionary and set the market cap to `33`.

- Delete `Wachovia` from the dictionary, as it is a deprecated bank acquired by Wells Fargo in 2008.

## Challenge

Group banks by their corresponding market capitalization tier.

- Iterate over the key-value pairs in the `banks` dictionary and calculate the following:

  - Total market capitalization
  - Total number of banks
  - Average market capitalization
  - Largest bank
  - Smallest bank

- Use an if-else statement and lists to compare and group banks by their corresponding market capitalization: `mega-cap`, `large-cap`, `mid-cap`, and `small-cap`.

  - `mega-cap`: Market capitalization greater than or equal to \$300 billion.

  - `large-cap`: Market capitalization greater than or equal to $10 billion and less than $300 billion.

  - `mid-cap`: Market capitalization greater than or equal to $2 and less than $10 billion.

  - `small-cap`: Market capitalization greater than or equal to $300 million and less than $2 billion.

## Hint

Your results should look similar to the following:

```
Total Market Capitalization: 1588
Total Numer of Banks: 15
Average Market Capitalization: 105.87
Largest Bank: JP Morgan Chase
Smallest Bank: Republic Bancorp
------------------------------------------------
Mega Cap Banks: ['JP Morgan Chase', 'Bank of America']
Large Cap Banks: ['Citigroup', 'Wells Fargo', 'Goldman Sachs', 'Morgan Stanley', 'U.S. Bancorp', 'TD Bank', 'PNC Financial Services', 'Capital One', 'Ally Financial', 'American Express']
Mid Cap Banks: ['FNB Corporation', 'First Hawaiian Bank']
Small Cap Banks: ['Republic Bancorp']
```

---

© 2019 Trilogy Education Services
