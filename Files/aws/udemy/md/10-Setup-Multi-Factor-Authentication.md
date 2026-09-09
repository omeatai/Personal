[← Course contents](../../01.md)

# 10. Setup Multi-Factor Authentication

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This lesson covers **IAM authentication methods** and **multi-factor authentication (MFA)**. **Username and password** (optionally plus an **MFA token**) authenticate you to the **Management Console**. **Access keys** (**access key ID** plus **secret access key**) are **long-term credentials** for the **CLI** and **API**. MFA adds **something you have** (a virtual authenticator app or a hardware token) to **something you know** (your password). AWS does **not** use biometrics (**something you are**). Enable MFA on the **root** account and on your **IAM user**. The hands-on walkthrough assigns a virtual MFA device to your IAM user, then proves console sign-in now requires a one-time code.

## Detailed Explanation

<details>
  <summary>Step 1 — Compare console and programmatic authentication</summary>

### Step 1 — Compare console and programmatic authentication

- [x] **Two ways to authenticate to AWS**
  - Example user: **John**.
  - **Management Console:** **username** and **password**.
  - Optionally supply an **MFA token** as well.
  - After authentication, IAM **authorizes** the operations John can perform in the console.
  - **CLI** and **API:** **access keys**, not the console password.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5f956b4d-de3c-40b9-842e-ff9946cea1ea" />

</details>

<details>
  <summary>Step 2 — Understand access keys as long-term credentials</summary>

### Step 2 — Understand access keys as long-term credentials

- [x] **Access keys (programmatic / long-term credentials)**
  - An access key has two parts: an **access key ID** and a **secret access key**.
  - Think of them as a **username and password** for programmatic use.
  - They are **long-term credentials**: you create them, they stay in the account, and you can use them while the key is **active**.
  - You must **download a copy** when you create the key; AWS will not show the secret again.
  - Use them with the **AWS CLI** or by calling the **API** directly (including SDKs).
  - **Access keys** = programmatic access; **username and password** = console access.

</details>

<details>
  <summary>Step 3 — Learn the factors that MFA adds</summary>

### Step 3 — Learn the factors that MFA adds

- [x] **What MFA adds (authentication factors)**
  - **Something you know:** your **password** — a secret you should not write down or share.
  - **Something you have:** a **physical device** in your possession.
    - A **smartphone** with an authenticator app that generates a token.
    - A **hardware token** / security key (cryptography on the device proves you have it).
  - **Something you are (biometrics):** retina scans, fingerprints — **not used in AWS**.
  - Even if someone learns your password, they still need the **second device**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f9c7ee48-a514-4b98-a60f-be6a7c70a541" />

</details>

<details>
  <summary>Step 4 — Choose between virtual and hardware MFA devices</summary>

### Step 4 — Choose between virtual and hardware MFA devices

- [x] **Virtual MFA vs hardware MFA**
  - **Virtual MFA device:** an authenticator app on a phone or computer (examples: **Google Authenticator**, **Authy**).
  - **Hardware:** **security keys** and **time-based one-time password (TOTP)** tokens.
  - The second factor is an **authentication code / token** from that device.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0ee82e3d-9371-4c30-9b7d-427820842842" />

</details>

<details>
  <summary>Step 5 — Apply MFA best practice to root, users, and the CLI</summary>

### Step 5 — Apply MFA best practice to root, users, and the CLI

- [x] **Best practice**
  - Enable MFA for the **root** account.
  - Enable MFA for **individual IAM user** accounts as well.
  - You are then less exposed if a password is guessed, leaked, or lost.
  - With MFA enabled, you must have the **physical device present** to sign in to the **console**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fd3566c9-76f5-4936-8ad7-cd568e2b3004" />

- [x] **MFA for CLI and API**
  - MFA can also protect **CLI** and **API** access.
  - That setup is covered **later in the course**; this lesson focuses on **console MFA**.

</details>

<details>
  <summary>Step 6 — Assign a virtual MFA device to your IAM user</summary>

### Step 6 — Assign a virtual MFA device to your IAM user

- [x] **HOL: assign MFA to your IAM user**
  - Sign in as your **individual IAM user** (not only as root).
  - The IAM dashboard may recommend **Add MFA** for **root** and for **yourself**.
  - Assign the device from the user’s **Security credentials** tab (you can also use the **Add MFA** button).
  - Choose an **authenticator app**, name the device (instructor: **AuthyPhone**), scan the **QR code**, then enter **two consecutive** MFA codes.
  - Sign out and sign back in: after password, AWS prompts for the **current MFA code**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5080b63f-f20e-4234-9002-4fc3243ef712" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/60bd8cb7-df86-4424-b410-df38d13d5ed5" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/56a6bee2-b4fa-489b-bd05-cd7d327cfd57" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f52487fa-bad5-4652-bbfd-1441552d6732" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/96b80976-e800-4aa2-8746-3c6bfa522d3c" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/79211840-3e76-425b-865e-e17007b08f6b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8b27bb8a-a0c8-4532-9cf4-509306320143" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7239a011-6978-49b1-a3d3-4cfa4500f154" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4ed28301-8d1b-48dd-96ff-1a7526c6b6cb" />

</details>

<details>
  <summary>Lab</summary>

## Lab

Stay signed in as your **individual IAM user**. Use **your** authenticator app and **your** one-time codes — the numbers in the video belong to the instructor and expire quickly. You can also enable MFA on **root**; this walkthrough does it for the IAM user.

### **Overview**

- [ ] Assign a **virtual MFA** device to your IAM user and prove console sign-in requires a second code.
- [ ] You will:
  - [ ] Open the IAM user → **Security credentials** → assign an MFA device.
  - [ ] Choose an **authenticator app**, name the device, and scan the **QR code**.
  - [ ] Enter **two consecutive** TOTP codes, then save.
  - [ ] **Sign out** and sign back in with username, password, **and** MFA code.
- [ ] Success: after password, the console asks for an MFA code, and you sign in with two-factor authentication.

### **Task 1: Open IAM as your IAM user**

- [ ] Sign in to the **AWS Management Console** as your **individual IAM user**.
- [ ] Search for **IAM** and open **Identity and Access Management**.
- [ ] Note the security recommendations if shown:
  - [ ] **Add MFA** for the **root user**.
  - [ ] **Add MFA** for your **IAM user**.
- [ ] You could click **Add MFA**, but this walkthrough goes through the **user** record instead.

### **Task 2: Start assigning an MFA device**

- [ ] Open **Users** and choose **your username**.
- [ ] Open the **Security credentials** tab.
- [ ] Choose **Assign MFA device** (or equivalent **assign / manage MFA** action).
- [ ] Select **Authenticator app** (examples: **Google Authenticator** or **Authy**).
- [ ] Give the device a name (instructor: **AuthyPhone** — use a name you will recognize).
- [ ] Note that **security keys** and **hardware tokens** are also options; this lab uses the app.
- [ ] Click **Next**.

### **Task 3: Register the authenticator app**

- [ ] Complete the three setup steps:
  - [ ] **Install** an authenticator app (for example **Google Authenticator** or **Authy**) on your phone or computer if you do not already have one.
  - [ ] **Show the QR code** on the AWS page and **scan** it with the app.
  - [ ] Or, if you cannot scan, **type the secret key** into the app instead.
- [ ] After the app is linked, it displays a **six-digit** code that changes on a timer.

### **Task 4: Enter two consecutive MFA codes**

- [ ] Type the **current** MFA code from the app into the **first** code box (instructor example: **414018** — use yours).
- [ ] Wait for that code to **expire**.
- [ ] Type the **next** code into the **second** code box (instructor example: **561486** — use yours).
- [ ] Confirm / **Add MFA**.
- [ ] The virtual MFA device is now assigned to the IAM user.

### **Task 5: Prove MFA at console sign-in**

- [ ] **Sign out** of the console.
- [ ] Sign in again as an **IAM user**.
- [ ] Enter your **account ID** or **alias**, **username**, and **password**.
- [ ] AWS now prompts for the **MFA code**.
- [ ] Enter the **current** code from the app (instructor example: **820902** — use yours) and submit.
- [ ] You should be signed in again, now with **two-factor authentication**.

Successfully assigned a virtual MFA device to the IAM user and signed in with username, password, and MFA code.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What credentials authenticate you to the AWS Management Console?

<details>
<summary>Answer</summary>

- [x] A **username** and **password**.
- [x] Optionally, an **MFA token** as well.

</details>

### Question 2: What credentials authenticate you to the CLI and API?

<details>
<summary>Answer</summary>

- [x] **Access keys**.
- [x] They are used for **programmatic access**, not console login.

</details>

### Question 3: What two values make up an access key?

<details>
<summary>Answer</summary>

- [x] An **access key ID**.
- [x] A **secret access key**.
- [x] Together they work like a **username and password** for the API.

</details>

### Question 4: Why are access keys called long-term credentials?

<details>
<summary>Answer</summary>

- [x] You create them and they are **stored in the account**.
- [x] You can use them **as long as the key remains active**.
- [x] You must **download a copy** when you create the key so you can use it yourself.

</details>

### Question 5: What is the difference between console credentials and access keys?

<details>
<summary>Answer</summary>

- [x] **Username and password** are for **Management Console** access.
- [x] **Access keys** are for **CLI** and **API** (programmatic) access.

</details>

### Question 6: What are the three classic authentication factors, and which does AWS MFA use?

<details>
<summary>Answer</summary>

- [x] **Something you know** — a **password**.
- [x] **Something you have** — a phone app or hardware token.
- [x] **Something you are** — biometrics (retina, fingerprint).
- [x] AWS MFA uses **something you know** plus **something you have**.
- [x] AWS does **not** use biometrics for this.

</details>

### Question 7: How does MFA help if someone learns your password?

<details>
<summary>Answer</summary>

- [x] They still need the **second factor** — the physical device or authenticator.
- [x] You must have that device **present** to complete console sign-in.

</details>

### Question 8: What is a virtual MFA device?

<details>
<summary>Answer</summary>

- [x] An **authenticator app** on a smartphone or computer.
- [x] Examples from the lesson: **Google Authenticator** and **Authy**.
- [x] It generates a **time-based one-time password (TOTP)** code.

</details>

### Question 9: What hardware MFA options does the lesson mention?

<details>
<summary>Answer</summary>

- [x] **Security keys**.
- [x] **Time-based one-time password (TOTP)** hardware tokens.

</details>

### Question 10: For which identities is MFA a best practice?

<details>
<summary>Answer</summary>

- [x] The **root** account.
- [x] **Individual IAM user** accounts as well.

</details>

### Question 11: Can you use MFA with the CLI and API in this lesson?

<details>
<summary>Answer</summary>

- [x] MFA **can** be used with the **CLI** and **API**.
- [x] That configuration is covered **later in the course**.
- [x] This lesson sets up MFA for **console** sign-in.

</details>

### Question 12: From which IAM page do you assign an MFA device to yourself in the lab?

<details>
<summary>Answer</summary>

- [x] Open your **IAM user**.
- [x] Go to **Security credentials**.
- [x] Choose **Assign MFA device**.
- [x] You could also use the dashboard **Add MFA** button; the lab uses the user record.

</details>

### Question 13: What three steps register an authenticator app?

<details>
<summary>Answer</summary>

- [x] **Install** the authenticator app on your phone or computer.
- [x] **Scan the QR code** on the AWS page (or type the **secret key**).
- [x] Enter **MFA codes** from the app to prove the device is linked.

</details>

### Question 14: Why does AWS ask for two MFA codes when you assign the device?

<details>
<summary>Answer</summary>

- [x] You enter the **current** code, wait for it to **expire**, then enter the **next** code.
- [x] Two consecutive TOTP codes prove the authenticator is in sync with AWS.

</details>

### Question 15: What extra prompt appears after MFA is enabled when you sign in to the console?

<details>
<summary>Answer</summary>

- [x] After **account ID** (or alias), **username**, and **password**, AWS asks for the **MFA code**.
- [x] You type the **current** code from the authenticator and submit.

</details>

### Question 16: After this lab, what authentication do you use for console access?

<details>
<summary>Answer</summary>

- [x] **Two-factor authentication**.
- [x] Password (**something you know**) plus MFA code from the device (**something you have**).

</details>

### Question 17: Should you reuse the MFA codes shown in the video?

<details>
<summary>Answer</summary>

- [x] **No.** Those codes belong to the **instructor’s** authenticator and expire in seconds.
- [x] Always use the **current** codes from **your** app.

</details>

</details>

## Summary

**Console** access uses **username and password** (plus optional **MFA**). **CLI** and **API** access use **access keys** (**access key ID** + **secret access key**) — **long-term** programmatic credentials you must **download** when created. MFA adds **something you have** (virtual app such as **Google Authenticator** / **Authy**, or a **security key** / TOTP hardware token) to **something you know**. AWS does **not** use biometrics. Enable MFA on **root** and on **IAM users**. In the lab, assign an **authenticator app** from **Security credentials**, scan the **QR code**, enter **two consecutive** codes, then sign out and sign back in with the extra MFA prompt.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [AWS multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [Assign an MFA device in the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable.html)
- [Enable a virtual MFA device (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)
- [IAM user passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords.html)
- [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [Configure MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)
