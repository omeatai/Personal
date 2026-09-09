# 18. IAM Architecture Patterns

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This is the first **Architecture Patterns** lesson. These lessons take section knowledge and put it in **exam** and **workplace** form: you are a **solutions architect**, the customer gives **requirements** and **challenges**, and you pick the **best solution**. That is the shape of many exam questions. Six IAM scenarios: who may **change passwords**, **EC2 → DynamoDB** via a **role**, **job-function** permissions on a **first AWS account**, **source IP** restrictions, **CLI access keys**, and **full EC2** via an **`ec2:*`** action wildcard.

## Detailed Explanation

<details>
  <summary>Step 1 — Understand how architecture pattern lessons work</summary>

### Step 1 — Understand how architecture pattern lessons work

- [x] **What Architecture Patterns lessons are for**
  - Apply what you just learned to **exam** and **real-world** scenarios.
  - Imagine you are a **solutions architect** building to a customer’s **requirements** and **challenges**.
  - You must choose the **best** solution for the job.
  - That is the kind of thinking that shows up in **exam questions**.
  - The instructor poses scenarios and states **his** preferred solution.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/a25c2511-4293-465b-9a1a-c5a2a7b12f09" />

</details>

<details>
  <summary>Step 2 — Limit password changes to a select group</summary>

### Step 2 — Limit password changes to a select group

- [x] **Requirement: only a select group may change their IAM password**
  - Not everyone should change IAM passwords.
  - Some **privileged** users should be allowed to.
  - **Solution:** create a **group** for those users and attach a **permissions policy** that grants the IAM **ChangePassword** API (`iam:ChangePassword`).

</details>

<details>
  <summary>Step 3 — Delegate EC2 access to DynamoDB with a role</summary>

### Step 3 — Delegate EC2 access to DynamoDB with a role

- [x] **Requirement: an EC2 instance must be delegated access to a DynamoDB table**
  - **Amazon DynamoDB** is another AWS service (not covered in depth yet).
  - **Delegation** is the point: how does the instance get permission to the table?
  - **Solution:** create an **IAM role**, attach a **permissions policy** that grants access to **DynamoDB**, and use that role on the instance.

</details>

<details>
  <summary>Step 4 — Assign permissions by job function on a first AWS account</summary>

### Step 4 — Assign permissions by job function on a first AWS account

- [x] **Requirement: first AWS account — assign permissions by job function**
  - The company just created their **first** AWS account.
  - They may **not** have strong AWS skills yet.
  - They need permissions based on **job function**.
  - **IAM best practices** for this case: start with **AWS managed policies**.
  - Those policies can be aligned with common **job functions**.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/edf44114-8f0f-49db-a810-c9495e114b56" />

</details>

<details>
  <summary>Step 5 — Restrict a service by the requester’s source IP</summary>

### Step 5 — Restrict a service by the requester’s source IP

- [x] **Requirement: restrict access to a service by the requester’s source IP**
  - The solutions architect must limit an AWS service based on **source IP**.
  - **Solution:** create an **IAM permissions policy** and use the **Condition** element to control access by **source IP address**.

</details>

<details>
  <summary>Step 6 — Give a developer programmatic access from the CLI</summary>

### Step 6 — Give a developer programmatic access from the CLI

- [x] **Requirement: a developer must make programmatic API calls from the AWS CLI**
  - **Solution:** instruct the developer to create a set of **access keys** and use them for **programmatic** access.

</details>

<details>
  <summary>Step 7 — Grant full EC2 API access with an action wildcard</summary>

### Step 7 — Grant full EC2 API access with an action wildcard

- [x] **Requirement: a group of users needs full access to all Amazon EC2 API actions**
  - **Solution:** create a **permissions policy** whose **Action** uses a **wildcard** for EC2.
  - That action looks like **`ec2:*`**.

```text
# Select group may change password  →  iam:ChangePassword on a group policy
# EC2 → DynamoDB                    →  instance role + DynamoDB permissions
# First account / job function      →  AWS managed policies
# Restrict by requester IP          →  Condition (source IP)
# Developer CLI                     →  access keys
# Full EC2 APIs                     →  Action "ec2:*"
```

Example: full EC2 API access (Action wildcard)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:*",
      "Resource": "*"
    }
  ]
}
```

</details>

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. There is no console walkthrough. Treat each requirement as a flashcard: name the **best** IAM construct.

### **Overview**

- [ ] Practice the six **requirement → solution** mappings (exam-style).
- [ ] You will:
  - [ ] Password change for a **select group** → **group** + **`iam:ChangePassword`**.
  - [ ] **EC2** needs **DynamoDB** → **role** + DynamoDB permissions policy.
  - [ ] First account, permissions by **job function** → **AWS managed policies**.
  - [ ] Restrict by **source IP** → policy **Condition**.
  - [ ] Developer **CLI** API calls → **access keys**.
  - [ ] Full **EC2** API access → Action **`ec2:*`**.

```text
# Select group may change password  →  iam:ChangePassword on a group policy
# EC2 → DynamoDB                    →  instance role + DynamoDB permissions
# First account / job function      →  AWS managed policies
# Restrict by requester IP          →  Condition (source IP)
# Developer CLI                     →  access keys
# Full EC2 APIs                     →  Action "ec2:*"
```

Example: full EC2 API access (Action wildcard)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:*",
      "Resource": "*"
    }
  ]
}
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are Architecture Patterns lessons for?

<details>
<summary>Answer</summary>

- [x] They put section knowledge into **exam** and **workplace** scenarios.
- [x] You act as a **solutions architect**: customer **requirements** and **challenges** → **best** solution.
- [x] That is the shape of many **exam questions**.

</details>

### Question 2: Only a select group should change their IAM passwords. What do you do?

<details>
<summary>Answer</summary>

- [x] Create a **group** for those users.
- [x] Attach a **permissions policy** that grants the IAM **ChangePassword** API (`iam:ChangePassword`).
- [x] Do **not** give that permission to everybody.

</details>

### Question 3: An EC2 instance must access a DynamoDB table. How do you delegate that?

<details>
<summary>Answer</summary>

- [x] Create an **IAM role**.
- [x] Attach a **permissions policy** that grants access to **DynamoDB**.
- [x] That is how you **delegate** permissions to the instance (not by embedding long-lived keys in the lesson’s solution).

</details>

### Question 4: A company just created their first AWS account and needs permissions by job function. What do IAM best practices suggest?

<details>
<summary>Answer</summary>

- [x] Use **AWS managed policies**.
- [x] Those policies align with common **job functions**.
- [x] Fits a team that may **not** yet have strong AWS policy-writing skills.

</details>

### Question 5: Why are AWS managed policies the preferred starting point in that first-account scenario?

<details>
<summary>Answer</summary>

- [x] It is their **first** AWS account.
- [x] They may not have good **AWS skills** yet.
- [x] Managed policies are already aligned to **job functions**.

</details>

### Question 6: How do you restrict access to an AWS service based on the requester’s source IP?

<details>
<summary>Answer</summary>

- [x] Create an **IAM permissions policy**.
- [x] Use the **Condition** element to control access by **source IP address**.

</details>

### Question 7: A developer needs to make programmatic API calls from the AWS CLI. What do you tell them?

<details>
<summary>Answer</summary>

- [x] Create a set of **access keys**.
- [x] Use those keys for **programmatic** access (CLI / API).

</details>

### Question 8: A group of users needs full access to all Amazon EC2 API actions. What does the Action look like?

<details>
<summary>Answer</summary>

- [x] Create a **permissions policy**.
- [x] Use a **wildcard** on the **Action** for EC2.
- [x] The action is **`ec2:*`**.

</details>

### Question 9: Map each requirement to the IAM construct the instructor chose.

<details>
<summary>Answer</summary>

- [x] Select users change password → **group** + **`iam:ChangePassword`**
- [x] EC2 talks to DynamoDB → **role** + DynamoDB policy
- [x] First account, job functions → **AWS managed policies**
- [x] Restrict by IP → policy **Condition**
- [x] Developer CLI → **access keys**
- [x] Full EC2 APIs → Action **`ec2:*`**

</details>

### Question 10: Why is a role the right answer for EC2 → DynamoDB, not an IAM user password?

<details>
<summary>Answer</summary>

- [x] The requirement is to **delegate** permissions to an **EC2 instance**.
- [x] You **create a role** and assign a policy that grants **DynamoDB** access.
- [x] That is the delegation pattern for a **service / instance**, not a console login.

</details>

### Question 11: Does “full access to all Amazon EC2 API actions” require listing every EC2 action?

<details>
<summary>Answer</summary>

- [x] **No.** Use the **Action** wildcard **`ec2:*`**.
- [x] That covers **all** EC2 API actions.

</details>

### Question 12: Who should receive `iam:ChangePassword` in the first scenario?

<details>
<summary>Answer</summary>

- [x] Only a **select** / **privileged** group of users.
- [x] Not every user in the account.

</details>

### Question 13: Which policy element implements “only from this source IP”?

<details>
<summary>Answer</summary>

- [x] The **Condition** element on an **IAM permissions policy**.
- [x] It evaluates the requester’s **source IP address**.

</details>

### Question 14: Access keys vs a role — when does this lesson pick each?

<details>
<summary>Answer</summary>

- [x] **Access keys:** a **developer** making **programmatic** calls from the **AWS CLI**.
- [x] **Role:** an **EC2 instance** that must be **delegated** permissions to **DynamoDB**.

</details>

### Question 15: How do Architecture Patterns differ from exam crams?

<details>
<summary>Answer</summary>

- [x] **Architecture Patterns:** **requirements** → **best solution** (exam / workplace scenarios).
- [x] **Exam crams:** fast **bullet-point facts** for last-minute revision (covered in the IAM Exam Cram lesson).

</details>

</details>

## Summary

**Architecture Patterns** turn IAM theory into **requirement → best solution** (exam and workplace). Only a **select group** may change passwords: a **group** plus **`iam:ChangePassword`**. An **EC2** instance that must use **DynamoDB**: create a **role** and attach a DynamoDB **permissions policy**. A company’s **first** AWS account assigning access by **job function**: start with **AWS managed policies**. Restrict a service by the requester’s **source IP**: an IAM policy **Condition**. A developer calling APIs from the **CLI**: **access keys**. A group that needs every **EC2** API: Action **`ec2:*`**.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [ChangePassword](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html)
- [Allow users to change their own passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html)
- [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
- [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies)
- [Job functions managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
- [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)
- [IAM condition keys for source IP](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceip)
- [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [IAM JSON policy elements: Action](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html)
- [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html)
