# Net Present Value

In this activity, you will conduct financial analysis on three potential company projects that are categorized as conservative, neutral, and aggressive. Then, you will use the NPV function to determine which project scenario is the optimal choice.

## Background

NPV, or net present value, compares the initial investment of a project to the sum of all the present values of the subsequent projected cash flows. Positive NPV values indicate a project that is profitable and should be considered; negative NPV values indicate a project that is not profitable and should not be considered.

In this activity, you will conduct financial analysis on three project scenarios: conservative, neutral, and aggressive. Each scenario requires an initial investment to generate the resulting cash flows for the following four years.

You will use the NPV function from the NumPy Financial library to calculate the NPV values for each project scenario, and determine the scenario that has the highest NPV value, or the project that is the optimal choice.

## Instructions

Use the [starter file](Unsolved/Core/net_present_value_core.py) to complete the following steps.

1. Import the NumPy Financial (`numpy_financial`) library. You may need to run `pip install numpy-financial` in your terminal in order to install this library.

2. Call the NumPy Financial NPV function for each of the three project scenarios (conservative, neutral, aggressive).

3. Assign the return values to a corresponding scenario key in a `npv_dict` dictionary.

4. Print out the project scenario that holds the max NPV value from the `npv_dict` dictionary.

Your results should look similar to the following:

```
{'conservative': 267.94617853971704, 'neutral': 401.91926780957544, 'aggressive': 285.8923570794341}
The optimal project scenario to undertake is 'neutral' with a NPV of 401.91926780957544
```

## Challenge

Use a for loop and an if-else conditional to calculate the max NPV value and associated key from the `npv_dict` dictionary. This will eliminate the need to manually choose the project scenario that has the max NPV value.

Your results should look similar to the following:

```
conservative 267.94617853971704
neutral 401.91926780957544
aggressive 285.8923570794341
---------------------------------------------------------
The project scenario with the max NPV value is 'neutral' with a NPV of 401.91926780957544
```

---

© 2020 Trilogy Education Services
