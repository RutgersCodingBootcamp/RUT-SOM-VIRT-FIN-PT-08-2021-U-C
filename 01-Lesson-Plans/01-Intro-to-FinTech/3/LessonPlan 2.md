## 1.3 Lesson Plan: FinTech Collaboration

---

### Overview

In today's class, students will learn how to utilize the git command line interface (CLI) and create markdown files to generate FinTech case studies that can be collaboratively stored, accessed/modified, and previewed on an online git or file repository such as GitHub. A solid understanding of the git CLI as well as knowing how to create markdown files will help students properly manage git repositories and construct visually enhanced README description files.

### Class Objectives

By the end of class, students will be able to:

* Configure the git CLI user credentials from the command line.

* Clone a repository using `git clone`.

* Modify git repositories by adding, committing, and pushing files.

* Create markdown files and implement visual capabilities such as text formatting, images, and links.

* Write a FinTech case study in markdown and host it in a shared GitHub repository.

### Instructor Notes

* As a reminder, slack out the [Anaconda Installation Guide](../../02-Python/Supplemental/AnacondaInstallGuide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. This should help catch installation issues with Python outside of the class time.

* Today's lesson may make students feel uneasy as they continue to use the command line to interact with both files on their local file system as well as files that are actively tracked via an online repository. Calm students' nerves by telling them that git is merely a command line tool––a program that exists on the local file system that executes from the command line, or terminal.

* Make sure that by the end of class students have the tools to create well-presented markdown README files to host in their git repositories. They'll need these to showcase their git repositories (and the coding assets within them) to potential future employers.

* More advanced git operations such as git branches, merges, and checkouts will not be introduced in this lesson. Therefore, be aware that students may face merge conflicts that prevent them from pushing their file changes to the git repository when collaborating with others working in the same git repository.

* Be mindful of students working in groups during the case study activity; some students may be less vocal than others. Circulate the classroom with the TAs and make sure that every student is actively engaged and participating in their group's discussion.

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [1.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=29698287-5856-45e6-9373-aa9800300d03) Note that this video may not reflect the most recent lesson plan.


### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 1.3 Slides](https://docs.google.com/presentation/d/13FM_RgUT0YqTRZJw01gMFNdufGl92tN2A8cR3-uxy0Y/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students to the third day of class and the final lesson of Unit 1.

**File:** [Lesson 1.3 Slideshow](https://docs.google.com/presentation/d/13FM_RgUT0YqTRZJw01gMFNdufGl92tN2A8cR3-uxy0Y/edit?usp=sharing)

Use the slides to introduce today's lesson and objectives. Then, review the following points with students:

* The previous two lessons focused on introducing the FinTech course structure as well as the FinTech industry more broadly. We discussed the history and current landscape of the FinTech ecosystem, as well as specific factors that have led to changes in various FinTech domains.

* Today, students will apply what they've learned so far about the FinTech industry to write their own case studies in visually enhanced markdown files, and then host them in a GitHub repository.

* Today's goal is twofold. Students will learn how to (1) manage their own repositories and develop in shared repositories, and (2) develop text-based assets in markdown to provide visually appealing README files that can be previewed in GitHub (and, therefore, showcased to potential employers).

* In this lesson, students will be divided into groups and given a selection of FinTech case study proposals to choose from. Students will need to work collaboratively and generate a visually appealing document that can be hosted online––which is where git CLI and markdown comes in!

Energize your students! Remind them that they'll be using collaborative tools (git) that real developers and industry professionals use to share and build upon code.

---

### 2. Instructor Do: GitHub Refresher (10 min)

This section provides students with a quick recap of how to create and download a git repository, use the command line to navigate and edit a text file in the local repository folder, and then upload the file to the git repository. This section serves as a precursor to the later git CLI activities, as it showcases the limitations of downloading a repository as a local folder versus performing a `git clone`, in which git can track and compare changes.

**File:** [GitHub Refresher Slides](https://docs.google.com/presentation/d/13FM_RgUT0YqTRZJw01gMFNdufGl92tN2A8cR3-uxy0Y/edit#slide=id.g5d815a1bb6_2_0)

Open the slideshow and present the following questions and answers.

* What is git?

  **Answer:** Git is a version-control system for tracking changes in files––often from a coding and software development standpoint. Git is designed for coordinating work among programmers, but it can be used to track changes in any set of files.

* What is a git repository?

  **Answer:** A git repository is a remote or online file repository in which git tracks files and conducts version control as changes are made.

* How is git used?

  **Answer:** Git is often used via the command line, but vendors such as GitHub and GitLab provide web and desktop apps that allow users to use git via a GUI.

* What is GitHub?

  **Answer:** GitHub is a web-based file-hosting service that is one of the many vendors that uses git for file version control.

* Why is git important?

  **Answer:** Git is an extremely powerful tool for software development. It has become the standard for versioning software and data science tools across industries, and is even used to version data and enhance data reproducibility. For these reasons, proficiency in GitHub has become a critical job skill. In fact, it will be one of the most essential job skills in students' careers in FinTech.

Then, demonstrate how to create a repository in GitHub, edit files in that repo, and commit and push changes. Be sure to cover the following points:

* Git repositories can be created via the GitHub website. Check the option to "Initialize this repository with a README" to automatically deploy the repository.

  ![github-website](Images/github-website.png)

  ![github-create-repository](Images/github-create-repository.png)

* A git repository can then be downloaded locally as a compressed ZIP file.

  ![github-download](Images/github-download.png)

* Unzip, or decompress, the ZIP file. Then, access the extracted git repository folder via the command line by performing a `cd` command to change directory inside the folder. Use the `ls` command with the `-l` parameter to display the folder's contents in list format.

  ![terminal-git-repository](Images/terminal-git-repository.png)

* The `code` utility opens text files from the command line in VS Code, where they are edited.

  ![terminal-vscode](Images/terminal-vscode.png)

  ![vscode-editor](Images/vscode-editor.png)

* Here, `README.md` is edited and saved in the local git repository. However, changes are still local and will need to be pushed to the remote repository in GitHub.

  ![git-local-change](Images/git-local-change.png)

* Files can be committed and changed in the online GitHub repo by clicking on the "Upload files" button, and then navigating to the file upload webpage.

  ![github-upload-files](Images/github-upload-files.png)

  ![github-remote-change](Images/github-remote-change.png)

* The `README.md` preview in GitHub confirms the changes.

  ![github-remote-change-confirmation](Images/github-remote-change-confirmation.png)

Ask if there are any questions before moving on.

---

### 3. Student Do: Refresher (15 min)

In this activity, students will follow the steps in the preceding instructor demo to create their own repository in GitHub and modify the README file in order to personalize their repo.

**Instructions:** [README.md](Activities/01-Stu_Refresher/README.md)

### 4. Instructor Do: Review Refresher (5 min)

Review the previous activity with students, highlighting the following points:

* Be sure to initialize the new GitHub repository with a `README.md` file. Otherwise, deployment of the repository will be halted until further setup is completed.

  ![github-create-repo-uninitialized](Images/github-create-repo-uninitialized.png)

* When downloading the GitHub repository as a ZIP file, contents must first be extracted in order to edit any of the files.

  ![github-repo-unzipped](Images/github-repo-unzipped.png)

* The `code` command line utility is often used as a quick shortcut to jump from the terminal to editing files directly in VS Code.

  ![vscode-familiarity](Images/vscode-familiarity.png)

* After modifying the `README.md` file on the local file system, changed files will have to be pushed or re-uploaded to the online repository.

  ![github-file-upload-update](Images/github-file-upload-update.png)

* GitHub should automatically be able to preview `.md`, or markdown, files, as they contain style formatting elements and therefore should immediately reflect the changes of the updated `README.md` file. If not, manually refresh the page.

  ![github-readme-update](Images/github-readme-update.png)

---

### 5. Instructor Do: Introduction to Git CLI (10 min)

In this section, students will be introduced to the git CLI and additional git operations, which will allow them to more efficiently track changes to a git repository.

**File:** [Introduction to Git CLI Slides](https://docs.google.com/presentation/d/13FM_RgUT0YqTRZJw01gMFNdufGl92tN2A8cR3-uxy0Y/edit#slide=id.g5d80c858bb_1_1206)

Use the slides to review the following points.

* How the GitHub web app differs from the git CLI:

  * The GitHub web app provides a convenient user interface for performing common git operations. The git CLI is a command line utility that provides all git operations; it is generally more robust than a git-based graphical user interface (GUI).

  * This is due to the fact that, more often than not, a GUI interacts with the underlying CLI to perform its functionality (e.g., click a button that executes a command on the back-end) and, therefore, is often a simplified version of the underlying functionality.

* How one configures the git CLI:

  * Open the command line.

  * Set your username:

      * `git config --global user.name "FIRST_NAME LAST_NAME"`

  * Set your email address:

      * `git config --global user.email "MY_NAME@example.com"`

![git-config](Images/git-config.png)

* Common git CLI commands:

  * `git clone`: Clones a git repository to the local file system.

  * `git add`: Adds changed files to the queue of tracked files ready to be committed.

  * `git commit`: Adds tracked files as a bulk checkpoint ready to be pushed to the remote git repository.

  * `git push`: Uploads changed files from the local git repository to the remote git repository and updates the remote files.

  * `git pull`: Downloads changed files from the remote git repository to the local git repository and updates the local files.

  Then, tell students it's time for a GitHub pop quiz. Use the slides to walk through the following questions and answers.

* What is a git commit?

  * A git commit saves a queue of tracked changed files as a **save** or **checkpoint** for a git repository before the changed files are pushed from the local to the remote git repository.

  * This way, a git repository can be restored to a previous checkpoint in time, thereby undoing any existing changes from that point.

* What is git's Snapshot Model?

  * Git thinks of its data as a series of snapshots of a miniature file system. Every time you commit, or save the state of your project in git, it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot.

  * To be efficient, if files have not changed, git doesn’t store the file again; rather, it stores a link to the previous identical file it has already stored.

Ask if there are any questions before moving on.

---

### 6. Instructor Do: Git CLI Demo (10 min)

In this section, you will demo how to add folder structures to students' newly created GitHub repositories.

Demo the following:

* Revisit the GitHub website and click the "Clone or download" button.

* This time, copy the URL, as it represents the GitHub repository link (which will be used for the `git clone` command).

  ![github-url](Images/github-url.png)

* Open the command line and run `pwd` to determine the current work directory. Then, perform the `cd` operation to navigate to the desktop.

  ![terminal-pwd-cd](Images/terminal-pwd-cd.png)

* Run `git clone <repository link>` to clone the repo to the current directory.

  * Copying a repository via the `git clone` command differs from just downloading a ZIP file of the repository.

  * `git clone` downloads a tracked git repository to the local file system, while the ZIP file merely downloads the contents without any kind of tracking or version control involved.

  ![git-clone](Images/git-clone.png)

* Create three folders in the local git repository via the `mkdir` command: `data`, `references`, and `code`. Add a `.gitkeep` file to each folder so that git knows to retain the folders. (Git refrains from keeping empty folders unless explicitly told to do so.)

  ![git-repository-mkdir](Images/git-repository-mkdir.png)

  ![git-repository-gitkeep](Images/git-repository-gitkeep.png)

* Once the folders and files have been created, go to the command line and navigate to the root of the git repo folder. Run the following lines to push the changes to the remote git repository:

**Note:** Be sure to explain each piece of code as you run it.

  ```bash
  # Displays git untracked/tracked status of files in the folder
  git status

  # Adds all files and sub-folder files into a staging area
  git add .

  # Performed again to check that the files were added correctly
  git status

  # Commits all the files to your repo and adds a message
  git commit -m <add commit message here>

  # Pushes the changes up to GitHub
  git push
  ```

* Navigate to the GitHub repository to confirm that the changes have been pushed up.

  ![git-push-results](Images/git-push-results.png)

Make sure all students were able to successfully clone a repository, add files to the repo, commit the changes, and then push the changes to GitHub all from the command line. Ask your TAs to assist students if needed.

---

### 7. Student Do: Git CLI (15 min)

In this activity, students will use the git CLI to clone their git repositories to their local file systems, and then add directories to their GitHub repositories.

**Instructions:** [README.md](Activities/02-Stu_Git_CLI/README.md)

### 8. Instructor Do: Review Git CLI (10 min)

In this section, review the previous activity and take some time to answer students' questions.

First, ask students if they have any questions, and review commands they are having trouble with. Encourage students to attend office hours if they need additional review.

Then, tell students the following:

* The process completed in this activity will be the primary way of submitting homework assignments to GitHub. (No more manual uploads!)

* If it takes some time to figure out, that's okay. By the end of the course, everyone will be git ninjas!

Encourage students to continue adding and committing to GitHub for extra practice.

---

### 9. Instructor Do: Markdown (10 min)

In this part of the lesson, students will be introduced to markdown files and their style formatting, which can be used to create visually appealing README files.

**File:** [Markdown Slides](https://docs.google.com/presentation/d/13FM_RgUT0YqTRZJw01gMFNdufGl92tN2A8cR3-uxy0Y/edit#slide=id.g5d815a1bb6_2_20)

Open the slideshow and review the Markdown slides, while presenting the following questions and answers.
* What is markdown?

  **Answer:** Markdown is a lightweight markup language that contains syntax for adding formatting elements to plain-text documents.

* Why use markdown?

  **Answer:** Markdown provides features for creating visually enhanced documents that are rendered on the web. It is commonly used for documents such as README files or online forum discussion posts.

* What are some common markdown features?

  * Header formatting

  * Text formatting

  * Line breaks

  * Text/code snippets

  * Block quotes

  * Links

  * Images

Reiterate to students the following:

* Markdown allows us to create visually enhanced documents such as README files (for GitHub repos, for example), which are valuable not only to potential employers, but also to potential collaborators (colleagues or teammates).

* A good README file helps people understand the purpose of the repository at a glance, and it shows developers how to navigate, install, and run a project.

Next, demo the following while explaining each step:

* Go to your local git repository and modify the README file within VS Code. Be sure to point to students the preview function (button on the upper right) that allows to see the final product (for those interested in a visually more appealing preview, you can refer students to the VS Code extension [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)). Also, if students do not have VS Code installed, you can refer them to an online Markdown editor (e.g. [Dillinger](https://dillinger.io/) 

  * Notice that there is a `#` in front of the README title; this is why the font appears larger in the GitHub webpage.

  * In markdown, the `#` sign represents a level 1 heading, `##` represents a level 2 heading, and so on.

  ![markdown-header](Images/markdown-header.png)

  ![markdown-header-results](Images/markdown-header-results.png)

* Use the `*` syntax to put the repository name in italics, and use `**` syntax to put the repository description in bold. Alternatively, the `*` syntax can represent a bullet point if used at the beginning of a new line.

  ![markdown-text](Images/markdown-text.png)

  ![markdwon-text-results](Images/markdown-text-results.png)

* Use the `---` syntax to put a line break below the repository name. Line breaks help to separate areas of the document.

  ![markdown-line-break](Images/markdown-line-break.png)

  ![markdown-line-break-results](Images/markdown-line-break-results.png)

* Use the backtick **`** syntax to wrap text as snippets or code. Wrapping text as snippet or code blocks adds emphasis to a specific item or piece of code.

  ![markdown-text-code-snippet](Images/markdown-text-code-snippet.png)

  ![markdown-text-code-snippet-results](Images/markdown-text-code-snippet-results.png)

* Use the `>` syntax to create a block quote with the following text: `"...to boldly go where no one has gone before".` Block quote formatting can be used when there is a large text excerpt or quote.

  ![markdown-blockquotes](Images/markdown-blockquotes.png)

  ![markdown-blockquotes-results](Images/markdown-blockquotes-results.png)

* Use the `[]()` syntax to create a directory for each folder in the repository. Links are useful in directing a reader to different webpages.

  ![markdown-links](Images/markdown-links.png)

  ![markdown-links-result](Images/markdown-links-result.png)

* Use the `![]()` syntax to add an image. Images help to visually enhance a markdown document.

  ![markdown-image-link](Images/markdown-image-link.png)

  ![markdown-image-link-results](Images/markdown-image-link-results.png)

* Notice how the newly formatted markdown file appears in comparison to the original.

Answer any questions before moving on.

---

### 10. Student Do: Markdown (15 min)

In this activity, students will visually enhance their README files for their GitHub repositories by adding additional markdown features.

**Instructions:** [README.md](Activities/03-Stu_Markdown/README.md)

### 11. Instructor Do: Review Markdown (5 min)

Take some time to review the previous activity with students, highlighting the following points:

* A well-formatted README file showcases the contents of a GitHub repository. Markdown syntax provides additional features for text formatting, links, images, and code snippets, among other things.

* Markdown is a common README format and renders on a webpage via specific syntax.

* Using markdown syntax is as easy as using the correct syntactical keyword or term. For example, the `![]()` syntax is used specifically for linking images to the markdown file.

Encourage students to continue building their GitHub README files as they progress through the course, particularly when they begin generating coding assets. The goal is to have professional-looking README files for their GitHub repo by the end of this course.

---

### 12. BREAK (40 min)

---

### 13. Instructor Do: Introduce Case Studies and Git Collaboration (15 min)

In this part of the lesson, you will prepare students to work in pairs to create a shortened FinTech case study in a shared GitHub repo. Remind students that this is an abbreviated version of their longer Unit 1 homework assignment, but they can use this activity to begin initial research on a potential FinTech company.

Tell students the following:

* Now that students know how to manage their own GitHub repositories and create text-formatted markdown files, they can move on to creating shared repositories in which multiple people collaborate to create a case study report.

* Git repositories are often shared and have multiple collaborators; therefore, this activity will give students practice in this kind of scenario.

As a brief introduction to collaboration on Git, create a new example repository that contains only the readme.md and demonstrate to students how you can invite collaborators to a repository  via 'Settings' and then 'Manage Access' (you could use one of your teaching assistants as a collaborator or set up a new test account for this purpose):

  ![markdown-image-link](Images/git-collab.png)

Be sure to remind students that the invitation should be sent to the e-mail associated with the Github account and that invitations won't show up on the github website, but need to be accessed via e-mail (click on link in invite).

Once you have invited a collaborator, make sure they clone the repository to their local computer (as illustrated earlier)  and ask your collaborator to make a few changes to the readme-file and push them to the repository. 

Since most students are fairly new to Git, introducing more advanced concepts such as 'branching' and 'forking' can become overwhelming and might be better suited for later classes when everyone has become comfortable with the initial steps.

Optional: If there is enough time, you could have students practice these initial steps by having them collaborate on a simple competition, where students are split up in groups of 2, and have to create as many steps of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in their Readme.md, where each number is the sum of the two preceding numbers:

0, 1, 1, 2, 3, 5, 8, 13, ...

That is the owner of the repository creates the first step of the series, and then the collaborator adds the next one, then the owner adds another one etc, where each commit can only contain one additional number. The group that adds the most steps within 5 minutes wins.


Next, provide an overview of the activity.

* In the class GitHub repository, there will be a list of FinTech case study proposals. These include information about the company, reasons the company might make for an interesting case study, and additional resources to explore.

* Students should pair off, choose one of the FinTech companies on the list, and then conduct their research.

* Students will have 20 minutes to develop their case studies, and 2 to 3 minutes to present their reports.

Slack out the [case study examples](Activities/04-Stu_Group_Case_Study/Resources) to the class for reference. Get them excited! This activity is a great opportunity for students to combine what they've learned technically (command line and git) as well as conceptually (FinTech domains) to produce a company analysis.

---

### 14. Student Do: Group Case Study (20 min)

In this activity, students will work in pairs to create a shortened case study report on a particular FinTech company, which will be chosen from a list of case study proposals. Each team will create a shared GitHub repository and write their report in markdown.

**Instructions:** [README.md](Activities/04-Stu_Group_Case_Study/README.md)

### 15. Instructor Do: Review Group Case Study (15 min)

Students will now present their findings to the class.

Explain that each team should take 2 to 3 minutes to share their reports. They should log into their shared GitHub repo and use the markdown file they created to guide their presentation.

**Note:** Make sure that all students participate in the presentation and are given an opportunity to speak.

After each group has presented, do a pulse check on the class; that is, check in with them to see how they're feeling about the material. Ask students if they have any questions and if they found the activity to be enjoyable.

Finally, remind students that the Unit 1 homework assignment is a FinTech case study. Students can leverage the content created in this activity to complete the homework requirements.

### 16. Instructor Do: Reflect (5 min)

Take a moment to reflect on the lesson with students. Ask for volunteers to share personal highlights and takeaways from the week.

---

### 17. Instructor Do: Career Services (35 min)

**Note:** If you are teaching this lesson on a weeknight, save this section for the next Saturday class.

**Note:** The 35 minutes allocated for this lesson are broken out into each subsection below.

#### 17.1 Instructor Do: Career Services Introduction (5 min)

Explain to students that we've spent a great deal of time introducing ourselves to the FinTech curriculum; learning the basics, and preparing our tools for the course. But we also want to make sure we're focusing on where you will go once the course is over. Starting today, we're going to dedicate time on certain Saturday classes to talk specifically about Career Services.

Students probably know fairly little about Career Services. So today, you will:

* introduce students to Career Services, the various people they'll come in contact with, and the services offered during and after boot camp,
* ensure students understand what it means and takes to become **employer-ready**,
* show students how to sign up for workshops offered by Career Services

#### 17.2 Instructor Do: Career Services Video (20 min)

* Navigate to the [Career Services resource page](https://mycareerspot.org/intro). Slack out the link to your students, so they have it as well.

* Let students know that this site contains many resources provided by Career Services that they can freely use during and after their time in boot camp.

* 🎬 Play the video in the middle of the page, `Employer-ready vs. Employer-competitive`. Ask students to write down any terms or words that are unfamiliar to them.

* After the video, ask the class the following questions (☝️) and call on students for the answers (🙋):

  ☝️ What is Career Services?

  🙋 Our partner in success. Whether we are job seekers or promotion seekers, Career Services can help us improve our behavioural and technical interviewing skills, as well as create great professional materials (resume, portfolio, LinkedIn etc.)

  ☝️ So there's a lot of keywords in this video, or jargon, that we may not know. Did anybody note anything down that they didn't know?

  🙋 Students will give a variety of answers, likely touching on some of these below. Take the time to run through each of them and give students a cursory idea of what they are:

  * **Employer-ready**: Career Services has talked with thousands of employers and they know exactly what employers are looking for when they receive an application. _Employer-ready means that you have the minimum requirements to enter into a typical job application process. Your job search materials are strong and complete._ Every job-seeking student in this class should make it their goal to be employer-ready BY graduation so that they are ready for the job search.

  * **Employer-competitive**: Taking it a step further, _employer-competitive candidates position themselves for success by networking and performing company research, as well as preparing exemplary professional materials, and demonstrating their commitment to ongoing learning. Employer-competitive candidates proactive seek and pursue jobs they desire with effective outreach and follow-up strategies._

  * **Career Director**: Offers quality coaching, strategies, and resources to help you become employer-competitive. You can meet with a Career Director by phone/video, 1:1 throughout and after the boot camp.

  * **Profile Coach (now, Career Material Advisor)**: Offers unlimited feedback on professional materials to help you become employer-competitive. Career Material Advisors receive your materials via digital submission (BootcampSpot, Canvas, etc.).

  * **Demo Day**: Once boot camp is over, we will invite you to present at an event where we will invite local employers and recruiters to view your projects, ask you questions, and hopefully, offer you a job!

  * **Whiteboarding sessions**: Actually, Career Services offers a wide range of sessions on whiteboarding, talking tech with recruiters, tackling online technical assessments and behavioural interviewing techniques. You can find these on your BootcampSpot or Canvas calendar.

#### 17.3 Students Do: Employer-Ready Criteria (8 min)

* Ask students to navigate [employer-ready section](https://mycareerspot.org/employerready) of the site.

* In groups of 2 or 3, ask students to review the employer-ready requirements.

#### 17.4 Instructor Do: Wrap-up (2 min)

* ✅ Let students know that if they already have some of these materials, and it's likely that some already do if they're working in a finance or tech-related field, that they can already submit these materials to a Career Materials Advisor (formerly, Profile Coach) for review!

* ✅ Encourage students to check out the Career Services workshops and sign up for anything that seems useful or interesting to them at this point. There are both general sessions and FinTech specific technical interviewing sessions available.




### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
