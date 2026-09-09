[← Course contents](../../01.md)

# 4. Create your own free AWS account

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

These lessons cover **what an AWS account is**, how **root** vs **IAM** access works, and how to **sign up** for your own account. Since **July 2025**, new customers choose a **Free plan** or a **Paid plan**. Both can receive up to **$200** in credits (**$100** at signup plus **$100** you can earn in the console). The Free plan is built so beginners do **not** get a surprise bill: when credits run out or **6 months** pass, AWS **closes** the account instead of charging the card. Later **HOL** lessons in this course use your own account, mostly in **US East (N. Virginia)**.

## Detailed Explanation

<details>
  <summary>Step 1 — Gather what you need to open an account</summary>

### Step 1 — Gather what you need to open an account

- [x] **What you need to open an AWS account**
  - A **credit card** (required even on the Free plan, so AWS can charge you if you later switch to Paid).
  - A **unique email address** that is **not** already tied to another AWS account.
  - You **can** create **multiple** AWS accounts; each needs a **different email**.
  - The **same credit card** can be reused across accounts.
- [x] **Dynamic email aliases (Gmail and some other providers)**
  - Example: if your inbox is `john@gmail.com`, you can use `john+awsaccount1@gmail.com`, `john+awsaccount2@gmail.com`, and so on.
  - Mail still arrives in the same inbox; AWS treats each alias as a **unique** address.
  - Match the alias to a memorable **account name** so you remember which inbox/login belongs to which account.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4baebe19-3815-478f-bcd1-d37df0327449" />

</details>

<details>
  <summary>Step 2 — Understand the root user and use IAM instead</summary>

### Step 2 — Understand the root user and use IAM instead

- [x] **Account root user**
  - Creating the account also creates the **root user**.
  - Root signs in with the **signup email** and a **password**.
  - Root has **full control**; you **cannot** meaningfully limit most of its permissions.
  - Best practice: set a **very strong password**, then **do not use root** unless you specifically need it.
- [x] **IAM instead of daily root use**
  - Use **Identity and Access Management (IAM)** to create **users**, **groups**, **roles**, and **policies**.
  - Typical pattern: create a **user**, put the user in a **group**, attach a **policy** (permissions) to the **group**.
  - Log in afterwards as that IAM user (e.g. your own name), not as root.
  - IAM best practice: **individual users**; **avoid root** except for the few tasks that require it.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/356d3bf0-b58a-4877-ba74-3601578784fd" />

</details>

<details>
  <summary>Step 3 — Authenticate, authorize, and choose an access method</summary>

### Step 3 — Authenticate, authorize, and choose an access method

- [x] **Authentication, authorization, and ways to access AWS**
  - After you have an account, the easiest start is the **AWS Management Console**.
  - An **IAM principal** (such as a user) must **authenticate** (prove who they are), e.g. username and password.
  - **Authorization** comes from **policies**: which **resources** you can use and at what **level**.
  - Three common access methods (all require authentication):
    - **Console**
    - **CLI** (command line interface)
    - **API** via an **SDK** when you write code
  - Example resources a policy might allow: **EC2**, **RDS**, **S3**, load balancers.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5327a6be-c29d-4e34-a3b6-275858d70f5d" />

- [x] **Where identities live**
  - Identities and resources are created **inside an AWS account**.
  - Multi-account setups can **centralize** some management, but each user still **exists in one account**.
  - Accessing resources in **another** account needs extra measures (covered later).

</details>

<details>
  <summary>Step 4 — Compare the Free plan and the Paid plan</summary>

### Step 4 — Compare the Free plan and the Paid plan

- [x] **Free plan vs Paid plan (from July 2025)**
  - Before this change there was one signup model: a **12-month Free Tier** with per-service usage limits.
  - New customers now **choose** **Free plan** or **Paid plan** at signup.
  - Credits are for **new customers only** (you get them **once**, according to AWS).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/18f4fcb5-0c25-4acf-b806-9bad2e5ea29d" />

- [x] **Credits on both plans**
  - **$100** at signup, applied against **consumption-based** usage so AWS draws from credits instead of the card first.
  - You can **earn another $100** by completing **actions in the console** (up to **$200** total).
  - The extra-credit promo may be temporary; it was available when the lesson was recorded.
  - Both plans also get **always-free** monthly usage on some services, plus **short-term trial** offers (Paid has fuller access).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/465329f0-9a1d-496d-b919-7b18d5bf7eb9" />

- [x] **What the Free plan allows**
  - Access to **select** services and features only—not everything.
  - AWS blocks actions that would **burn credits instantly**.
  - **Most** of this course’s labs fit the Free plan; some do **not** (see below).
  - **EC2** is available only for **certain instance types**.
  - **No charges** while you stay on Free; if credits run out, AWS **shuts the account** (or you **upgrade** to Paid).
  - Free plan **expires after 6 months or when credits are used**, whichever comes first.
- [x] **What the Paid plan allows**
  - Access to **all** AWS services; you take the **billing risk**.
  - After credits are gone, usage is billed to the **credit card**.
  - The account **stays active**; it does not auto-close after 6 months.
  - You can **scale** beyond credit limits.

</details>

<details>
  <summary>Step 5 — Plan for expiry, upgrades, and AWS Organizations</summary>

### Step 5 — Plan for expiry, upgrades, and AWS Organizations

- [x] **After Free plan expiry (90-day grace)**
  - When the account closes (6 months or credits gone), you have **90 days** to **upgrade to Paid** and reopen it.
  - Remaining credits can then apply to future bills (until they expire).
- [x] **Upgrading and AWS Organizations (do this before org labs)**
  - You can upgrade **manually**, or a **service/feature** can convert you **automatically**.
  - If conversion happens through **AWS Organizations**, **AWS Partner**, or other **enterprise** programs, **remaining Free Tier credits expire immediately** and are **not** applied to Paid usage.
  - This course uses **AWS Organizations** in several labs. **Manually upgrade to Paid first**, then create the organization, so credits **carry over**.
  - After a **manual** upgrade, credits last **12 months from the date you opened the account**.
  - A Free plan account still **auto-shuts after 6 months** even if credits remain—upgrade if you need those credits for longer.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ca33ecee-18ad-4d20-a23b-04dc96107555" />

</details>

<details>
  <summary>Step 6 — Decide which plan fits your situation</summary>

### Step 6 — Decide which plan fits your situation

- [x] **Which plan to choose**
  - **Free plan:** beginners who want **no surprise bill**; short-term use (one course, a couple of months); you do **not** need every service.
  - **Paid plan:** you already know AWS **pricing** and **cost controls**; you need services **not** on Free (examples: **Route 53 domain registration**, **AWS Organizations**); you need the account **after 6 months**.
  - Eventually **everyone** should move to Paid and learn how AWS charges.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/455b4fc9-3bd0-4a55-9726-b181470a14bc" />

</details>

<details>
  <summary>Step 7 — Control costs and finish the signup details</summary>

### Step 7 — Control costs and finish the signup details

- [x] **Cost controls (your responsibility)**
  - Learn what services cost; **terminate / delete** resources when a lab ends.
  - HOL lessons usually **show** what to shut down; you still must **check** yourself.
  - Set **billing alarms** (e.g. **$5 / $10 / $20**) so you get email when spend or forecast hits a limit (shown later in the course).
- [x] **Account ID, account name, and alias**
  - **Account ID:** long numeric identifier AWS assigns.
  - **Account name:** a **friendly** name (words, easier to remember); must be **unique across AWS**.
  - **Account alias:** also unique; used to build a **friendly login URL** (instead of typing the account ID).
  - Instructor tip: make **email alias**, **account name**, and **account alias** the **same** string.
- [x] **Sign-up extras**
  - A **phone** is required for an **SMS verification** code during signup.
  - After signup, AWS **activates** the account (can take a few minutes) and emails you when it is ready.
  - First console landing region may follow your location; this course uses **United States (N. Virginia)** / **us-east-1** for most labs.
  - Completing registration can leave you **already signed in as root**. After you **sign out**, the default login form asks for **account ID or alias** plus an **IAM username**—you do **not** have an IAM user yet. Use **Sign in using root user email**, then the signup email and root password.

</details>

<details>
  <summary>Lab</summary>

## Lab

This is a **console signup** walkthrough. Pause until you have a unique email, credit card, account name, and phone. Do **not** create an **AWS Organization** until you have **manually upgraded** to Paid if you want to keep credits.

### **Overview**

- [ ] Create your own **AWS Free plan** account so you can follow later **HOL** lessons.
- [ ] You will:
  - [ ] Collect signup details (email, card, name, phone).
  - [ ] Sign up from the **AWS Free Tier** page.
  - [ ] Choose **Free plan**, enter personal and billing details, and verify by SMS.
  - [ ] Open the **Management Console**, switch to **N. Virginia**, and practice **root user** sign-in.
- [ ] Success: you can sign in as **root** and see the console in **us-east-1**.

### **Task 1: Gather signup details**

- [ ] Confirm you have a **credit card** (needed even for Free plan).
- [ ] Choose a **unique email** not used on any other AWS account.
  - [ ] If you use Gmail, consider an alias such as `you+aws-saa@gmail.com`.
- [ ] Pick a **unique AWS account name** (friendly name, not the numeric ID).
- [ ] Optionally pick a matching **account alias** for a friendly login URL (you may set this later).
- [ ] Have a **phone** ready for SMS verification.

### **Task 2: Choose Free plan vs Paid plan**

- [ ] Choose **Free plan** if you are new to AWS and want **no surprise bills** for a short course.
- [ ] Choose **Paid plan** (or plan to **upgrade later**) if you will need:
  - [ ] **AWS Organizations**
  - [ ] **Route 53** domain registration
  - [ ] Access to **all** services / instance types
  - [ ] The account to stay open **after 6 months**
- [ ] If you start on Free and later need Organizations: **manually upgrade to Paid first**, then create the organization, so remaining credits are **not** wiped.

### **Task 3: Start signup on the Free Tier page**

- [ ] Open [AWS Free Tier](https://aws.amazon.com/free/).
- [ ] Click **Create a free tier account** (or **Create an AWS Account**).
- [ ] Enter the **root user email address** (your unique email).
- [ ] Enter the **AWS account name**.
- [ ] Click **Verify email address**.
- [ ] Open the inbox, copy the **verification code**, paste it, and click **Verify**.
- [ ] Set a **strong root user password**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2cb31c86-96f4-425e-b706-7aaa22b8294b" />

### **Task 4: Select the Free plan and contact details**

- [ ] On the plan screen, review Free vs Paid (6 months, up to **$200** credits, no charges on Free unless you switch).
- [ ] Click **Choose free plan** (unless you already decided on Paid).
- [ ] Select **Personal** (your own learning; not a business account).
- [ ] Fill in **name**, **phone**, **country/region**, **address**.
- [ ] Agree to the **terms** and click **Continue**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9129a268-92cb-4af9-aae8-01070e80e76e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ad6b462c-bb78-410c-9911-fa509c2fe2b0" />

### **Task 5: Billing and identity verification**

- [ ] Confirm **country** is correct.
- [ ] Enter **credit card** number, **expiration**, **security code**, and **cardholder name**.
- [ ] Click **Verify and continue**.
- [ ] Enter your **phone number** and click **Send SMS**.
- [ ] Enter the **SMS code** and click **Continue**.
- [ ] Wait for AWS to **activate** the account (a few minutes) and for the **confirmation email**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b84516b7-7a16-4623-815a-4892a3c6fa2b" />

### **Task 6: Open the console and set the region**

- [ ] When activation completes, open the **AWS Management Console**.
- [ ] If you landed in another region (e.g. Europe), switch the region to **US East (N. Virginia) `us-east-1`**.
- [ ] Most activities in this course use **N. Virginia**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/89288dfc-4468-4d4b-8a4b-753972d6bf9d" />

### **Task 7: Practice signing in as the root user**

- [ ] **Sign out** of the console.
- [ ] Go to sign in again.
- [ ] The form asks for **Account ID or alias** and an **IAM user** name—you have **not** created an IAM user yet.
- [ ] Click **Sign in using root user email**.
- [ ] Enter the **signup email** and **root password**, then **Sign in**.
- [ ] You are back in as **root**. Later lessons create an **IAM user** for daily use and add **billing alarms**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e5ce8cf5-7866-44c4-9966-e10ac0d6a3d7" />

Successfully created a Free plan account and signed in as the **root user**. Do not use root for daily work once IAM is set up.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What two things do you need before you can open an AWS account?

<details>
<summary>Answer</summary>

- [x] A **credit card**.
- [x] A **unique email address** that is not already associated with another AWS account.

</details>

### Question 2: Can multiple AWS accounts share a credit card? Can they share an email?

<details>
<summary>Answer</summary>

- [x] **Yes**, the **same credit card** can be used on multiple accounts.
- [x] **No**, each account needs a **different email address**.

</details>

### Question 3: How can you create several unique emails that still land in one Gmail inbox?

<details>
<summary>Answer</summary>

- [x] Use a **dynamic alias**, e.g. `john+awsaccount1@gmail.com` and `john+awsaccount2@gmail.com`.
- [x] Gmail (and some other providers) deliver those to `john@gmail.com`.

</details>

### Question 4: How does the account root user sign in, and what can it do?

<details>
<summary>Answer</summary>

- [x] Root signs in with the **email used at signup** and a **password**.
- [x] It has **full control** of the account.
- [x] You **cannot** meaningfully limit most root permissions.

</details>

### Question 5: What is the best practice for the root user?

<details>
<summary>Answer</summary>

- [x] Set a **very strong password**.
- [x] **Do not use** root for daily work unless you **specifically need** it.

</details>

### Question 6: What should you use instead of root for day-to-day access?

<details>
<summary>Answer</summary>

- [x] **IAM** (Identity and Access Management).
- [x] Create a **user**, put the user in a **group**, and attach a **policy** to the **group**.
- [x] Then log in as that **IAM user**.

</details>

### Question 7: What four IAM object types does the instructor list?

<details>
<summary>Answer</summary>

- [x] **Users**
- [x] **Groups**
- [x] **Roles**
- [x] **Policies**

</details>

### Question 8: What three ways can you access and manage AWS, and what must you always do first?

<details>
<summary>Answer</summary>

- [x] **Management Console**
- [x] **CLI**
- [x] **API** through an **SDK**
- [x] You must always **authenticate** (prove who you are).

</details>

### Question 9: What do IAM policies define?

<details>
<summary>Answer</summary>

- [x] Which **resources** you may access.
- [x] What **level of access** you have (authorization after authentication).

</details>

### Question 10: What changed in July 2025 for new AWS accounts?

<details>
<summary>Answer</summary>

- [x] New customers now choose a **Free plan** or a **Paid plan** at signup.
- [x] Previously there was essentially **one** account type with a simpler **12-month Free Tier** model.

</details>

### Question 11: How much Free Tier credit can a new customer get?

<details>
<summary>Answer</summary>

- [x] **$100** at signup.
- [x] Up to **another $100** by completing **actions in the console**.
- [x] Up to **$200** total, on **both** Free and Paid plans.
- [x] Credits are for **new customers** and you get them **once**.

</details>

### Question 12: What happens on the Free plan if you use up all credits?

<details>
<summary>Answer</summary>

- [x] AWS **closes / shuts** the account.
- [x] You are **not charged**.
- [x] You can **upgrade to Paid** instead.

</details>

### Question 13: What happens on the Paid plan after credits are gone?

<details>
<summary>Answer</summary>

- [x] Further usage is **charged to your credit card**.
- [x] The account **stays active**.

</details>

### Question 14: When does the Free plan expire, and what is the grace period?

<details>
<summary>Answer</summary>

- [x] After **6 months** or when **credits are used up**, whichever comes first.
- [x] You then have **90 days** to **upgrade to Paid** and reopen the account.

</details>

### Question 15: Why should you manually upgrade to Paid before using AWS Organizations?

<details>
<summary>Answer</summary>

- [x] Joining **Organizations** (or partner/enterprise programs) can **convert** Free to Paid **automatically**.
- [x] Remaining Free Tier credits then **expire immediately** and are **not** applied to Paid usage.
- [x] A **manual** upgrade first lets credits **carry over** to future bills.

</details>

### Question 16: How long do Free Tier credits last after a manual upgrade to Paid?

<details>
<summary>Answer</summary>

- [x] They expire **12 months from the date you opened the account**.
- [x] A Free plan account still **auto-closes at 6 months** even if credits remain, so upgrade if you need them longer.

</details>

### Question 17: When should you choose the Free plan vs the Paid plan?

<details>
<summary>Answer</summary>

- [x] **Free:** beginners who want **no surprise bill**; short-term / single-course use; you do not need every service.
- [x] **Paid:** you are comfortable with **pricing** and **cost controls**; you need services not on Free; you need the account **after 6 months**.
- [x] Eventually **everyone** should be on Paid and monitor spend.

</details>

### Question 18: Which course examples typically need the Paid plan?

<details>
<summary>Answer</summary>

- [x] Registering **Route 53** domain names.
- [x] Using **AWS Organizations**.
- [x] Labs that need **all** services or **any** EC2 instance type.

</details>

### Question 19: Why does AWS still require a credit card for a Free plan account?

<details>
<summary>Answer</summary>

- [x] So they can charge you if you **switch to a Paid plan**.

</details>

### Question 20: After you sign out, how do you sign back in as root?

<details>
<summary>Answer</summary>

- [x] The default form asks for **account ID or alias** and an **IAM username**.
- [x] Click **Sign in using root user email**.
- [x] Enter the **signup email** and **root password**.

</details>

</details>

## Summary

Open an AWS account with a **credit card** and a **unique email** (Gmail **plus-aliases** work). Signup creates an all-powerful **root** user—set a strong password and use **IAM** users/groups/policies for daily work. Since **July 2025**, pick **Free** (select services, **no charges**, closes after **6 months** or when credits run out, **90-day** upgrade window) or **Paid** (all services, billed after credits). Both can get up to **$200** in credits. **Manually upgrade before Organizations** so credits are not wiped. This course’s console work is mostly in **us-east-1**; after first logout, use **Sign in using root user email** until you create an IAM user. Set **billing alarms** and terminate lab resources yourself.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/)
- [Explore AWS services with AWS Free Tier (Billing user guide)](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html)
- [Choosing an AWS Free Tier plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html)
- [AWS Free Tier update: up to $200 in credits (AWS News Blog, July 2025)](https://aws.amazon.com/blogs/aws/aws-free-tier-update-new-customers-can-get-started-and-explore-aws-with-up-to-200-in-credits/)
- [AWS Free Tier Terms](https://aws.amazon.com/free/terms/)
- [IAM Identity Center and IAM best practices (root user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
