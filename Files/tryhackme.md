# TRYHACKME by Ifeanyi Omeata | [ONLINE](https://tryhackme.com/paths)

[Back to Personal Page](../README.md)

## A. PRE-SECURITY COURSE

### 1-Introduction to Cyber Security

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

### **Task 3: Use the transfer page**

- [ ] In the simulated browser, open `http://fakebank.thm/bank-transfer`.
- [ ] Use account number **8881**.
- [ ] Deposit **$2000** (or more).
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

No code sections in this room; the activity uses terminal commands (dirb) and the FakeBank web interface only.

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

<details>
  <summary>Defensive Security Intro</summary>

## Introduction

Defensive security is about defending and securing devices and systems by detecting and investigating attacks, then responding before damage occurs. Unlike offensive security, you do not attack systems—you monitor and protect them. In this TryHackMe room, you help apprentice SOC analyst Joe use a monitoring dashboard to spot suspicious traffic, identify the attack, and contain it against FakeBank.

## Detailed Explanation

- [x] **Think like a Defender**
  - Defensive security is the process of defending and securing devices and systems
  - Focus areas: detecting attacks, investigating them, and responding before damage occurs
  - Contrast with offensive security: defenders monitor and protect; they do not attack systems
- [x] **Detect Suspicious Activity**
  - Joe is an apprentice SOC analyst on his first solo shift
  - Real SOC analysts use monitoring dashboards to separate normal activity from suspicious behaviour
  - Lab steps:
    - Open the monitoring dashboard
    - Review recent alerts
    - Identify the suspicious source IP
  - Monitoring tools show what activity is taking place on computing devices so defenders can confirm legitimacy and investigate the rest
  - Suspicious source IP generating the traffic: **32.122.195.63**
- [x] **Identify the Attack**
  - Knowing something is wrong is only half the battle—you must determine what the attacker is trying to do
  - Lab steps:
    - Investigate the attack that has occurred
    - View the "URL Discovery Attempts" list
    - Look at the latest "URL Discovery Attempts" entry
  - The dashboard history shows the attacker rapidly trying many attempts to access hidden pages
  - Once you know the attacker's goal, you can stop them and fix the weakness that allowed the attack
  - Latest URL the attacker tried to find: **https://fakebank.com/admin**
- [x] **Stop the Attack (containment)**
  - Immediate priority in defensive security is **containment**—stopping the attack while it is happening to protect the organisation
  - Joe has already completed some security updates; you complete the last action
  - Lab steps:
    - Review the security actions (two already done for you)
    - Block the attacker's IP **32.122.195.63** via "Add Firewall Rule"
    - Select **BLOCK** from the dropdown and press **Apply**
  - Measures this monitoring tool supports:
    - **Blocking the IP address** — prevents the attacker's device from accessing systems entirely (good immediate step)
    - **Applying rate limiting** — limits connections in a given time for everyone; useful when the attacker rapidly hits many pages
    - **Updating security rules** — tightens access controls to sensitive pages the attacker slipped through
  - Success flag: **THM{FAKEBANK-SECURED}**

<details>
  <summary>Lab</summary>

## Lab

This is the room's **SOC monitoring dashboard** walkthrough (View Site). You help apprentice analyst Joe detect, identify, and contain an attack on FakeBank.

### **Overview**

- [ ] Detect suspicious traffic, identify the attacker's goal, and contain it.
- [ ] You will:
  - [ ] Open the monitoring dashboard and review recent alerts.
  - [ ] Identify the suspicious source IP and the latest URL discovery attempt.
  - [ ] Block the attacker with a firewall rule.
- [ ] Success: the attack is contained and the flag **THM{FAKEBANK-SECURED}** appears.

### **Task 1: Detect suspicious activity**

- [ ] Open the **monitoring dashboard**.
- [ ] Review **recent alerts**.
- [ ] Identify the suspicious source IP: **32.122.195.63**.

### **Task 2: Identify the attack**

- [ ] Open the **URL Discovery Attempts** list.
- [ ] Read the **latest** URL Discovery Attempts entry.
- [ ] Confirm the latest URL the attacker tried: **https://fakebank.com/admin**.

### **Task 3: Contain the attack**

- [ ] Review the security actions (two are already done).
- [ ] Under **Add Firewall Rule**, enter IP **32.122.195.63**.
- [ ] Select **BLOCK** from the dropdown.
- [ ] Press **Apply**.
- [ ] Confirm the success flag: **THM{FAKEBANK-SECURED}**.

Successfully contained the FakeBank attack by blocking **32.122.195.63**.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room uses an interactive monitoring dashboard in the browser (View Site). There are no primary command-line tools; investigation and response happen through the SOC-style UI (alerts, URL discovery list, and firewall rules).

```bash
# No primary terminal commands in this defensive dashboard lab.
```

</details>

<details>
  <summary>Code</summary>

## Code

No code sections in this room; the activity uses the monitoring dashboard and firewall rule controls only.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the main goal of defensive security?

<details>
<summary>Answer</summary>

- [x] Detect and respond to attacks

</details>

### Question 2: How does defensive security differ from offensive security?

<details>
<summary>Answer</summary>

- [x] Defensive security monitors and protects systems
- [x] Offensive security attacks or simulates attacks to find flaws
- [x] Defenders do not attack systems; they detect, investigate, and respond

</details>

### Question 3: What is defensive security defined as in this room?

<details>
<summary>Answer</summary>

- [x] The process of defending and securing devices and systems

</details>

### Question 4: Who is Joe in this room's scenario?

<details>
<summary>Answer</summary>

- [x] An apprentice SOC analyst on his first solo shift

</details>

### Question 5: Why do SOC analysts use monitoring dashboards?

<details>
<summary>Answer</summary>

- [x] To separate normal activity from suspicious behaviour
- [x] To see what activity is taking place on computing devices
- [x] To confirm legitimate activity and investigate what looks suspicious

</details>

### Question 6: Which source IP address generates the suspicious traffic?

<details>
<summary>Answer</summary>

- [x] 32.122.195.63

</details>

### Question 7: What three steps do you take to detect suspicious activity in the lab?

<details>
<summary>Answer</summary>

- [x] Open the monitoring dashboard
- [x] Review recent alerts
- [x] Identify the suspicious source IP

</details>

### Question 8: After spotting suspicious activity, what must Joe figure out next?

<details>
<summary>Answer</summary>

- [x] What the attacker is actually trying to do

</details>

### Question 9: Where do you look to see what the attacker is searching for on the site?

<details>
<summary>Answer</summary>

- [x] The "URL Discovery Attempts" list
- [x] Specifically the latest "URL Discovery Attempts" entry

</details>

### Question 10: What behaviour does the dashboard show about the attacker's URL attempts?

<details>
<summary>Answer</summary>

- [x] Many attempts to access hidden pages
- [x] Attempts happening very quickly

</details>

### Question 11: What is the latest URL the attacker tried to find?

<details>
<summary>Answer</summary>

- [x] https://fakebank.com/admin

</details>

### Question 12: What is the immediate priority in defensive security once you know who the attacker is and what they want?

<details>
<summary>Answer</summary>

- [x] Containment — stopping the attack while it is happening to protect the organisation

</details>

### Question 13: How do you block the attacker in the practical lab?

<details>
<summary>Answer</summary>

- [x] Add the IP 32.122.195.63 into the "Add Firewall Rule" textbox
- [x] Select BLOCK from the dropdown
- [x] Press Apply

</details>

### Question 14: What does blocking the IP address achieve?

<details>
<summary>Answer</summary>

- [x] Prevents the attacker's device from accessing our systems entirely
- [x] It is a good immediate containment step

</details>

### Question 15: Why is rate limiting effective against this attack?

<details>
<summary>Answer</summary>

- [x] The attacker was rapidly accessing many pages at once
- [x] Rate limiting limits how many connections are possible in a given time
- [x] That can reduce overload from rapid probing

</details>

### Question 16: What does updating security rules do in this context?

<details>
<summary>Answer</summary>

- [x] Tightens access controls to sensitive pages the attacker was able to slip through

</details>

### Question 17: What flag appears when the attack is successfully stopped?

<details>
<summary>Answer</summary>

- [x] THM{FAKEBANK-SECURED}

</details>

### Question 18: After containment, what should defenders still do according to the room?

<details>
<summary>Answer</summary>

- [x] Investigate the finer details
- [x] Fix any vulnerabilities that allowed the attack in the first place

</details>

</details>

## Summary

This room introduces defensive security by having you think like a defender with SOC analyst Joe. You use a monitoring dashboard to find the suspicious source IP **32.122.195.63**, identify URL discovery toward **https://fakebank.com/admin**, and contain the attack by blocking that IP with a firewall rule. Success yields the flag **THM{FAKEBANK-SECURED}**. Core idea: detect and respond—monitor, investigate, then contain before damage spreads.

## References

- [Defensive Security Intro – TryHackMe](https://tryhackme.com/room/defensivesecurityintro)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide](https://csrc.nist.gov/pubs/sp/800/61/r2/final)

</details>

<details>
  <summary>Careers in Cyber</summary>

## Introduction

Cyber security careers are in high demand and often offer high salaries. Roles span offensive work (pentesting and reporting vulnerabilities) through defensive work (defending against and investigating attacks). This TryHackMe room explains why people enter cyber, outlines major job roles and responsibilities, and links learning paths and career guides so you can start building skills toward a target role.

## Detailed Explanation

- [x] **Why get a career in cyber**
  - **High pay** — security jobs often have high starting salaries
  - **Exciting** — work can include legally hacking systems or defending against cyber attacks
  - **Be in demand** — there are over 3.5 million unfilled cyber positions
  - The room helps you break in by covering roles and linking learning paths for skill building
- [x] **Security Analyst**
  - Responsible for maintaining the security of an organisation's data
  - Builds security measures across organisations to protect against attacks
  - Explores and evaluates company networks for actionable data and recommendations for engineers
  - Works with stakeholders to understand security requirements and the security landscape
  - Responsibilities:
    - Analyse cyber security across the company with stakeholders
    - Compile ongoing reports on network safety, issues, and responses
    - Develop security plans using research on new attack tools, trends, and cross-team measures
  - Learning Paths: Pre Security, Cyber Security 101, SOC Level 1
  - Career Guides: Becoming a Cyber Security Analyst; How to Become a Level 1 SOC Analyst; A Day in the Life of a SOC Analyst; The Ultimate SOC L1 Analyst Interview Guide; From Student to SOC Analyst: Hayden’s Success Story
- [x] **Security Engineer**
  - Designs, monitors, and maintains security controls, networks, and systems to help prevent cyberattacks
  - Develops and implements solutions using threat and vulnerability data (often from other security staff)
  - Works across web application attacks, network threats, and evolving tactics
  - Goal: retain and adopt measures that mitigate attack and data-loss risk
  - Responsibilities:
    - Test and screen security measures across software
    - Monitor networks and reports to update systems and mitigate vulnerabilities
    - Identify and implement systems needed for optimal security
  - Learning Paths: SOC Level 1, JR Penetration Tester, Offensive Pentesting
  - Career Guides: Becoming a Security Engineer; How to Become a Security Engineer; A Day in the Life of a Security Engineer; Preparing for a Security Engineering Interview; Becoming a Security Engineer: Richárd’s Success Story
- [x] **Incident Responder**
  - Identifies and mitigates attacks while an attacker’s operations are still unfolding
  - Responds productively to breaches; creates plans, policies, and protocols for during and after incidents
  - Often high-pressure: assessments and responses happen in real time as attacks unfold
  - Metrics: **MTTD** (meantime to detect), **MTTA** (meantime to acknowledge), **MTTR** (meantime to recover)
  - Aim: swift effective response, protect financial standing, avoid negative breach impact; protect data, reputation, and finances
  - Responsibilities:
    - Develop and adopt a thorough, actionable incident response plan
    - Maintain strong security best practices and support IR measures
    - Post-incident reporting and preparation for future attacks using learnings
  - Learning Path: SOC Level 1
- [x] **Digital Forensics Examiner**
  - Uses digital forensics to investigate incidents and crimes
  - Law-enforcement focus: collect and analyse evidence to help solve crimes—charge the guilty and exonerate the innocent
  - Corporate/defence focus: analyse incidents such as policy violations
  - Responsibilities:
    - Collect digital evidence while observing legal procedures
    - Analyse digital evidence to answer case-related questions
    - Document findings and report on the case
- [x] **Malware Analyst**
  - Analyses all types of malware to learn how they work and what they do
  - Studies suspicious programs, discovers behaviour, and writes reports
  - Sometimes called a reverse-engineer: convert compiled programs from machine language to readable low-level code
  - Needs a strong programming background, especially assembly and C
  - Goal: learn all activities a malicious program carries out, how to detect it, and report findings
  - Responsibilities:
    - Static analysis of malicious programs (reverse-engineering)
    - Dynamic analysis by observing samples in a controlled environment
    - Document and report all findings
- [x] **Penetration Tester**
  - Tests technology products for security loopholes; also called pentesting or ethical hacking
  - Tests security of systems and software by uncovering flaws through systemised hacking
  - Exploits vulnerabilities to evaluate risk so the company can fix issues before real attacks
  - Responsibilities:
    - Conduct tests on computer systems, networks, and web-based applications
    - Perform security assessments, audits, and analyse policies
    - Evaluate and report insights with recommended actions for attack prevention
  - Learning Paths: Jr Penetration Tester, Offensive Pentesting
  - Career Guides: Becoming a Penetration Tester; How to Become a Penetration Tester; Preparing for a Junior Penetration Tester Interview; From IT Support to Pentester: Tom’s Success Story
- [x] **Red Teamer**
  - Plays the adversary: attacks an organisation and gives feedback from an enemy’s perspective
  - Similar to pentesters but more targeted: tests detection and response, not just finding many vulns
  - Imitates cyber criminals: emulate malicious attacks, retain access, avoid detection
  - Assessments can run up to a month, typically by a team external to the company
  - Best suited to organisations with mature security programs
  - Responsibilities:
    - Emulate a threat actor to uncover exploitable vulnerabilities, maintain access, and avoid detection
    - Assess security controls, threat intelligence, and incident response procedures
    - Evaluate and report insights with actionable data to avoid real-world instances
  - Learning Paths: JR Penetration Tester, Offensive Pentesting, Red Teamer
  - Career Guides: Red Teaming: Job Roles, Salaries & Opportunities

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. The room is a career map (roles, learning paths, and guides), not a machine or View Site walkthrough.

### **Overview**

- [ ] Review the role descriptions and pick a target path.
- [ ] You will:
  - [ ] Compare analyst, engineer, IR, forensics, malware, pentest, and red-team work.
  - [ ] Note the TryHackMe learning paths listed for the role you want.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room is informational and career-focused. It does not centre on specific terminal commands; later learning paths introduce hands-on labs and CLI work.

```bash
# No primary terminal commands for this careers overview room.
```

</details>

<details>
  <summary>Code</summary>

## Code

No code sections in this room; the focus is understanding cyber security job roles, responsibilities, learning paths, and career resources.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why are cyber security careers considered attractive?

<details>
<summary>Answer</summary>

- [x] High pay — jobs in security often have high starting salaries
- [x] Exciting — work can include legally hacking systems or defending against cyber attacks
- [x] Be in demand — over 3.5 million unfilled cyber positions

</details>

### Question 2: What two broad sides of cyber security work does this room contrast?

<details>
<summary>Answer</summary>

- [x] **Offensive** — pentesting (hacking machines and reporting vulnerabilities)
- [x] **Defensive** — defending against and investigating cyberattacks

</details>

### Question 3: What is a Security Analyst mainly responsible for?

<details>
<summary>Answer</summary>

- [x] Maintaining the security of an organisation’s data
- [x] Exploring and evaluating company networks
- [x] Providing actionable recommendations for preventative measures

</details>

### Question 4: Name three responsibilities of a Security Analyst.

<details>
<summary>Answer</summary>

- [x] Working with stakeholders to analyse cyber security throughout the company
- [x] Compiling ongoing reports about network safety, issues, and responses
- [x] Developing security plans based on research into new attack tools and trends

</details>

### Question 5: Which TryHackMe learning paths are suggested for a Security Analyst?

<details>
<summary>Answer</summary>

- [x] Pre Security
- [x] Cyber Security 101
- [x] SOC Level 1

</details>

### Question 6: What is the primary focus of a Security Engineer?

<details>
<summary>Answer</summary>

- [x] Design, monitor, and maintain security controls, networks, and systems to help prevent cyberattacks

</details>

### Question 7: What kinds of attacks do Security Engineers work across?

<details>
<summary>Answer</summary>

- [x] Web application attacks
- [x] Network threats
- [x] Evolving trends and tactics

</details>

### Question 8: Which learning paths are suggested for a Security Engineer?

<details>
<summary>Answer</summary>

- [x] SOC Level 1
- [x] JR Penetration Tester
- [x] Offensive Pentesting

</details>

### Question 9: What does an Incident Responder do while an attack is still unfolding?

<details>
<summary>Answer</summary>

- [x] Identifies and mitigates attacks while the attacker’s operations are still underway
- [x] Creates plans, policies, and protocols for during and after incidents
- [x] Responds under pressure in real time

</details>

### Question 10: What do MTTD, MTTA, and MTTR stand for?

<details>
<summary>Answer</summary>

- [x] **MTTD** — meantime to detect
- [x] **MTTA** — meantime to acknowledge
- [x] **MTTR** — meantime to recover

</details>

### Question 11: What is the core work of a Digital Forensics Examiner?

<details>
<summary>Answer</summary>

- [x] Using digital forensics to investigate incidents and crimes
- [x] Collecting digital evidence while observing legal procedures
- [x] Analysing evidence and documenting/reporting findings

</details>

### Question 12: How can a Digital Forensics Examiner’s context differ between law enforcement and company defence?

<details>
<summary>Answer</summary>

- [x] **Law enforcement** — collect and analyse evidence to help solve crimes (charge the guilty, exonerate the innocent)
- [x] **Company defence** — use forensic skills to analyse incidents such as policy violations

</details>

### Question 13: Why is a Malware Analyst sometimes called a reverse-engineer?

<details>
<summary>Answer</summary>

- [x] Their core task is converting compiled programs from machine language to readable code
- [x] Usually in a low-level language
- [x] They need strong programming skills, especially assembly and C

</details>

### Question 14: What are the two main analysis types a Malware Analyst performs?

<details>
<summary>Answer</summary>

- [x] **Static analysis** — reverse-engineering malicious programs
- [x] **Dynamic analysis** — observing malware activities in a controlled environment

</details>

### Question 15: What is a Penetration Tester responsible for?

<details>
<summary>Answer</summary>

- [x] Testing technology products for security loopholes
- [x] Uncovering flaws and vulnerabilities through systemised hacking
- [x] Evaluating risk and reporting insights so issues can be fixed before real attacks

</details>

### Question 16: Which learning paths are suggested for a Penetration Tester?

<details>
<summary>Answer</summary>

- [x] Jr Penetration Tester
- [x] Offensive Pentesting

</details>

### Question 17: How does a Red Teamer differ from a typical Penetration Tester?

<details>
<summary>Answer</summary>

- [x] **Penetration Tester** — uncover many vulnerabilities across systems to keep cyber-defence in good standing
- [x] **Red Teamer** — more targeted; tests the company’s detection and response capabilities
- [x] Red teamers emulate malicious attacks, retain access, and avoid detection

</details>

### Question 18: Why are Red Team assessments often best suited to organisations with mature security programs?

<details>
<summary>Answer</summary>

- [x] They test detection and response capabilities that assume monitoring and IR processes already exist
- [x] Assessments can run for up to a month and are typically run by an external team

</details>

### Question 19: Which learning paths are suggested for a Red Teamer?

<details>
<summary>Answer</summary>

- [x] JR Penetration Tester
- [x] Offensive Pentesting
- [x] Red Teamer

</details>

### Question 20: What is the overall aim of incident response metrics and practice described in the room?

<details>
<summary>Answer</summary>

- [x] Achieve a swift and effective response
- [x] Retain financial standing and avoid negative breach implications
- [x] Protect the company’s data, reputation, and financial standing from cyber attacks

</details>

</details>

## Summary

Careers in Cyber explains why security work is high-pay, exciting, and in demand (over 3.5 million unfilled roles), then surveys major roles: Security Analyst, Security Engineer, Incident Responder, Digital Forensics Examiner, Malware Analyst, Penetration Tester, and Red Teamer. For each role you get core purpose, responsibilities, and (where listed) TryHackMe learning paths and career guides to start building the right skills.

## References

- [Careers in Cyber – TryHackMe](https://tryhackme.com/room/careersincyber)
- [NICE Framework Resource Center (NIST)](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center)
- [NIST SP 800-181 Rev. 1 — Workforce Framework for Cybersecurity](https://csrc.nist.gov/pubs/sp/800/181/r1/final)
- [CISA cybersecurity career resources](https://www.cisa.gov/cybersecurity-career-resources)

</details>

## 2-Computer Fundamentals

<details>
  <summary>Inside a Computer System</summary>

## Introduction

Before securing systems, you need to understand what you are securing. This TryHackMe room is the first in the Computer Fundamentals module and uses a castle analogy: you cannot defend a castle you have never seen. You learn the building blocks of a computer, how they connect, and what happens from power-on to a running operating system—kept at a fundamentals level without deep jargon.

**Learning objectives:** recognize and understand the functions of various computing components.

## Detailed Explanation

- [x] **Why fundamentals matter**
  - Defending without understanding components is like defending an unseen castle
  - You need the layout (where things live), who enters and how, and who can move or change “treasure”
  - After this room you should have a general idea of how components interact to serve users
- [x] **Shared building blocks**
  - Nearly every computer system includes the same core parts, each with its own job
  - The room maps PC components to a human-body analogy (skeleton/nerves, brain, short-term memory, etc.)
  - Interactive static site: identify components to earn the flag `THM{4llpccomp0n3nts1d3nt1f13d}`
- [x] **Motherboard**
  - Like the skeleton and nervous system: holds components and connects them
  - Typical desktop board: CPU socket, RAM slots, expansion slots, ports
  - Every other component plugs into or connects through the motherboard
- [x] **CPU (Central Processing Unit)**
  - Comparable to part of the brain: continuously executes instructions
  - Modern CPUs have multiple cores that handle instructions in parallel
  - Connects via the CPU socket on the motherboard
- [x] **RAM (Random Access Memory)**
  - Like short-term / working memory: holds data the CPU needs quickly
  - **Volatile** — contents are lost when power is lost
  - Modern modules use technologies such as DDR5 or DDR6 for speed
- [x] **Storage (SSD / HDD)**
  - Like long-term memory: data saved permanently (until deleted or overwritten)
  - **HDD** — older tech with moving parts; large capacity at lower cost, slower
  - **SSD** — no moving parts; memory chips; much faster
  - Connects via SATA cables or PCI Express slots
- [x] **Network Adapter**
  - Like vocal cords for communication with other systems
  - Wired and wireless variants; often embedded on the motherboard or added as expansion cards
  - Typically connects via PCI Express
- [x] **Power Supply (PSU)**
  - Like the heart pumping blood: supplies energy to all components
  - Must provide enough wattage; undersized PSU can cause failure
  - Takes outlet power and distributes it via connectors (main motherboard connector, Molex, etc.)
- [x] **Graphics Card**
  - Like the visual cortex: turns OS/program data into images for a monitor
  - Connects to PCI Express slots on the motherboard
- [x] **Input / Output**
  - Input: keyboard, microphone, mouse, scanner
  - Output: monitor, printer, speakers
  - Common connectors: USB, HDMI, DisplayPort
- [x] **Boot sequence (press Start / power button)**
  - Analogy: waking up and checking that everything works before starting the day
  - **Step 1 — Press the power button:** signal to the PSU to allow power to flow
  - **Step 2 — Firmware starts:** UEFI (Unified Extensible Firmware Interface) manages startup; BIOS does a similar job but has largely been replaced by UEFI
  - **Step 3 — Power-On Self Test (POST):** checks that required components are present, configured, and working
  - **Step 4 — Select boot device:** UEFI uses an ordered priority list of devices to find the OS boot routine
  - **Step 5 — Initiate bootloader:** bootloader loads the OS from the boot device into RAM; UEFI then hands control of components to the OS
  - Boot-exercise flag: `THM{pc5ucce55fully5t4rt3d}`
- [x] **Why this matters for cyber security**
  - Later topics often require recalling what each component does and how they interact
  - The boot process is especially important because it can be targeted by attackers
  - Next room (coming soon): Computer Types — how component combinations create different system types

<details>
  <summary>Lab</summary>

## Lab

This room uses two **interactive static sites** (View Site): identify PC components, then walk the boot sequence.

### **Overview**

- [ ] Identify core PC parts and complete the five-step boot path.
- [ ] You will:
  - [ ] Open the component identification static site and match each part to its role.
  - [ ] Open the boot-sequence static site and press through power-on to OS load.
- [ ] Success: flags `THM{4llpccomp0n3nts1d3nt1f13d}` and `THM{pc5ucce55fully5t4rt3d}`.

### **Task 1: Identify PC components**

- [ ] Click **View Site** for the component exercise.
- [ ] Match each part to its job:
  - [ ] Motherboard — holds and connects components
  - [ ] CPU — executes instructions
  - [ ] RAM — volatile working memory
  - [ ] HDD / SSD — long-term storage
  - [ ] Network adapter — talks to other systems
  - [ ] PSU — supplies power
  - [ ] Graphics card — drives the display
  - [ ] Input / output devices and connectors
- [ ] Complete the site to earn `THM{4llpccomp0n3nts1d3nt1f13d}`.

### **Task 2: Walk the boot sequence**

- [ ] Click **View Site** for the boot exercise.
- [ ] Step through:
  - [ ] Press the power button (PSU allows power to flow)
  - [ ] Firmware starts (**UEFI**; BIOS is the older equivalent)
  - [ ] **POST** checks required components
  - [ ] UEFI picks a boot device from its priority list
  - [ ] Bootloader loads the OS into RAM; UEFI hands over control
- [ ] Complete the site to earn `THM{pc5ucce55fully5t4rt3d}`.

Successfully identified the components and completed the boot-sequence exercise.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room is conceptual and uses interactive static-site exercises in the browser (View Site). There are no primary command-line tools.

```bash
# No primary terminal commands in this computer-components and boot-sequence room.
```

</details>

<details>
  <summary>Code</summary>

## Code

No programming component; learning is through explanations, diagrams, and static-site identification exercises.

```py
# No code snippets for the Inside a Computer System room.
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why does the room say you must understand a computer before securing it?

<details>
<summary>Answer</summary>

- [x] Trying to defend what you don't understand is like defending a castle you have never seen
- [x] You need the layout, who enters and how, and who can access or change important resources

</details>

### Question 2: What is the motherboard compared to in the human-body analogy, and what does it do?

<details>
<summary>Answer</summary>

- [x] Skeleton and nervous system
- [x] Holds components in place and connects them (CPU socket, RAM slots, expansion slots, ports)

</details>

### Question 3: What does the CPU do, and how do modern CPUs improve throughput?

<details>
<summary>Answer</summary>

- [x] Executes instructions (like part of the brain)
- [x] Multiple cores handle instructions in parallel
- [x] Connects via the CPU socket on the motherboard

</details>

### Question 4: What is RAM, and why is it called volatile?

<details>
<summary>Answer</summary>

- [x] Short-term / working memory that holds data the CPU needs quick access to
- [x] Volatile means contents are lost when power is lost
- [x] Modern modules use technologies such as DDR5 or DDR6

</details>

### Question 5: How do HDDs and SSDs differ as long-term storage?

<details>
<summary>Answer</summary>

- [x] **HDD** — moving parts; typically slower; popular for large capacity at low cost
- [x] **SSD** — no moving parts; memory chips; much faster
- [x] Both connect via SATA or PCI Express

</details>

### Question 6: What is the role of a network adapter?

<details>
<summary>Answer</summary>

- [x] Lets computers communicate with other systems (wired or wireless)
- [x] Often embedded on the motherboard or added as an expansion card
- [x] Typically connects via PCI Express

</details>

### Question 7: Why must the PSU be sized carefully for a system?

<details>
<summary>Answer</summary>

- [x] It supplies power to all components
- [x] If components need more power than the PSU can provide, the system will fail
- [x] It takes outlet power and distributes it through connectors (motherboard, Molex, etc.)

</details>

### Question 8: What does a graphics card do, and how does it usually connect?

<details>
<summary>Answer</summary>

- [x] Processes visual data from the OS and programs for output to a monitor
- [x] Comparable to the visual cortex
- [x] Connects to PCI Express slots on the motherboard

</details>

### Question 9: Give examples of input devices, output devices, and common connectors.

<details>
<summary>Answer</summary>

- [x] **Input** — keyboard, microphone, mouse, scanner
- [x] **Output** — monitor, printer, speakers
- [x] **Connectors** — USB, HDMI, DisplayPort

</details>

### Question 10: What happens in Step 1 when you press the power button?

<details>
<summary>Answer</summary>

- [x] A signal is sent to the PSU to allow power to flow to the system

</details>

### Question 11: What firmware manages component startup, and how does BIOS relate?

<details>
<summary>Answer</summary>

- [x] **UEFI** (Unified Extensible Firmware Interface) is the central system that manages startup
- [x] **BIOS** does a similar job but has mainly been replaced by UEFI

</details>

### Question 12: What is POST (Power-On Self Test)?

<details>
<summary>Answer</summary>

- [x] A UEFI routine that tests whether every required component is present
- [x] Checks that components are configured correctly and functioning

</details>

### Question 13: How does the system choose where to boot from?

<details>
<summary>Answer</summary>

- [x] UEFI holds an ordered priority list of devices
- [x] It looks first (then next) for the boot routine for the operating system

</details>

### Question 14: What does the bootloader do in the final boot step?

<details>
<summary>Answer</summary>

- [x] On the selected boot device, the bootloader is initiated
- [x] It transfers the Operating System into RAM
- [x] UEFI then gives control of the components to the OS

</details>

### Question 15: What flag do you get after identifying all PC components on the static site?

<details>
<summary>Answer</summary>

- [x] `THM{4llpccomp0n3nts1d3nt1f13d}`

</details>

### Question 16: What flag do you get after completing the boot-sequence static-site exercise?

<details>
<summary>Answer</summary>

- [x] `THM{pc5ucce55fully5t4rt3d}`

</details>

### Question 17: Why is the boot process especially relevant later in cyber security?

<details>
<summary>Answer</summary>

- [x] You will often need to recall how core components interact
- [x] The boot process is sometimes targeted by attackers

</details>

### Question 18: What learning objective does the room state after completion?

<details>
<summary>Answer</summary>

- [x] Recognize and understand the functions of various computing components

</details>

</details>

## Summary

Inside a Computer System covers the core PC building blocks—motherboard, CPU, RAM, storage (HDD/SSD), network adapter, PSU, graphics card, and I/O—using a human-body analogy, then walks through the five-step boot path from power button to UEFI/POST, boot-device selection, bootloader, and OS in RAM. Interactive static sites reinforce component ID and boot order; flags `THM{4llpccomp0n3nts1d3nt1f13d}` and `THM{pc5ucce55fully5t4rt3d}` mark completion. These fundamentals matter later because component roles and the boot process underpin many security topics.

## References

- [Inside a Computer System – TryHackMe](https://tryhackme.com/room/insideacomputer)
- [UEFI Specifications](https://uefi.org/specifications)
- [Power-on self-test (overview)](https://en.wikipedia.org/wiki/Power-on_self-test)

</details>

<details>
  <summary>Computer Types</summary>

## Introduction

Sophia was connecting a new device to her home WiFi when she noticed “NexusCool Fridge X17”—her neighbor’s smart refrigerator. The moment underscored a core idea of this TryHackMe room: computers are no longer only laptops and phones; they also hide in everyday objects (appliances, doorbells, and more). Through Sophia’s summer internship story at Nova Labs, the room teaches you to identify and distinguish computers you use directly (laptops, smartphones) and indirectly (servers, IoT devices, embedded systems), and why each type fits its purpose.

**Learning objectives:** identify and distinguish types of computers used directly and indirectly, and understand what makes each suited to its purpose.

## Detailed Explanation

- [x] **Sophia’s insight — computers everywhere**
  - Smart devices (e.g. a network-connected fridge) show that “computer” is broader than screens and keyboards
  - Many systems are used indirectly—you never sit in front of them, but they still process data and act in the world
- [x] **Month 1 — computers you sit in front of (and ones you don’t)**
  - Not all computers are meant to move
  - Not all computers are meant for people to sit in front of
  - Four similar-looking types serve different purposes: laptop, desktop, workstation, server
- [x] **Laptop**
  - Screen and keyboard: yes
  - Main purpose: portable everyday computing (email, documents, general work)
  - Trade-off: small, battery-powered form factor makes sustained cooling hard; long heavy tasks can slow the machine
- [x] **Desktop**
  - Screen and keyboard: yes
  - Main purpose: sustained performance at a fixed location
  - Wall power and better cooling support longer, steadier workloads than a typical laptop
  - Designed for consistency rather than mobility
- [x] **Workstation**
  - Screen and keyboard: yes
  - Main purpose: precision and reliability for professional tasks (simulations, 3D models)
  - Looks like a desktop but uses specialized components to reduce errors during long or complex computations
- [x] **Server**
  - Screen and keyboard: usually no dedicated ones
  - Main purpose: providing services to many users over a network
  - Runs continuously, answering many requests at once; users often never touch the hardware directly
- [x] **Month 2 — computers hiding in everyday objects**
  - The most powerful computer many people own fits in a pocket
  - Millions more hide in doors, lamps, coffee machines, and similar devices
- [x] **Smartphone**
  - Pocket-sized computer optimized for battery life and connectivity
  - Examples: iPhone, Android phone
  - Currently the most popular pocket-sized computer
- [x] **Tablet**
  - Touch-first computer with a larger screen
  - Examples: iPad, drawing tablet
- [x] **IoT device**
  - Network-connected device with a single purpose
  - Examples: thermostat, smart doorbell, fitness tracker
  - Reports data or receives commands over a network
- [x] **Embedded computer**
  - Computer built into another device
  - Examples: coffee maker controller, automatic door sensor, lamp dimmer chip
  - May not connect to a network; often runs silently for years inside the host machine
- [x] **IoT vs Embedded**
  - Both can be small and single-purpose
  - Key difference is **connectivity**: IoT devices join a network; embedded computers may not connect to anything
  - Example: automatic doors use an embedded computer to detect movement and open—invisible, reliable, everywhere
- [x] **Why computers come in different flavors**
  - There is no single “best” computer that does everything well
  - Every design is a **trade-off**
  - Mobility costs power: smaller portable systems sacrifice sustained performance
  - Reliability costs money: servers and critical systems add redundancy (extra power supplies, disks)
  - Purpose shapes interaction: you touch a phone; you ask a server for information; an IoT device works quietly without demanding attention
  - Right tool for the job—not one machine for all jobs
- [x] **Interactive challenge**
  - Complete the static site (View Site) on computer types
  - Flag: `THM{8_computer_types}`

<details>
  <summary>Lab</summary>

## Lab

This room uses one **interactive static site** (View Site) on eight computer types from Sophia's Nova Labs internship story.

### **Overview**

- [ ] Distinguish computers you sit in front of from ones you use indirectly.
- [ ] You will:
  - [ ] Review laptop, desktop, workstation, server, smartphone, tablet, IoT, and embedded.
  - [ ] Complete the static-site challenge.
- [ ] Success: flag `THM{8_computer_types}`.

### **Task 1: Review the eight types**

- [ ] Computers with a screen and keyboard: **laptop**, **desktop**, **workstation**.
- [ ] Computer that usually has no dedicated screen/keyboard: **server**.
- [ ] Pocket / touch devices: **smartphone**, **tablet**.
- [ ] Hidden computers: **IoT device** (networked, single purpose) vs **embedded computer** (built-in; may be offline).

### **Task 2: Complete the static site**

- [ ] Click **View Site**.
- [ ] Classify each example into the correct type.
- [ ] Submit to earn `THM{8_computer_types}`.

Successfully classified the eight computer types on the static site.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room is conceptual and uses an interactive static-site exercise in the browser (View Site). There are no primary command-line tools.

```bash
# No primary terminal commands in this computer-types room.
```

</details>

<details>
  <summary>Code</summary>

## Code

No programming component; learning is through the Sophia narrative, comparison tables, and the static-site challenge.

```py
# No code snippets for this computer-types room.
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What learning objective does this room emphasize?

<details>
<summary>Answer</summary>

- [x] Identify and distinguish computers you use directly (e.g. laptops, smartphones) and indirectly (e.g. servers, IoT, embedded systems)
- [x] Understand what makes each type suited to its purpose

</details>

### Question 2: What two lessons did Sophia learn in Month 1 about computers?

<details>
<summary>Answer</summary>

- [x] Not all computers are meant to move
- [x] Not all computers are meant for people to sit in front of

</details>

### Question 3: What is the main purpose of a laptop?

<details>
<summary>Answer</summary>

- [x] Portable everyday computing

</details>

### Question 4: What is the main purpose of a desktop?

<details>
<summary>Answer</summary>

- [x] Sustained performance at a fixed location

</details>

### Question 5: Which computer type usually runs without a dedicated screen and keyboard?

<details>
<summary>Answer</summary>

- [x] Server

</details>

### Question 6: What kind of computer with specialized components would one buy for precision work?

<details>
<summary>Answer</summary>

- [x] Workstation

</details>

### Question 7: How do servers typically serve users?

<details>
<summary>Answer</summary>

- [x] They provide services to many users over a network
- [x] They run continuously and answer multiple requests at once
- [x] Users often never touch the hardware directly

</details>

### Question 8: What is the currently most popular pocket-sized computer?

<details>
<summary>Answer</summary>

- [x] Smartphone

</details>

### Question 9: What kind of computer would you expect to find in a coffee machine?

<details>
<summary>Answer</summary>

- [x] Embedded computer

</details>

### Question 10: How do a smartphone and a tablet differ in the room’s framing?

<details>
<summary>Answer</summary>

- [x] **Smartphone** — pocket-sized; optimized for battery life and connectivity
- [x] **Tablet** — touch-first computer with a larger screen

</details>

### Question 11: What is an IoT device, and what are examples?

<details>
<summary>Answer</summary>

- [x] A network-connected device with a single purpose
- [x] Examples: thermostat, smart doorbell, fitness tracker

</details>

### Question 12: What is an embedded computer, and what are examples?

<details>
<summary>Answer</summary>

- [x] A computer built into another device
- [x] Examples: coffee maker controller, automatic door sensor, lamp dimmer chip

</details>

### Question 13: What is the key difference between IoT and embedded computers?

<details>
<summary>Answer</summary>

- [x] **Connectivity** — IoT devices connect to a network to report data or receive commands
- [x] Embedded computers might not connect to anything; they do their job inside the machine

</details>

### Question 14: Why not build one computer that does everything?

<details>
<summary>Answer</summary>

- [x] Every design is a trade-off
- [x] Mobility costs power (portable systems sacrifice sustained performance)
- [x] Reliability costs money (redundancy such as extra power supplies and disks)
- [x] Purpose shapes how you interact with each type

</details>

### Question 15: What eight computer types does the room cover?

<details>
<summary>Answer</summary>

- [x] Laptop
- [x] Desktop
- [x] Workstation
- [x] Server
- [x] Smartphone
- [x] Tablet
- [x] IoT device
- [x] Embedded computer

</details>

### Question 16: What flag do you get from the computer-types static site?

<details>
<summary>Answer</summary>

- [x] `THM{8_computer_types}`

</details>

### Question 17: According to Sophia’s final report, what misconception did she leave behind?

<details>
<summary>Answer</summary>

- [x] She arrived thinking computers had screens and keyboards
- [x] She left knowing computers are everywhere—especially where you do not see them

</details>

### Question 18: Why are “silent” computers often among the most critical?

<details>
<summary>Answer</summary>

- [x] The most critical computers are not always the fastest or flashiest
- [x] Silent chips keep doors opening, planes flying, and coffee machines brewing

</details>

</details>

## Summary

Through Sophia’s Nova Labs internship, this room maps eight computer types—laptop, desktop, workstation, server, smartphone, tablet, IoT device, and embedded computer—and shows why purpose and trade-offs (mobility vs power, reliability vs cost, connectivity vs isolation) drive design. Interactive static-site completion yields `THM{8_computer_types}`. The takeaway: there is no best computer, only the right tool for the job—and many of the most important systems are the ones you never see.

## References

- [Computer Types – TryHackMe](https://tryhackme.com/room/computertypes)
- [NIST IoT initiatives](https://www.nist.gov/itl/applied-cybersecurity/nist-initiatives-iot)

</details>

<details>
  <summary>Client-Server Basics</summary>

## Introduction

Early computers mostly worked alone—local files, local programs, no communication with other machines. Organizations then interconnected systems for information exchange and resource sharing (precursors of the internet such as ARPANET, CYCLADES, NPL, and NSFNET). Interconnected systems specialized into roles that offer and consume services. This TryHackMe room explains how that works through the **client-server model**, using a pizza-takeaway analogy and a practical HTTP GET lab.

**Learning objectives (surface level):** client-server model, DNS, client, server, port, protocol, and network.

## Detailed Explanation

- [x] **From standalone machines to networks**
  - Early computers stored their own files and ran their own programs without talking to others
  - Interconnecting systems enabled exchange and sharing regardless of distance
  - Historical networks paved the way for the modern internet: ARPANET, CYCLADES, NPL, NSFNET
  - Systems began specializing—like people offering specific skills as services
- [x] **Pizza analogy — service, client, and server**
  - Alice and Bob order from Luigi’s Pizza: Alice chooses the order; Bob delivers the request and brings the response home
  - **Client** initiates the request (e.g. browser requesting a webpage)
  - **Server** provides the service / serves the resource
  - The client is always the one who initiates the request
- [x] **Request and response**
  - A correctly formed request for an available resource yields a successful response
  - Bad formatting or unavailable resources yield an error response (e.g. no pepperoni, or order not understood)
  - In computing: browser (client) requests a webpage; server sends the page (or an error) back
- [x] **Protocol**
  - A protocol defines how a client communicates with a server
  - Includes: commands both sides understand (e.g. GET), request structure, syntax/language, expected responses, and responses to faulty requests
  - Bob in the analogy is like the protocol that carries a shared language and order format between Alice and Luigi’s
- [x] **Port**
  - A **port** identifies a specific service running on a system
  - Clients must connect using the correct port for that service
  - Analogy: takeaway customers use a specific door; multiple services (takeaway, dine-in, delivery) use different doors
  - One server can run multiple services at once, each on a different port
- [x] **DNS (Domain Name Service)**
  - Names alone are not enough to reach a destination (like knowing “Luigi’s Pizza” without coordinates)
  - DNS resolves a name (e.g. a website) to a server location
  - That location is an **Internet Protocol (IP) address**—the “home address” for computer systems
- [x] **HTTP(S) — web communication in practice**
  - **HTTP(S)** is a **stateless** client-server protocol for the World Wide Web
  - Each request is processed independently; the protocol itself does not remember previous requests
  - Applications add state with session identifiers (cookies/tokens) so you stay logged in across requests
  - Without sessions, you would authenticate on every request
- [x] **HTTP methods (commands)**
  - RFCs define 9 core HTTP methods: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, CONNECT, TRACE
  - Room focus: **GET** — retrieve a resource from a web server (e.g. `GET https://tryhackme.com/index.php`)
  - Browsers construct GET messages behind the scenes when you type a URL
  - Server responds with a **status code** and the requested information
- [x] **Lab: inspect a GET request (DevTools Network)**
  - Start the lab machine; open Firefox; visit `http://httpdemo.local:8080`
  - Open Developer Tools (F12 or Inspect) → **Network** tab → reload the page
  - Click the first GET entry to inspect fields:
    - **Scheme** — HTTP or HTTPS
    - **Host** — name of the host you request from
    - **Filename** — file requested; `"/"` maps to `index.html`
    - **Address** — IP of the host (lab example: `127.0.0.1` when hosted locally)
    - **Status** — success indicator (example: **200 OK**)
  - Response has two parts: **header** (metadata) and **body** (requested content, e.g. HTML of the index page)
- [x] **Room Q&A answers**
  - Identify a specific service on a server → **Port**
  - Address of a server → **Internet Protocol address**
  - Host in `https://www.iamlearning.thm/contact` → **www.iamlearning.thm**
  - Scheme in that URL → **https**
- [x] **What comes next**
  - Next room covers the basics of **virtualization**—the infrastructure that supports internet services

<details>
  <summary>Lab</summary>

## Lab

This is a **browser Network-inspector** walkthrough on the TryHackMe lab machine. Pause until the machine is on and the split view is visible.

### **Overview**

- [ ] Inspect a real **GET** request and its response on the demo site.
- [ ] You will:
  - [ ] Start the lab machine and open Firefox.
  - [ ] Open Developer Tools → **Network** and reload the page.
  - [ ] Read scheme, host, filename, address, and status on the first GET.
  - [ ] Open the **Response** tab to see the HTML body.
- [ ] Success: you can name the host and scheme in `https://www.iamlearning.thm/contact` and you have seen a **200 OK** GET.

### **Task 1: Start the lab machine**

- [ ] Click **Start Lab Machine** (or **Start Split-screen** if the pane is hidden).
- [ ] Wait until the machine status is **On**.
- [ ] Confirm the desktop is visible in the split view.

### **Task 2: Open the demo site in Firefox**

- [ ] Click the **Firefox** icon on the lab desktop.
- [ ] Confirm the address bar shows `http://httpdemo.local:8080`.
- [ ] If it does not, type that URL and press Enter.

### **Task 3: Open Developer Tools on the Network tab**

- [ ] Press **F12**, or right-click the page and choose **Inspect**.
- [ ] Click the **Network** tab.
- [ ] Reload the page (circular reload control next to the address bar).
- [ ] Confirm multiple **GET** rows appear in the Network list.

### **Task 4: Inspect the first GET**

- [ ] Click the **first GET** entry.
- [ ] In the right-hand panel, note:
  - [ ] **Scheme** — HTTP or HTTPS
  - [ ] **Host** — name of the host you requested
  - [ ] **Filename** — file requested; `"/"` maps to `index.html`
  - [ ] **Address** — IP of the host (lab example: `127.0.0.1` when hosted locally)
  - [ ] **Status** — success indicator (example: **200 OK**)

### **Task 5: Read the response body**

- [ ] With the same GET selected, open the **Response** tab.
- [ ] Confirm the body is the **HTML** of the index page.
- [ ] Remember: the response has a **header** (metadata) and a **body** (content).

Successfully inspected a client GET and a server response in Firefox Developer Tools.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room uses a browser lab and Firefox Developer Tools (Network tab). There are no primary CLI tools; inspection is done in the UI.

```bash
# No primary terminal commands — inspect GET traffic via Firefox DevTools → Network on http://httpdemo.local:8080
```

</details>

<details>
  <summary>Code</summary>

## Code

No programming component. HTTP GET requests and HTML responses are inspected in the browser.

```py
# No code snippets for the Client-Server Basics room.
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What problem did early interconnected networks aim to solve?

<details>
<summary>Answer</summary>

- [x] Information exchange and resource sharing regardless of distance
- [x] Precursors of the internet include ARPANET, CYCLADES, NPL, and NSFNET

</details>

### Question 2: In the client-server model, who initiates communication?

<details>
<summary>Answer</summary>

- [x] The **client** always initiates the request
- [x] The **server** replies by providing the service or resource

</details>

### Question 3: In the pizza analogy, what do Alice, Bob, and Luigi’s represent?

<details>
<summary>Answer</summary>

- [x] **Alice / browser** — client that wants a service (webpage / pizza order)
- [x] **Bob / protocol** — carries the request and response in a shared language and format
- [x] **Luigi’s / server** — system that serves the resource

</details>

### Question 4: What happens if a request is malformed or the resource is unavailable?

<details>
<summary>Answer</summary>

- [x] You get an error response
- [x] Example: no pepperoni available, or the server does not understand the order

</details>

### Question 5: What does a protocol define?

<details>
<summary>Answer</summary>

- [x] Commands the client and server understand (e.g. GET)
- [x] How a request is structured
- [x] What syntax/language is used
- [x] What response to give for successful and faulty requests

</details>

### Question 6: What do we use to identify a specific service on a server?

<details>
<summary>Answer</summary>

- [x] **Port**

</details>

### Question 7: Can one server run multiple services, and how are they distinguished?

<details>
<summary>Answer</summary>

- [x] Yes — one server can run multiple services at the same time
- [x] Each service listens on a different port (like different doors for takeaway, dine-in, delivery)

</details>

### Question 8: What does DNS stand for, and what does it do?

<details>
<summary>Answer</summary>

- [x] **Domain Name Service**
- [x] Resolves a name (e.g. a website) to a server location
- [x] That location is an **Internet Protocol (IP) address**

</details>

### Question 9: What do we call the address of a server?

<details>
<summary>Answer</summary>

- [x] **Internet Protocol address** (IP address)

</details>

### Question 10: What does it mean that HTTP(S) is stateless?

<details>
<summary>Answer</summary>

- [x] Each request is processed independently
- [x] The protocol itself does not retain information about previous requests
- [x] Apps add state with session IDs (cookies/tokens) so login can persist across requests

</details>

### Question 11: Name the nine core HTTP methods listed in the room.

<details>
<summary>Answer</summary>

- [x] GET
- [x] POST
- [x] PUT
- [x] DELETE
- [x] PATCH
- [x] HEAD
- [x] OPTIONS
- [x] CONNECT
- [x] TRACE

</details>

### Question 12: What is the GET method used for?

<details>
<summary>Answer</summary>

- [x] Retrieve a resource from a web server
- [x] Example: `GET https://tryhackme.com/index.php` retrieves the homepage
- [x] The browser builds the request when you navigate to a URL

</details>

### Question 13: In DevTools, what do Scheme, Host, Filename, Address, and Status tell you?

<details>
<summary>Answer</summary>

- [x] **Scheme** — HTTP or HTTPS
- [x] **Host** — name of the host requested
- [x] **Filename** — file requested; `"/"` means `index.html`
- [x] **Address** — IP where the site is hosted (lab example: `127.0.0.1`)
- [x] **Status** — whether the request succeeded (e.g. **200 OK**)

</details>

### Question 14: What are the two parts of an HTTP response?

<details>
<summary>Answer</summary>

- [x] **Response header** — metadata about the response
- [x] **Response body** — the requested content (e.g. HTML)

</details>

### Question 15: What would be the host in `https://www.iamlearning.thm/contact`?

<details>
<summary>Answer</summary>

- [x] `www.iamlearning.thm`

</details>

### Question 16: What would be the scheme in `https://www.iamlearning.thm/contact`?

<details>
<summary>Answer</summary>

- [x] `https`

</details>

### Question 17: How do you open the Network inspector in the Firefox lab?

<details>
<summary>Answer</summary>

- [x] Press **F12** or right-click → **Inspect**
- [x] Open the **Network** tab, reload the page, then click the first GET entry

</details>

### Question 18: What topic does the room say comes next after client-server basics?

<details>
<summary>Answer</summary>

- [x] Basics of **virtualization** — infrastructure that supports internet services

</details>

</details>

## Summary

Client-Server Basics explains how networked machines offer and consume services: the client initiates requests, the server responds, protocols define the shared rules, ports identify services, and DNS maps names to IP addresses. A pizza analogy makes the model concrete; an HTTP GET lab in Firefox DevTools shows scheme, host, path, IP, status codes, and response headers/bodies. Room answers include Port, Internet Protocol address, host `www.iamlearning.thm`, and scheme `https`. Next up: virtualization.

## References

- [Client-Server Basics – TryHackMe](https://tryhackme.com/room/clientserverbasics)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [RFC 1034 — Domain Names (concepts and facilities)](https://www.rfc-editor.org/rfc/rfc1034.html)
- [MDN — HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [MDN — URL](https://developer.mozilla.org/en-US/docs/Web/API/URL)

</details>

<details>
  <summary>Virtualisation Basics</summary>

## Introduction

After computer components and client-server communication, this TryHackMe room explains how companies pack many workloads onto fewer physical machines. Running every website or application on its own server wastes money and capacity. **Virtualization** lets multiple isolated systems share one physical host, which is how modern internet infrastructure stays cheaper, faster to deploy, and easier to scale.

**Learning objectives:** why one-application-per-server is inefficient; how virtualization improves utilization and scale; what a lab machine (VM) is; how containers push utilization further.

## Detailed Explanation

- [x] **The old rule: one server = one application**
  - Early digital services ran on physical machines with a single purpose (website, database, email)
  - Adding services meant buying more boxes, so a company needed a separate server for each workload
  - NIST SP 800-125 describes full virtualization as running one or more operating systems and their applications on **virtual hardware** — used for efficiency (including cloud) and for running multiple OSs on one computer
- [x] **Why dedicated physical servers fail at scale**
  - **High cost** — hardware plus electricity, cooling, maintenance, and data-center space
  - **Low utilization** — many applications use only **5–20%** of a server’s CPU, memory, and storage
  - **Slow deployment** — new physical servers can take days or weeks
  - **Hard to scale** — a sudden resource spike often meant buying yet another server
- [x] **Virtualization’s core idea**
  - Multiple applications can share the same **physical server** safely
  - A **hypervisor** is the virtualization layer that referees lab machines so each virtual computer behaves independently
  - NIST SP 800-125A: the hypervisor virtualizes CPU, memory, network, and storage; it **mediates** access to physical resources and **isolates** resident VMs
- [x] **Building analogy**
  - One person living alone in a 10-floor building wastes most of the structure but still pays for electricity, cleaning, water, and security
  - Dividing the building into apartments gives each tenant a door, walls, kitchen, and privacy while sharing the core infrastructure
  - Mapping:
    - Building = physical server
    - Apartments = lab machines (VMs)
    - Tenants = applications or operating systems
    - Building manager = hypervisor
- [x] **Hypervisor (the building manager)**
  - Software that creates and manages lab machines
  - Divides a physical computer into multiple virtual ones
  - Gives each VM a share of CPU, memory, and storage
  - Keeps guests isolated
  - Manages lifecycle: start, stop, pause, clone, delete
- [x] **Type 1 vs Type 2 (NIST + room table)**
  - **Type 1 (bare-metal)** — installed directly on the hardware; fast and efficient; preferred for servers and professional environments
  - **Type 2 (hosted)** — installed on a conventional **host OS**; easier to install; preferred for learning, testing, and small setups
  - Room-recommended type by use case:
    - Type 1: production server, database server, data center
    - Type 2: test malicious files, software testing, Kali Linux
  - Oracle VirtualBox is officially a **hosted / Type 2** hypervisor; VMware Workstation is the other Type 2 example named in the room
- [x] **Malware-testing pitfall**
  - The guest can infect the host if isolation is weak
  - Room guidance: use a **different OS** for guest and host, or isolate the guest so it does not communicate with the host
  - NIST ITL guidance on hypervisors: disable unused virtual hardware and unneeded sharing (clipboard / file sharing) and treat the hypervisor as a high-value target
- [x] **Lab machine (VM) — the apartment**
  - A virtual computer created by the hypervisor
  - Has its own virtual CPU, RAM, storage, and network
  - Can run Windows, Linux, or another guest OS
  - Isolated: if one VM breaks, the others keep running
  - Home-lab examples: run Kali without buying another PC; detonate a suspicious file in an isolated VM
- [x] **Containers (rooms inside the apartment)**
  - Lightweight isolated environment for **one application** plus its dependencies
  - Shares the host **kernel** (the OS component that talks to hardware and manages memory and processes)
  - Starts quickly and uses fewer resources than a full VM
  - Must match the host OS type — you cannot run a Windows container on a Linux machine
  - Package the app and libraries; stay isolated from other containers; run consistently across machines
  - Docker is the usual way to build, deploy, and run containers
  - Docker docs: a container is an isolated process with everything it needs; multiple containers share one kernel; a **container image** is the pre-packed template that becomes a container at runtime
  - VMs and containers are often stacked: a VM provides the guest OS, then Docker runs several containers inside it
- [x] **Stack relationship**
  - Physical server → hypervisor → lab machines → (optional) containers inside a VM
  - VMs = full apartment (maximum separation and OS flexibility)
  - Containers = lightweight rooms (fast, dense, scalable apps)
- [x] **Virtualization Manager lab (AutoGalo)**
  - Simulated console with **Summary**, **Lab Machines**, and **Hosts**
  - Restart **Mail-SERVER** from Error with the blue square button
  - Create **Marketing-VM** (4 CPU, 8 GB RAM, 100 GB disk)
  - Hosts: **HV-PROD-01** has spare capacity; **HV-PROD-02** is near 100% and hosts the most VMs; **HV-BACKUP-01** is disconnected and hosts none
- [x] **Room Q&A answers**
  - Multiple applications share a **physical server**
  - Resource manager for each lab machine = **hypervisor**
  - Home study lab = **type 2**
  - Several small apps in one lab machine = **containers**
  - Longest-running VM = **Monitoring-SYS**
  - Highest memory VM = **DB-Cluster-01**
  - Running VMs after Mail-SERVER restart = **8**
  - Physical host with the most VMs = **HV-PROD-02**
- [x] **Benefits and next step**
  - Cost savings, better resource usage, safer cyber-security testing, faster deployment, flexibility, portability, scalability, centralized management
  - Next room: **Cloud Computing Fundamentals** (virtualization + containerization + automation)

<details>
  <summary>Lab</summary>

## Lab

This is the room’s **View Site** walkthrough in **Virtualization Manager** for AutoGalo. Work only in that simulated console. Pause until the site is visible.

### **Overview**

- [ ] Investigate the email outage, create a marketing VM, and report host health.
- [ ] You will:
  - [ ] Open **View Site** and find **Mail-SERVER**.
  - [ ] Restart the Error-state VM with the blue square button.
  - [ ] Create **Marketing-VM** with the hardware values below.
  - [ ] Read the **Hosts** section and answer the task questions.
- [ ] Success: Mail-SERVER is healthy, Marketing-VM exists, and you can name the longest-running VM, the highest-memory VM, the running-VM count, and the busiest host.

### **Task 1: Open Virtualization Manager**

- [ ] Click **View Site** on the room page.
- [ ] Confirm the home screen has three sections:
  - [ ] **Summary** — overall environment state
  - [ ] **Lab Machines** — each VM plus actions
  - [ ] **Hosts** — usage and performance of each physical server

### **Task 2: Restart Mail-SERVER**

- [ ] Open the **Lab Machines** section.
- [ ] Find the VM named **Mail-SERVER** (the room screenshot labels it Mal-SERVER).
- [ ] Confirm it is in an **Error** state.
- [ ] Click the **blue square** restart button.
- [ ] Confirm the VM returns to a healthy state with no errors.

### **Task 3: Create Marketing-VM**

- [ ] Stay in **Lab Machines**.
- [ ] Click **+ Create VM** (top right of that section).
- [ ] Fill the form:
  - [ ] Name: **Marketing-VM**
  - [ ] CPU Cores: **4**
  - [ ] Memory (GB): **8**
  - [ ] Disk Size (GB): **100**
- [ ] Click **Create VM**.
- [ ] Confirm **Marketing-VM** appears at the top of the Lab Machines list.

### **Task 4: Analyze host capacity**

- [ ] Open the **Hosts** section at the bottom of the page.
- [ ] Record these observations:
  - [ ] **HV-PROD-01** has capacity to host more VMs
  - [ ] **HV-PROD-02** is almost at **100%** capacity — report this
  - [ ] **HV-BACKUP-01** is disconnected and hosts no VMs

### **Task 5: Answer the shift questions**

- [ ] Longest-running lab machine: **Monitoring-SYS**
- [ ] Lab machine using the most memory: **DB-Cluster-01**
- [ ] VMs in the running state after fixing Mail-SERVER: **8**
- [ ] Physical machine hosting the most VMs: **HV-PROD-02**

Successfully completed the AutoGalo shift when Mail-SERVER is running, Marketing-VM exists, and the four task answers above are confirmed.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room uses the **View Site** Virtualization Manager UI. There is no primary CLI walkthrough.

```bash
# No primary terminal commands — manage VMs in the Virtualization Manager View Site
```

On your own Type 2 hypervisor later (not required here), Oracle VirtualBox and VMware Workstation expose GUI and CLI front ends. VirtualBox’s CLI is `VBoxManage`; do not invent flags or lab IPs for this room.

</details>

<details>
  <summary>Code</summary>

## Code

No application source in this room. The stack relationship from the room diagram is:

```text
Physical server
└── Hypervisor (Type 1 on bare metal, or Type 2 on a host OS)
    ├── Lab machine / VM  (guest OS + apps)
    └── Lab machine / VM
        ├── Container  (shares that VM’s kernel)
        └── Container
```

Marketing-VM create-form values used in the View Site:

```text
Name:          Marketing-VM
CPU Cores:     4
Memory (GB):   8
Disk Size (GB): 100
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why was “one server = one application” a problem?

<details>
<summary>Answer</summary>

- [x] High cost (hardware, power, cooling, space)
- [x] Low utilization (often 5–20% of CPU, memory, and storage)
- [x] Slow deployment (days or weeks for new physical servers)
- [x] Hard to scale (a spike often meant buying another server)

</details>

### Question 2: What does virtualization enable multiple applications to share?

<details>
<summary>Answer</summary>

- [x] physical server

</details>

### Question 3: What is the name of the software that manages the resources for each lab machine?

<details>
<summary>Answer</summary>

- [x] hypervisor

</details>

### Question 4: In the building analogy, what do the building, apartments, tenants, and manager represent?

<details>
<summary>Answer</summary>

- [x] Building = physical server
- [x] Apartments = lab machines (VMs)
- [x] Tenants = applications or operating systems
- [x] Building manager = hypervisor

</details>

### Question 5: How do Type 1 and Type 2 hypervisors differ?

<details>
<summary>Answer</summary>

- [x] Type 1 (bare-metal) runs directly on the physical hardware — fast, efficient, used for servers and data centers
- [x] Type 2 (hosted) runs on an existing host OS — easier to install, used for learning, testing, and small setups
- [x] NIST SP 800-125A uses the same Type 1 / Type 2 split

</details>

### Question 6: A user wants a study lab on their own machine for a cyber security certification. Which hypervisor type?

<details>
<summary>Answer</summary>

- [x] type 2

</details>

### Question 7: Which use cases fit Type 1 vs Type 2 in this room?

<details>
<summary>Answer</summary>

- [x] Type 1: production server, database server, data center
- [x] Type 2: test malicious files, software testing, Kali Linux

</details>

### Question 8: How should you reduce the chance that malware in a guest infects the host?

<details>
<summary>Answer</summary>

- [x] Use a different operating system for guest and host
- [x] Isolate the guest so it does not communicate with the host
- [x] Disable unused virtual hardware and unneeded clipboard/file sharing (NIST hypervisor guidance)

</details>

### Question 9: What is a lab machine (VM)?

<details>
<summary>Answer</summary>

- [x] A virtual computer created by the hypervisor
- [x] It has its own virtual CPU, RAM, storage, and network
- [x] It can run its own guest OS and is isolated from other VMs

</details>

### Question 10: What Type 2 tools does the room name for running VMs on your own computer?

<details>
<summary>Answer</summary>

- [x] Oracle VirtualBox
- [x] VMware Workstation
- [x] Oracle documents VirtualBox as a hosted / Type 2 hypervisor

</details>

### Question 11: How do containers differ from VMs?

<details>
<summary>Answer</summary>

- [x] A container packages one application and its dependencies
- [x] Containers share the host kernel, so they start faster and use fewer resources
- [x] A VM includes a full guest OS and its own kernel
- [x] Docker is the usual platform for building and running containers

</details>

### Question 12: Why can’t you run a Windows container on a Linux machine?

<details>
<summary>Answer</summary>

- [x] Containers share the host kernel
- [x] The container OS type must match the host system’s type

</details>

### Question 13: A company wants to host multiple small applications in the same lab machine. What should they use?

<details>
<summary>Answer</summary>

- [x] containers

</details>

### Question 14: What was wrong with Mail-SERVER, and how do you fix it in the View Site?

<details>
<summary>Answer</summary>

- [x] Mail-SERVER was in an Error state (email outage)
- [x] Open Lab Machines, select Mail-SERVER, click the blue square restart button
- [x] After restart it runs with no errors

</details>

### Question 15: What values do you use to create Marketing-VM?

<details>
<summary>Answer</summary>

- [x] Name: Marketing-VM
- [x] CPU Cores: 4
- [x] Memory (GB): 8
- [x] Disk Size (GB): 100

</details>

### Question 16: What do the three hosts show?

<details>
<summary>Answer</summary>

- [x] HV-PROD-01 has capacity for more VMs
- [x] HV-PROD-02 is almost at 100% capacity
- [x] HV-BACKUP-01 is disconnected and hosts no VMs

</details>

### Question 17: What is the name of the lab machine that has been running for the longest time?

<details>
<summary>Answer</summary>

- [x] Monitoring-SYS

</details>

### Question 18: What is the name of the lab machine that is using the biggest amount of memory?

<details>
<summary>Answer</summary>

- [x] DB-Cluster-01

</details>

### Question 19: How many VMs are in the running state after you solved the issue on Mail-SERVER?

<details>
<summary>Answer</summary>

- [x] 8

</details>

### Question 20: What is the name of the physical machine that is hosting most of the VMs?

<details>
<summary>Answer</summary>

- [x] HV-PROD-02

</details>

</details>

## Summary

Virtualization replaces “one server = one application” with many isolated lab machines on one physical host. A **hypervisor** (Type 1 on bare metal, Type 2 on a host OS) allocates CPU, memory, and storage and keeps guests apart. **VMs** are full virtual computers; **containers** (often via Docker) share a kernel and pack more apps into the same VM. The AutoGalo View Site walks through restarting **Mail-SERVER**, creating **Marketing-VM** (4 CPU / 8 GB / 100 GB), and reading host pressure on **HV-PROD-02**. Room answers: physical server, hypervisor, type 2, containers, Monitoring-SYS, DB-Cluster-01, 8, HV-PROD-02. Next: Cloud Computing Fundamentals.

## References

- [Virtualisation Basics – TryHackMe](https://tryhackme.com/room/virtualisationbasics)
- [Computer Fundamentals module – TryHackMe](https://tryhackme.com/module/computer-fundamentals)
- [Cloud Computing Fundamentals – TryHackMe](https://tryhackme.com/room/cloudcomputingfundamentals)
- [NIST SP 800-125 — Guide to Security for Full Virtualization Technologies](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-125.pdf)
- [NIST SP 800-125A Rev. 1 — Security Recommendations for Server-based Hypervisor Platforms](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-125Ar1.pdf)
- [NIST ITL Bulletin — Full Virtualization Technologies](https://csrc.nist.gov/CSRC/media/Publications/Shared/documents/itl-bulletin/itlbul2011-04.pdf)
- [Oracle VirtualBox — About Oracle VirtualBox (Type 2 / hosted hypervisor)](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/Introduction.html)
- [What is a container? – Docker Docs](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [What is a Container? – Docker](https://www.docker.com/resources/what-container/)

</details>


