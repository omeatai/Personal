# 15. Access Evaluation Tools

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This lesson covers **four IAM console tools** for evaluating **who can do what** in an account: **IAM Access Analyzer** (external / overly open access **findings**), the **credential report** (how users are set up: passwords, rotation, **MFA**), the **IAM Policy Simulator** (Allow vs Deny for selected **API actions**), and **Generate policy** on a **role** (build a tighter policy from **CloudTrail** events). Access Analyzer is a **one-click enable**; findings are warnings to investigate, not always a problem. Policy generation from a trail can take **several minutes**.

## Detailed Explanation

- [x] **IAM Access Analyzer — enable it**
  - Open the **IAM** Management Console and go to **Access Analyzer**.
  - If it is the **first time**, click the button to **enable** it for the account (**single click**).
  - It then runs an **access evaluation** quickly.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/77046bee-4c91-4b4d-8865-ee96e75d0d72" />

- [x] **Access Analyzer findings**
  - Instructor example: findings on **S3 buckets** and **IAM roles**.
  - One bucket policy allows access level **read**.
  - Another allows **write**, **read**, and **list**.
  - Click the **finding ID** for details.
- [x] **Public access finding (S3)**
  - The finding can warn that the resource allows **public access**.
  - That **might** be a problem — **not always** (some buckets are meant to be public).
  - Use the finding to **investigate** and **resolve** if it is too open.
  - Example access: **S3 `GetObject`** is allowed.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/f7f8610b-8358-46dd-8896-61167263a072" />

- [x] **IAM role finding (Cognito)**
  - Example finding on an IAM **role** related to **Amazon Cognito**.
  - Access level **write**.
  - API action: **`AssumeRoleWithWebIdentity`**.
  - Again: something you **might** want to look into.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/fcf21b2f-57c8-4b32-b791-ef0bfa70c7a6" />

- [x] **What Access Analyzer is for**
  - Analyzes access and lists **findings**.
  - Warns about access that may be **too open** (more than you intended).
- [x] **Archive rules, analyzers, and settings**
  - **Archive rules** control how you **archive** findings.
  - You can view **analyzers** and **create** new ones.
  - **Settings** show the **Access Analyzer Administrator**.
  - You can optionally add a **delegated administrator**.
- [x] **Credential report**
  - About **credentials**, not resource policies.
  - **Download** the report (spreadsheet-style rows/columns).
  - Instructor account: **three IAM users** plus the **root** account.
  - Columns include:
    - When the user was **created**
    - Whether there is a **password** for **console** access
    - When the password was **last used** and **last changed**
    - Whether the password will be **rotated**
    - Whether **MFA** is enabled
  - Use it to see how users are set up from a **security** perspective.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/fa8ab108-3ed0-4f3b-a51d-17a6514b2995" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/1779e548-89b1-43d0-bd85-1ad182b4371b" />

- [x] **IAM Policy Simulator (users)**
  - Lists **users** in the account.
  - Pick a user, pick a **service**, select **all** or **specific** actions, **run simulation**.
  - **Jack:** has **AdministratorAccess** → selected **EC2** actions (all) returned **Allow**.
  - **Clear** results, then pick another user.
  - **Chris:** has a policy named **bucket access**.
  - For **S3**, the instructor checked **specific** actions: **CreateBucket**, **DeleteObject**, **DeleteBucket**, **GetObject**, **ListAllMyBuckets**.
  - Result: **most denied**; only **ListAllMyBuckets** was **allowed**.
  - Useful to see what permissions policies actually **grant**.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/6e75c588-9b14-4b50-871e-a965fd20f237" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/ccd86907-0aac-4897-9995-6f87eb3e3539" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/1900cc06-f58e-4bf7-b9cf-f0f088c107c4" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/af26466d-0f74-4982-ac36-cc3857ba5bc6" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/9ecd8a0d-57ae-4412-811c-3d8914d10907" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/9a450995-5b48-4cdc-8162-142f671a35ce" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/839f0d77-66bd-472a-b3e6-8697bc778828" />

- [x] **Generate policy on a role (CloudTrail)**
  - **IAM** → **Roles** → open a role (instructor: **Elastic Beanstalk EC2** role with **multiple** policies).
  - At the **bottom**: **Generate policy**.
  - Builds a policy from **CloudTrail** events for **API actions** that role recently used — you need a **trail**, and the role must have been **used**.
  - Click **Generate policy**, choose a **timeframe** (example: last **60 days**), choose the **trail**, specify **regions** (example: **US East**), optionally use an **existing service role**, then generate.
  - Generation takes **several minutes**.
  - When complete: **view** the generated policy → **review the permissions** AWS thinks the role needs.
  - Instructor example: specific **Systems Manager** and **EC2** actions.
  - You can **add** more permissions, edit **JSON**, or add policy items from the **right-hand** side.
  - Then **generate** and **apply** the policy to the role.
  - Purpose: **tighten** the permissions you assign to **roles**.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/4b044118-4344-433d-aa44-75363158192b" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/55d03a34-d0cf-43bd-8a6f-937c477977b8" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/5f6d6b01-c847-4245-b27b-a94c5d6dc019" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/eb587be8-bed2-4dba-90a5-9c3d51444175" />

<details>
  <summary>Lab</summary>

## Lab

Walk the four tools in the **IAM** console. Your findings, users, and roles will differ from the instructor’s (**Jack**, **Chris**, Elastic Beanstalk EC2 role). Enable Access Analyzer if it is not on yet. Policy generation needs a **CloudTrail** trail and recent role activity; skip that generate step if you have no trail yet, but still locate the button.

### **Overview**

- [ ] Enable **Access Analyzer**, download a **credential report**, simulate two users, and find **Generate policy** on a role.
- [ ] You will:
  - [ ] Enable Access Analyzer (one click if first time) and open a **finding**.
  - [ ] Note archive rules, analyzers, and optional **delegated administrator**.
  - [ ] Download the **credential report** and scan password / MFA columns.
  - [ ] Simulate **Jack** (or an admin user) on **EC2** (all actions).
  - [ ] Simulate a limited user on **specific S3** actions.
  - [ ] On a role, open **Generate policy** and (if you have a trail) start a CloudTrail-based generation.
- [ ] Success: you can name the four tools and what each answers (external access, credential hygiene, Allow/Deny, least-privilege from CloudTrail).

### **Task 1: Enable IAM Access Analyzer**

- [ ] Sign in to the **AWS Management Console**.
- [ ] Open **IAM**.
- [ ] Go to **Access Analyzer**.
- [ ] If it is the **first visit**, click the button to **enable** Access Analyzer for the account (**one click**).
- [ ] Wait for the first **access evaluation**.

### **Task 2: Review Access Analyzer findings**

- [ ] Look for findings on **S3 buckets** and **IAM roles** (instructor examples).
- [ ] Note access levels such as **read**, or **write / read / list**.
- [ ] Click a **finding ID**.
- [ ] If it warns that the resource allows **public access**:
  - [ ] Read the **access level** and API action (instructor: **S3 `GetObject`**).
  - [ ] Decide whether public access is **intentional**; if not, use the finding to **fix** it.
- [ ] Open an **IAM role** finding if present (instructor: **Cognito**, access level **write**, **`AssumeRoleWithWebIdentity`**).
- [ ] Treat findings as **investigate**, not automatic “this is always wrong.”

### **Task 3: Archive rules, analyzers, and settings**

- [ ] Open **archive rules** and see how findings can be **archived**.
- [ ] Open **analyzers** (you can **create** additional analyzers).
- [ ] Open **settings**.
- [ ] Note the **Access Analyzer Administrator**.
- [ ] Optionally add a **delegated administrator** (skip if you are not using Organizations / do not need one).

### **Task 4: Download the credential report**

- [ ] In **IAM**, open the **credential report**.
- [ ] **Download** the report.
- [ ] Expand columns and confirm you can see:
  - [ ] IAM **users** plus **root**
  - [ ] User **created** date
  - [ ] Whether a **console password** exists
  - [ ] Password **last used** and **last changed**
  - [ ] Password **rotation**
  - [ ] Whether **MFA** is enabled
- [ ] Use this for a **security** snapshot of how users are set up.

### **Task 5: Policy Simulator — admin user (all EC2 actions)**

- [ ] Open the **IAM Policy Simulator**.
- [ ] Select a user with **AdministratorAccess** (instructor: **Jack**).
- [ ] Choose service **EC2**.
- [ ] **Select all** actions.
- [ ] **Run simulation**.
- [ ] Confirm results are **Allow**.
- [ ] **Clear** the results.

### **Task 6: Policy Simulator — limited S3 user (specific actions)**

- [ ] Select a user with a narrow S3 policy (instructor: **Chris**, policy **bucket access**).
- [ ] Choose service **S3**.
- [ ] Select **specific** actions, not all:
  - [ ] **CreateBucket**
  - [ ] **DeleteObject**
  - [ ] **DeleteBucket**
  - [ ] **GetObject**
  - [ ] **ListAllMyBuckets**
- [ ] **Run simulation**.
- [ ] Instructor result: **most denied**; only **ListAllMyBuckets** **allowed**.
- [ ] Other S3 actions you did **not** select are simply **not in this run**.

### **Task 7: Generate a role policy from CloudTrail**

- [ ] In **IAM**, open **Roles**.
- [ ] Open a role that has been **used** (instructor: **Elastic Beanstalk EC2** role with **multiple** policies).
- [ ] Scroll to the **bottom** and find **Generate policy**.
- [ ] If you have **no CloudTrail trail** or the role has no recent activity, stop after locating the button — generation will not have events to use.
- [ ] If you do have a trail:
  - [ ] Click **Generate policy**.
  - [ ] Set the **timeframe** (instructor: last **60 days**).
  - [ ] Choose the **trail**.
  - [ ] Specify **regions** (instructor: **US East**).
  - [ ] Optionally use an **existing service role**.
  - [ ] Start generation and wait (**several minutes**).
- [ ] When a generation has **completed** (instructor showed a finished **EC2**-related role):
  - [ ] **View** the generated policy.
  - [ ] **Review the permissions** AWS thinks the role needs (instructor: **Systems Manager** and **EC2** actions).
  - [ ] Optionally **add** permissions, edit in the **JSON** editor, or add items from the **right-hand** side.
  - [ ] **Generate** the policy and **apply** it to the role only if you intend to **tighten** that role.

Located all four tools. Access Analyzer is enabled (or already was), the credential report downloaded, simulations run, and **Generate policy** identified on a role.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

No terminal commands in this lesson. All four tools are used in the **IAM** console (Access Analyzer, credential report download, Policy Simulator, Generate policy on a role).

```bash
# No commands in this topic; use the IAM Management Console.
```

</details>

<details>
  <summary>Code</summary>

## Code

No application code. Access Analyzer and the Policy Simulator are console results. The credential report is a **download**. **Generate policy** produces **IAM JSON** from CloudTrail (instructor: **Systems Manager** and **EC2** actions). The sketch below is a study reminder of the **Chris** simulation, not a copy of the instructor’s **bucket access** policy.

```text
# Credential report (columns in the lesson)
# users (IAM users + root), created, password (console),
# password last used, last changed, rotation, MFA enabled
```

<details>
<summary>Chris S3 simulation (what the run showed)</summary>

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "WhatTheSimulationAllowed",
      "Effect": "Allow",
      "Action": ["s3:ListAllMyBuckets"],
      "Resource": "*"
    }
  ]
}
```

</details>

- [x] **Jack** + **AdministratorAccess** → selected **EC2** actions **Allow**.
- [x] **Chris** + **bucket access** → of the five S3 actions tested, only **ListAllMyBuckets** **Allow**.
- [x] Generated role policies list the **API actions CloudTrail** recorded for that role.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What four tools does this lesson use to evaluate access?

<details>
<summary>Answer</summary>

- [x] **IAM Access Analyzer**
- [x] The **credential report**
- [x] The **IAM Policy Simulator**
- [x] **Generate policy** on a **role** (from **CloudTrail**)

</details>

### Question 2: How do you turn on Access Analyzer the first time?

<details>
<summary>Answer</summary>

- [x] Open **Access Analyzer** in the **IAM** console.
- [x] Click the button to **enable** it for the account (**one click**).
- [x] It then runs an **access evaluation**.

</details>

### Question 3: What kinds of findings did the instructor see in Access Analyzer?

<details>
<summary>Answer</summary>

- [x] Findings on **S3 buckets** and **IAM roles**.
- [x] Example bucket access levels: **read**, and **write / read / list**.

</details>

### Question 4: What can a finding ID tell you about public S3 access?

<details>
<summary>Answer</summary>

- [x] The resource may be allowing **public access**.
- [x] That **could** be a problem, but **not necessarily**.
- [x] Use the finding to **investigate** and **resolve** it if it is too open.
- [x] Instructor example: **S3 `GetObject`** allowed.

</details>

### Question 5: What did the Cognito-related role finding show?

<details>
<summary>Answer</summary>

- [x] An **IAM role** related to **Amazon Cognito**.
- [x] Access level **write**.
- [x] Action **`AssumeRoleWithWebIdentity`**.

</details>

### Question 6: What else can you configure under Access Analyzer besides findings?

<details>
<summary>Answer</summary>

- [x] **Archive rules** for how you archive findings.
- [x] **Analyzers** (view and **create** new ones).
- [x] **Settings**: **Access Analyzer Administrator**, optional **delegated administrator**.

</details>

### Question 7: What is the credential report for?

<details>
<summary>Answer</summary>

- [x] A **download** about **user credentials**, not resource policies.
- [x] It shows how users are set up from a **security** perspective.

</details>

### Question 8: What columns does the credential report include in this lesson?

<details>
<summary>Answer</summary>

- [x] Users in the account (instructor: **three IAM users** plus **root**)
- [x] When the user was **created**
- [x] Whether there is a **password** for **console** access
- [x] Password **last used** and **last changed**
- [x] Whether the password will be **rotated**
- [x] Whether **MFA** is enabled

</details>

### Question 9: In the Policy Simulator, what happened when Jack ran all EC2 actions?

<details>
<summary>Answer</summary>

- [x] **Jack** has **AdministratorAccess**.
- [x] The simulation returned **Allow**.

</details>

### Question 10: Which S3 actions did the instructor test for Chris, and what was allowed?

<details>
<summary>Answer</summary>

- [x] **CreateBucket**
- [x] **DeleteObject**
- [x] **DeleteBucket**
- [x] **GetObject**
- [x] **ListAllMyBuckets**
- [x] **Most denied**; only **ListAllMyBuckets** was **allowed**.
- [x] Chris’s policy was named **bucket access**.

</details>

### Question 11: Why use the Policy Simulator instead of only reading a policy JSON?

<details>
<summary>Answer</summary>

- [x] It shows what the user is **granted** for the **actions you select**.
- [x] You can test **all** actions on a service or **specific** API actions.

</details>

### Question 12: Where do you generate a policy based on CloudTrail, and what does it need?

<details>
<summary>Answer</summary>

- [x] **IAM** → **Roles** → open a role → **Generate policy** (at the **bottom**).
- [x] The role should have been **used recently**.
- [x] You need a **CloudTrail trail**.
- [x] The policy is built from **API actions** in that trail.

</details>

### Question 13: What options do you set when generating a role policy from CloudTrail?

<details>
<summary>Answer</summary>

- [x] **Timeframe** (instructor: last **60 days**)
- [x] Which **trail** to use
- [x] Which **regions** (instructor: **US East**)
- [x] Optionally an **existing service role**
- [x] Generation takes **several minutes**

</details>

### Question 14: After generation completes, what can you do with the result?

<details>
<summary>Answer</summary>

- [x] **View** the generated policy.
- [x] **Review the permissions** AWS thinks the role needs.
- [x] Instructor example: **Systems Manager** and **EC2** actions.
- [x] **Add** more permissions if you want.
- [x] Customize in the **JSON** editor or add items from the **right-hand** side.
- [x] **Generate** and **apply** the policy to the role.

</details>

### Question 15: Why generate a policy from CloudTrail instead of leaving broad role policies?

<details>
<summary>Answer</summary>

- [x] It helps you **tighten** permissions on **roles**.
- [x] You assign what the role **actually used**, not a wide managed policy by default.

</details>

### Question 16: Are Access Analyzer findings always a misconfiguration?

<details>
<summary>Answer</summary>

- [x] **No.** Public or cross-account access **might** be intentional.
- [x] Findings are **warnings** to **look into**, then fix if the access is **too open**.

</details>

### Question 17: Which tool answers “is MFA on?” vs “can this user call GetObject?” vs “is this bucket public?”

<details>
<summary>Answer</summary>

- [x] **MFA / password / rotation:** **credential report**
- [x] **Can this user call this API action:** **IAM Policy Simulator**
- [x] **Is this resource allowing public or unexpected access:** **Access Analyzer**

</details>

</details>

## Summary

Four **IAM** tools evaluate access. **Access Analyzer** is **enabled** once, then lists **findings** (instructor: **S3** read/write/list, possible **public** **`GetObject`**, a **Cognito** role with **`AssumeRoleWithWebIdentity`**). Findings are **investigate**, not always wrong; configure **archive rules**, **analyzers**, and an optional **delegated administrator**. The **credential report** downloads user security fields: created, console **password**, last used/changed, **rotation**, **MFA** (plus **root**). The **Policy Simulator** tests selected actions: **Jack** + **AdministratorAccess** → **EC2** **Allow**; **Chris** + **bucket access** → only **ListAllMyBuckets** **Allow** among the S3 actions tested. On a **role**, **Generate policy** uses **CloudTrail** (timeframe, trail, regions; **several minutes**) so you can **review**, edit **JSON**, and **apply** a **tighter** policy (instructor: **Systems Manager** and **EC2**).

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [Getting started with AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)
- [Archive findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)
- [Delegated administrator for IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-settings.html)
- [Getting credential reports for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)
- [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
- [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)
- [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
