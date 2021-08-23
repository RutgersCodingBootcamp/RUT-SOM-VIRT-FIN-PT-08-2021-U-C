## 2.3 Lesson Plan: Functions and Files

### Overview

This lesson focuses on financial functions, file I/O, and working with CSV files. Students will practice basic financial analysis skills in the context of both internal (hard-coded) and external (file I/O) manipulation of data.

### Class Objectives

By the end of this class, students will be able to:

- Define time value of money and explain how it relates to net present value via discounted future values/cash flows.

- Perform basic financial analysis from user-defined financial functions (NPV).

- Import standard and custom Python libraries.

- Read and write text files.

- Identify tabular data and its form.

- Read and write CSV files.

---

### Instructor Notes

- Today’s class will introduce concepts like time value of money, zero-coupon bonds, and net present value. Take your time as you review these topics; a few extra moments to answer questions and review complex concepts goes a long way in aiding comprehension, especially if the majority of the class seems to be struggling.

- Students need to have a thorough understanding of financial concepts and how they are used in order to develop a mindset for solving financial use cases programmatically. Make sure to relate each financial use case to its corresponding programmatic process.

- Remember that students most likely have varying levels of finance experience. Therefore, make sure your lectures are clear and thorough for newcomers while serving as interesting refreshers for veterans. Draw upon your industry experience or tell a story that relates to the concepts at hand; make things simple to understand as well as memorable!

- Make sure TAs circulate the classroom to provide assistance to students who are still struggling with Python concepts. If the lesson moves ahead of schedule, you can use the extra time to review those topics.

- Remind students to activate their conda environment so that they can access libraries like NumPy (and its financial cousin, numpy_financial), which they will need for this lesson. If they have issues importing the NumPy library, suggest running `conda install anaconda` or `conda install numpy`. The conda environment may not have included the Anaconda tools, as this is a common error.

  * `numpy` and  `numpy_financial` are two separate packages that will both need to be installed for this lesson.

  * To install `numpy_financial` run the commnd `conda install -c conda-forge numpy-financial`.

- Make sure that students are properly setting their file paths when reading in files. Ensure that their paths are properly set and look out for erroneous relative or absolute paths.

- The pathlib library allows students to ignore the differences between Windows OS `\` back slashes and Unix-based OS `/` forward slashes in regard to file paths. However, they should still be aware of these differences in case they are not able to access the pathlib library.

- Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [2.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2599df21-0a03-4b4f-94aa-aaa0004756ce) Note that this video may not reflect the most recent lesson plan.

### Class Slides and Time Tracker

- The slides for this lesson can be viewed on Google Drive here: [Lesson 2.3 Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss).

- To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

- **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

- The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Review (10 min)

**Corresponding Activity:** [01-Ins_Refresher](Activities/01-Ins_Refresher)

In this section, welcome students to class, review the lesson objectives, and complete a review activity.

**Files:**

- [Welcome Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss)

- [refresher.py](Activities/01-Ins_Refresher/Solved/refresher.py)

Welcome students back to class. Tell them that in today's lesson we will begin to apply Python concepts to financial use cases. Today will be fun!

Use the [slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57c97b9346_4_1) to review the class objectives.

Use the solution file to perform a live coding session and quickly recap concepts learned in previous classes. During the session, ask the following questions:

- What are variables?

  **Answer:** Variables are reserved memory allocations that are used to store information that can be referenced and manipulated later.

  ```python
  # Creates a variable with a string "Frankfurter"
  title = "Frankfurter"
  years = 23
  hourly_wage = 65.40
  expert_status = True
  ```

- What are conditionals?

  **Answer:** Conditionals are if-else statements that make true or false comparisons that determine corresponding actions for either scenario.

  ```python
  # Declare variables and values for evaluation
  x = 1
  y = 10

  # Checks if one value is equal to another
  if x == 1:
      print("x is equal to 1")
  ```

  ```
  x is equal to 1
  ```

- What are lists?

  **Answer:** Lists are mutable (changeable), ordered data structures that hold data of a single type.

  ```python
  # Create a list of Pokemon
  print("Creating a list of Pokemon...")
  pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx"]
  print(pokemon)
  ```

  ```
  ['Pikachu', 'Charizard', 'Bulbasaur', 'Gyarados', 'Dragonite', 'Onyx']
  ```

- What are dicts?

  **Answer:** Dicts are mutable (changeable), unordered data structures that hold key-value pairs of potentially varying data types.

  ```python
  # Initialize a dictionary
  trading_pnl = {
      "title": "Trading Log",
      "03-18-2019": -224,
      "03-19-2019": 352,
      "03-20-2019": 252,
      "03-21-2019": 354,
      "03-22-2019": -544,
      "03-23-2019": -650,
      "03-24-2019": 56,
      "03-25-2019": 123,
      "03-26-2019": -43,
      "03-27-2019": 254,
      "03-28-2019": 325,
      "03-29-2019": -123,
      "03-30-2019": 47,
      "03-31-2019": 321,
      "04-01-2019": 123,
      "04-02-2019": 133,
      "04-03-2019": -151,
      "04-04-2019": 613,
      "04-05-2019": 232,
      "04-06-2019": -311
  }
  ```

  ```
  {'title': 'Trading Log', '03-18-2019': -224, '03-19-2019': 352, '03-20-2019': 252, '03-21-2019': 354, '03-22-2019': -544, '03-23-2019': -650, '03-24-2019': 56, '03-25-2019': 123, '03-26-2019': -43, '03-27-2019': 254, '03-28-2019': 325, '03-29-2019': -123, '03-30-2019': 47, '03-31-2019': 321, '04-01-2019': 123, '04-02-2019': 133, '04-03-2019': -151, '04-04-2019': 613, '04-05-2019': 232, '04-06-2019': -311}
  ```

- What are for loops?

  **Answer:** For loops are blocks of code that allow you to repeat a process a fixed number of times.

  ```python
  # Loop through a range of numbers (0 through 4)
  for x in range(5):
      print(x)
  ```

  ```
  0
  1
  2
  3
  4
  ```

- What are functions?

  **Answer:** Functions are callable blocks of reusable code that perform an action.

  ```python
  # Define a main function that accepts a string argument
  def main(stock_ticker):
      print(stock_ticker + " is booming right now!")

  stock_ticker = "SBUX"
  main(stock_ticker)
  ```

  ```
  SBUX is booming right now!
  ```

- How do you traverse, or access, nested objects?

  **Answer:** Specify the index for each level of iteration.

  ```python
  # List of Dicts
  ceo_nested_dict = [
      {
          "name": "Warren Buffet",
          "age": 88,
          "occupation": "CEO of Berkshire Hathaway"
      },
      {
          "name": "Jeff Bezos",
          "age": 55,
          "occupation": "CEO of Amazon"
      },
      {
          "name": "Harry Markowitz",
          "age": 91,
          "occupation": "Professor of Finance"
      }
  ]

  print(ceo_nested_dict[0]['occupation'])
  ```

  ```
  CEO of Berkshire Hathaway
  ```

Ask if there are any questions before moving on.

---

### 2. Student Do: Refresher Activity (15 min)

**Corresponding Activity:** [02-Stu_Refresher](Activities/02-Stu_Refresher)

In this activity, students will apply skills learned in the previous lessons to a financial use case. They will act as analysts who categorize customers based on revenue and assign each customer a business tier: platinum, gold, silver, or bronze. A personalized message is generated for each customer depending on the assigned business tier.

**File:** [Starter Code](Activities/02-Stu_Refresher/Unsolved/marketing.py)

**Instructions:** [README.md](Activities/02-Stu_Refresher/README.md)

### 3. Instructor Do: Review Refresher Activity (10 min)

Take some time to review the previous refresher activity with students.

**File:** [Solution](Activities/02-Stu_Refresher/Solved/marketing.py)

Open the [solution file](Activities/02-Stu_Refresher/Solved/marketing.py) to review the solution and explain the following:

- The `customers` list is a nested list of dictionaries that represents a collection of customer records, with each record containing `first_name`, `last_name`, and `revenue` key-value pairs.

  ```python
  # List of dicts
  customers = [
      { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
      { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
      { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
      { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
  ]
  ```

- The `create_greeting()` function takes in three parameters––`first_name`, `last_name` and `revenue`––and returns the dynamically generated `greeting`.

- An if-else statement is used to create the conditional logic that determines the business tier for each customer based on their revenue. This defines the appropriate `greeting` to be generated.

  ```python
  # Define a function that accepts a customer first_name, last_name, and revenue and returns a custom greeting using the full name.
  # Use these ranges to determine the business tier (and corresponding message) for each customer.
  #   Platinum = 3001+
  #   Gold = 2001-3000
  #   Silver = 1001-2000
  #   Bronze = 0-1000
  def create_greeting(first_name, last_name, revenue):
  """Creates a customer greeting based on revenue status.

  Args:
      first_name (str): The first name of the customer.
      last_name (str): The last name of the customer.
      revenue (int): The revenue of the customer.

  Returns:
      A customized greeting string.
  """

  if revenue > 3000:
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a platinum member."
  elif (revenue > 2000 and revenue <= 3000):
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a gold member."
  elif (revenue > 1000 and revenue <= 2000):
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a silver member."
  elif (revenue >= 0  and revenue <= 1000):
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a bronze member."

  return greeting
  ```

- Since each customer in the list is a dict datatype, call the `first_name`, `last_name`, and `revenue` keys of each customer to pass it into the `create_greeting()` function.

  ```python
  # Loop through the list of customers and use your function to print custom greetings for each customer.
  for customer in customers:
      greeting = create_greeting(customer['first_name'], customer['last_name'], customer['revenue'])
      print(greeting)
  ```

Ask if there are any questions before moving on.

---

### 4. Instructor Do: Time Value of Money (10 min)

**Corresponding Activity:** [03-Ins_Time_Value_of_Money](Activities/03-Ins_Time_Value_of_Money)

In this part of the lesson, students will be introduced to the concept of time value of money, as well as how to calculate it.

**Files:**

- [Time Value of Money Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57bb043f18_0_4333)

- [time_value.py](Activities/03-Ins_Time_Value_of_Money/Solved/time_value.py)

This section will focus on core financial calculations in Python. Students should understand that these calculations are fundamental to financial analysis, and that they will actually be writing code for each of these formulas.

**Note:** When reviewing the slides, leverage the knowledge of students with a finance background by asking them to help explain time value of money and how it is used.

Use the [slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57bb043f18_0_4333) as you explain time value of money. Be sure to highlight the following:

- The **time value of money (TVM)** describes the additional value that is created through receiving money today compared to receiving money at a later date, as money today can continue to grow with interest.

- The time value of money can change due to factors such as interest rate, compounding periods, and the length of time.

- The formula for the future value of money can be reversed to obtain the present value, given a future amount. This allows us to properly evaluate the value of a future cash flow or asset in terms of what it's worth today.

Open [time_value.py](Activities/03-Ins_Time_Value_of_Money/Solved/time_value.py) and explain the following:

- The purpose of a function is to reuse blocks of code. The `calculate_future_value` function contains the logic required to calculate the future value of money.

  - The function can be called over and over again with new inputs, and a future value is calculated for each of those inputs.

  - In programming, this concept of code reuse is called DRY (**D**on't **R**epeat **Y**ourself).

- Functions don't always have to be user defined; there are many built-in Python functions already available for use. For example:

  - List objects have multiple functions such as `append()`, `len()`, and `remove()`.

  - Dict objects have multiple functions such as `keys()` and `items()`.

- In previous examples, functions were called by supplying values for each of the parameters. However, functions can also be called by using variables to pass in the values for the parameters. The parameters for `calculate_future_value` are `present_value`, `interest_rate`, `compounding_periods`, and `years`.

- Functions often return one or more values. The value that the function returns can be assigned to a variable for use in other parts of the code. In this example, `future_value` is assigned the value that the `calculate_future_value` function returns.

Answer any questions before moving on.

---

### 5. Student Do: Zero-Coupon Bonds (25 min)

**Corresponding Activity:** [04-Stu_Time_Value_of_Money](Activities/04-Stu_Time_Value_of_Money)

In this activity, students will apply the concept of time value of money (TVM) to discount the future value of a zero-coupon bond and determine its present value. They will also compare the present value to its current selling price in order to decide whether or not to purchase the bond.

Encourage students to work in pairs for this activity. Motivate students to help each other by explaining that the best way to learn is to teach, so taking the time to help their neighbor will really reinforce the concepts.

**File:** [Starter Code](Activities/04-Stu_Time_Value_of_Money/Unsolved/zero_coupon_bonds.py)

**Instructions:** [README.md](Activities/04-Stu_Time_Value_of_Money/README.md)

### 6. Instructor Do: Review Zero-Coupon Bonds (5 min)

Take some time to review the Zero-Coupon Bonds activity with students.

**File:** [Solution](Activities/04-Stu_Time_Value_of_Money/Solved/zero_coupon_bonds.py)

Open `zero_coupon_bonds.py` to review the solution and explain the process of valuing a zero-coupon bond:

- The `present_value` function allows us to value the promised future value of the bond upon its maturity.

- Because the `present_value` formula is merely a manipulation of the `future_value` formula in the previous activity, its parameters are generally equivalent as well:

  - `future_value`: The face value or maturity value of the bond; the lump sum distributed at the end of the duration of the bond.

  - `interest_rate`: The rate at which we discount the future value or maturity value over the duration of the bond.

  - `compounding_periods`: The compounding periods (assumed to be 1 for bonds).

  - `years`: The number of years representing the duration of the bond.

- After calculating the present value of the bond, compare it to its market price. The decision whether or not to purchase the bond is based on if the bond is selling at a `discount` or `premium` in relation to its present value.

Answer any questions before moving on.

---

### 7. Instructor Do: Imports (10 min)

**Corresponding Activity:** [05-Ins_Imports](Activities/05-Ins_Imports)

This section is exciting because it showcases the power of imports in Python.

**Files:**

- [NPV Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57bb043f18_0_4663)

- [imports.py](Activities/05-Ins_Imports/Solved/imports.py)

Review the following points to motivate students and help them understand how powerful imports can be:

- **Imports** allow developers to plug in preexisting libraries to their own programs. Imports allow developers to share and use code that others have written.

- Imports provide a way to "stand on the shoulders of giants" and leverage existing tools and libraries to build more sophisticated programs. Instead of building everything from scratch each time, you can use tools that have been built by other brilliant people to enhance your own code and build even greater programs!

Explain that we will be importing some really cool financial functions to calculate things like net present value (NPV).

Using the [slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57bb043f18_0_4663), discuss the theory behind NPV. Then, review the code in `imports.py`, highlighting the following:

- Imports allow us to call upon other Python programs and gain access to their functions and variables.

- There are two ways to perform imports:

  - Import the additional Python program as a reference object.

    ```python
    # Call the print_hello() function via a reference to the imported module functions.py
    import functions
    functions.print_hello()
    ```

    ```
    hello!
    ```

  - Import the specific attribute (e.g., function, variable) of the additional Python program into the namespace, or scope, of the current Python program.

    ```python
    # Call the print_hello() function imported directly from functions.py
    from functions import print_hello
    print_hello()
    ```

    ```
    hello!
    ```

Introduce NumPy.

- NumPy is a Python library that provides fast input/output, or I/O, on multidimensional or nested array objects. Among other things, NumPy can be used as a scientific computing or financial analysis tool.

- A Numpy offshoot library applicable to fintech is called numpy-financial. The built-in NPV function from the NumPy Financial library makes calculating NPV values simple so that you don't have to reinvent the wheel.

- Note that NumPy Financial may not be installed for many students, take the opportunity to walk them though using `pip install numpy-financial`.

  ```python
  # Import the NumPy library (for most calculations)
  import numpy

  # Import the NumPy Financial library (for some finance-specific calculations)
  import numpy_financial as npf

  # Initialize variables
  interest_rate = .1
  cash_flows = [-1000, 400, 400, 400, 400]

  # Call the NPV function from the NumPy Financial library
  net_present_value = npf.npv(interest_rate, cash_flows)
  print(f"NPV = {net_present_value}")
  ```

Answer any questions before moving on.

---

### 8. Student Do: Net Present Value (15 min)

**Corresponding Activity:** [06-Stu_Imports](Activities/06-Stu_Imports)

In this activity, students will use the `npv` function from the NumPy Financial library to calculate the net present value of three potential company projects (and their cash flows) and assess which is the optimal project to undertake.

**File:** [Starter Code](Activities/06-Stu_Imports/Unsolved/Core/net_present_value_core.py)

**Instructions:** [README.md](Activities/06-Stu_Imports/README.md)

### 9. Instructor Do: Review Net Present Value (5 min)

In this part of the lesson, you will review the previous Net Present Value activity with students.

**File:** [Solution](Activities/06-Stu_Imports/Solved/Core/net_present_value_core.py)

Open the [solution file](Activities/06-Stu_Imports/Solved/Core/net_present_value_core.py) and explain the process of performing financial analysis using net present value (NPV):

- NumPy Financial's built-in NPV function makes it easy to calculate NPV values.

- Each list of cash flows represents a project proposal.

  - The first element of each list represents the project's initial investment.

  - The remaining elements of the list represent the cash flows as a result of the initial investment.

- Resolving the return values of the NPV functions as key-value pairs lets us easily retrieve the NPV value of an associated scenario, for example, when looking to determine the scenario associated with the calculated max NPV value.

Answer any questions before moving on.

---

### 10. Instructor Do: File I/O (10 min)

**Corresponding Activity:** [07-Ins_File_IO](Activities/07-Ins_File_IO)

This section of the lesson focuses on file I/O, or input/output, with a Python file.

**File:** [file_io.py](Activities/07-Ins_File_IO/Solved/file_io.py)

Begin your discussion of file I/O, or file inputs and outputs, with the following introduction.

- Data will not (and should not) always be hard-coded within a Python file. Often, data is saved within a file and accessed externally in order to perform some kind of data manipulation or analysis.

- File pathing is extremely important when attempting to access files saved within a folder structure.

- Python natively supports the input and output of files, and the pathlib library makes file pathing easy.

Open Terminal (Mac) or Git Bash (Windows) and navigate to the project folder.

- Run `pwd` to show where the current folder is located.

- Open Finder (Mac) or Explorer (Windows) to check the location of the script files and the resource file.

Open the solution file and highlight the following:

- `Path.cwd()` allows us to check our _current working directory_ from where the Python program is executing.

- Windows and Mac operating systems treat file paths differently; Windows uses `\` back slashes and Mac uses `/` forward slashes as file path separators.

- An **absolute path** is the fully qualified path to a specified file, while a **relative path** takes into account the current working directory of the executing program.

- For example, the following pair of code blocks target the same file:

  **Absolute Path:**

  ```python
  from pathlib import Path

  # Absolute path to the file
  absolute_filepath = Path("/Users/trilogyed/Desktop/File_IO/Resources/file.txt")

  with open(absolute_filepath, 'r') as file:
      print(file.read())
  ```

  ```
  I'm a text file header!
  Line 1
  Line 2
  Line 3
  ```

  **Relative Path:**

  ```python
  from pathlib import Path

  # Current working directory is "/Users/trilogyed/Desktop/File_IO/"
  cwd = Path.cwd()
  print(f"Current Working Directory: {cwd}")
  print()

  # Relative path to the file, equivalent to "{cwd}/Resources/file.txt"
  relative_filepath = Path("Resources/file.txt")

  with open(relative_filepath, 'r') as file:
      print(file.read())
  ```

  ```
  Current Working Directory: /Users/trilogyed/Desktop/File_IO/

  I'm a text file header!
  Line 1
  Line 2
  Line 3
  ```

- The `..` keyword means "go one level up" from the current working directory. For example, examine the following folder structure:

  ```
  /Users
    /trilogyed
      /File_IO
        /Resources
          file.txt
        /Solved
          file_io.py
  ```

  - If executing code from `file_io.py`, the relative path `../Resources/file.txt` can be used to target `file.txt`.

  - This is because `file_io.py` resides at `/Users/trilogyed/File_IO/Solved/file_io.py`. The `..` keyword goes one level up from `/Users/trilogyed/File_IO/Solved/` to `/Users/trilogyed/File_IO/` and descends into `Resources/file.txt` to hit the file.

- The pathlib library allows us to set file paths regardless of the operating system (OS).

  ```python
  filepath = Path("../Resources/input.txt")
  ```

- The `with open(filepath, 'r') as file:` operation opens a file residing at a specified `filepath` as a file object.

- We can read in the entirety of the text file by calling upon the `read()` function on the text file object `file`.

- Files can be read line by line using a loop. This will read every line of text until the end of the file.

  ```python
  line_num = 1
  for line in file:
      print(f"line {line_num}: {line}")
      line_num += 1
  ```

- After a file is read and reaches the last line, no more lines can be read for that file object. This is why if we run both methods of reading in the file in succession, only the preceding file read operation (all lines at once) will output, as the subsequent file read operation (line by line) will have already reached the end of the file by this point.

- Writing to a text file is very similar to reading in a text file; the main difference is we use the `write()` function instead of the `read()` function.

Answer any questions before moving on.

---

### 11. Student Do: E-Commerce Traffic (15 min)

**Corresponding Activity:** [08-Stu_File_IO](Activities/08-Stu_File_IO)

In this activity, students will perform file I/O by parsing a text file and calculating the sum and average of customer e-traffic, and then writing the results back to a text file.

**File:** [Starter Code](Activities/08-Stu_File_IO/Unsolved/ecommerce_traffic.py)

**Instructions:** [README.md](Activities/08-Stu_File_IO/README.md)

### 12. Instructor Do: Review E-Commerce Traffic (5 min)

Review the previous activity, E-Commerce Traffic, with students.

**File:** [Solution](Activities/08-Stu_File_IO/Solved/ecommerce_traffic.py)

Open the [solution file](Activities/08-Stu_File_IO/Solved/ecommerce_traffic.py) and review the solution with students. Explain the following:

- It's important to understand where a program is executing from. Knowing the current working directory facilitates the use of relative paths and helps diagnose `file not found` errors.

- The `Path.cwd()` function allows us to see the current working directory.

  ```python
  # Check the current directory where the Python program is executing from
  print(f"Current Working Directory: {Path.cwd()}")
  ```

- When text is read from files, it will first be interpreted as strings.

  - To do numerical calculations, we'll have to convert the values from string datatypes to int or float datatypes.

  - The `int()` datatype conversion function converts a string to an integer.

    ```python
    # Open the file in "read" mode ('r') and store the contents in the variable 'file'
    with open(file, 'r') as file:
        # Parse the file line by line
        for line in file:

            # Convert the number in the text file from string to int (allows for numerical calculations)
            number = int(line)

            # Sum the total and count of the numbers in the text file
            customer_total += number
            day_count += 1
    ```

- The operation `num_total += number` is equivalent to the more verbose operation `num_total = num_total + number`.

- When writing data to a text file, the content needs to be string data types. Therefore, any non-string data being written to a text file will need to be converted to a string data type.

Answer any questions before moving on.

---

### 13. BREAK (40 min)

---

### 14. Instructor Do: Tabular Data (5 min)

In this section, go over the definition of tabular data.

**File:** [Tabular Data Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57d7f6e59f_1_0)

Use the [slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57d7f6e59f_1_0) to review the following points about tabular data.

- **Tabular data** is data in a table format with rows, columns, and values for each row-column intersection.

- A simple example is an Excel spreadsheet, where columns are headers, rows are records, and values are cells located at the intersection of each row and column.

---

### 15. Instructor Do: CSV Reader (5 min)

**Corresponding Activity:** [09-Ins_CSV_Reader](Activities/09-Ins_CSV_Reader)

This part of the lesson focuses on CSV files, or comma-separated values, and how to read and write to CSVs.

**File:** [csv_reader.py](Activities/09-Ins_CSV_Reader/Solved/csv_reader.py)

Open [csv_reader.py](Activities/09-Ins_CSV_Reader/Solved/csv_reader.py). Walk through the demo while highlighting the following points:

- **CSV** stands for comma-separated values. A CSV file follows a tabular format in which the first line is usually a header containing column names, and each subsequent line is a row containing values that intersect with each row-column pair.

- The `csv` library parses data in order to make it more easily accessible.

- The `csv` library includes a `reader()` function that parses CSV data by a separator or delimiter, and creates a `row` list object that contains the values for every row in the CSV data.

  ```python
  with open(filename, 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')

      # Read each row of data after the
      for row in csvreader:
          # Print the row
          print(row)
          # Set salary variable equal to the value in the 4th column of each row
          salary = int(row[3])
          # Append the row salary value to the list of salaries
          salaries.append(salary)
  ```

- Writing to a CSV file is very similar syntactically to reading a CSV file. Use the `writerow()` function to write a list or row of data to the output CSV file.

  ```python
  # Open the output path as a file object
  with open(output_path, 'w') as csvfile:
      # Set the file object as a csvwriter object
      csvwriter = csv.writer(csvfile, delimiter=',')
      # Write the header to the output file
      csvwriter.writerow(header)
      # Write the list of metrics to the output file
      csvwriter.writerow(metrics)
  ```

Ask if there are any questions before moving on.

---

### 16. Student Do: Sales Analysis (15 min)

**Corresponding Activity:** [10-Stu_CSV_Reader](Activities/10-Stu_CSV_Reader)

In this activity, students will perform file I/O with a CSV file. Students will read in a CSV file to calculate customer revenue averages and then output results back to a CSV file.

**File:** [sales_analysis.py](Activities/10-Stu_CSV_Reader/Unsolved/Core/sales_analysis_core.py)

**Instructions:** [README.md](Activities/10-Stu_CSV_Reader/README.md)

### 17. Instructor Do: Review Sales Analysis (5 min)

Take some time to review the previous activity, Sales Analysis, with students.

**File:** [sales_analysis.py](Activities/10-Stu_CSV_Reader/Solved/Core/sales_analysis_core.py)

Open the [solution file](Activities/10-Stu_CSV_Reader/Solved/Core/sales_analysis_core.py) to review the solution. Explain the following:

- Python's CSV module parses CSV data and creates `row` list objects, making it easier to access specific column values for each row.

- Data that is read in from CSV files is interpreted as strings. To perform numerical calculations, we'll need to convert the strings to ints or floats.

  ```python
  for row in csvreader:
      # Print the row
      print(row)

      # Set the 'name', 'count', and 'revenue' variables for better readability, convert strings to ints for numerical calculations
      name = row[0]
      count = int(row[1])
      revenue = int(row[2])

      # Calculate the average and round to the nearest 2 decimal places
      average = round(revenue / count, 2)
  ```

- To add data to each row of the input CSV data, append values to the `row` list object.

  ```python
  # Append the average to the row
  row.append(average)
  ```

- `csvwriter.writerow()` takes in lists and outputs the data to a CSV file using the specified `delimiter`.

  ```python
  # Open the output path as a file and pass into the 'csv.writer()' function
  # Set the delimiter/separater as a ','
  with open(output_path, 'w') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')

  # Loop through the list of records and write every record to the output csv file
  for record in records:
      csvwriter.writerow(record)
  ```

- Using the `analysis` dictionary combined with if-else conditionals allows us to group and aggregate data by making checks to see if a particular key exists.

- If the key does not exist, then we add the key and initialize the nested dictionary value containing the `count` and `revenue` key-value pairs.

  ```python
  # If name is not already in the analysis dict, initialize the nested dict
  # Else continue to add to the existing key and nested key-value pairs
  if name not in analysis.keys():
      analysis[name] = {
          "count": count,
          "revenue": revenue
      }
  else:
      analysis[name]['count'] += count
      analysis[name]['revenue'] += revenue
  ```

- It's possible to write nested dicts to a CSV by first adding the contents to a list and then using `csvwriter.writerow()`.

  ```python
  # Open the output path as a file and pass into the 'csv.writer()' function
  # Set the delimiter/separater as a ','
  with open(aggregate_path, 'w') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')

      # Write the header as the first row
      csvwriter.writerow(header)

      # Loop over every key in analysis and write the associated key (name) and nested key-value pairs (metrics)
      for name in analysis:
          csvwriter.writerow([name, analysis[name]['count'], analysis[name]['revenue'], round(analysis[name]['revenue'] / analysis[name]['count'], 2)])
  ```

Answer any questions before moving on.

---

### 18. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35 minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings

---

## End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
