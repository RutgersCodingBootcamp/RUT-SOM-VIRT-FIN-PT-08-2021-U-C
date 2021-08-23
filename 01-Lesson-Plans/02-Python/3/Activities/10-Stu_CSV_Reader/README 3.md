# Sales Analysis

In this activity, you will read in the `sales.csv` file to calculate customer revenue averages.

## Instructions

Using the [starter file](Unsolved/Core/sales_analysis_core.py), complete the following steps.

1. Import the pathlib and CSV libraries.

2. Set the `sales.csv` path.

3. Initialize a `records` list.

4. Read and iterate over the `sales.csv` file using `csv.reader()`.

5. Append a new column, average, to the header, and then add the header to the list of records.

6. Set the `name`, `count`, and `revenue` variables and convert strings to ints for numerical calculations.

7. Calculate the simple average (`revenue` over `count`), append the average to the row, and append the row to the list of records.

8. Write the list of records contained in `records` to an output CSV file.

9. Loop over every record in `records`, and use the `writerow()` function to write to an output CSV file.

Your output should look similar to the following:

  ```python
  Name,Count,Revenue,Average
  Andrew,9,58,6.44
  Phil,8,377,47.12
  Madison,5,302,60.4
  Sally,1,75,75.0
  Tyler,1,334,334.0
  Billy,7,146,20.86
  Steve,1,178,178.0
  Madison,7,313,44.71
  Sarah,8,103,12.88
  Tim,5,344,68.8
  Andrew,5,349,69.8
  Phil,8,61,7.62
  Madison,4,196,49.0
  Carl,1,374,374.0
  Devon,9,220,24.44
  Megan,9,321,35.67
  Sarah,7,277,39.57
  David,2,246,123.0
  Sally,9,198,22.0
  Tom,5,221,44.2
  Andrew,1,191,191.0
  Paul,5,399,79.8
  Carl,1,300,300.0
  Tim,1,345,345.0
  Madison,4,202,50.5
  John,4,305,76.25
  Phil,6,249,41.5
  Madison,7,113,16.14
  Sally,6,256,42.67
  ```

## Challenge

Calculate the aggregate average for each unique customer name and output to a CSV file by completing the following steps:

1. Initialize an `analysis` dictionary.

2. Read and iterate over the `sales.csv` file using `csv.reader()`. Use an if-else statement to check the following:

    * If the customer name is not already in the `analysis` dictionary, initialize the nested key-value pairs `count` and `revenue`.

      ```python
      analysis[name] = {
          "count": count,
          "revenue": revenue
      }
      ```

    * Else the customer name is already in the `analysis` dictionary, cumulatively add the `count` and `revenue` nested key-value pairs.

      ```python
      analysis[name]['count'] += count
          analysis[name]['revenue'] += revenue
      ```

3. Set the output file path for `aggregate.csv`.

4. Write the contents of the `analysis` dictionary to `output.csv` using `csv.writer()`. Be sure to add a header to the CSV file.

Your output should look similar to the following:

```
Name,Count,Revenue,Average
Andrew,15,598,39.87
Phil,22,687,31.23
Madison,27,1126,41.7
Sally,16,529,33.06
Tyler,1,334,334.0
Billy,7,146,20.86
Steve,1,178,178.0
Sarah,15,380,25.33
Tim,6,689,114.83
Carl,2,674,337.0
Devon,9,220,24.44
Megan,9,321,35.67
David,2,246,123.0
Tom,5,221,44.2
Paul,5,399,79.8
John,4,305,76.25
```

## Hint

Remember that the `csvwriter.writerow()` takes in lists!

---

© 2019 Trilogy Education Services
