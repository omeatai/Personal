<details>
  <summary>Offensive Security Intro</summary>

## Introduction

Offensive Security is about thinking like an attacker to find weaknesses before real hackers do. In this TryHackMe room, you hack your first website in a safe and legal environment using FakeBank, a fake banking application, to see how ethical hackers operate.

## Detailed Explanation

- [x] **Think like a hacker**
  - Offensive Security means simulating a hacker's actions to find weaknesses
  - The room lets you practice ethical hacking against FakeBank in a controlled lab
- [x] **Starting the lab**
  - The room uses a virtual desktop to simulate a real system
  - A browser opens automatically and displays FakeBank, the target application
  - Your bank account number in FakeBank is **8881**
- [x] **Find hidden pages**
  - A common weakness is leaving hidden pages accessible (e.g. admin or transfer panels)
  - Use the terminal on the machine to run **dirb** (Dirbuster-style directory brute-forcing)
  - Lines in dirb output that start with `+` are pages that were found
  - Dirb finds two URLs on FakeBank: `/images` and `/bank-transfer`
- [x] **Attack the admin page**
  - The hidden admin panel at `/bank-transfer` lets you add money to an account
  - Open `http://fakebank.thm/bank-transfer` in the simulated browser (append `/bank-transfer` to the URL)
  - Use account number **8881** and deposit **$2000** (or more)
  - Return to your account page and confirm the balance is positive
  - When the balance turns positive, a green pop-up appears with the words **BANK-HACKED** (ALL CAPS)

<details>
  <summary>Lab</summary>

## Lab

This is the room's **FakeBank** walkthrough on the TryHackMe virtual desktop. Work only in that lab. Pause until the machine is on and the FakeBank browser tab is visible.

### **Overview**

- [ ] Practice offensive security against **FakeBank** in a legal lab.
- [ ] You will:
  - [ ] Start the virtual desktop and note account **8881**.
  - [ ] Use **dirb** to find hidden pages.
  - [ ] Open `/bank-transfer`, deposit funds, and confirm the balance.
- [ ] Success: the account page shows a positive balance and a green pop-up **BANK-HACKED**.

### **Task 1: Start the lab**

- [ ] Click **Start Machine** (or **Show Split View** if the desktop is hidden).
- [ ] Wait until the simulated browser opens **FakeBank**.
- [ ] Note your FakeBank account number: **8881**.

### **Task 2: Find hidden pages**

- [ ] Open the **Terminal** on the lab machine.
- [ ] Run directory brute-force against FakeBank:

```bash
dirb http://fakebank.thm
```

- [ ] In the output, treat lines that start with `+` as discovered pages.
- [ ] Confirm dirb reports `/images` and `/bank-transfer`.

<details>
<summary>Example dirb hits</summary>

```text
+ http://fakebank.thm/images
+ http://fakebank.thm/bank-transfer
```

</details>

### **Task 3: Use the transfer page**

- [ ] In the simulated browser, open `http://fakebank.thm/bank-transfer`.
- [ ] On the transfer form, enter:
  - [ ] Account number **8881**
  - [ ] Amount **$2000** (or more)
- [ ] Return to your account page and confirm the balance is positive.
- [ ] Read the green pop-up: **BANK-HACKED** (ALL CAPS).

Successfully completed the FakeBank lab when the balance is positive and **BANK-HACKED** is shown.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

Dirb is used to discover hidden directories and pages on a target website. Pass the target URL; any output lines starting with `+` indicate discovered pages.

```bash
dirb http://fakebank.thm
```

Example idea of what you are looking for: dirb reports existing paths such as `http://fakebank.thm/images` and `http://fakebank.thm/bank-transfer`. Use the hidden `/bank-transfer` path in the browser to continue the attack.

</details>

<details>
  <summary>Code</summary>

## Code

When the simulated browser opens the hidden transfer page, the request looks like this:

```http
GET /bank-transfer HTTP/1.1
Host: fakebank.thm

```

No application source is included in this room; the activity uses terminal commands (dirb) and the FakeBank web interface.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which term describes simulating a hacker's actions to find weaknesses?

<details>
<summary>Answer</summary>

- [x] Offensive Security

</details>

### Question 2: What is Defensive Security in contrast to Offensive Security?

<details>
<summary>Answer</summary>

- [x] Defensive Security focuses on protecting systems and responding to threats, rather than simulating attacker actions to find weaknesses.

</details>

### Question 3: What application do you target in this room?

<details>
<summary>Answer</summary>

- [x] FakeBank — a fake banking application in a safe, legal lab environment.

</details>

### Question 4: What is the bank account number in the FakeBank application?

<details>
<summary>Answer</summary>

- [x] 8881

</details>

### Question 5: Why might hidden pages on a website be a security risk?

<details>
<summary>Answer</summary>

- [x] They can leave sensitive functionality (e.g. admin or money-transfer panels) accessible if not properly restricted.

</details>

### Question 6: Which tool do you use in the terminal to find hidden pages on FakeBank?

<details>
<summary>Answer</summary>

- [x] dirb (Dirbuster-style directory brute-forcing)

</details>

### Question 7: What command runs dirb against FakeBank?

<details>
<summary>Answer</summary>

- [x] `dirb http://fakebank.thm`

</details>

### Question 8: How does dirb mark pages it has found in its output?

<details>
<summary>Answer</summary>

- [x] Lines that start with `+` indicate discovered pages.

</details>

### Question 9: Dirb found `http://fakebank.thm/images`. What is the other hidden URL?

<details>
<summary>Answer</summary>

- [x] http://fakebank.thm/bank-transfer

</details>

### Question 10: How do you open the hidden admin panel in the simulated browser?

<details>
<summary>Answer</summary>

- [x] Append `/bank-transfer` to the FakeBank URL in the browser.

</details>

### Question 11: What do you do on the `/bank-transfer` page to complete the hack?

<details>
<summary>Answer</summary>

- [x] Use account number 8881
- [x] Deposit $2000 (or more)
- [x] Return to your account page and confirm the balance is positive

</details>

### Question 12: When your balance turns positive, what appears and what is the answer flag?

<details>
<summary>Answer</summary>

- [x] A pop-up with green text
- [x] BANK-HACKED (ALL CAPS)

</details>

### Question 13: What is the main goal of Offensive Security as described in this room?

<details>
<summary>Answer</summary>

- [x] Think like an attacker to find weaknesses before real hackers do.

</details>

### Question 14: What environment does this room use so you can practice safely?

<details>
<summary>Answer</summary>

- [x] A virtual desktop that simulates a real system, with FakeBank opened in a browser.

</details>

### Question 15: After depositing money, where do you confirm success?

<details>
<summary>Answer</summary>

- [x] On your account page — confirm the balance is now positive and note the green pop-up text.

</details>

</details>

## Summary

This room introduces Offensive Security by having you think like a hacker against FakeBank. You start a virtual lab, note account **8881**, use **dirb** to find hidden pages (`/images` and `/bank-transfer`), abuse the exposed transfer panel to deposit funds, and capture the green flag **BANK-HACKED** when the balance turns positive.

## References

- [Offensive Security Intro – TryHackMe](https://tryhackme.com/room/offensivesecurityintro)
- [Gobuster (OJ Reeves)](https://github.com/OJ/gobuster)
- [dirb | Kali Tools](https://www.kali.org/tools/dirb/)
- [OWASP WSTG — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README)

</details>
