## 1.2 Lesson Plan: Deep Dive Into FinTech

---

### Overview

Today's lesson will focus on command line basics. It will also further investigate the key factors leading to the growth of the FinTech industry.

Specifically, students will be introduced to basic command line, which will help them use more advanced CLI tools in the next lesson as well as future units in the course; learn more about the history of FinTech and the areas that have been disrupted through innovation; and collaborate with others to make predictions about various FinTech domains in the form of future news headlines.

### Class Objectives

By the end of this class, students will be able to:

* Use the command line to execute basic file system operations.

* Download and upload files to GitHub using the git GUI.

* Describe the factors that led to the evolution of the FinTech industry.

* Identify the domains of the FinTech industry that have been disrupted.

* Make predictions about FinTech domains.

### Instructor Notes

* Slack out the [Anaconda Installation Guide](../../02-Python/Supplemental/AnacondaInstallGuide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. This should help catch installation issues with Python outside of the class time.

* **Note:** If you or a student has an M1 chip machine, please refer the [M1 Chip Troubleshooting Guide](../../../05-Student-Resources/Troubleshooting-Guides/M1_Chip_Troubleshooting_Guide.md) for assistance with installations.

* Students may have trouble grasping the notion of the command line. You can explain it like this: when students double-click on a folder to change directories, they are essentially executing a backend `cd` command. The GUI that a student sees is merely a visual overlay of the backend operations of the computer.

* Emphasize that understanding the history and larger context of FinTech is just as important as knowing what FinTech is. Employers will measure candidates not only by their technical skills, but also by their knowledge of what is happening in the financial services industry and the ability to grasp the bigger picture.

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [1.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0ab213e1-73b9-430f-b329-aa9500e80c9f) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 1.2 Slides](https://docs.google.com/presentation/d/1OnGPqJKAwQhVHlFKzhetS-3wLk0sOk0a7-G0Xe9vvSo/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (10 min)

Welcome students to the second day of class and the next lesson in Unit 1.

Take some time to introduce the topics that will be covered in this lesson: command line and a brief history of FinTech. This lesson will give students both the skills and knowledge required to gain a deeper understanding of the changing landscape of the FinTech ecosystem.

Use the slideshow to review the objectives for today's class.

Cover the following points:

* While later units and activities will utilize more advanced tools and technical concepts (APIs, algorithmic trading, etc.), today’s lesson will start small. We’ll begin by practicing the fundamentals of technical programming so that students can begin their FinTech journey.

* Students will begin working with fundamental developer tools such as the command line, a text-based utility for performing file system operations and executing programs. By the end of the day, students will join the ranks of millions of developers who also use the command line for file system operations and third-party CLIs (e.g., Conda).

* Today's lesson will briefly provide insight into the factors leading up to the current state of FinTech, as well as the financial sectors and FinTech domains that technology has helped to disrupt. It will also include a group activity in which students will research the factors for change of a particular FinTech domain.

* Understanding and being able to discuss FinTech's history is useful, particularly when applying to jobs; it will show employers that you care enough to familiarize yourself with the industry, as well as showcase an understanding of potential opportunities and pitfalls within the industry.

Encourage students and get them excited for the lesson. Reiterate that today will be a crash course in both hard and soft skills: students will learn technical skills and contextual knowledge to aid them in their future careers in FinTech.

---

### 2. Instructor Do: Terminal (10 min)

In this section, students will learn the basics of using the command line to perform basic file system operations on their machines.

Continue using the slides as you present the following questions and answers:

* What is the command line?

  **Answer:** The command line, or terminal, is an interface in which a user can type and execute text-based commands.

* When should you use the command line?

  **Answer:** The command line can be used at any time in place of the graphical user interface (GUI). The GUI is merely a visual overlay to the programs executed via the command line. Also, when remotely connecting to a server, such as via the Secure Shell (SSH) protocol, a GUI will not be provided.

* Why use the command line?

  **Answer:** Using the command line is efficient, as it does not expend the additional processing needed to produce the visuals associated with a graphical user interface (GUI).

Open the command line and demo the following commands. Tell students that on a Mac, the command line is accessed via Terminal, while Windows uses Git Bash.

* `cd` changes the directory.

* `cd ~` navigates to the home directory.

* `cd ..` moves up one directory.

* `ls` lists files in the folder.

* `pwd` shows the current directory.

* `mkdir <FOLDERNAME>` creates a new directory with the folder name as `<FOLDERNAME>`.

* `touch <FILENAME>` creates a new empty file with the file name as `<FILENAME>`.

* `code <FILENAME>` opens a file in the VS Code editor.

* `cat <FILENAME>` reads a file and outputs to the command line.

* `rm <FILENAME>` deletes a file.

* `rm -r <FOLDERNAME>` deletes a folder recursively; make sure to note the -r.

* `open .` opens the current folder in Terminal (Mac users).

* `explorer .`opens the current folder in Git Bash (Windows users).

* `open <FILENAME>` opens a specific file in Terminal (Mac users).

* `explorer <FILENAME>` opens a specific file in Git Bash (Windows users).

![terminal-example](Images/terminal-example.png)

Slack out [CommonCommands.txt](Activities/01-Ins_Terminal/Solved/CommonCommands.md) for students to use as a reference.

Answer any questions before moving on.

---

### 3. Student Do: Terminal (15 min)

In this activity, students will perform their own file system operations via the command line.

**File:** [README.md](Activities/02-Stu_Terminal/README.md)

---

### 4. Instructor Do: Review Terminal (5 min)

Open [file_system_operations.sh](Activities/02-Stu_Terminal/Solved/file_system_operations.sh) and cover the following points. You can also use the slides to show these definitions to students:

* `mkdir` creates folder directories.

* `cd` navigates into specified folder directories.

* `touch` creates an empty file.

* `cat` reads files and outputs the results to the console.

* `code` opens files in the VS Code.

* `cd ..` navigates up one level.

* `cp` copies files from source to target.

* `rm -r` recursively deletes all files in a folder (that may have subfolders).

* `mv` moves files from source to target. It can also be used to rename a file.

* `ls` lists the contents of the current directory.

---

### 5. Instructor Do: Version Control and GitHub (20 min)

In this section, students will learn about file version control and how to upload files to GitHub, which will be used to submit homework assignments in this course.

Continue through the slides while covering the following points about version control.

* **Versioning** is simply a way to keep track of changes to files and folders over time.

* Git and GitHub are tools that make tracking changes easy.

* GitHub is a central location to create projects and track changes to files and folders in that project.

* Developers use GitHub as a centralized place to push and pull (upload and download) their code; GitHub always holds the most up-to-date code and files and handles everyone's updates appropriately.

* Under the covers, GitHub uses the git tool for file versioning.

  * GitHub is just one of many vendors that use git in the backend (e.g., GitLab).

  * For now, students will only be introduced to the GitHub GUI; however, in the next lesson, students will learn to work with GitHub via the command line using git, which allows for more advanced git operations.

* GitHub uses `commits` to track changes. You can think of a commit as a snapshot of what the files and folders looked like at a particular moment in time. You can always see any version of your changes by looking at the previous commits.

Finally, have the students follow along to complete these steps:

* Visit [the GitHub website](https://github.com) and ask students to log in to their personal accounts.

* From the main page, create a new repository with an initialized `README.md` file.

  * Note that the convention in the software world is for each repository to have a README file that explains what the repository contains.

  ![git repo](Images/GitDemo_1.png)

* Create a new Excel file and save it to your desktop. This file will be used to demonstrate how to upload new files.

* Navigate back to GitHub and click the "Upload files" button.

  ![upload file](Images/GitDemo_upload.png)

* Choose your Excel file in the dialog box.

  * Note that you can also drag and drop the file rather than use the "Upload files" button.

* Add a commit message and commit the changes.

* Refresh the webpage to show that the new file is now safely saved to the repository.

  ![drag file](Images/GitDemo_filedrag.gif)

Encourage students to practice using GitHub before the next class and attend office hours if they run into any problems.

---

### 6. BREAK (15 min)

---

### 7. Instructor Do: The Impact of FinTech (10 min)

In this activity, you will transition students from the technical demos of the first half of the class (command line and git GUI) to the more interactive discussion-based second half; now, we will quickly discuss what we've learned about FinTech so far and begin to focus not just on its history, but also the current state of its ecosystem and its future possibilities.

First, allow students to do a quick turn-and-teach with each other and pose the question "what have we learned about FinTech so far?" Then, ask for any volunteers who would be willing to share their thoughts. Student responses should be similar to the following:

* FinTech is the combination of finance and technology and represents the state of the modern finance industry; it aims to bolster traditional financial methods and services with technology to increase efficiencies in finance.

* FinTech has changed immensely over the past 20+ years, due to advancements in technology and shifts in consumer preferences.

* Due to FinTech's rapid growth in recent years, demand for technological investment, and more importantly the technical expertise driving such investment, has exploded. Thus, there is a shortage of workers in the FinTech industry, and this makes it an attractive career opportunity in terms of growth and pay.

Lastly, explain the following to the students:

* The remainder of class will be a deep dive into FinTech's past, present, and future.

* Specifically, we will focus on the factors leading to the recent explosion of technological investment in the FinTech realm, the current breakdown of the FinTech ecosystem, and the potential outcomes of the FinTech realm given its current trajectory.

---

### 8. Instructor Do: Evolution of FinTech (10 min)

In this section, give students a brief summary of some of the key factors leading to the growth of the FinTech space. Understanding the historical background of FinTech as well as its current trajectory will give students knowledge that will help them both in employer interviews and their FinTech career.

Using the slides to review the key historical factors leading to the present-day FinTech boom.

* Mobile Infrastructure and Shifting Consumer Preferences

  * With the advancements in mobile network infrastructure (2G, 3G, 4G LTE), consumers have become more connected to the internet (as well as each other) than ever before.

  * As a result, consumers not only have a greater resource pool to cross-check and validate information (e.g., checking prices), but also have become a resource pool themselves, which companies look to target for business.

  * Today, consumers demand quick, reliable, and quality channels of engagement. They are inclined to place their trust in a company that boasts a dynamic and beautiful website, a well-designed and efficient mobile application, and (if possible) a social user platform for connecting with others using the similar product.

  * Therefore, companies have been forced to make large investments in technology in order to stay competitive with their industry peers. Consumers have more product choices and are loyal to companies they trust. Therefore, the technological channels affecting consumer engagement have a direct impact on a company's ability to market itself and, ultimately, capitalize on demand.

* Big Data

  * Over the years, computer processing units (CPUs), random access memory (RAM), and hard drive storage devices have become more powerful and less expensive. Therefore, more companies were able to purchase and utilize large clusters of computers working in parallel.

  * Parallel processing paradigms have also shifted to become more efficient. Traditionally, to enable machines to work in parallel, the concept of MapReduce was born. With MapReduce, data workloads were split among multiple machines for disk-based processing, and then re-aggregated at the end to produce the result. With the advent of Spark, that same process has been refined for in-memory processing, in which data workloads utilize RAM that is much faster at processing data (though more costly).

  * Because big data processing has become more efficient, the time needed to curate and analyze data has also decreased. Therefore, modern-day companies are able to employ tactics like machine learning to drive business decision-making in real time.

  * Companies have placed enormous emphasis on technological investment due to the growing feasibility and allure of housing large clusters of machines to drive real-time, data-driven analysis.

* Cloud Infrastructure

  * Traditionally, server farms, or large clusters of machines, required large up-front costs and overhead related to server maintenance.

  * With the inception of cloud computing, however, companies no longer had to purchase their own servers for their data-processing needs, but instead could "rent" servers from another vendor on an as-needed (and, therefore, much cheaper) basis. This allowed smaller companies to compete with larger, more established companies in regard to utilizing big data.

  * In addition, because cloud vendors like Amazon Web Services (AWS) manage hosting and deployment of servers in the cloud, the time-to-market for companies to reap the benefits of investing in technology has decreased, as they are able to push their applications and features quicker.

  * The business landscape has become increasingly competitive, as smaller companies now have the capabilities to disrupt markets with their fully fledged, productionalized applications and services––which previously would have required large up-front costs serving as a potential barrier to entry of the industry.

Answer any questions before moving on.

---

### 9. Instructor Do: FinTech Domains (10 min)

This section will be a brief discussion of the positive impact that technology has had on the finance world. Then, we'll transition to the topic of specific FinTech domains in which traditional financial activities have been replaced with more efficient means due to technological innovations.

Use the slideshow to ask the students the following questions.

* What are some areas in the financial industry in which technology has disrupted traditional finance activities?

  **Sample Answer:** Blockchain and financial transactions; robo advisors and investment management; payment applications and money transfers.

* How did these technologies allow for the disruption of traditional finance?

  **Sample Answer:** Blockchain allows for cheaper and more secure transactional validation. Robo advisors utilize machine learning algorithms for portfolio management, thereby reducing overhead costs. Payment applications utilize modern infrastructure such as mobile and cloud-based networking.

* How might cloud-based networking contribute to the advent of start-ups and technological innovators?

  **Sample Answer:** Traditionally, hosting servers meant purchasing on-premises server farms with large up-front costs and regular maintenance, which was a barrier for entry for small start-ups. However, with cloud-based networking such as AWS, small start-ups and even individuals can quickly spin up servers faster and on an as-needed basis, thereby minimizing time to deployment and reducing up-front costs. This allows small start-ups to compete more efficiently with larger firms that have existing infrastructures.

* Where else might technology disrupt traditional finance?

  **Sample Answer:** Machine learning can be used in lending to more efficiently target customers who have a higher likelihood of paying back their loans, while avoiding those who have a higher likelihood of *not* paying back their loans.

Then, end the discussion with the following points:

* The field of FinTech is so vast and rapidly changing due to technological innovation that even entire domains of the FinTech ecosystem have begun to change the way in which companies operate and compete with their peers.

* In order to complete the Unit 1 homework assignment (FinTech case study), students will need to comprehend the nature of the FinTech domains as well as the competitive factors affecting the underlying companies within those domains. Therefore, we will need to take a closer look at the FinTech landscape.

---

### 10. Student Do: FinTech Domains, Part 1 (35 min)

In this activity, students will work in groups to research and answer questions about various FinTech domains.

**File:** [README.md](Activities/03-Stu_FinTech_Domains_Part_I/README.md)

**Note:** There should be an even number of groups for this activity.

---

### 11. Instructor Do: Review FinTech Domains, Part 1 (10 min)

First, ask students the following questions:

* Did you find any of the FinTech domains, companies, or technologies to be confusing?

* Did you find anything notable or interesting while researching the FinTech domains?

If students are confused or want more information, use the appendix section of the slides to review the following FinTech domains and trends.

* Payments and Remittances
* Robo Advisors and Personal Finance
* RegTech
* Digital Banking
* InsurTech
* Alternative Finance

---

### 12. Student Do: FinTech Domains, Part 2 (10 min)

In this activity, students will build on the research gathered in Part 1 to create hypothetical news headlines for each FinTech domain for events that could potentially occur within the next five years. Students will continue working in their groups to complete this activity.

---

**File:** [README.md](Activities/04-Stu_FinTech_Domains_Part_II/README.md)

### 13. Instructor Do: Review FinTech Domains, Part 2 (15 min)

To review the previous activity, facilitate a class discussion based on each group's findings and thoughts.

Tell students the following:

* This review will be done in the form of a turn-and-teach, in which each group will present their news headlines to the group next to them.

* Students that they can send any relevant documents (containing FinTech domain information) to their peer group members to facilitate quicker and easier information transfer.

**Note:** There should be an even number of groups to perform a turn-and-teach; however, if there is an odd number of groups, feel free to put three groups together to share their headlines.

Walk around the class with your TAs to support any discussions if necessary.

After the turn-and-teach, ask for volunteers to share notable or interesting FinTech news headlines that they heard from their peer groups. Then, explain the following:

* The intent of this activity was to provide students with not only the breadth but also the depth of knowledge for each FinTech domain. This knowledge will prove valuable when applying for roles within the FinTech industry.

* It's not enough to simply restate the past; you should also analyze and predict the future. After completing this activity, students should have a general idea about the trends affecting each FinTech domain as well as the potential outcomes that may result for each domain in the near future.

Ask if there are any questions before moving on.

---

### 14. Instructor Do: Review and Reflect (5 min)

Use the last few minutes of class to allow the students to digest and decompress from this lesson.

First, congratulate students for completing this class! They should be proud, as the pace of today's class was much quicker than the previous class.

Recap today's objectives. Students are now able to:

* Use the command line to execute basic file system operations.

* Download and upload files to GitHub using the git GUI.

* Describe the factors that led to the evolution of the FinTech industry.

* Identify the domains of the FinTech industry that have been disrupted.

* Make predictions about FinTech domains.

Remind students that as FinTech professionals, they need to be both technical experts with cutting-edge skills as well as seasoned financiers. Today's lesson was good practice in both of these aspects; students are on their way to becoming FinTech subject matter experts (SMEs).

Ask if students have any remaining questions before ending the class. If needed, TAs will be hosting office hours after class.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
