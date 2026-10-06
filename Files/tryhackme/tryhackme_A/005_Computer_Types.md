# Computer Types

[Back to TryHackMe](../../tryhackme.md)

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

## Summary

Through Sophia’s Nova Labs internship, this room maps eight computer types—laptop, desktop, workstation, server, smartphone, tablet, IoT device, and embedded computer—and shows why purpose and trade-offs (mobility vs power, reliability vs cost, connectivity vs isolation) drive design. Interactive static-site completion yields `THM{8_computer_types}`. The takeaway: there is no best computer, only the right tool for the job—and many of the most important systems are the ones you never see.

## References

- [Computer Types – TryHackMe](https://tryhackme.com/room/computertypes)
- [NIST IoT initiatives](https://www.nist.gov/itl/applied-cybersecurity/nist-initiatives-iot)
