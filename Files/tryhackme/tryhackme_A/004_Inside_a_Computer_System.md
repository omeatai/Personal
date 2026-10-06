# Inside a Computer System

[Back to TryHackMe](../../tryhackme.md)

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
