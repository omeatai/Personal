# 17. IAM Exam Cram

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

Most sections end with an **exam cram**: a **fast** run-through of **important facts** for **revision**, not a new explanation. Change **playback speed** if it is too fast. Crams are **bullet points** (not visual like the main lessons); some facts appear here but not in the theory videos, or the other way around. The instructor uses them so **visual**, **reading**, and **hands-on** learners all have a last-minute tool. This cram is **IAM**: what it controls, users / groups / roles / policies, consistency, authentication methods, policy types, and a best-practice checklist.

## Detailed Explanation

<details>
  <summary>Step 1 — Understand what an exam cram is for</summary>

### Step 1 — Understand what an exam cram is for

- [x] **What an exam cram is**
  - A **quick** reminder of key facts after you finish the section.
  - Use it for **revision** and **cramming**, not as the first pass.
  - The instructor goes **fast**; slow the video if needed.
  - Some bullets may be **new** vs the lessons, or the lessons may include topics **not** in the cram.
  - Main lessons stay **visual**; crams are **death by bullet points** on purpose so **readers** are covered too.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/434ca0b5-78cf-4d41-a434-4c55c0776021" />

</details>

<details>
  <summary>Step 2 — Recall what IAM does and the new-user default</summary>

### Step 2 — Recall what IAM does and the new-user default

- [x] **What IAM does**
  - **Securely control** individual and **group** access to **AWS resources**.
  - Makes it easy to give **multiple users** access to those resources.
  - You manage **users**, **groups**, **access policies**, **roles**, and **user credentials**.
  - You can configure **user password policies**.
  - Enable **MFA** — **recommended**.
  - Generate **API keys** for **programmatic** access.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/8f96f37c-5c8d-48f9-a1c0-95c189c542ff" />

- [x] **Default for new IAM users**
  - New users are created with **no access** to any services.
  - They can **log in** to AWS but **cannot do anything**.
  - Permissions must be **explicitly granted** before a user can use an AWS service.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/51db6540-21f5-4548-8545-d164dabb2157" />

</details>

<details>
  <summary>Step 3 — Know IAM users and IAM’s global, eventually consistent nature</summary>

### Step 3 — Know IAM users and IAM’s global, eventually consistent nature

- [x] **IAM users**
  - Individuals (or services) who have been **granted access** to an AWS account.
  - An IAM user is an **entity** that represents a **person** or a **service**.
  - By default they **cannot access anything** in the account.
  - IAM users that represent applications are **service accounts**.
  - Limit: up to **5,000 users** per AWS account.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/3669adc1-a77a-44cd-bcf2-d430166c6117" />

- [x] **IAM is global and eventually consistent**
  - IAM is a **universal / global** service — it is **not** tied to a specific **region**.
  - IAM is **eventually consistent**.
  - If you make a change and **immediately** read it back, you **might not see** the change yet; wait a bit.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/db29a0e0-c57e-445e-96bc-e3ed1f20e207" />

</details>

<details>
  <summary>Step 4 — Compare authentication methods and the root user</summary>

### Step 4 — Compare authentication methods and the root user

- [x] **Authentication methods**
  - **Console passwords** — sign in to the **Management Console**.
  - **Access keys** — **programmatic** access (CLI / API).
  - **Server certificates** — used with **some** services.
- [x] **Root user**
  - Credentials are the **email address** used to create the account, plus a **password**.
  - Root has **full administrative** permissions.
  - Those permissions **cannot be restricted**.

</details>

<details>
  <summary>Step 5 — Assign permissions with groups and roles</summary>

### Step 5 — Assign permissions with groups and roles

- [x] **IAM groups**
  - A **collection of users** with **policies** attached.
  - A group is **not an identity** itself.
  - A group **cannot** be identified as a **principal** in a policy (you cannot put a group **ARN** where a user principal goes).
  - Use groups to **assign permissions** to users.
  - Always follow **least privilege** when assigning permissions.
  - You **cannot nest** groups (no group inside a group).

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/c62b0007-802f-4773-a147-08f4b270a865" />

- [x] **IAM roles**
  - Created, then **assumed** by **trusted entities**.
  - A way to **delegate** permissions to **users** and **services**.
  - Users and services assume a role to get **temporary security credentials**.
  - Those credentials are issued by **AWS Security Token Service (STS)**.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/fec625e0-6b92-466f-a7d1-0e00bb52b95b" />

</details>

<details>
  <summary>Step 6 — Work through policies and the five policy types</summary>

### Step 6 — Work through policies and the five policy types

- [x] **IAM policies**
  - **Documents** that define permissions.
  - Applied to **users**, **groups**, and **roles**.
  - Written as **key-value** pairs (an **attribute** and a **value**).
  - All permissions are **implicitly denied** by default.
  - If multiple policies **conflict**, the **most restrictive** policy is applied.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/91987d46-18fe-4b3b-a18b-31931ff389e6" />

- [x] **Policy types**
  - **Identity-based policies** — attach to **users**, **groups**, or **roles**.
  - **Resource-based policies** — attach to **resources** (example: **S3 buckets**); they define permissions for **principals** that access the resource.
  - **Permissions boundaries** — set the **maximum** permissions an identity-based policy can grant to an IAM entity. **Not really covered** at **Associate**; they are on the **Professional** exam.
  - **Organizations service control policies (SCPs)** — specify the **maximum** permissions for an **organization** or an **OU**.
  - **Session policies** — used with **assumed-role** API actions.

```text
# New IAM user: can log in, cannot do anything until permissions are granted
# Implicit deny by default; conflicts → most restrictive wins
# Group: not a principal (no group ARN in Principal); cannot nest groups
# Role assume → STS temporary credentials
# Policy types:
#   identity-based | resource-based | permissions boundary
#   Organizations SCP (org / OU max) | session (assumed-role APIs)
```

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/28465f36-6ad9-4c08-af78-8ec775ce184f" />

</details>

<details>
  <summary>Step 7 — Run the IAM best-practice checklist</summary>

### Step 7 — Run the IAM best-practice checklist

- [x] **IAM best-practice checklist (exam cram list)**
  - **Lock away** the account **root user access keys**.
  - Create **individual users**.
  - Use **groups** to assign permissions to users.
  - Grant **least privilege**.
  - Get started with **AWS managed policies**.
  - Prefer **customer managed policies** over **inline** policies.
  - Use **access levels** to review IAM permissions (still thinking **least privilege**).
  - Configure a **strong password policy** for users.
  - Enable **MFA**.
  - Use **roles** for applications that run on **EC2** instances.
  - Use **roles** to **delegate** permissions.
  - Do **not share** access keys — keep them to yourself and use them only for your account.
  - **Rotate** all credentials regularly.
  - **Remove** unnecessary credentials.
  - Use **policy conditions** for extra security.
  - **Monitor** activity in your account.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/c3e3f2d7-9297-4d33-a4d6-69ff34411f1e" />
<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/9ffc6262-90a7-4ee1-bdd4-80e0f711928a" />

</details>

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. This is a **revision** cram, not a console walkthrough.

### **Overview**

- [ ] Recite what **IAM** controls and the default for a **new user**.
- [ ] You will:
  - [ ] Distinguish **users**, **groups** (not a principal; no nesting), **roles** + **STS**, and **root**.
  - [ ] Name the five **policy types** and the default **implicit deny**.

```text
# New IAM user: can log in, cannot do anything until permissions are granted
# Implicit deny by default; conflicts → most restrictive wins
# Group: not a principal (no group ARN in Principal); cannot nest groups
# Role assume → STS temporary credentials
# Policy types:
#   identity-based | resource-based | permissions boundary
#   Organizations SCP (org / OU max) | session (assumed-role APIs)
```
  - [ ] Run through the **best-practice** checklist (root keys, groups, least privilege, MFA, roles on EC2, rotate / remove credentials).

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is IAM used for?

<details>
<summary>Answer</summary>

- [x] To **securely control** individual and **group** access to **AWS resources**.
- [x] It makes it easy to give **multiple users** access.
- [x] You manage **users**, **groups**, **access policies**, **roles**, and **credentials**.

</details>

### Question 2: What access does a new IAM user have by default?

<details>
<summary>Answer</summary>

- [x] **None** — no access to any services.
- [x] They can **log in** but **cannot do anything**.
- [x] Permissions must be **explicitly granted**.

</details>

### Question 3: Is IAM regional? What consistency model does it use?

<details>
<summary>Answer</summary>

- [x] IAM is **universal / global** — not tied to a specific **region**.
- [x] It is **eventually consistent**.
- [x] A change you write may **not show immediately** if you read it right away.

</details>

### Question 4: What authentication methods does this cram list?

<details>
<summary>Answer</summary>

- [x] **Console passwords** for the **Management Console**.
- [x] **Access keys** for **programmatic** access.
- [x] **Server certificates** for **some** services.

</details>

### Question 5: What are the root user’s credentials, and can you restrict root?

<details>
<summary>Answer</summary>

- [x] The **email** used to create the account plus a **password**.
- [x] Root has **full administrative** permissions.
- [x] Those permissions **cannot be restricted**.

</details>

### Question 6: How many IAM users can you have per account, and what is a service account?

<details>
<summary>Answer</summary>

- [x] Up to **5,000 users** per AWS account.
- [x] An IAM user that represents an **application** is a **service account**.

</details>

### Question 7: Why is an IAM group not a principal?

<details>
<summary>Answer</summary>

- [x] A group is **not an identity** itself.
- [x] You **cannot** put a group **ARN** as the **principal** in a policy (the way you can a user).
- [x] Groups exist to **attach policies** and assign permissions to **users**.

</details>

### Question 8: Can you nest IAM groups?

<details>
<summary>Answer</summary>

- [x] **No.** You cannot create a group **inside** a group.

</details>

### Question 9: How do IAM roles grant access?

<details>
<summary>Answer</summary>

- [x] A role is **assumed** by a **trusted entity** (user or service).
- [x] That is how you **delegate** permissions.
- [x] The assumer gets **temporary security credentials** from **STS**.

</details>

### Question 10: What is the default for IAM permissions, and what happens if policies conflict?

<details>
<summary>Answer</summary>

- [x] All permissions are **implicitly denied** by default.
- [x] If statements **conflict**, the **most restrictive** policy is applied.

</details>

### Question 11: What are identity-based vs resource-based policies?

<details>
<summary>Answer</summary>

- [x] **Identity-based:** attach to **users**, **groups**, or **roles**.
- [x] **Resource-based:** attach to a **resource** (example: an **S3 bucket**).
- [x] A resource policy names the **principals** that may access that resource.

</details>

### Question 12: What do permissions boundaries, SCPs, and session policies each cap?

<details>
<summary>Answer</summary>

- [x] **Permissions boundary:** maximum an **identity-based** policy can grant to an IAM **entity**.
- [x] **SCP:** maximum permissions for an **organization** or an **OU**.
- [x] **Session policy:** used with **assumed-role** API actions.
- [x] Permissions boundaries are **not really** Associate-level; they are on the **Professional** exam.

</details>

### Question 13: What should you do with the root user according to this cram?

<details>
<summary>Answer</summary>

- [x] **Lock away** the account **root user access keys**.
- [x] Create **individual users** instead of working as root.

</details>

### Question 14: How should you assign permissions to people (groups, least privilege, policy style)?

<details>
<summary>Answer</summary>

- [x] Use **groups** to assign permissions to users.
- [x] Grant **least privilege**.
- [x] Start with **AWS managed policies**.
- [x] Prefer **customer managed** policies over **inline** policies.
- [x] Use **access levels** to review permissions against least privilege.

</details>

### Question 15: Which credential and password practices does the cram list?

<details>
<summary>Answer</summary>

- [x] Configure a **strong password policy**.
- [x] Enable **MFA**.
- [x] Do **not share** access keys.
- [x] **Rotate** all credentials regularly.
- [x] **Remove** unnecessary credentials.

</details>

### Question 16: When should you use IAM roles (best-practice list)?

<details>
<summary>Answer</summary>

- [x] For **applications that run on EC2** instances.
- [x] To **delegate** permissions.

</details>

### Question 17: What extra controls does the cram mention after writing policies?

<details>
<summary>Answer</summary>

- [x] Use **policy conditions** for extra security.
- [x] **Monitor** activity in the account to see what is actually happening.

</details>

### Question 18: How should you use exam cram lessons in this course?

<details>
<summary>Answer</summary>

- [x] After you finish the **section**, for **revision** / last-minute **cramming**.
- [x] They **remind** you of facts; they are not the visual first-pass lessons.
- [x] Slow **playback** if the instructor is too fast.
- [x] A fact might appear in the cram **or** in the lessons, not always both.

</details>

</details>

## Summary

**Exam crams** are fast **bullet-point** revision after a section. **IAM** securely controls who can use AWS resources: you manage **users**, **groups**, **roles**, **policies**, **credentials**, **password policies**, **MFA**, and **API keys**. New users can **log in** but have **no access** until you **explicitly grant** it. IAM is **global** and **eventually consistent**. Auth methods: **console passwords**, **access keys**, **server certificates**. **Root** is the signup **email** + password, with **unrestrictable** full admin. Users (including **service accounts**) cap at **5,000** per account. **Groups** hold users and policies but are **not principals** and **cannot nest**. **Roles** are **assumed**; **STS** issues **temporary** credentials. Policies are documents; default is **implicit deny**; conflicts take the **most restrictive** statement. Policy types: **identity-based**, **resource-based**, **permissions boundaries** (Professional more than Associate), **SCPs** (org / OU max), **session** (assumed-role APIs). Best practices: lock **root keys**, individual users, **groups**, **least privilege**, managed then **customer managed** (not inline), review **access levels**, strong passwords, **MFA**, **roles** on **EC2** and for delegation, never **share** keys, **rotate** / **remove** credentials, **conditions**, **monitor**.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
- [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
- [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)
- [Resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html#principal_vs_identity)
- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)
- [IAM and quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html)
- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [MFA in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [Setting an account password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
