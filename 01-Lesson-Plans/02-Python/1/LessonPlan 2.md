## 2.1 Lesson Plan: The Emergence of Python

### Overview

Today's class will introduce students to the basics of the Python programming language. The lesson will cover a brief history of Python, its audience and use cases, and functional concepts like variables, conditionals, loops, and calculations. Students will also install Python and get acquainted with its environment. The goal of the lesson is to enable students to automate and solve financial problems with Python.

### Class Objectives

By the end of this class, students will be able to:

* Open a project using JupyterLab.

* Pseudocode a task using Python comments.

* Create, store, and retrieve data using Python variables.

* Control program flow with conditional logic.

* Repeat blocks of code with loops.

---

### Instructor Notes

* As a reminder, slack out the [Anaconda Installation Guide](../Supplemental/AnacondaInstallGuide.md). Tell students that they need to have Anaconda installed prior to class today and to use office hours to debug any problems.

* **Note:** If you or a student has an M1 chip machine, please refer the [M1 Chip Troubleshooting Guide](../../../05-Student-Resources/Troubleshooting-Guides/M1_Chip_Troubleshooting_Guide.md) for assistance with installations.

* Welcome to the first day of programming with Python! You will be guiding students through a series of increasingly complex activities, which serve as the foundation for the next class as well as the homework. The class should feel like an evenly paced introduction to Python that provides a challenge and engages students with relatable use cases.

* Today's class will introduce students to fundamental Python concepts, including what Python is, technical and financial problems it solves, and factors that make Python different from other programming languages. Students' familiarity with Python will likely vary, so be prepared to answer questions ranging from basic to complex.

* This class will be challenging for some students as they become acquainted with coding standards, syntax, and the debugging process. Each instructor lecture or demo (Instructor Do) will be followed by an activity in which students will be able to practice these concepts. Review questions are also included to reinforce key information.

* Look for opportunities to include real-world examples in your lectures to make concepts more concrete and relatable for students. Feel free to draw upon your own experience using Python in the professional world.

* Be encouraging. Remind students that all developers have started where the students are right now. Actively work to build confidence, engagement, and promote effective problem-solving skills by letting students explain concepts if they feel comfortable.

* As you review the activities, find ways to connect the concepts to FinTech. Include brief discussions about emerging or disruptive/innovative technologies and how they have changed the FinTech landscape.

* Today's class will include a tour of JupyterLab. There will also be several live-coding activities that should be completed in a Python Notebook. Make sure JupyterLab is installed and running properly on your machine.

* Activities that involve programming solutions will have an associated coding file linked at the beginning of the activity section. Click on the link to take you to the coding file required for the activity.

* Remind the class that a student guide for each unit can be found in the corresponding unit's supplemental folder. Each guide has helpful links and FAQ's for the unit. The unit 2 student guide can be found [here](../Supplemental/StudentGuide.md). If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [2.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1de669fb-50a0-41c4-b4c6-aa9a0189d16f) Note that this video may not reflect the most recent lesson plan.


### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 2.1 Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Introduce Python (5 min)

In this section, you'll welcome students to class and introduce the Python programming language.

**File:** [Welcome and Python Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit?usp=sharing)

Welcome students to class and introduce the class objectives for the day. Then, explain that today will be the exciting first step toward automating their work with Python!

Slack out the following files to be used as reference guides as students progress through Python.

  * [Student Guide](../Supplemental/StudentGuide.md)

  * [Python Cheat Sheet](../Supplemental/Python_Reference_Guide.pdf)

Introduce Python by covering the following points:

* Python is a high-level, general purpose programming language used to create applications, as well as solve smaller, individual development needs.

* Python has been used to build robust applications and analytic pipelines for a wide range of computing needs.

* In the financial industry, Python has been used to solve complex quantitative problems such as sophisticated financial modeling/forecasting, algorithmic trading and decision making, and iterative and recursive data processing.

* Python can be used to automate work that's done in Excel, such as data cleaning, data manipulation, and calculations.

Review the advantages of using Python.

* Python supports disparate data formats, from text and Excel files to CSV, JSON, and XML files.

* Python integrates with database systems (e.g., Oracle, MySQL), providing a mechanism to load and extract data from databases.

* Python also has libraries and functions, such as NumPy and Pandas, that were developed specifically to help create financial applications and support data visualization.

* Creating data visualizations with Python allows data elements and their complexity and relationships to be visualized. This is especially valuable for financial algorithms that require trend or time analysis.

Slack out the following link to students. Tell them that this is a great resource for more information about FinTech-related Python libraries: https://financetrain.com/best-python-librariespackages-finance-financial-data-scientists/.

---

### 2. Instructor Do: Introduction to JupyterLab (5 min)

**Corresponding Activity:** [Ins_JupyterLab](Activities/01-Ins_JupyterLab)

In this section, you will introduce JupyterLab. Students should already have Anaconda and JupyterLab installed and can proceed to first-time setup. If not, distribute the following installation guidelines to the class.

**Files:**

* [AnacondaInstallGuide.md](../Supplemental/AnacondaInstallGuide.md)

* [JupyterLabInstallGuide.md](../Supplemental/JupyterLabInstallGuide.md)

* [JupyterLab Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57bb043f18_0_4333)

Introduce JupyterLab by first asking students if they have ever heard of Jupyter Notebook.

Use the [slideshow](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57bb043f18_0_4333) to cover the following points.

* Jupyter Notebook was created by Project Jupyter to provide developers and data scientists with a development environment (integrated development environment) that includes all of the tools needed to build Python programs.

* An **integrated development environment (IDE)** is software that provides a text editor as well as technology to package code and interpret it.

  * Most IDEs have plugins that allow you to customize the look and feel and download additional software.

  * For example, some IDEs connect with code repositories to make sure code is always backed up in a source control repository.

* Jupyter Notebooks are an interactive, web-based IDE that supports the integration of live coding, document manipulation, narrative text, and data visualization.

* Jupyter Notebooks support a number of different programming languages, including Python, Scala, and R. Over 40 languages are supported.

* JupyterLab, the next generation of Jupyter Notebook, is an open-source, web-based interactive development environment that provides a space for users to code, take notes, write computational narrative, manipulate data, and visually represent data.

Explain the advantages of JupyterLab vs. Jupyter Notebook.

* Whereas Jupyter Notebook provides an interactive space to write code and access a terminal, JupyterLab provides an actual environment to develop. JupyterLab is a true integrated development environment that provides connectivity to various plugins and services.

* JupyterLab allows you to create customizable layouts and multiple tabs/workspaces, as well as have multiple files open at once (notebooks, markdowns, HTML pages, etc.).

* JupyterLab is a great way to develop shareable research and analytical notebooks that include code, output, and text documentation.

* It has a clean and organized UI that enables developers and data scientists to easily switch between projects and documents. Users can have a terminal, console, Python file, notebook, and live preview of output all in one view.

* JupyterLab supports multiple file formats, such as .py, .md, and .txt. It also supports editing of CSV, JSON, and markdown files.

* It offers an extensive repository of extensions that enhance the interactive experience of JupyterLab, ranging from visualization extensions for Matplotlib and Plotly to big data services like YARN.

Walk students through the process of setting up JupyterLab:

1. Update the conda environment.

    ```shell
    conda update conda
    conda update anaconda
    ```

2. Activate the conda dev environment.

    ```shell
    conda activate dev
    ```

3. Launch JupyterLab from the terminal.

    ```shell
    jupyter lab
    ```

Pause here to check if students are able to launch JupyterLab. If any students are having trouble, direct them to troubleshoot their installation with a TA during the next activity or the break. Instruct students to use a temporary hosted Jupyter server located at [https://jupyter.org/try](https://jupyter.org/try) until their environments are up and running.

  ![jupyterlab.png](Images/jupyterlab.png)

---

### 3. Instructor Do: Creating Projects with JupyterLab (10 min)

**Corresponding Activity:** [Ins_Jupyter_Project](Activities/02-Ins_Jupyter_Project)


Walk through the following slides and then proceed to the instructor activity on creating projects with JupyterLab.

**Files:**

* [JupyterLab Demo Slide](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g594d5df485_0_1103)

* [JupyterLabProjectGuide.md](../Supplemental/JupyterLabProjectGuide.md)

Tell students that they will now learn how to create JupyterLab projects, navigate the JupyterLab interface, and execute code in Jupyter.

Review the following points about JupyterLab projects:

* JupyterLab projects are the organizational system of JupyterLab applications.

* Everything used and associated with a JupyterLab application goes in a JupyterLab project. This includes notebooks, files, images, etc. They are essentially a folder on a file system.

Open [JupyterLabProjectGuide.md](../Supplemental/JupyterLabProjectGuide.md). Walk through the solution and highlight the following:

* The JupyterLab launcher is one of the central components.

* The launcher lists all of the configured extensions available for use in JupyterLab. Extensions include a web notebook, Python console, and terminal.

* The launcher can also create text files.

  ![LP_Ins_Jupyter_Project_Launcher.png](Images/LP_Ins_Jupyter_Project_Launcher.png)

* The launcher can only run one extension at a time. Therefore, if a Python notebook extension is already running, a new launcher would be needed to run a second application, such as the terminal.

  ![LP_Ins_Jupyter_Project_New_Launcher.png](Images/LP_Ins_Jupyter_Project_New_Launcher.png)

* JupyterLab interacts with the file system: it reads in the structure of the file system, registers its folders and files, and represents them in the left-side window. Files and directories can be created, edited, and deleted without having to leave the JupyterLab interface.

  ![LP_Ins_Jupyter_Project_File_Explorer.png](Images/LP_Ins_Jupyter_Project_File_Explorer.png)

* JupyterLab allows you to create Jupyter Notebooks, which communicate data well in many programming languages, including Python. The majority of development throughout the course will take place in a Jupyter Notebook.

  ![LP_Ins_Jupyter_Project_Notebooks.png](Images/LP_Ins_Jupyter_Project_Notebooks.png)

Answer any questions before moving on.

---

### 4. Student Do: Creating a JupyterLab Project (10 min)

**Corresponding Activity:** [Stu_Jupyter_Project](Activities/03-Stu_Jupyter_Project)


In this activity, students will create a JupyterLab project and run a Python `hello world` print statement in a Python notebook.

**Instructions:** [README.md](Activities/03-Stu_Jupyter_Project/README.md)

Open the instructions and introduce the student activity.

Instructional staff should circulate the classroom during this activity, monitoring students to ensure that everyone can successfully launch JupyterLab. If anyone has issues, direct them to use [Try Jupyter](https://jupyter.org/try) for this activity and to troubleshoot their install with a TA during the next break.

Take some additional time here if necessary, as students may need to familiarize themselves with the layout of JupyterLab. Students will not be able to participate in the upcoming coding activities if this activity is not completed successfully.

---

### 5. Instructor Do: Review Creating a JupyterLab Project (5 min)

Review JupyterLab projects by engaging students with a series of review questions.

**File:** [Review JupyterLab Projects Slide](https://docs.google.com/presentation/d/11YSMAXfDc_eDNFKayDVKT6-iWajgeJKCQe1N74bokrM/edit#slide=id.g594d5df485_0_1125)

Use the slides and the following questions to review JupyterLab projects with students.

* What is JupyterLab?

  **Sample Answer:** JupyterLab is a web-based user interface that enables users to work with documents, write code, and create visualizations. JupyterLab is essentially a communication tool––it allows coders to organize and communicate the results of code in a way that is both fun and easy to read and understand.

* What are some of the advantages of JupyterLab?

  **Sample Answer:** JupyterLab is the next generation of web-based IDEs that gives coders a highly customizable and modular workspace to create and present code and data. You can easily share code, research, and analytical notebooks with team members and leadership, which improves communication and facilitates collaboration.

* Where are files saved when created in JupyterLab: on the file system or on a separate server?

  **Sample Answer:** Files are saved on the file system. By default, newly created files and directories are created in the user's home folder.

* How many activities can be opened in one launcher?

  **Sample Answer:** Multiple activities can be opened as several tabs in JupyterLab. Just like in a browser, there is no set limit to the number of tabs one can have open; however, more tabs generally mean more allocated memory, which can lead to computer performance degradation––so beware!

* What are JupyterLab projects?

  **Sample Answer:** Conceptually, JupyterLab projects are the underlying organizational system of JupyterLab. Like a hiking backpack holds everything you need to operate on a hiking trip, a Jupyter project holds everything needed to run a Jupyter program. Physically, JupyterLab projects are folders on the file system.

* How do you create a project in JupyterLab?

  **Sample Answer:** You can create a Jupyter project by using the create folder button in File Explorer. From there, a notebook, terminal, or text file can be created in the folder.

* What can go into a JupyterLab project?

  **Sample Answer:** A JupyterLab project can include documents, text files, code scripts (i.e., Python scripts/files), terminals, and so on.

To guide students, you may want to follow up with questions such as:

* Does JupyterLab work with languages other than Python, such as Scala or R?

* What is the output extension for a Python Jupyter notebook?

  **Sample Answer:** Yes, JupyterLab can be configured to work with Scala and R. JupyterLab supports up to 40 languages, including Java. This is awesome because it means you don't have to learn language-specific tools. You can learn how to use JupyterLab, and then as you learn new languages and begin to alternate languages on coding projects, you don't have to worry about switching the IDE being used. JupyterLab can be the one-stop shop for all IDE and programming needs!

Answer any questions before moving on.

---

### 6. Instructor Do: Variables (10 min)

**Corresponding Activity:** [Ins_Variables](Activities/04-Ins_Variables)

In this section, students will learn how to use variables in Python to perform value assignment and store and recall data.

**Files:**

* [Variables Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57f3228557_0_1)

* [variables.py](Activities/04-Ins_Variables/Solved/variables.py)

Begin this section by saying something like the following: "Now that the environment and tools have been greased and prepped, it's time to start coding!"

At this point, students may feel apprehensive about the upcoming coding activities. Build confidence by saying:

* "Now that our battle stations (environments) are up and running, we can start coding! This can be a really exciting experience, but it can also be very intimidating. Both of these feelings are understandable, but don't worry. If you think about it, computers themselves aren't even really that smart. They are super logical, so you have to tell them what to do and how to do it, including what to remember (variables)."

Set up the following real-world scenario to help explain variables:

* Think about any time you've kept score for a game or watched someone else keep score. It can be an involved process. Scores change all the time. Tally marks and points have to be tracked and calculated, and you're always searching for pen and paper.

* In this scenario, `score` is a variable that represents an ever-changing numeric number. We can track two scores in two different variables: `team_a_score` and `team_b_score`. Whenever Team A gets a point, the `team_a_score` variable should be incremented by 1. The same goes for Team B. At any moment, the two scores can be compared to find out who is winning.

* There are advantages to tracking performance or ranking in a game as `score`. First, it increases flexibility. We can reference `score` without specifying if its the score of a baseball game, video game, or even an exam. Regardless of context, `score` has a value, and that value has meaning. `score` as a word and concept is also easy to remember, and its significance is stored in people's mind (memory). `score` can be referenced in conversation, and others will understand its representation. This makes `score` a great example of a variable."

Transition to discussing variables. Use the [slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57f3228557_0_1) to direct your discussion.

* Variables are one of the key components of programming languages and serve as the primary means of data storage. All variables must have a name, value, and type.

* One way to think about variables is from the perspective of Excel:

  * Each cell label in Excel serves as a variable; for example, A1, B1, C1.

  * Each cell has a name (e.g., A1), a value (e.g., 5), and a type (integer).

* Variables allow us to name our data in ways that make it easier to understand and use in code, and provides the freedom of choice in regard to variable names.

  * For example, computers allow us to name a string of text characters something like `first_name` or `first_nm`.

  * Either way works, and both provide meaning for a person reading the code.

* Variables have three main operations: create, put, and retrieve.

  * To create a variable, `declare` it.

  * To put a value in a variable, `assign` it.

  * To retrieve a variable, `call` it.

* A useful analogy for understanding the relationship between variables and values is an envelope and a letter: the envelope is the variable, and the value is the letter, or contents. `calling` a variable is like opening an envelope and withdrawing the contents.

* All variables have a **data type**.

  * Data types correspond to the type of data being stored, e.g., letters/words, phrases, or numbers.

  * Python has five standard data types: number (integer, float, etc.), string, list, dictionary, and tuple.

* Depending on the type of data that you store, Python provides different functions for that data. For example, you can find the length of a string of characters (how many letters are in the string).

Open [variables.py](Activities/04-Ins_Variables/Solved/variables.py) and highlight the following:

* Variables can be used to store fundamental types of data such as strings of characters, numbers, and Boolean (true/false) values.

* An advantage of storing data as variables is that they can be referred to by name in later parts of the code.

* The following code defines several variables and then prints them as part of sentences.

  ```python
  title = "Frankfurter"
  years = 23
  hourly_wage = 65.40
  expert_status = True

  # Print the variables
  print(title)
  print(years)
  print(hourly_wage)
  print(expert_status)

  # Prints the data type of each declared variable
  print("The data type of variable title is " + type(title))
  print("The data type of variable years is " + type(years))
  print("The data type of variable hourly_wage is " + type(hourly_wage))
  print("The data type of variable expert_status is " + type(expert_status))
  ```

* Variables can be used in calculations. Using variable names can make it easier to understand the logic in the code.

  ```python
  total_miles = 257
  gallons_gas = 7.2
  miles_per_gallon = total_miles / gallons_gas
  ```

* When a value is put into a variable, the value is **assigned**. The variable on the left of the `=` sign is assigned the value on the right. Values and calculation results can be stored as variables.

  ```python
  miles = 48
  kilometers = 0.621371 * miles
  ```

* Variables can be substituted inside of strings using a formatted string literal, or f-string. F-strings allow for **concatenation**, or combination of multiple strings. In the following code, the variable `kilometers` is converted to a string and then concatenated with the rest of the `message`.

  ```python
  message = f"The total kilometers driven was: {kilometers}"
  print(message)
  ```

Take a moment to discuss best practices for naming variables:

* Variable names should be descriptive.

* Avoid acronyms or abbreviations. For example:

  ```python
  # Bad Example
  mpg = 24
  # Better Example
  miles_per_gallon = 24
  ```

* A convention in Python is to use [snake_case](https://www.python.org/dev/peps/pep-0008/), where each word is separated by an underscore.

Explain to students that good variable names can greatly increase the readability of Python code.

Send a link to the [PEP 8 documentation](https://www.python.org/dev/peps/pep-0008/). Encourage students to refer to this documentation to improve the readability and overall quality of their code.

Answer any questions before moving on.

---

### 7. Student Do: Hello Variable World (10 min)

**Corresponding Activity:** [Stu_Variables](Activities/05-Stu_Variables)

In this activity, students will learn how to perform calculations and operations using variables. Students will find the percent increase of Apple stock and complete coding drills.

**File:** [hello_variable_world.py](Activities/05-Stu_Variables/Unsolved/Core/hello_variable_world.py)

**Instructions:** [README.md](Activities/05-Stu_Variables/README.md)

If students need additional assistance or finish early, direct them to the Python style guide, which can be found [here](https://www.python.org/dev/peps/pep-0008/).

---

### 8. Instructor Do: Review Hello Variable World (5 min)

**File:** [hello_variable_world.py](Activities/05-Stu_Variables/Solved/Core/hello_variable_world.py)

Review the solution to the variables activity, highlighting the following points:

* Declaring variables requires a variable name, and in most cases, a value.

* Variables can be assigned values derived from the calculation of other variables.

* Data types are implicitly understood in Python. This means that users do not have to specify the data type for a variable.

  * The Python interpreter receives the value, evaluates it internally, and determines what data type it is.

  * This process is similar to a taste-testing challenge: Python unknowingly receives an item and has to "sense" what it is.

* String formatting can be used to improve the appearance of values when they are printed to the screen.

  * Note that numeric values should only be formatted for display purposes.

  * Storing a numeric value as a variable with a percent sign or dollar sign changes the type to a string, which also eliminates the ability to use numerical functions (sum, avg, etc.).

Engage students with the following review questions:

* How do you create a variable?

  **Answer:** Declare it.

* How do you put a value in a variable?

  **Answer:** Assign it.

* How do you retrieve a value from a function?

  **Answer:** Call it.

* What are the three attributes of a variable?

  **Answer:** Name, type, and value

* What are some of the data types covered so far?

  **Answer:** String, integer, Boolean, float

* What is concatenation?

  **Answer:** The operation of joining two strings

* What is the function to display output to the screen?

  **Answer:** `print()`

* How do you determine the data type of a variable?

  **Answer:** `type()`

* How do you format a variable in a `print` statement?

  **Answer:** By providing the `f` indicator at the beginning of a print statement. The variable being formatted should be wrapped in curly braces.

To guide students, you may want to follow up with questions such as:

* Can a string be concatenated with an integer?

  **Answer:** No, a string can only be concatenated with another string. Other data types like integers must first be converted to a string before it can be concatenated to another string.

* What type of calculations can be done with integers?

  **Answer:** Any types of mathematical calculations that involve numerical integers. For example, addition `+`, subtraction `-`, multiplication `*`, and division `/`.

Ask if there are any questions before moving on.

---

### 9. Instructor Do: Conditionals (10 min)

**Corresponding Activity:** [Ins_Conditionals](Activities/06-Ins_Conditionals)

In this section, students will learn how to apply logic to the values assigned to variables. This establishes a workflow in which a program exhibits a specific behavior based on the evaluation of a condition.

**Files:**

* [Conditional Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57f3228557_0_8)

* [conditionals.py](Activities/06-Ins_Conditionals/Solved/conditionals.py)

Use the [slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57f3228557_0_8) to review the following points and associated code examples.

* **Conditionals** are comparisons or evaluations of variables and their associated values.

* In the previous activity, variables were used to tell computers what (data) to remember/store.

* In this section, variables and their associated values are called upon and evaluated via conditionals, which determine the decisions or behavior the computer should exhibit.

* Computers are simple in that they do exactly what you tell them to do. If you want to have a useful script, you must program decision logic into the computer.

* Imagine a self-driving car. Writing code that tells the car's computer to drive forward is great for straight stretches of road. But what happens when a pedestrian is in the path? You need to include additional logic to instruct the car's computer to not hit the pedestrian. Computers only do what you tell them to!

* This decision making is called **conditional logic**, and it is a fundamental building block of all computer programs.

* Conditions can be specified, or variables can be used to store conditions for conditional statements.

* Conditionals can be executed by using **if-else statements**.

  * If-else statements are created using the `if` and `else` keywords. Both keywords accept a condition.

  * Colons are used to indicate what action needs to be taken if the condition evaluates as `True`.

Open a console within JupyterLab and live code the example of the self-driving car:

* What would happen if a driver fell asleep behind the wheel of a car? Well, if it's a self-driving car, nothing. The car's safety mechanisms will activate, and the car will begin auto-piloting itself to avoid collisions and swerving. If it's not a driverless car, well, a miracle might be needed. An example of such a case could look like the following:

  ```python
  driverless_car = True

  if driverless_car == True:
      # Do something
      print("Oh no! The driver's asleep! What do we do?!")
      print()
      print("All is good. Auto-pilot initiated.")
  else:
      # Do something else
      print("Oh no! The driver's asleep! MAYDAY! MAYDAY!")
  ```

* Conditionals operate based on Boolean conditions: `True` or `False` values.

  * If a conditional statement returns `True`, the corresponding code will execute.

  * If a conditional statement evaluates as `False`, the program will behave in a different way.

    ```python
    is_raining = True
    if is_raining:
      print("Bring an umbrella!")
    else:
      print("Leave the umbrella at home!")
    ```

* `Boolean` is a pretty weird word, which makes it easier to remember! Booleans are named after their inventor, George Boole, a famous 19th-century logician.

* Conditional statements can be used to make decisions about what will be stored in a variable.

  * Revisit the self-driving car scenario. A car could have a variable `immediate_action`. The value stored in `immediate_action` is dependent on how conditional statements evaluate.

  * If there's not a pedestrian in the path, put `"drive"` in `immediate_action`.

  * Else, put `"stop"` in `immediate_action`.

    ```python
    if not pedestrian:
        immediate_action = "drive"
    else:
        immediate_action = "stop"
    ```

* Conditional statements can be considered optional gatekeepers of blocks of code. If you want code to execute only under specific circumstances or conditions, you would use conditionals.

Open [conditionals.py](Activities/06-Ins_Conditionals/Solved/conditionals.py) and review the following points:

* Equality is the most frequently used comparison operator. The equality operator checks to see if the value of one variable equals another; it returns `True` if both values equal one another.

  ```python
  x = 5
  if x == 1:
      print("x is equal to 1")
  ```

* Variables can be used to store condition requirements.

  * Instead of specifying what the condition is, it can be stored in a variable. If the condition needs to be updated, the only thing that needs to be updated is the value of the variable.

  * In the following example, `y` is the condition stored in a variable. `y` can be updated to any number, and the program will dynamically evaluate the condition.

    ```python
    x = 5
    y = 10
    if x == y:
        print("x is equal to y")
    ```

* Conditionals can also be used to check inequality.

  * There will be instances where computations/actions should not be executed if equality is not achieved.

  * The inequality operator returns `True` if the two values do not equal one another.

    ```python
    y = 9
    if y != 1:
        print("y is not equal to 1")
    ```

* Conditionals can include one or many conditions. When more than one condition is provided, the conditions have to be separated by logical operators. Logical operators include `AND` (&&) and `OR` (||).

  * `AND` requires that both conditions return `True` for the action/computation to occur.

  * `OR` only requires one condition to return `True`.

    ```python
    x = 1
    y = 10
    if x == 1 and y < 10:
        print("Both values returned True")
    ```

* Complex conditional statements can be created by **nesting** if-else statements.

  * Nested if-else statements allow you to execute layers of computation.

  * In order for a nested if-else statement to execute, the first if-else condition must return `True`.

  * Note that the `elif` keyword can be used to include an extra set of conditions within the if-else decision structure. `elif` works just as `if` does.

    ```python
    if x < 10:
        if y < 5:
            print("x is less than 10 and y is less than 5")
        elif y == 5:
            print("x is less than 10 and y is equal to 5")
        else:
            print("x is less than 10 and y is greater than 5")
    ```

Revisit the self-driving car scenario to reinforce the power of using `elif` and nested if-else statements.

* Let's say you're in your self-driving car in the state of Florida, and you somehow get into an accident. Your insurance company might have a program that will predict, based on a series of conditions (e.g., at-fault liability, accident forgiveness policy, loyalty elite status), whether your premium will increase. That logic might look something like the following code.

Open the following code snippet in JupyterLab. Do not run it. Let students read it to see if they can guess whether `increase_insurance_premium` will be `True` or `False`.

```python
  # Declare Variables
  accident = True
  at_fault = False
  accident_forgiveness = True
  elite_status = True

  increase_insurance_premium = True

  print("Insurance premium will increase. True or False?")

  # Nested Conditional Statements
  if accident:
      if at_fault and accident_forgiveness:
          increase_insurance_premium = False
      elif at_fault and not accident_forgiveness and not elite_status:
          increase_insurance_premium = True
      else:
          increase_insurance_premium = False
  elif not accident and elite_status:
      increase_insurance_premium = False
  else:
      increase_insurance_premium = True

  print(f"Prediction: {increase_insurance_premium}")
```

After a minute has passed, run the code. Review the following conditions:

* Whether or not the driver was at fault

* Whether or not the policy is eligible for accident forgiveness

* Whether or not the driver has elite status

Answer any questions before moving on.

---

### 10. Student Do: The Conditional Conundrum (15 min)

**Corresponding Activity:** [Stu_Conditionals](Activities/07-Stu_Conditionals)

In this activity, students will create a Python script that implements conditional statements using the comparison and logical operators.

**Instructions:** [README.md](Activities/07-Stu_Conditionals/README.md)

---

### 11. Instructor Do: Review the Conditional Conundrum (5 min)

Take some time to walk through the solution while gauging students' level of comfort with conditionals.

**File:** [conditionals.md](Activities/07-Stu_Conditionals/Solved/conditionals.py)

Begin by saying something like:

* "You've just learned a lot of new syntax and keywords. We've also introduced logical and comparison operators, and if-else statements are about to become your best friend."

* "Let's reflect for a minute. What makes sense, and what is still confusing? Is anything a point of frustration?"

Be prepared to explain the following, for example:

* The comparison operators use the double equals sign `==` to represent equality. The equals sign `=` is used to assign values to variables. What's the difference?

  * `==` checks to see if a value equals another; it double-checks equality. (Like all work, you want to double-check what you're doing!) So, when you're basing a condition on equality, you should double-check what's being compared. You don't want to compare apples to oranges. They'll never be equal!

  * `=` is used to set and put values in a variable; it is used to assess and declare that a variable is something. You're not comparing it; you know for sure this is the answer. Think back to algebra. When you finish showing your work and steps in the calculation, you declare that `x = <some value>`. This is exactly how using the `=` works when declaring variables. You're declaring rather than evaluating.

* It's difficult to remember when to use _greater than_ `>` and _less than_ `<` operators, and when to use _greater than or equal to_ `>=` and _less than or equal to_ `<=`.

  * Deciding when to use specific comparison operators comes down to whether you want your conditional statement to include the minimum and maximum values needed to pass the condition.

  * This is best explained with the example of drinking age. In the U.S., you have to be 21 years of age or older to legally drink. 21 is the minimum age acceptable.

  * If we were to write a program to check whether someone's age meets the legal conditions, we would need to check for the minimum value acceptable, plus all numbers greater than it. If the minimum number is not included, the program will say that people who are 21 cannot drink.

Tell students to look at the following code. Ask:

* Are the results as expected, based on the logic?

* What are two possible ways to fix the logic?

    **Answer:**

1. Switch from using `>` to `>=`.

2. Check `if age > 20`.

    ```python
    age = 21
    if age > 21:
        print("You are of drinking age!")
    else:
        print("Argggggh! You think you can hoodwink me, matey?! You're too young to drink!")
    ```

    ```
    Argggggh! You think you can hoodwink me, matey?! You're too young to drink!
    ```

* `Elif` seems redundant. If conditional statements can end with an `else` block, why use `elif`?

  * `elif` statements pretty much indicate, "Hey, if the first round of conditions don't evaluate to true, try these!"

  * Consider `elif` statements a list of thorough checks used to weigh every option.

  * `else` is used to encapsulate all scenarios that were not covered in the aforementioned conditions.

  * Consider the `else` block like a contingency plan: no matter what happens, the `else` statement has your back and is equipped with a plan of action.

If time remains, continue to review the activity solution and highlight the following:

* Comparison and logical operations can be married to create complex decision structures.

* `if` conditions can be hard-coded or calculated.

  * A specific value can be provided as a condition (`x` must be greater than 10). `10` is the hard-coded condition.

  * A calculation can be used to figure out what the condition value should be.

Use the following code from the solution as an example. Instead of hard-coding the condition value, logic is used to compute the condition:

* Condition 1: x ** 3 >= y

* Condition 2: y ** 2 < 26

  ```python
  # 3. Output: `GOT QUESTION 3!`
  x = 2
  y = 5
  if (x ** 3 >= y) and (y ** 2 < 26):
      print("GOT QUESTION 3!")
  else:
      print("Oh good you can count")
  ```

* If-else statements can have multiple conditions, which can be achieved by using `elif` or by nesting if-else statements.

Engage the students with the following questions:

* If you want to instruct your program or computer to behave a certain way, what should you use?

  **Answer:** Conditional statements. Conditional statements require specific conditions to be met in order for a block of code to be executed. Conditional statements evaluate expressions to determine if the code should be executed. If the expression evaluates as `True`, the code is executed.

* How does the `AND` operator work?

  **Answer:** The `AND` logical operator requires all conditions to return `True` in order to satisfy the condition. The `AND` operator is used to include two conditions for evaluation.

* How does the `OR` operator compare to the `AND` operator?

  **Answer:** The `OR` logical operator works much like the `AND` operator; however, only one condition must return as `True`.

* How do nested if-else statements work?

  **Sample Answer:** A nested if-else statement is an if-else statement within another if-else statement. The statements execute sequentially. In order for the nested if-else statement to execute, the first if-else statement must evaluate accordingly.

Review what was just learned by asking the following questions:

* We learned about two types of operators: logical and comparison. Is a _greater than_ sign a logical or comparison operator?

  **Answer:** Comparison

* Is `OR` a logical or comparison operator?

  **Answer:** Logical

* If you want TWO conditions to be met, you would need to write _If x..._

  **Answer:** `AND`

* If you have two conditions, but either one is good enough, you would write _x..._

  **Answer:** `OR`

* What is used to tell the computer we want something that is _not equal to_ something else?

  **Answer:** `!`

* If you want to declare (or assign) a variable, do you use one or two equals signs?

  **Answer:** `=` (one)

* When do you use double equals signs?

  **Answer:** When you are checking equality.

Answer any questions before moving on.

---

### 12. BREAK (15 min)

---

### 13. Instructor Do: For Loops (10 min)

**Corresponding Activity:** [Ins_Loops](Activities/08-Ins_Loops)

**Files:**

* [For Loops Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g58d1bae602_0_153)

* [loop_de_loop.py](Activities/08-Ins_Loops/Solved/loop_dee_loop.py)

Introduce for loops by presenting the following scenario:

* Imagine that your new job at Accrual World, Inc. is to generate a daily report for each of your client's total sales. Every day, you need to gather the sales data from each client, and then break out your trusty calculator to add up their total sales. This results in hours of manual labor.

* Just before you finish, you realize that you were given last week's data. You have to start over! Well, there's a better way to handle repetitive tasks like this.

At this point, transition to your discussion to for loops. Use the [slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g58d1bae602_0_153) as you cover the following points:

* We have already learned how to tell computers what to remember by using variables. We also learned how to tell computers to make simple decisions by using conditionals. Now we're going to tell computers to do what they do best: endlessly repeat an action.

* The ability to endlessly repeat the same decision or action for a large dataset is very valuable, and something that computers can do much better than people can. Computers don't make as many mistakes, and they don't get tired!

* Almost every programming language has the concept of loops. **Loops** allow programs to execute code over and over until a condition exists to exit the loop. Simply put, a loop is a repeating process.

* Python has two types of loops: `for` and `while`.

* **For loops** are used for iterating over a sequence or collection. As the sequence or collection is iterated, a process is executed. This means the process is executed with every round in the loop.

  * For loops are called for loops because every time a loop happens, a repeating decision or behavior happens.

  * For example, if you have a string `Hello World`, a loop would allow you to iterate over each letter in the phrase and perform some type of operation (e.g., capitalize each letter).

  * Another way to think about it is if you loop a song, the song will play over and over again until the loop ends. DJs loop songs to make trendy beats; programmers loop blocks of code to make decisions and automate tasks.

    ```python
    for x in range(5):
      print(x)
    ```

Open [loop_dee_loop.py](Activities/08-Ins_Loops/Solved/loop_dee_loop.py) and review the following points about for loops.

* Using a for loop means you are instructing the computer to do something for every element in the sequence.

* For loops should be used when you want a process to run _n_ number of times.

  * For example, when you want to execute a decision or behavior for each number in a range, you would use a for loop: you know you have _n_ number of items, and you want a behavior executed for each item.

  * For loops should be used if you know a process needs to be executed a specific number of times.

  * For example, let's say you're training a new robotic supermarket cashier. `for` every egg (element) in the carton (sequence), the robot must move the element around to inspect if it's broken. The robot would leverage the below loop:

    ```python
    for egg in carton:
        # Inspect egg
    ```

* Loops need something to loop over. This can be a sequence of numbers, known as a **range**, or a sequence of letters like a word or string.

  * The `range` function can be used to create a sequence of numbers based on the limit provided as input (e.g., 5).

  * Ranges begin with 0 and increment by one. When looping over the range of numbers, we will put each number in variable `x`.

    ```python
    for x in range(5):
      print(x)
    ```

* Because strings are a sequence of letters, they can be looped. When strings are looped, each character is iterated.

* In the following example, `x` is the variable and `phrase` is the sequence.

  * In the first iteration of the loop, `x` is _H_.

  * In the second iteration, `x` is _e_.

    ```python
    phrase = "Hello World"
    for x in phrase:
      print(x)
    ```

* The `break` keyword can be used to stop a loop. This is valuable when a loop is executing and needs to stop when a specific condition is met.

* The `break` keyword will cause the loop to be exited completely. It does not operate like a skip.

  ```python
  desired_number = 5
  for x in range(10):
    if (x == desired_number):
      break
    print(x)
  ```

* The `continue` keyword can be used to stop the current iteration of a loop in order to skip to the next.

  ```python
  desired_number = 5
  for x in range(10):
    if (x == desired_number):
      continue
    print(x)
  ```

Now introduce while loops and compare them to for loops.

* Whereas for loops loop until they've completed a decision or behavior for each element in a sequence, **while loops** loop until a condition no longer evaluates as `True`.

* For example, `while` you are wearing your uniform (uniform = `True`), keep ringing up customers at the checkout line.

  ```python
  uniform = True
  while(uniform):
      # Ring up customers
  ```

* While loops should be used when you want a decision or behavior to be executed continuously until a condition is no longer `True`. In other words, use a while loop when there's a specific condition that must be met in order for the loop to end.

* While loops require an **iterator**, or counter variable, to be created and incremented. If the iterator is not incremented, the loop will not iterate correctly.

  * For example, in the following block of code, if `i` is not incremented, `i` will always equal 1.

  * The syntax to increment an iterator is shown below. The value to the right of the equals sign is added to the value of `i`.

  * The `+` indicates to increment; `-` indicates to decrement.

    ```python
    #Initializing iterator
    i = 1

    while i < 6:
      print(i)

      #Incrementing iterator
      i+=1
    ```

Encourage students to spend some additional time at home reviewing for and while loops. Documentation can be found [here](https://docs.python.org/3/reference/compound_stmts.html#while).

Answer any questions before moving on.

---

### 14. Student Do: Loop De Loop (15 min)

**Corresponding Activity:** [Stu_Loops](Activities/09-Stu_Loops)

In this activity, students will work with for loops in a Python file. The objective is to adapt the for loop concepts and actions in the previous instructor demo by creating a cheerleading Python program that loops through the characters of a string.

**File:** [cheer.py](Activities/09-Stu_Loops/Unsolved/cheer.py)

**Instructions:** [README.md](Activities/09-Stu_Loops/README.md)

---

### 15. Instructor Do: Review Loop De Loop (5 min)

**File:** [cheer.py](Activities/09-Stu_Loops/Solved/cheer.py)

Review the solution while engaging the students with the following questions:

* How do for loops execute?

  **Answer:** For loops operate by executing iteratively over a sequence or collection.

* What are the components of for loops?

  **Answer:** For loops are comprised of a variable and a sequence or collection.

* What do variables represent in a for loop?

  **Answer:** Variables represent a single element contained within the sequence or collection. This element holds a specific position, which the for loop can access.

* What is an iteration?

  **Answer:** For loop

* Let's say you need to loop over 10 financial reports and calculate growth earnings for each dataset. What type of loop should you use?

  **Answer:** For loop

* If you want to identify the square root for every number in a list from 0–200, should you use a loop? If so, what type of loop?

  **Answer:** Yes; for loop.

* If you want to process trades as long as the market is open, what type of loop should you use?

  **Answer:** For loop

* How do you exit a for loop?

  **Answer:** The `break` keyword will allow you to exit a loop.

* How do you skip an iteration in a for loop?

  **Answer:** The `continue` keyword will allow you to skip an iteration in a loop.

* How do you create a range of numbers to loop over?

  **Answer:** The `range()` function can be used to create a range of numbers.

Review the following points related to the activity:

* The solution works because it loops over an object that is a sequence (the word "cheer").

* Strings can be substituted for a range of numbers.

* In future classes, loops will be used with objects called lists and dictionaries, which are types of collections.

Ask students what would happen if any of the last four print statements were added to the for loop.

* **Answer:** The print statement would repeat itself for every letter in the `cheer` variable.

Emphasize the importance of indentation with `for` loops.

* If the indentation is incorrect, lines of code that should not be in the loop will be included.

* Lines that should be included but are not properly indented will not run iteratively.

Answer any questions before moving on.

---

### 16. Instructor Do: Pseudocoding (10 min)

**Corresponding Activity:** [Ins_Pseudocoding](Activities/10-Ins_Pseudocoding)

In this section, students will be introduced to pseudocoding, which will help them approach coding activities in this course as well as real-world professional settings and job interviews. You will demo how to pseudocode using an example from the previous activity.

**File:** [Pseudocoding Slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57f3228557_0_22)

Introduce the module with a series of questions regarding how students organize their thoughts when coding:

* How did you organize your thoughts when thinking through the coding activities?

* What was your thought process when deciding which lines of code to code first?

* Was it difficult to come up with an approach or starting point for any of the activities?

Discuss the importance of using a problem-solving methodology when developing programs.

* Having a good approach to understanding problems will enable students to design complex applications and troubleshoot errors and bugs.

Go over G Polya's techniques to problem solving, which are are straightforward and easy to remember. The steps are:

1. Understand the problem: Gather as much information as possible pertaining to the problem being solved, inputs, desired outputs, and limitations.

2. Devise a plan: Pseudocode an algorithm.

3. Carry out the plan: Code the algorithm.

4. Test and evaluate the plan: Review the algorithm and determine areas of improvement.

Define pseudocoding and explain its effectiveness. Use the [slides](https://docs.google.com/presentation/d/1fgulsaDy5mVRrZ0lUAOOg_f1GE58IrZwX1bfLvjoSbw/edit#slide=id.g57f3228557_0_22) to accompany the lecture.

* **Pseudocode** is a high-level description (essentially, a prototype or outline) of the inner workings of a program or algorithm. Pseudocode is written in human language to ensure readability.

* Pseudocoding is best done at the beginning of the development life cycle, in a planning or brainstorming phase. Using pseudocode to plan development allows ideas to be captured in human language and then transformed into fine-tuned programs.

* When added as a comment at the beginning of a script, pseudocode can serve as valuable, internal documentation that helps other developers understand the program.

* Pseudocoding allows developers to focus on the bigger picture and develop a clear and viable plan of action. This action includes a high level, step-by-step approach to solve the problem.

Demonstrate pseudocoding for the previous activity:

```
Pseudocode for a cheerleading program:

1. Initialize "cheer" variable to a string to be cheered
2. Create a for loop and iterate through each character in "cheer" variable
    2.1 Print each letter to screen with a cheer
3. Print exclamations to screen ("Woohoo!!!")
```

Explain that pseudocode is a great tool to use on interviews.

* Pseudocoding on interviews allows employers to see a candidate's thought process and problem-solving skills, as well as their ability to design algorithms.

* Some employers even specifically ask interviewees to complete a pseudocoding activity, which shows how interested employers are in developers' ability to solve problems, design and envision algorithms, and articulate process. Data shows that employers are looking for interviewees to pseudocode during interviews.

* Pseudocoding ensures that interviewees don't jump head first into a technical question; it requires them to think about what they're going to do. The last thing anyone wants is to start coding and not know what to do next.

Walk students through the following pseudocode:

```
Pseudocode for calculating simple interest:

1. Initialize "principal" and "interest_rate" variables to a float
2. Initialize "time_period" variable to an integer
3. Compute "simple_interest" by multiplying principal, interest_rate, and time_period
```

Take a moment to discuss best practices when pseudocoding:

* Use human language; pseudocode should be readable and understandable.

* Maintain naming and indentation conventions.

* Include variable instantiation and any operations or calculations that need to be performed.

* Use keywords like `if`, `then`, and `else` for conditional statements.

* Specify loop conditions.

* Be concise.

Present the following example of pseudocode.

```
Pseudocode for determining if credit should be acquired based off of simple interest:

1. Initialize "principal" and "interest_rate" variables to a float
2. Initialize "time_period" variable to an integer
3. Compute "simple_interest" by multiplying "principal", "interest_rate", and "time_period"
4. Determine if credit should be accepted
    IF "simple_interest" is less than or equal to 2000
        THEN print("We highly recommend you get this line of credit. Total simple interest paid is less than $2,000")
    ELSE If "simple_interest" is greater than 2000 but less than or equal to 4000
        THEN print("This is an okay deal. You might find better. Total simple interest paid will between $2,000 and $4,000")
    ELSE print("Total simple interest paid will be over $4,000. Do not accept this line of credit")
```

Answer any questions before moving on.

---

### 17. Student Do: Conditionally Yours, Part 1 (10 min)

**Corresponding Activity:** [Stu_Pseudocoding](Activities/11-Stu_Pseudocoding)

In this activity, students will pseudocode a solution to recommend whether or not a stock should be purchased, based on a specific threshold of percentage increase or decrease. When students have finished pseudocoding, they will implement their algorithm. The objective of the assignment is for the students to learn how to pseudocode solutions prior to developing them.

**File:** [conditionally_yours.py](Activities/11-Stu_Pseudocoding/Unsolved/conditionally_yours_part_1.py)

**Instructions:** [README.md](Activities/11-Stu_Pseudocoding/README.md)

---

### 18. Student Do: Conditionally Yours, Part 2 (15 min)

**Corresponding Activity:** [Stu_Challenge_Activity](Activities/12-Stu_Challenge_Activity)

In this activity, students will leverage the pseudocode they created in the previous activity to develop a program that will recommend whether or not a stock should be purchased based on a specific threshold of percentage increase or decrease. The objective of the assignment is for the students to learn how to evolve pseudocode into an algorithm or program.

**File:** [conditionally_yours.py](Activities/12-Stu_Challenge_Activity/Unsolved/Core/conditionally_yours.py)

**Instructions:** [README.md](Activities/12-Stu_Challenge_Activity/README.md)

---

### 19. Instructor Do: Review Conditionally Yours, Part 2 (5 min)

**File:** [conditionally_yours.py](Activities/12-Stu_Challenge_Activity/Solved/Core/conditionally_yours_part_2.py)

Engage the students with the following questions:

* How did pseudocoding improve or hinder your coding process?

  **Sample Answer:**  Pseudocoding provides a human-readable set of requirements from which a program should operate. In other words, pseudocoding makes it easier to define and outline the behavior of an application.

* What are some best practices for pseudocoding?

  **Sample Answer:** Best practices for pseudocoding include subscribing to naming conventions, listing out variables, specifying input and output, writing calculations and operations in human language, and using keywords such as `if` and `else`, just to name a few.

* True or false: pseudocode should include lines of code.

  **Sample Answer:** False. Pseudocode should be in human language. Function names can be used, but operations should be written out in human language.

* How do you identify a dependent statement in pseudocode?

  **Sample Answer:** Indentation is used to indicate a dependent statement.

Review the activity solution, highlighting the following:

* The solution's pseudocode uses a mix of human-readable language and Python keyword commands and functions. It's ideal for pseudocode to be a balance of the two.

* Pseudocode should match line by line with code implementation.

* Adding pseudocode to the beginning of a Python file is a great way to outline what the script does and the order of operations.

* This is particularly valuable when working on teams in the real world: Because the person who develops the code may not be the same person performing QA and eventually maintaining it in production, having pseudocode readily available increases the effectiveness of knowledge transfer.

* The key to completing the solution is to use the appropriate comparison and logical conditional operators.

Answer any questions before moving on.

---

### 20. Instructor Do: Preview Homework and End Class (5 min)

**File:** [Homework Instructions](../../../02-Homework/02-Python/Instructions/README.md)

Take a few moments to review the instructions to the homework and give students an idea of the kind of concepts that will be required to complete the assignment. Explain that they will be building the skills to complete this assignment during this week's classes.

Congratulate students on making it through their first lesson on programming! Offer some words of encouragement such as:

"This lesson helped you acquire your first new superpower. But, like all new superheroes, it will take some time and practice to use your superpower efficiently. Over time, it will become more natural. Just keep practicing and you will be saving the world before you even know it!"

## End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
