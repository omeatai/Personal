# Virtualisation Basics

[Back to TryHackMe](../../tryhackme.md)

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
  - On your own machine later, VirtualBox’s CLI is `VBoxManage`. This room’s lab stays in the View Site UI and does not use that CLI.
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

```text
Physical server
└── Hypervisor (Type 1 on bare metal, or Type 2 on a host OS)
    ├── Lab machine / VM  (guest OS + apps)
    └── Lab machine / VM
        ├── Container  (shares that VM’s kernel)
        └── Container
```

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

```text
Name:          Marketing-VM
CPU Cores:     4
Memory (GB):   8
Disk Size (GB): 100
```

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
