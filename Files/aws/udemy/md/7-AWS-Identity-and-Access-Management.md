# 7. AWS Identity and Access Management

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This lesson introduces **AWS Identity and Access Management (IAM)**—the service you use to **authenticate** and **authorize** access to an AWS account. You connect through the **Management Console**, the **command line interface (CLI)**, and the **API** (including SDKs). The core identities are **users**, **user groups**, **roles**, and **policies**. You also cover **access keys**, **identity-based** and **resource-based policies**, **multi-factor authentication (MFA)**, **password policies**, **Amazon Resource Names (ARNs)**, and why you **lock away the root user** after setup.

## Detailed Explanation

- [x] **Why IAM comes first**
  - The first thing to understand in detail is how to **securely connect** to your AWS account.
  - You connect through the **console**, the **CLI**, and the **API**.
  - Learn the constructs: **users**, **groups**, **roles**, and **policies**.
  - Learn how you **authenticate** and are **authorized** to access AWS services.
  - Mechanisms include **access keys**, **identity-based policies**, and **resource-based policies**.
  - Configure **MFA** and **password policies** so accounts stay as secure as possible.
  - Know IAM **best practices** for the exam and for keeping real accounts secure.
- [x] **What IAM is**
  - **IAM** = **Identity and Access Management** (sometimes said **I-am**).
  - It is the service used for **authentication** and **authorization**.
  - You manage AWS through the **console**, the **CLI**, and the **API** via **SDKs**.
  - Through IAM you can create **users** and **roles**, use **federated users**, and enable **authentication for applications**.
- [x] **Principals must be authenticated**
  - All IAM **principals** must be **authenticated** to send requests (any **API request** to AWS).
  - A **principal** is a **person** or **application** that requests an **API action / operation** on an AWS **resource**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a2222001-6d5c-4aef-975b-3e0e96e74118" />

- [x] **Authentication vs authorization**
  - **Authentication:** proving you are who you say you are (for example, supplying a **password**).
  - **Authorization:** being **allowed** or **denied** access to resources.
  - **Policies** (identity-based and resource-based) define **what you are allowed to do**.
  - Flow: **authenticate first**, then AWS determines what you may do.
  - Example authorized API actions:
    - **RunInstances** on **EC2** — launch a virtual server
    - **GetBucket** — retrieve information about buckets
    - **CreateUser** — create a user in IAM
  - API actions are authorized **on the AWS resources**.
- [x] **Core IAM components**
  - **Users**, **user groups**, **roles**, and **policies**.
  - **User groups:** add users, then apply **permissions policies** to the group.
  - A **user** can log in with a user account.
  - A **policy** determines which **API actions** the user may take in the account or on a specific resource.
  - Attach policies to a **group** so you manage **one policy** for many people with the same job role.
  - Users **inherit** the permissions applied to the group through the policy.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e52c0364-d2d7-4101-905f-12689fd27cf3" />

- [x] **Identity-based policies**
  - Applied to **users**, **groups**, and **roles**.
  - They grant the permissions those identities get when they make requests.
- [x] **Roles (delegation)**
  - Roles are used for **delegation** and are **assumed**.
  - A role is an **identity** with permissions assigned via **policy**.
  - You **assume the role** and take on those permissions (like putting on a **hat**).
  - Example: put on a **development** hat for development permissions, then switch to an **ops** hat for ops permissions.
- [x] **What policies do**
  - Policies define **permissions** for the **identities** or **resources** they are associated with.
- [x] **Root user vs creating IAM users**
  - Creating the account with an **email address** creates the **root user**.
  - Root has **full permissions**; you **cannot restrict most** of them.
  - **Best practice:** do **not** use the root account for daily work.
  - Set a **very strong password** and enable **MFA** on root.
  - Then create **IAM user** accounts for people.
  - You can create up to **5,000** individual user accounts.
  - **New IAM users have no permissions by default** — an important exam fact.
  - If you enable **Management Console** access, the user can **log in** but **cannot do anything** until you apply permissions.
- [x] **Friendly name and ARN**
  - Example user: **Andrea**.
  - The **friendly name** is a simple **text string** (here, her name).
  - She logs in with that name plus a **password**.
  - Every AWS resource has an **Amazon Resource Name (ARN)** — a **unique identifier** in AWS.
  - An IAM user ARN includes:
    - That it is an **AWS** / **IAM** resource
    - The **account number**
    - The resource type **user**
    - The **friendly name** (for example, Andrea)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/afa6d266-4ea9-46d3-a8a5-4bf5436efa13" />

- [x] **How an IAM user authenticates**
  - **Management Console:** **username** and **password**, optionally **MFA**.
  - **CLI** and **API:** **access keys**.
- [x] **User groups**
  - Help from a **management** perspective.
  - Example groups: **admin**, **development**, **operations**.
  - Add users to groups; some users may be in **multiple groups**.
  - Attach a **permissions policy** to the group; members **automatically inherit** it.
  - If a user is in multiple groups, the permission sets are **combined**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2e33ccd7-9bd9-4e8e-a705-01e2fad66265" />

- [x] **Authentication methods in more detail**
  - Console: **username / password** plus an **MFA token** for extra security (example: John authenticated and performing operations in the console).
  - CLI and API need **credentials**.
  - One way: generate an **access key ID** and a **secret access key** (like a username and password for programmatic use).
  - Use those via the **CLI** and **API** to authenticate to the AWS API.
  - **AWS Security Token Service (STS)** can generate **short-term credentials**.
  - **Access keys** are for **programmatic access**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c3bb0672-ac60-4d5a-826c-e7d47e5b9fe3" />

- [x] **Root user vs IAM user (summary)**
  - **Root:** log in with the **email** used when you created the account; **full**, **unrestricted** access; some permissions **cannot** be restricted.
  - A few actions still **require root**, but once the account is running you mostly **do not need it**.
  - **Lock root away** and do not use it for daily work.
  - **IAM user:** has a **friendly name**; you log in with the account **alias** or **account ID**.
  - Permissions come from **permissions policies**.
  - If **no policies** are applied **directly** or via **groups**, the user has **no permissions**.
  - Enable permissions by assigning policies **directly**, or **preferably through a user group**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/13eea521-9f00-4216-942e-884ad51f9555" />

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. Hands-on IAM work comes in later **HOL** lessons.

### **Overview**

- [ ] This lesson explains IAM identities and authentication; there is no console walkthrough here.
- [ ] You will:
  - [ ] Distinguish **authentication** from **authorization**.
  - [ ] Recall **users**, **groups**, **roles**, and **policies**.
  - [ ] Remember that **new IAM users have no permissions by default**.
  - [ ] Plan to **lock away root** (strong password + **MFA**) and use IAM users for daily work.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

No terminal commands in this IAM theory lesson. Later HOL lessons use the console, CLI, and access keys.

```bash
# No commands in this topic; the lesson is IAM concepts only.
```

</details>

<details>
  <summary>Code</summary>

## Code

No application code in this lesson. The unique identifier for an IAM user is an **ARN**. Example shape:

```text
arn:aws:iam::123456789012:user/Andrea
```

- [x] **arn** — Amazon Resource Name
- [x] **aws** — AWS partition
- [x] **iam** — IAM service
- [x] **123456789012** — account number
- [x] **user** — resource type
- [x] **Andrea** — friendly name

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is AWS IAM, and why is it important?

<details>
<summary>Answer</summary>

- [x] **IAM** is **Identity and Access Management**.
- [x] It is the service used for **authentication** and **authorization**.
- [x] You need it to **securely connect** to an AWS account through the **console**, **CLI**, and **API**.

</details>

### Question 2: What three ways can you manage AWS?

<details>
<summary>Answer</summary>

- [x] The **Management Console**
- [x] The **command line interface (CLI)**
- [x] The **API** through **SDKs**

</details>

### Question 3: What is an IAM principal?

<details>
<summary>Answer</summary>

- [x] A **person** or **application** that makes a request for an **API action / operation** on an AWS **resource**.
- [x] All principals must be **authenticated** before they can send requests to AWS.

</details>

### Question 4: What is the difference between authentication and authorization?

<details>
<summary>Answer</summary>

- [x] **Authentication** proves you are who you say you are (for example, a **password**).
- [x] **Authorization** **allows** or **denies** access to resources.
- [x] **Policies** define what you are allowed to do.

</details>

### Question 5: After you authenticate, what does AWS do next?

<details>
<summary>Answer</summary>

- [x] AWS determines **what you are allowed to do**.
- [x] That includes authorizing **API actions** on AWS **resources**.

</details>

### Question 6: Give three example API actions mentioned in this lesson.

<details>
<summary>Answer</summary>

- [x] **RunInstances** on **EC2** — launch a virtual server
- [x] **GetBucket** — retrieve information about buckets
- [x] **CreateUser** — create a user in IAM

</details>

### Question 7: What are the four core IAM components?

<details>
<summary>Answer</summary>

- [x] **Users**
- [x] **User groups**
- [x] **Roles**
- [x] **Policies**

</details>

### Question 8: How do user groups help you manage permissions?

<details>
<summary>Answer</summary>

- [x] Put users with a **common job role** in a group.
- [x] Attach **one permissions policy** to the group.
- [x] Members **inherit** those permissions, so you manage one policy instead of many.

</details>

### Question 9: What are identity-based policies applied to?

<details>
<summary>Answer</summary>

- [x] **Users**
- [x] **Groups**
- [x] **Roles**

</details>

### Question 10: What is an IAM role?

<details>
<summary>Answer</summary>

- [x] An **identity** with permissions assigned via **policy**.
- [x] Used for **delegation**; you **assume** the role and take on those permissions.
- [x] Like putting on a **hat** (for example, a development hat vs an ops hat).

</details>

### Question 11: What is the root user, and what is the best practice for it?

<details>
<summary>Answer</summary>

- [x] Created with the **email address** you used when you created the account.
- [x] Has **full permissions**; you **cannot restrict most** of them.
- [x] **Do not use it** for daily work.
- [x] Set a **very strong password**, enable **MFA**, then **lock it away**.

</details>

### Question 12: How many IAM users can you create, and what permissions do they have by default?

<details>
<summary>Answer</summary>

- [x] Up to **5,000** individual user accounts.
- [x] They have **no permissions by default**.
- [x] They can log in if console access is enabled, but they **cannot do anything** until you apply permissions.

</details>

### Question 13: What is a friendly name, and what is an ARN?

<details>
<summary>Answer</summary>

- [x] A **friendly name** is a simple **text string** used to log in (for example, **Andrea**).
- [x] An **ARN** (**Amazon Resource Name**) is the **unique identifier** for that resource in AWS.
- [x] An IAM user ARN includes that it is an **IAM user**, the **account number**, and the **friendly name**.

</details>

### Question 14: How does an IAM user authenticate to the console vs the CLI and API?

<details>
<summary>Answer</summary>

- [x] **Console:** **username** and **password**, optionally **MFA**.
- [x] **CLI** and **API:** **access keys** (**access key ID** and **secret access key**).

</details>

### Question 15: What happens if a user belongs to multiple groups?

<details>
<summary>Answer</summary>

- [x] The user gains **multiple sets of permissions**.
- [x] Those permission sets are **combined**.

</details>

### Question 16: What are access keys, and what is STS used for?

<details>
<summary>Answer</summary>

- [x] An **access key ID** and **secret access key** are like a username and password for **programmatic access**.
- [x] They authenticate the **CLI** and **API** to the AWS API.
- [x] **AWS Security Token Service (STS)** generates **short-term credentials**.

</details>

### Question 17: When you log in as an IAM user, what do you supply besides the username?

<details>
<summary>Answer</summary>

- [x] The **alias** for the account **or** the **account ID**.
- [x] Plus the user’s credentials (password for the console).

</details>

### Question 18: How does an IAM user get permissions?

<details>
<summary>Answer</summary>

- [x] Through **permissions policies**.
- [x] Policies can be attached **directly** to the user or via **groups**.
- [x] If no policies apply, the user has **no permissions**.
- [x] Prefer assigning policies through a **user group**.

</details>

### Question 19: Which IAM identities can you create besides users, and what else can IAM enable?

<details>
<summary>Answer</summary>

- [x] **Roles**
- [x] **Federated users**
- [x] **Authentication for applications**

</details>

### Question 20: Besides policies and access keys, what two account-security features should you configure?

<details>
<summary>Answer</summary>

- [x] **Multi-factor authentication (MFA)**
- [x] **Password policies**

</details>

</details>

## Summary

**IAM** authenticates and authorizes **principals** (people or applications) before they can send **API** requests via the **console**, **CLI**, or **API/SDKs**. Core pieces are **users**, **groups**, **roles**, and **policies**. **Authenticate** first (prove who you are), then **authorization** (policies allow or deny actions on resources). **Identity-based policies** attach to users, groups, and roles; **roles** are **assumed**. **Root** has nearly unrestricted access—use a strong password and **MFA**, then **lock it away**. New IAM users have a **friendly name**, an **ARN**, and **no permissions by default**; grant access preferably via **groups**. Console login uses username/password (plus optional MFA); programmatic access uses **access keys**; **STS** issues **short-term credentials**.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [IAM identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
- [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [The AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
- [IAM identifiers (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)
- [IAM access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [Multi-factor authentication](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [Setting an account password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
