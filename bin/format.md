<details>
  <summary>Install Tools and Configure AWS CLI</summary>

## Introduction

This short setup lesson covers the **tools** you need before later **HOL** work: download the **course code** from the last lesson in this section (GitHub), install **Visual Studio Code**, install the **AWS CLI** on your computer, and confirm you can open **AWS CloudShell**. CloudShell is a **browser CLI** that is **already authenticated** as the user you are signed in as. The local CLI cannot run AWS commands until you configure credentials later, after you create an **IAM user**. AWS CLI commands are the **same** in CloudShell and on your machine; only **OS** file-system commands differ.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c57815e8-f988-4333-99ba-e0f78a1023a4" />

## Detailed Explanation

- [x] **Download the course code first**
  - Finish this section by opening the **last lesson**—it contains the **code**.
  - That lesson links to a **GitHub** page where you download the files.
  - If you already use **Git**, you can **synchronize / clone** the repository instead of downloading a zip.
- [x] **Visual Studio Code**
  - Used to open **code snippets** and **instruction files** in later lessons.
  - **Microsoft** product and **free**.
  - Search for **Visual Studio Code**, download the build for **your OS**, and install it.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/997a02b7-e9e0-42bf-8803-9f5899276ddb" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fdf025c1-9cb1-4097-9401-7fd566bcc46e" />

- [x] **AWS Command Line Interface (CLI)**
  - Search for **AWS command line interface**, then open **Install or update to the latest version of the AWS CLI**.
  - Lets you run **CLI commands from your computer**.
  - Installers exist for **Linux**, **macOS**, and **Windows**—pick yours and follow the package steps.
  - After install you still **cannot** run AWS commands until you **authenticate**.
  - Credential setup is shown **later**, after you create an **individual IAM user**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/de0242a0-9b90-42fd-8754-4c00d9484f67" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5a204020-6d45-4d0c-8d3d-d1c7b3343d32" />

- [x] **AWS CloudShell**
  - A **command line interface in the cloud** (browser), opened from the **Management Console**.
  - The instructor now prefers it over a local CLI **in most cases**.
  - It is **preconfigured with credentials** for the user you are **logged in as**.
  - Search for **CloudShell**, click it, and wait for the environment (often up to **~30 seconds**).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/973dddc1-438d-402c-bd7b-7e64ad7b0f37" />

- [x] **CloudShell may be blocked on some new accounts**
  - AWS sometimes **restricts CloudShell** for **new accounts** that use a **new credit card** they have not seen before.
  - Students who reuse a card they already used on other AWS accounts often do **not** hit this.
  - If CloudShell will not start: **contact AWS Support** and ask them to **enable** it.
  - If Support will not enable it yet, use the **AWS CLI on your computer** instead (same AWS commands).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b590b24d-7590-4bdf-a0c7-da7e15ac45a4" />

- [x] **Same AWS CLI, different OS shell**
  - **AWS CLI commands are identical** in CloudShell and on your PC.
  - CloudShell is a **Linux** shell.
  - On **Windows**, navigating the file system is different from what you see in CloudShell.
- [x] **CloudShell usability and a first credential check**
  - Font can be small: **top-right settings** → increase size.
  - `aws help` opens CLI help; **spacebar** pages through it; **`q`** quits.
  - `aws s3 ls` lists **S3 buckets**. A brand-new account may have **none**.
  - **No error** (even with an empty list) means CloudShell already has **credentials** for that call.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1f05210f-e59b-4759-8f6c-edc2233a19b9" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ef8f6f17-6479-4076-9f2b-8f8d3427ab5c" />

<details>
  <summary>Lab</summary>

## Lab

Install the local tools, get the course code, and prove CloudShell (or the local CLI path) works. You still sign in as **root** for CloudShell; IAM credentials for the local CLI come in a later lesson.

### **Overview**

- [ ] Download the **course code**, install **VS Code** and the **AWS CLI**, and open **CloudShell**.
- [ ] You will:
  - [ ] Get the code from the **last lesson** in this section (GitHub download or `git` clone).
  - [ ] Install **Visual Studio Code** for your OS.
  - [ ] Install the **AWS CLI** for Linux, macOS, or Windows.
  - [ ] Open **CloudShell**, enlarge the font, run `aws help` and `aws s3 ls`.
  - [ ] If CloudShell is blocked, contact **AWS Support** or fall back to the local CLI later.
- [ ] Success: VS Code and the AWS CLI are installed, and CloudShell runs `aws s3 ls` without an auth error (or you have a Support / local-CLI plan).

### **Task 1: Download the course code**

- [ ] Open the **last lesson** in this section (the one that contains the **code**).
- [ ] Follow the link to the instructor **GitHub** page.
- [ ] Either:
  - [ ] **Download** the repository (zip) and extract it somewhere you will keep for HOL lessons.
  - [ ] Or, if you use Git, **clone / synchronize** the repository.

### **Task 2: Install Visual Studio Code**

- [ ] Search for **Visual Studio Code** (Microsoft, free).
- [ ] Open the official download page.
- [ ] Choose the installer for **your operating system**.
- [ ] Install VS Code and confirm it launches.
- [ ] You will use it later to open **code snippets** and **instruction files**.

### **Task 3: Install the AWS CLI**

- [ ] Search for **AWS command line interface**.
- [ ] Open **Install or update to the latest version of the AWS CLI**.
- [ ] Follow the steps for **Linux**, **macOS**, or **Windows**.
- [ ] Confirm the package installed (you will **not** run authenticated AWS commands on this machine until a later IAM-user lesson).

### **Task 4: Open AWS CloudShell**

- [ ] Sign in to the **AWS Management Console**.
- [ ] Search for **CloudShell** and open it.
- [ ] Wait for the environment to start (often up to **~30 seconds**).
- [ ] If CloudShell fails on a **new account / new credit card**:
  - [ ] Contact **AWS Support** and ask them to **enable CloudShell**.
  - [ ] If they will not enable it yet, plan to use the **local AWS CLI** after credentials are configured.

### **Task 5: Check CloudShell and credentials**

- [ ] In CloudShell, open **settings** (top right) and **increase the font size** if the text is hard to read.
- [ ] Run help and page through it:

```bash
aws help
```

- [ ] Press **spacebar** to page; type **`q`** to quit.
- [ ] List S3 buckets (a new account may show none):

```bash
aws s3 ls
```

<details>
<summary>Example successful empty list</summary>

```text
# no buckets listed, and no authentication error
```

</details>

- [ ] Confirm you did **not** get an authentication error—that means CloudShell is **preconfigured with credentials**.

Successfully installed the local tools and verified CloudShell (or documented the Support / local-CLI fallback). Local `aws` commands stay unauthenticated until the IAM user lesson.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

These AWS CLI commands are the **same** in **CloudShell** and on your computer. CloudShell is already authenticated; a local install is not until you configure credentials later.

```bash
# Open AWS CLI help (spacebar pages; q quits)
aws help
```

```bash
# List S3 buckets. Empty output with no error still means credentials work.
aws s3 ls
```

CloudShell is a **Linux** shell. On **Windows**, `cd`, `dir` / `ls`, and paths differ, but the `aws …` commands do not.

</details>

<details>
  <summary>Code</summary>

## Code

No application code in this lesson. Download the HOL files from the **GitHub** link in the **last lesson** of this section (or clone the repo). You will open those files in **Visual Studio Code** later.

```text
# No code snippets in this topic.
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where do you get the course code for later HOL lessons?

<details>
<summary>Answer</summary>

- [x] From the **last lesson** in this section.
- [x] That lesson links to a **GitHub** page.
- [x] Download the files, or **clone / synchronize** the repo if you use Git.

</details>

### Question 2: Why install Visual Studio Code for this course?

<details>
<summary>Answer</summary>

- [x] To open **code snippets** and **instruction files**.
- [x] It is a **free Microsoft** editor.
- [x] Install the build that matches **your operating system**.

</details>

### Question 3: What official page should you use to install the AWS CLI?

<details>
<summary>Answer</summary>

- [x] **Install or update to the latest version of the AWS CLI**.
- [x] Choose the package for **Linux**, **macOS**, or **Windows**.

</details>

### Question 4: Can you run AWS CLI commands on your computer right after installing the CLI?

<details>
<summary>Answer</summary>

- [x] **No.** You have not **authenticated** yet.
- [x] Credential setup is shown **later**, after you create an **IAM user**.

</details>

### Question 5: What is AWS CloudShell?

<details>
<summary>Answer</summary>

- [x] A **command line interface in the cloud**, opened from the **Management Console**.
- [x] The instructor prefers it over a local CLI **in most cases**.

</details>

### Question 6: Why is CloudShell easier than the local AWS CLI at this point in the course?

<details>
<summary>Answer</summary>

- [x] It is **preconfigured with credentials** for the user you are **logged in as**.
- [x] You do not need to run `aws configure` first.

</details>

### Question 7: How do you open CloudShell, and how long can startup take?

<details>
<summary>Answer</summary>

- [x] In the console, search for **CloudShell** and click it.
- [x] The environment often takes up to **~30 seconds** to start.

</details>

### Question 8: Why might CloudShell fail for some students?

<details>
<summary>Answer</summary>

- [x] AWS can **restrict CloudShell** on **new accounts** that use a **new credit card**.
- [x] Reusing a card already known to AWS often avoids the problem.

</details>

### Question 9: What should you do if CloudShell is restricted on your account?

<details>
<summary>Answer</summary>

- [x] **Contact AWS Support** and ask them to **enable CloudShell**.
- [x] If they will not enable it yet, use the **AWS CLI on your computer** instead.

</details>

### Question 10: Are AWS CLI commands different in CloudShell vs on your PC?

<details>
<summary>Answer</summary>

- [x] **No.** The **AWS CLI commands are identical**.
- [x] **Operating-system** commands (file-system navigation) can differ.
- [x] CloudShell is **Linux**; a local **Windows** shell uses different navigation commands.

</details>

### Question 11: How do you make CloudShell text easier to read?

<details>
<summary>Answer</summary>

- [x] Open **settings** in the **top-right** corner.
- [x] **Increase the font size**.

</details>

### Question 12: How do you use `aws help` in CloudShell?

<details>
<summary>Answer</summary>

- [x] Run `aws help`.
- [x] Press **spacebar** to page through the help.
- [x] Type **`q`** to quit.

</details>

### Question 13: What does `aws s3 ls` do, and what should a new account show?

<details>
<summary>Answer</summary>

- [x] It lists **Amazon S3 buckets**.
- [x] A **brand-new** account may have **no buckets**.

</details>

### Question 14: How can you tell CloudShell already has working credentials?

<details>
<summary>Answer</summary>

- [x] Run `aws s3 ls`.
- [x] **No error message** means you have credentials for that operation, even if the bucket list is empty.

</details>

### Question 15: What four setup checks does the instructor want before you leave this lesson?

<details>
<summary>Answer</summary>

- [x] **Download the code**.
- [x] Install **Visual Studio Code**.
- [x] Install the **AWS CLI** if you want to run it on your computer.
- [x] Confirm you can **access CloudShell**.

</details>

### Question 16: When will you configure local AWS CLI credentials?

<details>
<summary>Answer</summary>

- [x] **Later**, after you create your **individual IAM user**.
- [x] Not in this lesson.

</details>

### Question 17: If you use Windows locally and CloudShell in the browser, what stays the same and what changes?

<details>
<summary>Answer</summary>

- [x] **`aws` commands stay the same**.
- [x] **File-system** commands and paths follow the OS (**Linux** in CloudShell, **Windows** locally).

</details>

</details>

## Summary

Before HOL labs, get the **course code** from the **last lesson** (GitHub download or Git clone), install **Visual Studio Code**, and install the **AWS CLI** for your OS. Open **CloudShell** from the console—it is a Linux CLI **already authenticated** as the signed-in user. New accounts with a **new credit card** may have CloudShell blocked; ask **Support** or use the local CLI later. `aws help` and `aws s3 ls` confirm the CLI; **no error** on `aws s3 ls` means credentials work even with zero buckets. Local CLI auth waits until the **IAM user** lesson. AWS commands match everywhere; only OS navigation differs.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Download Visual Studio Code](https://code.visualstudio.com/download)
- [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [What is AWS CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)
- [Getting started with AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html)
- [aws s3 ls](https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html)

</details>
