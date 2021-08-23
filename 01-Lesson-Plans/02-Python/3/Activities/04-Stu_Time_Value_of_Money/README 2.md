# Zero-Coupon Bonds

In this activity, you will calculate the present value of a zero-coupon bond from its future value, and compare the resulting present value to its selling price in order to determine whether or not the bond is worth purchasing.

## Background

A zero-coupon bond is a debt security that does not pay interest (a coupon) as an annual cash flow; instead, it simply distributes a lump sum, or its face value, upon bond maturity (when the bond completes its duration). Zero-coupon bonds trade at a discount to their future value.

## Instructions

Using the [starter file](Unsolved/zero_coupon_bonds.py), walk through the following steps.

* Recreate the `present_value` formula as a function in Python. Make sure the function has the following parameters:

  * `future_value`: This is equivalent to the face value, or maturity value, of bonds; a lump sum given at the end of the duration of the bond.

  * `discount_rate`: This is the rate of return over the duration of the bond.

  * `compounding_periods`: Assumed to be equal to 1 for bonds.

  * `years`: The number of years constituting the duration of the bond.

* Pass the bond parameters into the `present_value` function and return the value to a variable `bond_value`.

* Compare the `bond_value` to its `price` and determine if the bond is worth purchasing or not.

  * If the bond is selling at a `discount`, purchase the bond.

  * Else if the bond is selling at a `premium`, do not purchase the bond.

  * Else the bond is selling at its fair market value, you're neutral to the decision.

## Hint

Don't overthink it! We are simply calculating the present value of a future value! If you need to refer to the present value formula, look to the slides.

---

© 2019 Trilogy Education Services
