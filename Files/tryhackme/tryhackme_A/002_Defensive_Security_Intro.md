# Defensive Security Intro

[Back to TryHackMe](../../tryhackme.md)

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

## Summary

This room introduces defensive security by having you think like a defender with SOC analyst Joe. You use a monitoring dashboard to find the suspicious source IP **32.122.195.63**, identify URL discovery toward **https://fakebank.com/admin**, and contain the attack by blocking that IP with a firewall rule. Success yields the flag **THM{FAKEBANK-SECURED}**. Core idea: detect and respond—monitor, investigate, then contain before damage spreads.

## References

- [Defensive Security Intro – TryHackMe](https://tryhackme.com/room/defensivesecurityintro)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
