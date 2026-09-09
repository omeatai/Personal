[← Course contents](../../01.md)

# 11. Permissions Boundaries

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

**Permissions boundaries** are an **advanced IAM** feature. They set the **maximum permissions** an IAM **entity** can receive from an **identity-based policy**. The boundary is assigned to **users** and **roles**. Effective access is limited to what appears on **both** the identity-based policy **and** the boundary — extra actions on the policy but missing from the boundary are **blocked**. This lesson uses **Joanne** (developer vs boundary) and **Lindsay** (IAM full access vs privilege escalation) to show why boundaries matter and how they stop a created user from becoming **more powerful** than the person who created them.

## Detailed Explanation

<details>
  <summary>Step 1 — Understand what a permissions boundary does</summary>

### Step 1 — Understand what a permissions boundary does

- [x] **What a permissions boundary is**
  - An **advanced IAM** feature.
  - It defines the **maximum permissions** available to an IAM **entity** via an **identity-based policy**.
  - You assign a boundary to **users** and to **roles**.
  - The identity-based policy can _offer_ more; the boundary **caps** what is actually allowed.

</details>

<details>
  <summary>Step 2 — Trace the Joanne example: developer policy versus boundary</summary>

### Step 2 — Trace the Joanne example: developer policy versus boundary

- [x] **Example: Joanne (developer policy + tighter boundary)**
  - **Joanne** needs access to certain AWS resources.
  - She has a **developer** identity-based policy with **full control** of:
    - **Amazon S3**
    - **Amazon CloudWatch**
    - **Amazon EC2**
    - **IAM**
  - A **permissions boundary** is also assigned to Joanne **directly**.
  - The boundary has **fewer** permissions: only **S3**, **CloudWatch**, and **EC2** (no IAM).
  - Result: even though the developer policy includes **IAM**, IAM is **not** on the boundary, so those actions are **limited**.
  - She **can** do things like **list buckets** in Amazon S3.
  - She **cannot** **create a user** in IAM.
  - The boundary restricted the **maximum** permissions that can be assigned to Joanne.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ee4ee652-51ca-4a82-ad7e-9347677150bb" />

</details>

<details>
  <summary>Step 3 — Work out effective permissions as an overlap</summary>

### Step 3 — Work out effective permissions as an overlap

- [x] **Effective permissions (intersection)**
  - Allowed actions must be present on the **identity-based policy** _and_ on the **permissions boundary**.
  - Developer policy: S3 + CloudWatch + EC2 + IAM.
  - Boundary: S3 + CloudWatch + EC2.
  - Effective: **S3 + CloudWatch + EC2** only.

```text
# Joanne — identity-based (developer): S3, CloudWatch, EC2, IAM
# Joanne — permissions boundary:        S3, CloudWatch, EC2
# Joanne — effective permissions:       S3, CloudWatch, EC2
# (IAM create-user is denied: it is on the policy but not on the boundary.)
```

</details>

<details>
  <summary>Step 4 — See how privilege escalation happens without a boundary</summary>

### Step 4 — See how privilege escalation happens without a boundary

- [x] **Privilege escalation (the attack)**
  - **Lindsay** has **IAM Full Access**.
  - She can do **anything in IAM**, but **not** other AWS services.
  - She **cannot** launch **EC2** instances or create **VPCs**.
  - She creates a user called **X-User**.
  - Because she has IAM full access, she can **create users** and **attach any policy**.
  - She attaches **AdministratorAccess** to **X-User**.
  - **X-User** is now **more powerful than Lindsay**.
  - She signs in as **X-User** and performs actions she should not (lesson example: **mine Bitcoins** on company spend).
  - That is a **privilege escalation** attack: create a user with **more** permissions than you have, then act as that user.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f00e0857-1215-4e70-b7db-ba94bd0d9c8a" />

</details>

<details>
  <summary>Step 5 — Stop escalation by adding a permissions boundary</summary>

### Step 5 — Stop escalation by adding a permissions boundary

- [x] **Mitigation with a permissions boundary**
  - Lindsay still needs **IAM Full Access** — that is her **job role**.
  - Add a **permissions boundary** so users **she creates** have the **same or fewer** permissions than she does.
  - She can still create **X-User** and still attach **AdministratorAccess**.
  - When she signs in as that user, the user does **not** get more permissions than Lindsay already has.
  - The boundary **prevents privilege escalation**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/91233bca-4ece-4805-a4a5-8a13136ed8ee" />

</details>

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. There is no console walkthrough. Later IAM lessons apply these ideas in HOL work.

### **Overview**

- [ ] This lesson explains **permissions boundaries** and **privilege escalation**; there is nothing to click in the console here.
- [ ] You will:
  - [ ] Remember that a boundary sets the **maximum** permissions for a **user** or **role**.
  - [ ] Trace **Joanne**: developer policy includes IAM, boundary does not → she cannot create IAM users.
  - [ ] Trace **Lindsay**: IAM Full Access without a boundary can create a more powerful user (**X-User** + **AdministratorAccess**).
  - [ ] Remember that a boundary on created users keeps them at the **same or fewer** permissions than Lindsay.

```text
# Joanne — identity-based (developer): S3, CloudWatch, EC2, IAM
# Joanne — permissions boundary:        S3, CloudWatch, EC2
# Joanne — effective permissions:       S3, CloudWatch, EC2
# (IAM create-user is denied: it is on the policy but not on the boundary.)
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a permissions boundary in IAM?

<details>
<summary>Answer</summary>

- [x] An **advanced IAM** feature.
- [x] It defines the **maximum permissions** an IAM **entity** can have via an **identity-based policy**.

</details>

### Question 2: Which IAM entities can you assign a permissions boundary to?

<details>
<summary>Answer</summary>

- [x] **Users**
- [x] **Roles**

</details>

### Question 3: How do an identity-based policy and a permissions boundary work together?

<details>
<summary>Answer</summary>

- [x] The boundary **caps** what the identity-based policy can grant.
- [x] An action is allowed only if it is on **both** the policy **and** the boundary.
- [x] Extra permissions on the policy that are **missing** from the boundary are **blocked**.

</details>

### Question 4: What services does Joanne’s developer policy allow full control of?

<details>
<summary>Answer</summary>

- [x] **Amazon S3**
- [x] **Amazon CloudWatch**
- [x] **Amazon EC2**
- [x] **IAM**

</details>

### Question 5: What services are on Joanne’s permissions boundary?

<details>
<summary>Answer</summary>

- [x] **Amazon S3**
- [x] **Amazon CloudWatch**
- [x] **Amazon EC2**
- [x] **Not IAM** — the boundary has **fewer** permissions than the developer policy.

</details>

### Question 6: Can Joanne list S3 buckets? Can she create an IAM user?

<details>
<summary>Answer</summary>

- [x] **Yes** — she can **list buckets** in Amazon S3 (S3 is on both the policy and the boundary).
- [x] **No** — she **cannot create a user** in IAM (IAM is on the policy but **not** on the boundary).

</details>

### Question 7: What is privilege escalation in this lesson?

<details>
<summary>Answer</summary>

- [x] Creating a user that has **more permissions** than you do.
- [x] Then **signing in as that user** and performing API actions you should not be able to perform.

</details>

### Question 8: What can Lindsay do with IAM Full Access, and what can she not do?

<details>
<summary>Answer</summary>

- [x] She can do **anything in IAM**.
- [x] She **cannot** use other AWS services with that policy alone.
- [x] Examples she cannot do: **launch EC2** instances or **create VPCs**.

</details>

### Question 9: How does Lindsay escalate privileges in the attack scenario?

<details>
<summary>Answer</summary>

- [x] She creates **X-User**.
- [x] She attaches **AdministratorAccess** (she can assign **any** policy because she has IAM full access).
- [x] **X-User** is now **more powerful than Lindsay**.
- [x] She signs in as **X-User** and abuses the extra access (lesson example: **mine Bitcoins** on company spend).

</details>

### Question 10: Why can Lindsay attach AdministratorAccess to X-User in the attack?

<details>
<summary>Answer</summary>

- [x] She has **IAM Full Access**.
- [x] That lets her **create users** and **assign any policy** she wants.

</details>

### Question 11: After the boundary is applied, does Lindsay still get IAM Full Access?

<details>
<summary>Answer</summary>

- [x] **Yes.** She still needs those permissions for her **job role**.
- [x] The boundary is added **in addition**, not as a replacement for her job policy.

</details>

### Question 12: How does a permissions boundary stop Lindsay’s privilege escalation?

<details>
<summary>Answer</summary>

- [x] Users **created by Lindsay** are limited to the **same or fewer** permissions than she has.
- [x] She can still create **X-User** and still attach **AdministratorAccess**.
- [x] When she signs in as that user, the user does **not** get more permissions than Lindsay already has.

</details>

### Question 13: After mitigation, can Lindsay still create X-User and attach AdministratorAccess?

<details>
<summary>Answer</summary>

- [x] **Yes** — she can still create the user and attach the policy.
- [x] The boundary means **X-User** still cannot exceed Lindsay’s maximum permissions.

</details>

### Question 14: Who is a permissions boundary assigned to in the Joanne example?

<details>
<summary>Answer</summary>

- [x] To **Joanne directly** (the IAM user / entity).
- [x] It is **in addition to** her identity-based **developer** policy.

</details>

### Question 15: If a policy grants IAM but the boundary does not, what happens?

<details>
<summary>Answer</summary>

- [x] IAM is **not** effectively allowed.
- [x] The missing service on the boundary **limits** the entity.
- [x] Example: Joanne cannot **create a user** even though the developer policy includes IAM.

</details>

</details>

## Summary

A **permissions boundary** sets the **maximum** permissions an IAM **user** or **role** can get from an **identity-based policy**. Effective access is the **overlap** of both. **Joanne** has a developer policy (S3, CloudWatch, EC2, **IAM**) and a tighter boundary (S3, CloudWatch, EC2 only), so she can **list S3 buckets** but **cannot create IAM users**. **Lindsay** with **IAM Full Access** can create **X-User**, attach **AdministratorAccess**, and sign in as a **more powerful** user (**privilege escalation**). Adding a boundary so users she creates have the **same or fewer** permissions than she does still lets her create users and attach admin, but blocks the extra power.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [When to use permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html#access_policies_boundaries-when-to-use)
- [AWS managed policy: IAMFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/IAMFullAccess.html)
- [AWS managed policy: AdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html)
- [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)
