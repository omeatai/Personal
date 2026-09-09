# 14. IAM policy simulator

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This lesson is another **IAM** tool: the **IAM Policy Simulator**. You pick a **user**, **group**, or **role**, see the **policies**, **permissions**, and **boundaries** attached to it, choose a **service** and **API actions**, and **run a simulation** to see which actions are **allowed** or **denied**. That is how you inspect **aggregate** permissions when several policies apply (inline, group, boundary). **Existing policies** mode tests what is already attached. **New policy** mode opens a **policy sandbox** so you can paste JSON you plan to attach and simulate **before** you apply it.

## Detailed Explanation

<details>
  <summary>Step 1 — Open the simulator and set the context</summary>

### Step 1 — Open the simulator and set the context

- [x] **Open the IAM Policy Simulator**
  - The lesson includes a **link**; otherwise search for **IAM Policy Simulator**.
  - You should land on a page where the **left** side is the **context** (who the simulation applies to).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/29832ad8-4694-47ae-ae11-a7a75f9cab04" />

- [x] **Context: users, groups, or roles**
  - Choose whether the simulation runs against **users**, **groups**, or **roles**.
  - **Users** is the default.
  - **Groups:** the instructor has one **admin** group.
  - **Roles:** a long list of roles in the account.
  - Switch back to **Users** for this walkthrough.
- [x] **Which user to simulate**
  - Instructor users: **Neil** (full **admin** permissions) and **testuser** (from the **IAM policy generator** lesson).
  - **testuser** only has a **few** **S3** API actions and some **EC2 instance** API actions.
  - That limited user is the **better** simulation target — the results are easier to read than a full-admin user.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ae0e6020-091e-4de5-8633-441abb30a913" />

</details>

<details>
  <summary>Step 2 — Review the policies attached to the principal</summary>

### Step 2 — Review the policies attached to the principal

- [x] **What appears after you select the user**
  - The simulator lists **policies**, **permissions**, **boundaries**, and similar items **attached** to that user.
  - Instructor example: **testuser** has an **inline** policy named **test poll**.
  - Other policies might come from **groups**.
  - You can also see or **simulate a permissions boundary**.
- [x] **Why the simulator matters**
  - With one simple inline policy, you are checking what that policy grants in the console.
  - With a **large** or **complex** policy, or **several** policies (group + inline + boundary), the simulator shows the **aggregate** permissions the principal actually has.

</details>

<details>
  <summary>Step 3 — Choose a service and actions, then run the simulation</summary>

### Step 3 — Choose a service and actions, then run the simulation

- [x] **Select a service and actions, then run**
  - Pick a service (for example **EC2**).
  - Choose **specific** actions, or **select all**.
  - Click **Run simulation**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e3ac96d4-0749-4b0c-84c6-67869ac5afb1" />

</details>

<details>
  <summary>Step 4 — Read the EC2 and EC2 Auto Scaling results</summary>

### Step 4 — Read the EC2 and EC2 Auto Scaling results

- [x] **EC2 simulation (allowed)**
  - With **all** EC2 actions selected, the instructor’s **testuser** simulation returned **Allow** for those actions (in the **EC2** context).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8bd7d98e-90cf-49a2-bda3-db76bc3c6fa7" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b171fda8-1531-4a31-aeff-7490b70549bb" />

- [x] **EC2 Auto Scaling simulation (denied)**
  - **Amazon EC2 Auto Scaling** was **not** allowed in the policy.
  - The UI can be **finicky**: **clear** previous results, select the service, **select all**, then run again.
  - Result: Auto Scaling actions are **denied**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/36da6569-3743-4c5d-add6-25b6ee5883f0" />

</details>

<details>
  <summary>Step 5 — Narrow down which S3 actions are actually allowed</summary>

### Step 5 — Narrow down which S3 actions are actually allowed

- [x] **S3 simulation (mostly denied)**
  - Switch to **S3**, **clear** results, **select all** S3 actions, run.
  - Most S3 actions are **denied**.
  - **Allowed** in this example:
    - **GetBucketLocation**
    - **GetObject**
    - **ListAllMyBuckets**
    - **ListBucket**
  - That is exactly what **testuser** can do on S3.

S3 actions allowed for **testuser** (from the simulation):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListAllMyBuckets",
        "s3:ListBucket"
      ],
      "Resource": "*"
    }
  ]
}
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/069f83b7-5663-4b22-846f-bfe6055d94dc" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/71431233-0793-4215-9f3b-41471a940e2b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3ba58b71-d3fe-4729-ae96-d51c3fd35cc9" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9ffd8851-9c97-41bd-8b68-4d32f6cbfa4e" />

</details>

<details>
  <summary>Step 6 — Dry-run a policy you have not attached yet</summary>

### Step 6 — Dry-run a policy you have not attached yet

- [x] **Mode: existing policies vs new policy (sandbox)**
  - Default mode: **existing policies** (what is already attached).
  - **New policy** opens a **policy sandbox**.
  - Paste JSON you **plan** to attach to a **user**, **group**, or **role**.
  - You can make the statement **more restrictive**, **apply** it in the sandbox, **clear** results, **select all**, and **run** again.
  - Instructor example: after removing some actions, only **GetObject** and **ListAllMyBuckets** stayed **allowed**.

Stricter sandbox policy (after removing actions):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListAllMyBuckets"],
      "Resource": "*"
    }
  ]
}
```
  - Use this to simulate permissions **before** you attach the policy in IAM.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/21a0bc4f-98c1-407d-976f-451401c387fa" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ac79568a-1145-4e99-9717-96d0afbd9975" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c35cbdb5-3b27-4b18-95dd-5d3ce29bf67a" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d71f5715-9175-4d8f-9024-b82f01030b06" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2c82a29d-5716-4ff2-83a7-a49fe60ee935" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9af007c5-86a7-4d55-a363-c84e2b9189ee" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e23f9d7e-750e-45c7-9e42-242997be2e97" />

</details>

<details>
  <summary>Lab</summary>

## Lab

Use the **IAM Policy Simulator** against a **limited** user (instructor: **testuser** from the policy generator lesson). Compare **existing** attached policies with a **new-policy sandbox**. If your account names differ, use **your** limited user instead of **testuser**.

### **Overview**

- [ ] Simulate **Allow** vs **Deny** for **EC2**, **EC2 Auto Scaling**, and **S3**, then test a **stricter** policy in the **sandbox**.
- [ ] You will:
  - [ ] Open the **IAM Policy Simulator** and set context to **Users**.
  - [ ] Select **testuser** (or your limited user) and review attached policies / boundaries.
  - [ ] Run **all** **EC2** actions (expect **Allow** in the instructor demo).
  - [ ] Clear, run **EC2 Auto Scaling** (expect **Deny**).
  - [ ] Clear, run **all** **S3** actions and note the few **Allow** results.
  - [ ] Switch to **New policy**, paste / restrict JSON, simulate again.
- [ ] Success: you can explain which S3 actions **testuser** can call, and you have simulated a policy you have **not** attached yet.

### **Task 1: Open the IAM Policy Simulator**

- [ ] Use the **link** on the lesson page, **or** search for **IAM Policy Simulator**.
- [ ] Confirm you see a page with **context** on the **left** (**Users**, **Groups**, **Roles**).

### **Task 2: Choose context and inspect identities**

- [ ] Context defaults to **Users** — leave it there after you look at the other tabs.
- [ ] Open **Groups** and note the instructor’s **admin** group (or **your** groups).
- [ ] Open **Roles** and note that many roles can appear.
- [ ] Switch back to **Users**.
- [ ] Instructor users:
  - [ ] **Neil** — full **admin**.
  - [ ] **testuser** — limited **S3** and **EC2 instance** actions.

### **Task 3: Select testuser and review attached policies**

- [ ] Select **testuser** (or your limited user).
- [ ] Review whatever is attached:
  - [ ] **Inline** policy (instructor: **test poll**).
  - [ ] Policies from **groups**, if any.
  - [ ] **Permissions boundary**, if any — you can **simulate** a boundary here too.
- [ ] You are checking the **aggregate** permissions this principal would have.

### **Task 4: Simulate all EC2 actions**

- [ ] Under services, choose **EC2**.
- [ ] **Select all** actions (or pick specific ones if you want a narrower test).
- [ ] Click **Run simulation**.
- [ ] Confirm the instructor result: **EC2** actions show **Allow**.

### **Task 5: Simulate EC2 Auto Scaling (expect deny)**

- [ ] **Clear** the previous results (the simulator can be **finicky** if you leave old selections).
- [ ] Choose **EC2 Auto Scaling** (Amazon EC2 Auto Scaling).
- [ ] **Select all**, then **Run simulation**.
- [ ] Confirm actions are **denied** — Auto Scaling was **not** in the attached policy.

### **Task 6: Simulate all S3 actions**

- [ ] **Clear** results.
- [ ] Type **S3**, select **S3**.
- [ ] **Select all** S3 actions (or pick specific actions).
- [ ] **Run simulation**.
- [ ] Expect **mostly Deny**. Note the **Allow** rows in the instructor demo:
  - [ ] **GetBucketLocation**
  - [ ] **GetObject**
  - [ ] **ListAllMyBuckets**
  - [ ] **ListBucket**

S3 actions allowed for **testuser** (from the simulation):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListAllMyBuckets",
        "s3:ListBucket"
      ],
      "Resource": "*"
    }
  ]
}
```

### **Task 7: New policy mode (policy sandbox)**

- [ ] At the top, change mode from **existing policies** to **new policy**.
- [ ] The **policy sandbox** appears.
- [ ] Paste the policy JSON from the **previous lesson** (IAM policy generator).
- [ ] **Restrict** the **Action** list further (instructor removed some of the allowed actions).
- [ ] **Apply** the sandbox policy.
- [ ] **Clear** results, **select all** for the service you are testing, **Run simulation**.
- [ ] Instructor result after tightening: **GetObject** and **ListAllMyBuckets** still **allowed**; more actions **denied**.

Stricter sandbox policy (after removing actions):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListAllMyBuckets"],
      "Resource": "*"
    }
  ]
}
```
- [ ] This is how you test a policy you **plan** to attach to a **user**, **group**, or **role** **before** you save it in IAM.

Successfully used the simulator to read **aggregate** permissions on an existing user and to dry-run a **sandbox** policy.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the IAM Policy Simulator for?

<details>
<summary>Answer</summary>

- [x] Another **IAM** tool for testing permissions.
- [x] You simulate **API actions** against a **user**, **group**, or **role**.
- [x] Results show whether each action is **allowed** or **denied**.

</details>

### Question 2: How do you open the IAM Policy Simulator in this lesson?

<details>
<summary>Answer</summary>

- [x] Use the **link** attached to the lesson.
- [x] Or **search** for **IAM Policy Simulator**.

</details>

### Question 3: What context can you simulate against?

<details>
<summary>Answer</summary>

- [x] **Users**
- [x] **Groups**
- [x] **Roles**
- [x] **Users** is the **default**.

</details>

### Question 4: Why did the instructor simulate testuser instead of Neil?

<details>
<summary>Answer</summary>

- [x] **Neil** has **full admin** permissions, so almost everything would show **Allow**.
- [x] **testuser** has only a **few** **S3** actions and some **EC2 instance** actions.
- [x] A **limited** principal makes **Allow** vs **Deny** easier to see.

</details>

### Question 5: What does the simulator list after you select a user?

<details>
<summary>Answer</summary>

- [x] **Policies**, **permissions**, **boundaries**, and similar items **attached** to that user.
- [x] Instructor example: an **inline** policy named **test poll**.
- [x] Other policies can come from **groups**.
- [x] You can also **simulate a permissions boundary**.

</details>

### Question 6: When is the simulator especially useful?

<details>
<summary>Answer</summary>

- [x] When the policy is **large** or **complex**.
- [x] When **several** policies apply (**group** + **inline** on the user, plus a **boundary**).
- [x] You need the **aggregate** permissions, not one statement in isolation.

</details>

### Question 7: After you pick a service, what do you select before running?

<details>
<summary>Answer</summary>

- [x] **Specific** API actions, **or** **select all**.
- [x] Then click **Run simulation**.

</details>

### Question 8: What did the EC2 simulation return for testuser?

<details>
<summary>Answer</summary>

- [x] With **all** EC2 actions selected, the demo showed **Allow**.
- [x] That is the **EC2** service context, matching the EC2 instance actions on the user.

</details>

### Question 9: What did the EC2 Auto Scaling simulation return, and why?

<details>
<summary>Answer</summary>

- [x] **Deny** for the Auto Scaling actions.
- [x] Auto Scaling was **not** allowed in the attached policy.
- [x] **Clear** old results if the UI is **finicky**, then **select all** and run again.

</details>

### Question 10: Which S3 actions were allowed for testuser in the demo?

<details>
<summary>Answer</summary>

- [x] **GetBucketLocation**
- [x] **GetObject**
- [x] **ListAllMyBuckets**
- [x] **ListBucket**
- [x] Other S3 actions were **denied**.

</details>

### Question 11: What is the difference between existing policies mode and new policy mode?

<details>
<summary>Answer</summary>

- [x] **Existing policies** tests what is **already attached**.
- [x] **New policy** opens a **policy sandbox**.
- [x] In the sandbox you **paste JSON**, optionally **restrict** it, **apply**, and simulate.

</details>

### Question 12: What can you test in the policy sandbox?

<details>
<summary>Answer</summary>

- [x] A policy you **plan** to attach to a **user**, **group**, or **role**.
- [x] You see what permissions that JSON would grant **before** you apply it in IAM.

</details>

### Question 13: What happened after the instructor restricted the sandbox policy?

<details>
<summary>Answer</summary>

- [x] More actions returned **Access denied**.
- [x] **GetObject** and **ListAllMyBuckets** were still **allowed**.

</details>

### Question 14: Why clear results between simulations?

<details>
<summary>Answer</summary>

- [x] The simulator can be **finicky**.
- [x] Leftover service/action selections can confuse the next run.
- [x] **Clear**, select the service, **select all** (or the actions you want), then **run**.

</details>

### Question 15: Does the simulator replace attaching the policy in IAM?

<details>
<summary>Answer</summary>

- [x] **No.** It **simulates** the decision.
- [x] **Existing** mode reads attached policies; **new policy** mode tests JSON in a **sandbox**.
- [x] You still **attach** the policy in IAM when you are ready to grant it for real.

</details>

### Question 16: What identities did the instructor have under Users and Groups?

<details>
<summary>Answer</summary>

- [x] Users: **Neil** (admin) and **testuser** (limited).
- [x] Groups: one **admin** group.
- [x] Roles: **many** roles in the account.

</details>

### Question 17: What is a permissions boundary doing in this screen?

<details>
<summary>Answer</summary>

- [x] The simulator can **show** a boundary attached to the principal.
- [x] You can **simulate** a permissions boundary as part of the evaluation.
- [x] Boundaries cap the **maximum** permissions identity policies can grant.

</details>

</details>

## Summary

The **IAM Policy Simulator** tests **Allow** vs **Deny** for **API actions** on a **user**, **group**, or **role**. Open it from the lesson **link** or by searching. Pick a **limited** principal (instructor: **testuser** with inline policy **test poll**) so you can see **aggregate** permissions from inline, **group**, and **boundary** policies. Select a **service**, choose actions or **select all**, and **run**; **clear** results if the UI is sticky. Demo: **EC2** allowed, **EC2 Auto Scaling** denied, **S3** mostly denied except **GetBucketLocation**, **GetObject**, **ListAllMyBuckets**, and **ListBucket**. **New policy** mode is a **sandbox**: paste JSON you plan to attach, tighten it, and simulate **before** applying it in IAM.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
- [IAM Policy Simulator](https://policysim.aws.amazon.com/)
- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html)
- [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html)
- [Actions, resources, and condition keys for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html)
