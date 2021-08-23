## Prework Module 3: Investing

---

### Overview

In this module, we will begin introducing some of the core concepts related to investing, why we want to invest, and some of the ways we can compare potential investments.

### Module Objectives

By the end of this module, you will be able to:

* Identify reasons for making investments and how risk influences profits

* Understand the importance of the time value of money, and how to discount a future value to a present one

* Understand the key concepts of Modern Portfolio Theory and how we can look at the efficient frontier to optimize a portfolio's risk-return profile


### Reading: Inflation and Investing

For a [variety of reasons](https://en.wikipedia.org/wiki/Inflation#Causes) the cost of goods and services in a market will increase over time, meaning that one dollar will buy less of a given good or service over time. We refer to this process of the devaluing of money over time as **inflation**. We often measure inflation using the [consumer price index](https://www.bls.gov/cpi), which essentially is an index that tracks the prices of a basket of goods and services over time. The central bank (a part of the government) attempts to keep inflation from getting too high in part through manipulation of the supply of money.

Due to a fear of inflation and a desire to generate profits, individuals and companies seek to make **investments** - purchase of an asset that will (hopefully) be worth a higher value at a later date and/or produce a stream of profits. All investments involve some amount of risk and thus are expected to make returns that are higher than the rate of inflation. In some investments, like loans, the interest rate is directly related to the amount of risk associated with the investment. In others, the reward to risk profile is less present, but still there. For example, equity investments in a company will often pay period cash flows (a dividend) and also increase in price over time. The riskier the equity, the higher the dividend yield, and anticipated future stock price. Equities are riskier than loans, and thus tend to have higher investment returns. Generally speaking, this means that while equity investments may not outperform bonds from one particular month to the next, they can be expected to outperform over the long run (e.g., 2 to 10+ years).

### Student Activity: Inflation Reflection

See instructions in [activity file](Activities/01-Stu_Inflation_Reflection/README.md)


### Reading: Time Value of Money

Which would you rather have: ``10,000`` today or ``10,000`` next year? If you had to choose one, you'd probably select today, because if you did, you can take that money and invest it. By the end of a year (if you invested wisely), you'd end up with more than $10,000. This is the time value of money: there's a benefit to having money now, rather than later.

We quantify that benefit from interest rates or the expected percentage return on capital. Put it this way: Would you rather have $10,000 now, or $10,010 a year from now? The latter option doesn't sound very appealing, does it? Indeed, that's only one-tenth of a percent of return. That doesn't even beat inflation--you'd effectively be losing money! But how about this: $10,000 now, or $15,000 in a year? A 50% annual return sounds pretty appealing.

These rates, 0.10%, and 50%--are interest rates or rates of return. In a competitive market, what goes into determining a particular interest rate ultimately depends on the alternative options the borrower and lender both have. If there's a lot of money looking to be parked somewhere, and no one really interested in borrowing, interest rates will drop. If people expect inflation to be really high, they'll only lend their money out if the interest rate is high enough to compensate them for that.

There's a way to compare money today versus money tomorrow. Money today, or in the present, is called **Present Value**, or PV. **Money tomorrow**, or in the future, is called Future Value, or FV. The two are linked by the expected return each time period. For example, to find out what $10,000 is worth 5 years from now, assuming a 10% annual return and assuming that profits are reinvested annually, we use this formula:

```
FV = PV * [1+(i/n)]^(n*t)
```

Where FV is the future value, PV is the past value, i is the interest rate, n is the number of compounding periods within a year, and t is the number of years:

```
FV = $10,000 * [1+(.10/1)]^(1*5)
FV = $10,000 * (1+.10)^5
FV = $16,105
```
Here, we assumed that our returns were re-invested each year. If we put these re-invested returns to work more quickly (perhaps if we received dividend payments every quarter, reinvesting as soon as they were received), our compounding period would be shorter. Since this means we'd be investing capital earlier, a more frequent compounding period means that we'll end up with slightly more investment return in the future. Taking the same example above, returns were the same, but the returns were re-invested quarterly, instead of annually (so that the annual 10% return were received and re-invested in four equal installments each year):
```
FV = $10,000 * [1+(.10/4)]^(4*5)
FV = $10,000 * (1+.025)^20
FV = $16,386
```
The annual return was the same, but we ended up with $281 more after five years because we consistently had a bit of a head start when re-investing those returns. This is why compound returns are important.

It's important to note that if you rearrange the above formula, you can solve for present value:

```
FV = PV * [1+(i/n)]^(n*t)
-->
PV = FV / [1+(i/n)]^(n*t)
```
A lot of financial models for valuing stocks, companies, and even real estate use this formula. Consider why with a simple example: If there was a building for sale that you knew would be worth $100,000 next year, but you were only considering investments yielding at least a 10% return, what's the maximum price you'd offer to buy it for?

     Future Value: You expect it's worth $100,000
     Your Required Return: 10%
     Time Horizon: 1 year
     Compounding Period: 1 (only at the end of the year do you finally sell the building and earn any cash)

     Using the Formula:
     PV = FV / [1+(i/n)]^(n*t)
     PV = $100,000 / (1+.10)^1
     PV = $90,909

You'd pay no more than $90,909 to acquire the building. Anything less, and your expected return would fall below 10%.

Real estate is not the only area that uses the present value to evaluate investments. Investment bankers use present value when trying to figure out how much a company might sell for. Venture capitalists estimate present value on more established start-ups to estimate how much a given equity funding round is worth. Stock traders will use their forecasts for what a stock will be worth in the future to estimate a fair price to pay for it today. In practice, the approach is a bit more involved for each of these scenarios (for example, a stock trader would need to find not just the present value of the expected future price of the stock, but also the present value of each expected dividend received while holding it), but the basic formula and principle is exactly the same. Present value is an important and frequently used concept in finance.



### Student Activity: Calculate TVM

See instructions in [activity file](Activities/02-Stu_Calculating_TVM/README.md)

### Modern Portfolio Theory

Now that we’ve talked about both risk and investments, we should discuss how to manage them together as part of a larger portfolio.

Imagine a portfolio containing three stocks that each achieve an annual return of five percent. However, all three of those stocks have a tendency to **not** move together on a daily basis: on a given day, one stock may have a positive return, whereas another will have a negative one. In other words, on a day-to-day basis, some of the ups and downs get "washed out", even if, over the long run each stock individually reaches 5%.

Therefore, if you absolutely knew that each stock's annual return was going to be 5%, would you be better off by buying only one stock, or a combination (portfolio) of all three? Does it matter?

As it turns out, it's wiser to have a portfolio of all three. That's because even if you knew both investment options would return 5% at the end of the year, the portfolio option is a lower risk bet: on any given day during that year, the value of that option will fluctuate less. You'll be more secure on a day-to-day basis the value of your investment.

Let's put it this way: Suppose you could choose two stocks, A or B. Both cost 5,000 initially, and both will be worth 10,000 in a year. You can wait a year, or you could sell and cash out anytime before that at whatever each is worth at that time. However, on any given day, Option A might range in worth from 2,000 to 8,000, whereas Option B will only range in value from 4,000 to 6,000. If you had to choose which one would you buy?

Unless you just like thrills, you'll probably select Option B. That's because it ultimately offers the same financial return ($10,000) for the same cost, but offers much less volatility (or uncertainty about what you could sell it for if you had to) in the meantime.

This is the essential idea behind Modern Portfolio Theory (MPT). A portfolio or asset is not only evaluated based on the returns that it makes, but also on how risky, or volatile, it is. Moreover, because some assets are less correlated with each other (when one goes up, the other goes down, and vice-versa), different investments can be strategically combined into a portfolio to reduce overall portfolio volatility.

Modern portfolio theory (MPT) helps us to optimize our return for given risk tolerance. The less tolerance we have about interim financial performance, the more we'll seek out assets that have lower volatility or that move less in tandem with the other investments that we have (less "correlation"). Wherever possible, we'll always try to find investments that have strong expected returns, yet each exhibits short-term performance that does not align with each other.

In sum, within MPT, we often analyze the volatility (large short-term movements in value) of individual stocks in order to understand their risk. We also evaluate the correlation stocks or how they move in comparison to each other. By balancing the assets in a portfolio, the risk associated with any given asset is partially mitigated by other assets. An ideal portfolio should attempt to not only produce strong returns but also minimize risk both as a whole.

Last, one of the most central ideas of MPT is the concept of an Efficient Frontier. When you have a lot of different individual investment choices, you can basically build any number of different portfolios, each a different combination of these individual assets. When plotting each potential portfolio's projected returns on one axis, and its projected risk (volatility) on the other, we can show a set of different portfolio options. From here, we can draw a curve, that for each level of risk, tells us the best portfolio (highest return) to select. This curve is the **Efficient Frontier**: the portfolio that provides the best return for a given tolerance of risk. The Efficient Frontier is used frequently in quantitative equity portfolio management: stock managers will select how much money to invest in each individual stock ("portfolio weightings") so that the expected return of the resulting portfolio is as high as possible for a given level of risk.

For those interested in taking a deeper dive into the updated Post-Modern Portfolio theory, definitely take a [look into the Wikipedia article](https://en.wikipedia.org/wiki/Post-modern_portfolio_theory) as delves into many of the fundamental statistical issues with MPT.

### Student Activity:

See instructions in the [activity file](Activities/03-Stu_Portfolio_Comparisons/README.md).
