# 13. IAM policy structure

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This lesson is about **reading IAM policies in JSON** (**JavaScript Object Notation**). In AWS, the console, CLI, and SDKs all call **API actions** (for example **EC2 RunInstances**, **RDS StopDBInstance**). A policy is a JSON document with a **Version**, one or more **Statement** blocks, and in each statement an **Effect** (`Allow` or `Deny`), **Action** (API operations, often with `*` wildcards), and **Resource** (**ARNs**). You can allow or deny a single action, a family of actions, or a whole service. JSON must be valid — a missing comma breaks the policy. The slide example allows **all S3 actions** on a bucket **and** its objects, plus **DynamoDB Describe\*** on a named table.

## Detailed Explanation

<details>
  <summary>Step 1 — Understand that every operation is an API action</summary>

### Step 1 — Understand that every operation is an API action

- [x] **Everything is an API action**
  - Console, **CLI**, and **SDK** usage all make **API calls**.
  - Each service has its **own set** of API actions.
  - Launching an EC2 instance in the console calls **EC2 `RunInstances`**.
  - Stopping an RDS database (CLI or console) calls **RDS `StopDBInstance`**.
  - Policies can be **narrow** (one action) or **broad** (an entire service, or more).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4982836d-a747-44d0-bbaa-d8272515fe09" />

</details>

<details>
  <summary>Step 2 — Read IAM policies as strict JSON</summary>

### Step 2 — Read IAM policies as strict JSON

- [x] **Policies are JSON**
  - All AWS IAM policies are written in **JSON** (**JavaScript Object Notation**).
  - Formatting is strict: miss a **comma** and the policy **breaks**.
  - **Visual Studio Code** and the **AWS Management Console** policy editor usually **highlight** JSON errors.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ec7bacfb-710e-4028-8539-c4bb8cc3930d" />

</details>

<details>
  <summary>Step 3 — Identify the Version and Statement elements</summary>

### Step 3 — Identify the Version and Statement elements

- [x] **Version**
  - The top-level **Version** looks like a date (commonly **`2012-10-17`**).
  - It is **not** a typo or “wrong date.”
  - It identifies the **JSON policy language** version being used.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6c030749-004c-4135-ab18-7092e04159f8" />

- [x] **Statement**
  - A **statement** is a block of policy code.
  - Each statement has **Effect**, **Action**, **Resource**, and related elements, evaluated **together**.
  - A policy may contain **more than one** permission statement.
  - Extra statements are additional JSON objects in the `Statement` array, separated by **commas**.

</details>

<details>
  <summary>Step 4 — Set the Effect and list the Action</summary>

### Step 4 — Set the Effect and list the Action

- [x] **Effect**
  - Only two values: **`Allow`** or **`Deny`**.
  - Choose whether you want to **allow** or **deny** the listed actions on the listed resources.
- [x] **Action**
  - Lists the **resource operations** (API actions) the statement affects.
  - Example: allow or deny **S3** and **DynamoDB** operations.
  - You can be **specific** or **generic**.
  - Slide examples:
    - **`s3:*`** — **wildcard**; **all** S3 API actions.
    - **`dynamodb:Describe*`** — more specific: every DynamoDB action whose name starts with **Describe** (for example **DescribeTable**).

</details>

<details>
  <summary>Step 5 — Scope the statement to resources with ARNs and wildcards</summary>

### Step 5 — Scope the statement to resources with ARNs and wildcards

- [x] **Resource (ARNs)**
  - Lists the **specific resources** the statement applies to, as **Amazon Resource Names (ARNs)**.
  - **S3 needs two resource lines** in this example:
    - Bucket ARN (bucket-level actions).
    - Same ARN with **`/*`** (object-level actions — the files **in** the bucket).
  - S3 has **bucket-level** API actions and **object-level** API actions; objects can have their **own** permissions.
  - **`*`** on those two ARNs together means **all bucket-level and all object-level** permissions for that bucket (here, **Allow**).
  - **DynamoDB:** one table ARN that includes **region**, **account number**, and **table name**.
- [x] **Wildcard `*`**
  - Means **everything from that point onward**.
  - **`s3:*`** = every API action that starts with **`s3:`** — all Amazon S3 actions.

Illustrative JSON matching the slide: **Allow** all **S3** actions on a bucket **and** its objects, plus **DynamoDB `Describe*`** on one table. Replace the bucket name, account, region, and table with yours. **`Version`** is the policy language version, not a “wrong date.”

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*", "dynamodb:Describe*"],
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*",
        "arn:aws:dynamodb:us-east-1:123456789012:table/example-table"
      ]
    }
  ]
}
```

- [x] **`s3:*`** — all S3 API actions.
- [x] **`dynamodb:Describe*`** — DynamoDB actions that start with **Describe**.
- [x] Two S3 ARNs: bucket-level, then **`/*`** for objects.
- [x] DynamoDB ARN includes **region**, **account ID**, and **table name**.
- [x] A second statement would be another object in the `Statement` array, separated by a **comma**.

</details>

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. You read a JSON policy on a slide; you do not create one in the console here.

### **Overview**

- [ ] This lesson is **how to read IAM JSON**; there is no console walkthrough.
- [ ] You will:
  - [ ] Map console/CLI clicks to **API actions** (for example **RunInstances**, **StopDBInstance**).
  - [ ] Identify **Version**, **Statement**, **Effect**, **Action**, and **Resource**.
  - [ ] Explain **`s3:*`**, **`dynamodb:Describe*`**, and why S3 lists **two** ARNs (bucket and `/*` objects).
  - [ ] Remember JSON is strict — a missing **comma** invalidates the policy.

Illustrative JSON matching the slide: **Allow** all **S3** actions on a bucket **and** its objects, plus **DynamoDB `Describe*`** on one table. Replace the bucket name, account, region, and table with yours. **`Version`** is the policy language version, not a “wrong date.”

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*", "dynamodb:Describe*"],
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*",
        "arn:aws:dynamodb:us-east-1:123456789012:table/example-table"
      ]
    }
  ]
}
```

- [x] **`s3:*`** — all S3 API actions.
- [x] **`dynamodb:Describe*`** — DynamoDB actions that start with **Describe**.
- [x] Two S3 ARNs: bucket-level, then **`/*`** for objects.
- [x] DynamoDB ARN includes **region**, **account ID**, and **table name**.
- [x] A second statement would be another object in the `Statement` array, separated by a **comma**.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are you actually doing when you use the console, CLI, or SDK?

<details>
<summary>Answer</summary>

- [x] Making an **API call**.
- [x] Each service has its **own set** of API actions.

</details>

### Question 2: Which API actions match launching an EC2 instance and stopping an RDS database?

<details>
<summary>Answer</summary>

- [x] Launch EC2: **`RunInstances`**.
- [x] Stop RDS: **`StopDBInstance`**.

</details>

### Question 3: In what language are IAM policies written?

<details>
<summary>Answer</summary>

- [x] **JSON** (**JavaScript Object Notation**).
- [x] All AWS policies use JSON.

</details>

### Question 4: What is the Version field at the top of a policy?

<details>
<summary>Answer</summary>

- [x] The **JSON policy language** version.
- [x] The date (commonly **`2012-10-17`**) is **correct**, not a typo.

</details>

### Question 5: What is a Statement, and can a policy have more than one?

<details>
<summary>Answer</summary>

- [x] A **statement** is a block that holds **Effect**, **Action**, **Resource**, and related elements.
- [x] Those elements in a statement are evaluated **together**.
- [x] A policy **may contain more than one** permission statement (comma-separated in JSON).

</details>

### Question 6: What happens if you miss a comma in a JSON policy?

<details>
<summary>Answer</summary>

- [x] The policy **breaks** (invalid JSON).
- [x] **VS Code** and the **Management Console** policy editor usually **highlight** the error.

</details>

### Question 7: What values can Effect have?

<details>
<summary>Answer</summary>

- [x] **`Allow`**
- [x] **`Deny`**
- [x] Those are the **only two** effects.

</details>

### Question 8: What does the Action element list?

<details>
<summary>Answer</summary>

- [x] The **resource operations** (API actions) the policy affects.
- [x] You choose **allow** or **deny**, then **which** actions.

</details>

### Question 9: What does `s3:*` mean?

<details>
<summary>Answer</summary>

- [x] A **wildcard**.
- [x] **All** Amazon S3 API actions (every action that starts with **`s3:`**).

</details>

### Question 10: What does `dynamodb:Describe*` mean?

<details>
<summary>Answer</summary>

- [x] DynamoDB actions whose names start with **Describe**.
- [x] Example: **DescribeTable**.
- [x] More specific than `dynamodb:*`, still broader than a single action.

</details>

### Question 11: What does the Resource element list?

<details>
<summary>Answer</summary>

- [x] The **specific resources** the statement applies to.
- [x] Identified by **Amazon Resource Names (ARNs)**.

</details>

### Question 12: Why does the S3 example use two resource ARNs?

<details>
<summary>Answer</summary>

- [x] One ARN is **bucket-level** (the bucket itself).
- [x] The ARN with **`/*`** is **object-level** (objects **inside** the bucket).
- [x] S3 has **bucket-level** and **object-level** API actions.
- [x] Together they allow **all bucket-level and all object-level** permissions for that bucket.

</details>

### Question 13: What does a DynamoDB table ARN include in this lesson?

<details>
<summary>Answer</summary>

- [x] The **account number**.
- [x] The **region**.
- [x] The **table name**.

</details>

### Question 14: What does the `*` wildcard mean in a policy?

<details>
<summary>Answer</summary>

- [x] **Everything from that point** onward.
- [x] Example: **`s3:*`** = all S3 API actions.

</details>

### Question 15: Can a policy allow a whole service instead of one API action?

<details>
<summary>Answer</summary>

- [x] **Yes.** You can restrict or allow **individual** API actions.
- [x] You can also write **broader** policies that allow or deny an **entire service** (or more).

</details>

</details>

## Summary

Console, CLI, and SDK calls are **API actions** (for example **EC2 RunInstances**, **RDS StopDBInstance**). IAM policies are **JSON**: **Version** (policy language, often **`2012-10-17`**), one or more **Statement** blocks, **Effect** (`Allow` or `Deny` only), **Action**, and **Resource** (ARNs). JSON must be valid — a missing **comma** breaks the policy; editors highlight errors. **`s3:*`** is all S3 actions; **`dynamodb:Describe*`** is Describe-family DynamoDB actions. S3 often needs **two** ARNs: the **bucket** and **`bucket/*`** for **objects**. A DynamoDB table ARN includes **region**, **account**, and **table name**. `*` means everything from that point.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [IAM JSON policy elements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)
- [IAM JSON policy elements: Version](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html)
- [IAM JSON policy elements: Effect](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html)
- [IAM JSON policy elements: Action](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html)
- [IAM JSON policy elements: Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html)
- [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)
- [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html)
- [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html)
- [StopDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstance.html)
