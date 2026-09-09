[← Course contents](../../01.md)

# 8. Creating IAM Users and Groups

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This **HOL** creates an **IAM user group**, attaches **AdministratorAccess**, then creates an **IAM user** with **Management Console** access and adds that user to the group so they **inherit** admin permissions. You copy the one-time **console sign-in** details, log in from a **private window**, switch to **US East (N. Virginia)** if needed, and from this point use the **IAM user**—not **root**—for course labs. AWS recommends **IAM Identity Center** for SSO and multi-account access, but this course still uses **IAM** because it is **core to the exams**.

## Detailed Explanation

<details>
  <summary>Step 1 — Open IAM and plan what you will build</summary>

### Step 1 — Open IAM and plan what you will build

- [x] **Goal of this lesson**
  - Open the **IAM** service in the **AWS Management Console**.
  - Create a **user account** you can log in with.
  - Assign that user to a **group**.
  - Log in **as that user**.
  - A new account may have **no IAM users** yet.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8578f52c-b9ca-4e92-b178-35c55046c8df" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8a4c2821-1d16-4e5b-ad3d-37714e4de681" />

</details>

<details>
  <summary>Step 2 — Create the admins group first</summary>

### Step 2 — Create the admins group first

- [x] **Create the group first (permissions live on the group)**
  - The **user group** is how you assign permissions to the user.
  - Attach the policy to the **group**, add the **user** to the group, and the user **inherits** those permissions.
  - Instructor group name: **admins** (the user will be an administrative account).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0d36978a-c826-47ce-8340-0bbcbe145533" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f720ca0b-c4ca-499a-a37d-60a90bdb6d9b" />

</details>

<details>
  <summary>Step 3 — Attach AdministratorAccess and read the policy JSON</summary>

### Step 3 — Attach AdministratorAccess and read the policy JSON

- [x] **AdministratorAccess is a very powerful policy**
  - Attach **AdministratorAccess**.
  - IAM policies are written in **JSON** (**JavaScript Object Notation**).
  - Expanding the policy shows:
    - **Effect:** `Allow`
    - **Action:** `*` — a **wildcard** meaning **any / all actions**
    - **Resource:** `*` — another **wildcard**, **all resources**
  - Meaning: **allow all actions on all resources** (you can do anything).
  - That is what this course admin user needs.
  - Create the group (bottom right).

**AdministratorAccess** is an AWS managed policy. `*` is a **wildcard**. Together, **Effect Allow**, **Action \***, and **Resource \*** mean the identity can perform **any API action** on **any resource**.

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

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1ac90128-db2b-401f-a8ff-a93d1b0ae185" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d653e6bd-46d6-4a4f-8b44-2603a9bd040e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/be09e8ec-2bc2-418c-8d2c-bdd00e55281c" />

</details>

<details>
  <summary>Step 4 — Create the IAM user with console access</summary>

### Step 4 — Create the IAM user with console access

- [x] **Create the IAM user with console access**
  - Open **Users** → **Create user**.
  - Instructor username: **Neil** (use **your own** name).
  - Select **Provide user access to the AWS Management Console**.
  - That lets the user log in to the **console**, not only **programmatic** methods.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/425eafa6-48d6-4a02-b281-9c69771d6dc2" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cadb6265-778b-413f-aba4-d57c8f865bb6" />

- [x] **IAM user vs IAM Identity Center**
  - AWS now **recommends** **IAM Identity Center**.
  - Identity Center offers **single sign-on (SSO)**, access to **business applications**, and **multiple accounts**.
  - It is a useful service; AWS is encouraging people to use it.
  - This course covers Identity Center **later**.
  - You still need **IAM**: it is **core to the AWS exams**, and the instructor uses IAM for most of his accounts because he often does **not** need SSO.
  - For this lesson, choose **create an IAM user**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4941f3b2-9358-4531-bb6c-8514086dc073" />

- [x] **Password options**
  - Set a **custom password**.
  - **Deselect** the requirement to **change the password at next login**.
  - Click **Next**.

</details>

<details>
  <summary>Step 5 — Add the user to a group and copy the sign-in details</summary>

### Step 5 — Add the user to a group and copy the sign-in details

- [x] **Add the user to the group (prefer groups over direct policies)**
  - Add the user to the **admins** group.
  - Other options exist: **copy permissions from existing users**, or **attach policies directly**.
  - For **multiple users with the same permissions**, a **group** is better than attaching policies to every individual user—easier to **manage**.
  - Click **Next**, then **Create user**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7e17387e-0180-42f8-8b95-3e61b2711c09" />

- [x] **Console sign-in details (copy now)**
  - After create, AWS shows **console sign-in** details (the IAM sign-in URL from earlier, plus username and password).
  - **Copy** them so you can log in as this user.
  - Username example: **Neil**.
  - The **console password** is shown **once**; if you forget it you must **change it later**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f4568fab-4bfa-43b1-8c46-9f3c7d24c439" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7830a084-400a-42b9-919d-88537f6dd317" />

</details>

<details>
  <summary>Step 6 — Sign in as the IAM user and switch region</summary>

### Step 6 — Sign in as the IAM user and switch region

- [x] **Log in as the IAM user**
  - Return to the **user list**.
  - Open a **private / incognito window** so you can log in separately (root can stay signed in in the original window).
  - Paste the **IAM sign-in link**.
  - Enter **username** and **password**, then **Sign in**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4f348af4-598f-497f-bb03-2bdd7d22cbbb" />

- [x] **Region: N. Virginia for most course labs**
  - After sign-in the console may land in another region (instructor was put in **Ohio** after being in **US East**).
  - Switch back to **US East (N. Virginia) `us-east-1`**.
  - Most labs in this course run in **N. Virginia**.
  - It is **not always** essential, but often **required** depending on the **code** or **instructions** provided.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fdefa821-8fec-4d60-b22e-d9fd28e3999e" />

</details>

<details>
  <summary>Step 7 — Stop using root for everyday work</summary>

### Step 7 — Stop using root for everyday work

- [x] **From now on, do not use root**
  - You should see you are logged in as the IAM user (instructor: **Neil** at **DCT Lab training**).
  - This account has **full administrative permissions** for the **lab exercises** in this course.
  - From now on, log in with your **individual IAM user**, **not** the **root** account.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d99fe606-1ce6-4c3c-82a4-cd095799ae80" />

</details>

<details>
  <summary>Lab</summary>

## Lab

Stay signed in as **root** in one browser session while you create the group and user. Then sign in as the new IAM user in a **private window**. Use **your** username, not the instructor’s **Neil**.

### **Overview**

- [ ] Create an **admins** group with **AdministratorAccess**, create a console IAM user, and log in as that user.
- [ ] You will:
  - [ ] Open **IAM** and create a group named **admins**.
  - [ ] Attach **AdministratorAccess** (`Allow` / `*` / `*`).
  - [ ] Create an IAM user with **console access** and a **custom password**.
  - [ ] Add the user to **admins** and copy the **sign-in URL** and password.
  - [ ] Sign in from a **private window** and switch to **N. Virginia** if needed.
- [ ] Success: you are signed in as the IAM user with **admin** permissions, and you will use this user (not root) for later labs.

### **Task 1: Open IAM**

- [ ] Sign in to the **AWS Management Console** as **root** (this is the last root daily-use step).
- [ ] Search for **IAM** and open **Identity and Access Management**.
- [ ] Confirm there may be **no IAM users** yet.

### **Task 2: Create the admins group**

- [ ] Create a **user group** (do this **before** the user).
- [ ] Name the group **admins**.
- [ ] Attach the **AdministratorAccess** permissions policy.
- [ ] Expand the policy and confirm it is **JSON**:
  - [ ] **Effect:** `Allow`
  - [ ] **Action:** `*` (wildcard — all actions)
  - [ ] **Resource:** `*` (wildcard — all resources)
- [ ] Meaning: **allow all actions on all resources**.
- [ ] Click **Create group** (bottom right).

**AdministratorAccess (JSON)**

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


### **Task 3: Create the IAM user with console access**

- [ ] Open **Users** → **Create user**.
- [ ] Enter a **username** (your name; instructor used **Neil**).
- [ ] Select **Provide user access to the AWS Management Console**.
- [ ] When AWS recommends **IAM Identity Center**, choose **create an IAM user** instead (Identity Center comes later; IAM is what the exam needs here).
- [ ] Set a **custom password**.
- [ ] **Deselect** **Users must create a new password at next sign-in**.
- [ ] Click **Next**.

### **Task 4: Add the user to admins and create the user**

- [ ] Add the user to the **admins** group.
- [ ] Do **not** attach policies directly unless you have a reason; groups are easier when several people share the same permissions.
- [ ] Skip **copy permissions from existing users** unless you already have a template user.
- [ ] Click **Next**, then **Create user**.

### **Task 5: Copy console sign-in details**

- [ ] On the success page, copy:
  - [ ] The **console sign-in URL** (IAM user sign-in link from the earlier alias lesson)
  - [ ] The **username**
  - [ ] The **console password**
- [ ] Store the password now — you **will not** see it again; you would have to **reset** it later.
- [ ] Return to the **user list**.

### **Task 6: Sign in as the IAM user**

- [ ] Open a **private / incognito** browser window.
- [ ] Paste the **IAM sign-in URL**.
- [ ] Enter the **username** and **password**.
- [ ] Click **Sign in**.
- [ ] If the region is not **US East (N. Virginia) `us-east-1`** (for example **Ohio**), switch to **N. Virginia**.
- [ ] Confirm the console shows you as **your-user@your-account** (instructor: **Neil** at **DCT Lab training**).
- [ ] Confirm this user can perform admin work for later labs.

Successfully created the **admins** group and an IAM user with **AdministratorAccess**, and signed in as that user. From now on, use this **IAM user**, not **root**.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why create a user group before the IAM user?

<details>
<summary>Answer</summary>

- [x] The **group** is how you assign **permissions** to the user.
- [x] Attach the policy to the **group**, add the **user** to the group, and the user **inherits** those permissions.

</details>

### Question 2: What group name and policy did the instructor use for the admin account?

<details>
<summary>Answer</summary>

- [x] Group name: **admins**
- [x] Policy: **AdministratorAccess**

</details>

### Question 3: What does the AdministratorAccess JSON statement allow?

<details>
<summary>Answer</summary>

- [x] **Effect:** `Allow`
- [x] **Action:** `*` — **all actions** (wildcard)
- [x] **Resource:** `*` — **all resources** (wildcard)
- [x] Meaning: **allow all actions on all resources**.

</details>

### Question 4: What language are IAM policies written in?

<details>
<summary>Answer</summary>

- [x] **JSON** (**JavaScript Object Notation**)

</details>

### Question 5: What console option must you select so the IAM user can log in to the Management Console?

<details>
<summary>Answer</summary>

- [x] **Provide user access to the AWS Management Console**
- [x] Without it, the user would only have **programmatic** access methods.

</details>

### Question 6: What does AWS recommend instead of creating an IAM user, and why skip it here?

<details>
<summary>Answer</summary>

- [x] AWS recommends **IAM Identity Center**.
- [x] It provides **SSO**, access to **business applications**, and **multiple accounts**.
- [x] This course covers it **later**.
- [x] You still create an **IAM user** because **IAM is core to the exams**.

</details>

### Question 7: Why does the instructor still use IAM for most of his accounts?

<details>
<summary>Answer</summary>

- [x] He often does **not** need **single sign-on**.
- [x] IAM is still what he uses for most accounts in this course.

</details>

### Question 8: How should you set the new user’s password in this lab?

<details>
<summary>Answer</summary>

- [x] Set a **custom password**.
- [x] **Deselect** the requirement to **change the password at next login**.

</details>

### Question 9: Besides adding a user to a group, what other permission options exist?

<details>
<summary>Answer</summary>

- [x] **Copy permissions** from existing users.
- [x] **Attach policies directly** to the user.

</details>

### Question 10: Why prefer a group over attaching policies to every user?

<details>
<summary>Answer</summary>

- [x] When **multiple users** need the **same permissions**, one group policy is easier to **manage**.
- [x] You do not attach the same policy to every individual user account.

</details>

### Question 11: What must you copy after you create the user, and why immediately?

<details>
<summary>Answer</summary>

- [x] The **console sign-in URL**, **username**, and **console password**.
- [x] The password is shown **once**; if you forget it you must **change / reset** it later.

</details>

### Question 12: Why sign in from a private / incognito window?

<details>
<summary>Answer</summary>

- [x] So you can log in as the **IAM user** **separately**.
- [x] The original window can stay signed in as **root** while you test the new user.

</details>

### Question 13: Which region should you use for most labs in this course?

<details>
<summary>Answer</summary>

- [x] **US East (N. Virginia) `us-east-1`**
- [x] After IAM sign-in, the console may land elsewhere (instructor was put in **Ohio**).
- [x] Switch back; many labs require N. Virginia because of **course code** or **instructions**.

</details>

### Question 14: After this lesson, which account should you use for daily lab work?

<details>
<summary>Answer</summary>

- [x] Your **individual IAM user**.
- [x] **Not** the **root** account.
- [x] The IAM user has **full administrative permissions** for the course labs.

</details>

### Question 15: What is the permission inheritance path used in this lab?

<details>
<summary>Answer</summary>

- [x] **AdministratorAccess** is attached to the **admins** group.
- [x] The IAM user is a **member** of **admins**.
- [x] The user **inherits** admin permissions from the group.

</details>

### Question 16: What does a star (`*`) mean in an IAM policy?

<details>
<summary>Answer</summary>

- [x] It is a **wildcard**.
- [x] On **Action**, it means **any / all actions**.
- [x] On **Resource**, it means **all resources**.

</details>

</details>

## Summary

Create an **admins** group and attach **AdministratorAccess** (`Allow`, `Action *`, `Resource *` — all actions on all resources). Create an **IAM user** with **console access**, a **custom password**, and **no** forced password change, then add the user to **admins** so they **inherit** admin rights. Prefer **groups** over attaching policies to every user. Copy the **sign-in URL** and password **immediately** (the password is shown once). Sign in from a **private window**, switch to **N. Virginia (`us-east-1`)** if needed, and use this **IAM user**—not **root**—for remaining labs. Skip **IAM Identity Center** for now; IAM is still **core to the exams**.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [AWS managed policy: AdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html)
- [IAM JSON policy elements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)
- [How IAM users sign in to AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_sign-in.html)
- [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [IAM and AWS STS condition context keys (Action / Resource wildcards)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html)
