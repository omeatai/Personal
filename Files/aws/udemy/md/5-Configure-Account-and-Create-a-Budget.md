[← Course contents](../../01.md)

# 5. Configure Account and Create a Budget

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

After the account exists, configure it **before** you start HOL labs. Still signed in as **root**, you set an **account alias** so IAM users can log in with a memorable URL, enable **IAM access to billing**, turn on **Free Tier** and **CloudWatch billing** email alerts, request **PDF invoices**, and create a **$5 monthly AWS Budget**. That budget is the backup if you forget to terminate a resource. **Cost Explorer** shows an itemized spend breakdown, but a brand-new account needs about **24 hours** before data appears.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/221fe32c-6241-4300-bd72-fcc3697df7ab" />

## Detailed Explanation

<details>
  <summary>Step 1 — Know why account configuration comes before the labs</summary>

### Step 1 — Know why account configuration comes before the labs

- [x] **Why this lesson comes next**
  - Make a few **account configuration** changes, then set a **budget** that emails you when spend is **forecast** to hit, or has **exceeded**, a monthly dollar threshold.
  - You are still using the **root user**; an **IAM user** is created in a later lesson.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3d59862b-ceab-423e-b495-dd6f1c0e630b" />

</details>

<details>
  <summary>Step 2 — Open IAM and create an account alias</summary>

### Step 2 — Open IAM and create an account alias

- [x] **IAM is a global service**
  - Search for **IAM** in the console (you can **favorite** it).
  - The console shows IAM is **global**: you do **not** pick a region.
  - Create users and related IAM resources **once**; they apply across regions.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3303fe59-1774-4f10-a6cd-de22ccd43c5a" />

- [x] **Account ID vs account alias vs sign-in URL**
  - The IAM dashboard shows **AWS account**, the numeric **account ID**, and **account alias**.
  - The **IAM user sign-in URL** includes the **account ID** by default—hard to remember.
  - Create an **account alias** (must be **unique across all of AWS**). If someone else already took it, pick another.
  - Instructor example: account name **DCT Lab training**, then the **same string** as the alias (yours must be unique; do not reuse his).
  - Change the **account name** on the **Account** page if needed.
  - After the alias exists, open/copy the **sign-in URL** and **save it**—you will use it later to log in as an IAM user.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c8090cfb-2400-4d49-a81d-e495ee62a74e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/45896974-2492-4281-b189-2989a098f39c" />

</details>

<details>
  <summary>Step 3 — Enable IAM access to billing on the Account page</summary>

### Step 3 — Enable IAM access to billing on the Account page

- [x] **Account page: regions and IAM billing access**
  - Top right → **Account**.
  - Not **all regions** are enabled by default; enable extra regions only if you need them.
  - Find **IAM user and role access to billing information**.
  - Once you stop using root, billing pages often tell you to **sign in as root** unless this is on.
  - **Enable** it so you can grant billing permissions through **IAM** and view bills as an admin user.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ac3dad49-725b-42b3-a189-1c766e6d5be8" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/826967b5-b83c-46b6-aa55-92f2bb147c70" />

</details>

<details>
  <summary>Step 4 — Turn on billing alerts and PDF invoices</summary>

### Step 4 — Turn on billing alerts and PDF invoices

- [x] **Billing preferences (alerts and invoices)**
  - Left menu → **Billing preferences**.
  - Under **alert preferences**, enable:
    - **AWS Free Tier alerts**
    - **CloudWatch billing alerts**
  - Enter the **email** that should receive those alerts (email if you use up Free Tier credits).
  - Enable **receive invoices as PDF** attached to email so you do not have to open the console to see charges.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d6e6783e-5f14-407d-8083-21ea5e7fa420" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b75bf1ab-648e-4b28-8e38-c050be66b18a" />

</details>

<details>
  <summary>Step 5 — Create a $5 monthly cost budget</summary>

### Step 5 — Create a $5 monthly cost budget

- [x] **AWS Budgets ($5 monthly cost budget)**
  - Left menu → **Budgets and planning** → **Budgets** (AWS Budgets service).
  - **Create a budget** using a **template**.
  - Options include a **zero-spend** budget if you are extremely cost-sensitive.
  - Instructor choice: **monthly cost budget** of **$5**.
  - You get email when you are **forecast** to reach **$5** in the month, or when you **actually** reach it.
  - The template notifies **twice** on actual spend: at **85%** and at **100%**.
  - Enter your **email** and create the budget; AWS fills in the rest.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1f1357bb-fb7e-45b2-a28c-b306ea41b423" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e35d43e9-b967-4bbc-843d-c6b6a040c666" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/089b8123-8826-46e7-a720-77d085733bb0" />

</details>

<details>
  <summary>Step 6 — Watch the small charges and inspect spend</summary>

### Step 6 — Watch the small charges and inspect spend

- [x] **What might still cost a little (and what blows past $5)**
  - Some items have small ongoing fees, e.g. a **Route 53 hosted zone** (usually **under $1/month**).
  - Occasional couple-of-dollar charges can appear; following the course **shutdown/terminate** steps should keep you **under $5**.
  - **Registering a domain** is the usual exception: cheapest domains are about **$5–$6**, which **exceeds** this budget.
  - If you forget a resource, the budget email is the **backup**; then inspect spend in **Cost Explorer**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cd6b213c-4ffe-419d-b155-afa705e32256" />

- [x] **Cost Explorer**
  - Billing left menu → **Cost Explorer**.
  - Shows an **itemized breakdown** of spend.
  - A **new** account may say to wait **24 hours** before data appears.

</details>

<details>
  <summary>Lab</summary>

## Lab

Stay signed in as **root**. Set alias, billing access, alert preferences, a **$5** budget, and know where Cost Explorer lives. Pick your **own** unique alias; do not copy the instructor’s.

### **Overview**

- [ ] Configure the account so IAM logins and billing alerts work, then create a **$5 monthly budget**.
- [ ] You will:
  - [ ] Create an **account alias** and save the **IAM sign-in URL**.
  - [ ] Enable **IAM user and role access to billing information**.
  - [ ] Turn on **Free Tier** and **CloudWatch billing** alerts, plus **PDF invoices**.
  - [ ] Create a **monthly cost budget** of **$5**.
  - [ ] Open **Cost Explorer** (data may take 24 hours).
- [ ] Success: the IAM sign-in URL uses your alias, billing access is on, and the $5 budget exists.

### **Task 1: Open IAM and confirm it is global**

- [ ] Sign in as the **root user**.
- [ ] In the search bar, type **IAM** and open **Identity and Access Management**.
- [ ] Optionally **favorite** IAM for later.
- [ ] Confirm the console shows IAM as a **global** service (no region to choose).

### **Task 2: Create an account alias and save the sign-in URL**

- [ ] On the IAM dashboard, find **AWS account**.
- [ ] Note the numeric **Account ID**.
- [ ] Note the default **IAM user sign-in URL** (it contains the account ID).
- [ ] Create an **account alias**:
  - [ ] Use a string that is **unique across AWS**.
  - [ ] Prefer matching your **account name** (instructor used **DCT Lab training**—choose your own).
- [ ] If the alias is taken, try another until it succeeds.
- [ ] Click the new **sign-in URL**, copy it, and **store it** somewhere you can find when you create an IAM user.

### **Task 3: Review the Account page and enable IAM billing access**

- [ ] Click the account menu in the **top right**.
- [ ] Choose **Account**.
- [ ] Confirm or change the **account name** if needed.
- [ ] Scroll the **AWS Regions** list; note that **not all regions** are enabled by default.
- [ ] Find **IAM user and role access to billing information**.
- [ ] **Enable** this setting so future IAM admin users can view billing without signing in as root.

### **Task 4: Set billing preferences and email alerts**

- [ ] In the left menu, open **Billing preferences**.
- [ ] Under **alert preferences**, enable:
  - [ ] **Receive AWS Free Tier alerts**
  - [ ] **Receive CloudWatch billing alerts**
- [ ] Enter your **email address** for those alerts.
- [ ] Enable **Receive PDF invoices by email**.
- [ ] Save the preferences.

### **Task 5: Create a $5 monthly budget**

- [ ] Left menu → **Budgets and planning** → **Budgets**.
- [ ] Click **Create a budget**.
- [ ] Under **budget setup**, use a **template**.
- [ ] Choose **Monthly cost budget** (or **Zero spend budget** if you want alerts at any spend).
- [ ] Set the amount to **$5**.
- [ ] Confirm notifications:
  - [ ] Email when **forecast** spend reaches the budget.
  - [ ] Email when **actual** spend reaches **85%**.
  - [ ] Email when **actual** spend reaches **100%**.
- [ ] Enter your **email address**.
- [ ] Click **Create budget**.

### **Task 6: Open Cost Explorer**

- [ ] Left menu → **Cost Explorer**.
- [ ] If the account is new, expect a message to wait about **24 hours**.
- [ ] After data appears, use Cost Explorer for an **itemized breakdown** if a budget alert fires.

Budget created. Keep terminating lab resources; expect to exceed **$5** mainly when you **register a domain**.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which user are you signed in as during this lesson?

<details>
<summary>Answer</summary>

- [x] The **root user**.
- [x] An **IAM user** is created in a **later** lesson.

</details>

### Question 2: Is IAM regional, and why does that matter?

<details>
<summary>Answer</summary>

- [x] IAM is a **global** service.
- [x] You do **not** select a region.
- [x] You create users and related resources **once**, not per region.

</details>

### Question 3: Why create an account alias?

<details>
<summary>Answer</summary>

- [x] The default IAM **sign-in URL** includes the numeric **account ID**, which is hard to remember.
- [x] An alias gives a **friendly** login URL for **IAM users**.

</details>

### Question 4: Must an account alias be unique?

<details>
<summary>Answer</summary>

- [x] **Yes.** It must be unique **across AWS**.
- [x] If the name is taken, the create step **fails** and you pick another.

</details>

### Question 5: Where do you change the account name?

<details>
<summary>Answer</summary>

- [x] Top right → **Account**.
- [x] You can edit the **account name** on that page.

</details>

### Question 6: Why enable IAM user and role access to billing information?

<details>
<summary>Answer</summary>

- [x] After you stop using root, billing often requires a **root** login unless this is on.
- [x] Enabling it lets you grant billing access through **IAM** and view bills as an admin user.

</details>

### Question 7: Are all AWS regions enabled by default?

<details>
<summary>Answer</summary>

- [x] **No.** Some regions must be **enabled** before you can use them.

</details>

### Question 8: Which two alert types should you enable in billing preferences?

<details>
<summary>Answer</summary>

- [x] **AWS Free Tier alerts**
- [x] **CloudWatch billing alerts**
- [x] Enter an **email address** so you are notified if you use up Free Tier credits.

</details>

### Question 9: Why enable PDF invoices by email?

<details>
<summary>Answer</summary>

- [x] Invoices are **attached to email**.
- [x] You do not have to open the AWS console just to see what you were charged.

</details>

### Question 10: How do you open AWS Budgets from the account/billing area?

<details>
<summary>Answer</summary>

- [x] Left menu → **Budgets and planning** → **Budgets**.

</details>

### Question 11: What budget does the instructor create, and what is the zero-spend alternative?

<details>
<summary>Answer</summary>

- [x] A **template** **monthly cost budget** of **$5**.
- [x] A **zero-spend** budget is an option if you want alerts at any spend.

</details>

### Question 12: When does the $5 budget send email?

<details>
<summary>Answer</summary>

- [x] When you are **forecast** to reach **$5** in the month.
- [x] When **actual** spend reaches **85%**.
- [x] When **actual** spend reaches **100%**.

</details>

### Question 13: Should you stay under $5 if you follow the course shutdown steps?

<details>
<summary>Answer</summary>

- [x] **Yes**, in normal HOL labs, if you **terminate** resources as instructed.
- [x] Small fees can still appear (e.g. a **Route 53 hosted zone**, usually **under $1/month**).

</details>

### Question 14: What course activity is expected to exceed the $5 budget?

<details>
<summary>Answer</summary>

- [x] **Registering a domain**.
- [x] The cheapest domains are about **$5–$6**.

</details>

### Question 15: What should you do if a budget alert fires because you forgot a resource?

<details>
<summary>Answer</summary>

- [x] Treat the email as a **backup warning**.
- [x] Open **Cost Explorer** for an **itemized** spend breakdown.

</details>

### Question 16: Why might Cost Explorer show no data on a new account?

<details>
<summary>Answer</summary>

- [x] New accounts often need about **24 hours** before Cost Explorer data appears.

</details>

### Question 17: What should you save after creating the account alias?

<details>
<summary>Answer</summary>

- [x] The **IAM user sign-in URL** that uses the alias.
- [x] You will use it later to log in as an **IAM user**.

</details>

</details>

## Summary

As **root**, create a unique **account alias** and save the **IAM sign-in URL**, enable **IAM access to billing**, turn on **Free Tier** and **CloudWatch billing** emails plus **PDF invoices**, and create a **$5 monthly budget** (alerts at forecast, **85%**, and **100%** actual). Stay under $5 by terminating labs; **domain registration** is the usual overage. Use **Cost Explorer** after ~**24 hours** if you need a spend breakdown.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Using an alias for your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)
- [Activate access to the Billing and Cost Management console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html)
- [AWS Billing preferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-account-payment.html)
- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Using Amazon CloudWatch billing alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)
