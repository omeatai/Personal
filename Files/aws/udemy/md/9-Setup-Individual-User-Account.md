# 9. Setup Individual User Account

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This **HOL** creates the **individual IAM user** you will use for the rest of the course. There are two user types: the **root user** (the signup **email**, **full and unrestricted** access—**do not** use it day to day) and an **IAM user** (a **friendly name** plus the **account ID or alias**, with permissions from an **IAM policy**). You create the IAM user **with no permissions**, confirm that default, then create an **admins** group with the AWS managed **AdministratorAccess** policy, add the user to the group, **sign out of root**, and sign back in as the IAM user.

## Detailed Explanation

- [x] **Two types of user**
  - **Root user:** created with the **email address** you specified when you created the AWS account.
  - Root has **full and unrestricted** access; it is very difficult to **remove** those permissions or privileges.
  - Root is a **very powerful** user; **best practice is not to use it**.
  - After the account exists: set a **really strong password**, **hide it away**, and **do not use root again**.
  - **IAM user:** a **friendly name** (for example **John**) plus the **account ID** or **alias**.
  - That is what you use to **sign in to the console**.
  - Apply permissions with an **IAM permissions policy**.
- [x] **Create the IAM user (still signed in as root)**
  - Open the **IAM** console (search for **IAM**).
  - **Users** → **Add users**.
  - Instructor username: **Neil** (use **your** name).
  - Select **Provide user access to the AWS Management Console**.
  - AWS recommends a **federated identity through IAM Identity Center**—**do not** use that option here.
  - Choose **create an IAM user**.
  - Specify a **custom password**.
  - **Do not** force a password change at next login.
  - Click **Next**.
  - You **can** add permissions now; **skip that**—click **Next**, then **Create user**.
- [x] **How this user signs in**
  - Use the **console sign-in URL**, or specify the **account alias** when signing in as an IAM user.
  - You also need the **username**.
  - Return to the **users** list.
- [x] **IAM users have no permissions by default (critical)**
  - Open the user: **no permissions policies** assigned.
  - **Groups:** **no groups** assigned.
  - The account can exist and sign in, but it **cannot do anything** until you grant permissions.
- [x] **Best way to grant permissions: a group**
  - **User groups** → **Create group**.
  - Instructor group name: **admins** (a very powerful group with **full administrator access**).
  - Search for **administrator** and select **AdministratorAccess**.
  - This is an **AWS managed** policy (pre-created by AWS).
  - Expand with the **plus** to see the **JSON** (**JavaScript Object Notation**).
  - This simple policy: **Effect** = **Allow**, **Action** = `*` (**wildcard** = all actions), **Resource** = `*` (all resources) → **allow everything**.
  - **Create group**.
  - Open the group → **Add users** → select the IAM user → **Add users**.
  - The user is now a **full administrative** user with **full access** to AWS.
- [x] **Sign out of root and sign in as the IAM user**
  - Top right → **Sign out**.
  - Log back in and choose **IAM user** (not **root user**).
  - Enter the **account ID** or **alias** (instructor: **DCT-Labs-AWS** — use **your** alias from the earlier lesson).
  - Click **Next**, then enter **username** and **password**.
  - Top right shows you as the IAM user (instructor: **Neil** at **DCT-Labs-AWS**).
  - This user has **full administrative permissions**.
  - Use this account for **all remaining lessons** in the course.

<details>
  <summary>Lab</summary>

## Lab

Stay signed in as **root** while you create the user and group. Use **your** username and **your** account alias. Skip Identity Center. Create the user **without** permissions first so you can see the empty default.

### **Overview**

- [ ] Create an IAM user with console access, prove it has **no** permissions, then grant admin via an **admins** group and sign in as that user.
- [ ] You will:
  - [ ] Create an IAM user with a **custom password** and **no** forced password change.
  - [ ] Confirm **no policies** and **no groups**.
  - [ ] Create **admins** with **AdministratorAccess** and **add the user** to the group.
  - [ ] **Sign out** of root and sign in as the IAM user with your **alias**.
- [ ] Success: the console shows **your-user@your-alias**, and you will use this user (not root) for the rest of the course.

### **Task 1: Open IAM as root**

- [ ] Sign in to the **AWS Management Console** as the **root user**.
- [ ] Search for **IAM** and open **Identity and Access Management**.
- [ ] You should see a dashboard similar to the instructor’s.

### **Task 2: Create the IAM user with no permissions**

- [ ] Choose **Users** → **Add users**.
- [ ] Enter a **username** (your name; instructor used **Neil**).
- [ ] Select **Provide user access to the AWS Management Console**.
- [ ] Skip **IAM Identity Center** / federated identity; choose **create an IAM user**.
- [ ] Set a **custom password**.
- [ ] **Deselect** the option to **change the password at next login**.
- [ ] Click **Next**.
- [ ] **Do not** add permissions yet.
- [ ] Click **Next**, then **Create user**.
- [ ] Note the **console sign-in URL** (or that you will use your **account alias** plus **username**).
- [ ] Return to the **users** list.

### **Task 3: Confirm the user has no permissions**

- [ ] Open the new user.
- [ ] Confirm there are **no permissions policies** assigned.
- [ ] Open **Groups** on the user and confirm there are **no groups**.
- [ ] Remember: IAM users have **no permissions by default**.

### **Task 4: Create the admins group and add the user**

- [ ] Open **User groups** → **Create group**.
- [ ] Name the group **admins**.
- [ ] Search for **administrator** and attach **AdministratorAccess**.
- [ ] Confirm it is an **AWS managed** (pre-created) policy.
- [ ] Expand the policy (**plus**) and confirm the JSON:
  - [ ] **Effect:** `Allow`
  - [ ] **Action:** `*` (wildcard — all actions)
  - [ ] **Resource:** `*` (all resources)
- [ ] Meaning: **allow everything**.
- [ ] Click **Create group**.
- [ ] Open the **admins** group.
- [ ] Click **Add users**, select your IAM user, then **Add users**.
- [ ] The user now has **full administrative** access.

<details>
<summary>AdministratorAccess (JSON)</summary>

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

</details>

### **Task 5: Sign out of root and sign in as the IAM user**

- [ ] Top right → **Sign out**.
- [ ] Choose **log back in**.
- [ ] Select **IAM user** (not **root user**).
- [ ] Enter your **account alias** or **account ID** (instructor: **DCT-Labs-AWS** — use yours).
- [ ] Click **Next**.
- [ ] Enter the **username** and **password**.
- [ ] Sign in.
- [ ] Top right should show **your-user@your-alias** (instructor: **Neil** at **DCT-Labs-AWS**).

Successfully created an IAM user, granted admin via the **admins** group, and signed in as that user. Use this account for the **remainder of the course**, not root.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

No terminal commands in this lesson. You create the user and group in the **IAM console** and sign in through the browser.

```bash
# No commands in this topic; the walkthrough is console-only.
```

</details>

<details>
  <summary>Code</summary>

## Code

**AdministratorAccess** is an **AWS managed** policy. `*` is a **wildcard**. **Effect Allow** plus **Action \*** plus **Resource \*** means **allow all actions on all resources**.

<details>
<summary>AdministratorAccess policy JSON</summary>

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

</details>

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the two types of user in this lesson?

<details>
<summary>Answer</summary>

- [x] The **root user**
- [x] An **IAM user**

</details>

### Question 2: How is the root user created, and what access does it have?

<details>
<summary>Answer</summary>

- [x] It is created with the **email address** you specified when you created the AWS account.
- [x] It has **full and unrestricted** access.
- [x] It is very difficult to **remove** those permissions or privileges.

</details>

### Question 3: What is the best practice for the root user after you create the account?

<details>
<summary>Answer</summary>

- [x] Set a **really strong password**.
- [x] **Hide** that password away.
- [x] **Do not use** the root user account again for daily work.

</details>

### Question 4: What do you use to sign in as an IAM user?

<details>
<summary>Answer</summary>

- [x] A **friendly name** (for example **John** or **Neil**)
- [x] Plus the **account ID** or **account alias**
- [x] Permissions come from an **IAM permissions policy**

</details>

### Question 5: Should you use IAM Identity Center in this lab?

<details>
<summary>Answer</summary>

- [x] **No.** AWS recommends a **federated identity through Identity Center**, but you **skip** that option here.
- [x] Create an **IAM user** instead.

</details>

### Question 6: How should you set the password when creating the IAM user in this lesson?

<details>
<summary>Answer</summary>

- [x] Specify a **custom password**.
- [x] **Do not** force a password change at next login.

</details>

### Question 7: Do you attach permissions while creating the user in this walkthrough?

<details>
<summary>Answer</summary>

- [x] **No.** Click **Next** without adding permissions, then **Create user**.
- [x] Permissions are added later through a **group**.

</details>

### Question 8: What is the most important default about a new IAM user?

<details>
<summary>Answer</summary>

- [x] The user has **no permissions by default**.
- [x] There are **no permissions policies** assigned.
- [x] There are **no groups** assigned.

</details>

### Question 9: What is the best way to assign permissions to the user in this lesson?

<details>
<summary>Answer</summary>

- [x] Through a **user group**.
- [x] Create the group, attach a policy, then **add the user** to the group.

</details>

### Question 10: What group and policy grant full admin in this lab?

<details>
<summary>Answer</summary>

- [x] Group name: **admins**
- [x] Policy: **AdministratorAccess**
- [x] It is an **AWS managed** policy (pre-created by AWS).

</details>

### Question 11: What does the AdministratorAccess JSON allow?

<details>
<summary>Answer</summary>

- [x] **Effect:** `Allow`
- [x] **Action:** `*` — **wildcard**, all actions
- [x] **Resource:** `*` — all resources
- [x] Meaning: **allow everything**.

</details>

### Question 12: After the group exists, how do you attach the user in this lesson?

<details>
<summary>Answer</summary>

- [x] Open the **admins** group.
- [x] Click **Add users**, select the IAM user, then **Add users**.

</details>

### Question 13: How do you switch from root to the IAM user after setup?

<details>
<summary>Answer</summary>

- [x] Top right → **Sign out**.
- [x] Log back in and choose **IAM user** (not **root user**).
- [x] Enter the **account alias** or **account ID**, then **username** and **password**.

</details>

### Question 14: What alias did the instructor type at IAM sign-in?

<details>
<summary>Answer</summary>

- [x] **DCT-Labs-AWS**
- [x] Use **your own** alias (or account ID), not his.

</details>

### Question 15: After you sign in as the IAM user, which account do you use for the rest of the course?

<details>
<summary>Answer</summary>

- [x] This **individual IAM user**.
- [x] It has **full administrative permissions**.
- [x] **Not** the **root** account.

</details>

### Question 16: In which language are IAM policies defined?

<details>
<summary>Answer</summary>

- [x] **JSON** (**JavaScript Object Notation**)

</details>

</details>

## Summary

**Root** is the signup **email** with **unrestricted** access—set a strong password and **stop using it**. Create an **IAM user** with a **friendly name**, **console access**, and a **custom password** (no forced change), and **do not** attach permissions at create time. New IAM users have **no policies and no groups**. Create an **admins** group, attach the AWS managed **AdministratorAccess** policy (`Allow` / `*` / `*`), **add the user** to the group, **sign out of root**, and sign in as the IAM user with your **account alias**. Use that admin IAM user for the **remainder of the course**. Skip **IAM Identity Center** for this lab.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [Create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [The AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
- [AWS managed policy: AdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html)
- [IAM JSON policy elements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)
- [How IAM users sign in to AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_sign-in.html)
- [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Using an alias for your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)
