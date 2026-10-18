[Back to Microsoft Learn | AZ-900: Azure Fundamentals ](../../../azure_ai.md)

# Chapter 1 — Introduction to Cloud Infrastructure: Describe cloud concepts

## Table of Contents

- [Introduction](#introduction)
- [Detailed tutorial](#detailed-tutorial)
  - [What this learning path covers](#what-this-learning-path-covers)
  - [What Azure Fundamentals is](#what-azure-fundamentals-is)
  - [Why take Azure Fundamentals](#why-take-azure-fundamentals)
  - [What cloud computing is](#what-cloud-computing-is)
  - [Describe the shared responsibility model](#describe-the-shared-responsibility-model)
  - [Define cloud models](#define-cloud-models)
  - [Multicloud, Azure Arc, and Azure VMware Solution](#multicloud-azure-arc-and-azure-vmware-solution)
  - [Describe the consumption-based model](#describe-the-consumption-based-model)
  - [Cloud concepts knowledge check](#cloud-concepts-knowledge-check)
  - [High availability and scalability](#high-availability-and-scalability)
  - [Reliability and predictability](#reliability-and-predictability)
  - [Security and governance](#security-and-governance)
  - [Manageability](#manageability)
  - [Sustainability](#sustainability)
  - [Cloud benefits knowledge check](#cloud-benefits-knowledge-check)
  - [Infrastructure as a service](#infrastructure-as-a-service)
  - [Platform as a service](#platform-as-a-service)
  - [Software as a service](#software-as-a-service)
  - [Cloud service types knowledge check](#cloud-service-types-knowledge-check)
  - [Practice prompts](#practice-prompts)
- [Summary](#summary)
- [References](#references)

## Introduction

This chapter is the first learning path in Introduction to Cloud Infrastructure, the four-part series for Exam AZ-900: Microsoft Azure Fundamentals. It defines cloud computing, then splits responsibility between you and the cloud provider, compares public, private, hybrid, and multicloud deployments, and shows why cloud spend is an operating expense. The later sections cover the benefits of running in the cloud and the three service types: infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). Describe cloud concepts is 25–30% of the exam.

## Detailed tutorial

**AZ-900: Azure Fundamentals** · Learning path: [Describe cloud concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/)

<details id="what-this-learning-path-covers">
<summary><strong>What this learning path covers</strong></summary>

New to the cloud? Introduction to Cloud Infrastructure is a four-part series that teaches basic cloud concepts, gives a streamlined overview of many Azure services, and walks through hands-on exercises that deploy your first services for free. Complete every learning path in the series if you are preparing for Exam AZ-900: Microsoft Azure Fundamentals.

This file is Part 1, Introduction to Cloud Infrastructure: Describe cloud concepts. The rest of the series is:

1. Part 2: Describe Azure architecture and services.
2. Part 3: Describe Azure management and governance.
3. Part 4: Apply Azure skills in guided projects.

In this series you cover cloud computing basics, meet some of the core services Microsoft Azure provides, and learn the governance and compliance services you can use.

Microsoft Azure is a cloud computing platform with an expanding set of services for solutions from simple to complex. You can host a simple web service for an internet-facing app, run fully virtualized computers for custom software, or use cloud services such as remote storage, database hosting, and centralized account management. Azure also offers capabilities in artificial intelligence (AI) and Internet of Things (IoT).

![Azure covers simple web apps through virtual machines, storage, databases, identity, AI, and IoT](https://github.com/user-attachments/assets/875ccd14-111a-4102-9d09-0de73cc005b8)

_Figure: Azure Fundamentals introduces the platform, from ordinary IT services through AI and IoT._

</details>

<details id="what-azure-fundamentals-is">
<summary><strong>What Azure Fundamentals is</strong></summary>

Azure Fundamentals is a series of three learning paths that familiarize you with Azure and its services and features, plus one learning path where you explore Azure and build solutions to realistic IT challenges.

Whether you care about compute, networking, or storage, about cloud security practices, or about governance and management, treat Azure Fundamentals as a curated guide to Azure. It includes guided content and knowledge checks that reinforce the key concepts.

Technical IT experience is not required. General IT knowledge helps you get more from the material.

</details>

<details id="why-take-azure-fundamentals">
<summary><strong>Why take Azure Fundamentals</strong></summary>

If you are just beginning with the cloud, or you already have cloud experience, Azure Fundamentals is the starting point. Take this course if you:

- Have a general interest in Azure or in cloud computing.
- Want to earn the official Microsoft certification (AZ-900).

The series prepares you for Exam AZ-900: Microsoft Azure Fundamentals. The exam has three knowledge domains. Each domain maps to a learning path. The percentage is the relative weight: a higher percentage means more questions from that area. Read the exam page for the skills covered in each area.

| AZ-900 domain area                       | Weight |
| ---------------------------------------- | ------ |
| Describe cloud concepts                  | 25–30% |
| Describe Azure architecture and services | 35–40% |
| Describe Azure management and governance | 30–35% |

This training builds a broad understanding of Azure. The first module starts with cloud computing in general, then shared responsibility, the cloud models, and the consumption-based price. If those ideas are already familiar, treat the module as review. After it you should be able to:

- Define cloud computing.
- Describe the shared responsibility model.
- Define cloud models, including public, private, and hybrid.
- Identify an appropriate use case for each cloud model.
- Describe the consumption-based model.
- Compare cloud pricing models.

</details>

<details id="what-cloud-computing-is">
<summary><strong>What cloud computing is</strong></summary>

Cloud computing is the delivery of computing services over the internet. Computing services include common IT infrastructure such as virtual machines, storage, databases, and networking. Cloud services also expand traditional IT to include Internet of Things (IoT), machine learning (ML), and artificial intelligence (AI).

Because these services arrive over the internet, they are not constrained by physical infrastructure the way a traditional datacenter is. If you need to grow IT infrastructure quickly, you do not wait to build a new datacenter. You use the cloud to expand the footprint.

Suppose a retail team expects high traffic during a seasonal launch. Instead of buying and configuring extra physical servers months in advance, they deploy additional compute capacity in the cloud for the launch and scale down afterward. That improves agility and lines spending up with actual demand.

At a fundamentals level, cloud computing changes infrastructure planning from long procurement cycles to on-demand provisioning. Teams can test faster, recover faster, and adapt capacity as requirements change. Cloud platforms also offer global reach, so teams can place services closer to users and design for regional resilience without building multiple physical datacenters.

</details>

<details id="describe-the-shared-responsibility-model">
<summary><strong>Describe the shared responsibility model</strong></summary>

The shared responsibility model says which security and operations tasks stay with you and which move to the cloud provider.

Start with a traditional on-premises datacenter. Your team maintains the physical space, security, and the servers. The IT department maintains the infrastructure and software that keep the datacenter running, and it keeps systems patched and on the correct version.

In the cloud, those responsibilities are shared. Physical security, power, cooling, and network connectivity belong to the cloud provider. You are not in the datacenter, so those tasks would not make sense as yours.

You stay responsible for the data and information stored in the cloud. You would not want the provider to read it. You are also responsible for access security: only the people who need access get it.

Some duties depend on the service. If you use a cloud SQL database, the provider maintains the database engine, and you still own the data ingested into it. If you deploy a virtual machine and install SQL Server on it, you patch and update that database, and you still maintain the data stored in it.

On-premises, you are responsible for everything. In the cloud, responsibilities shift. The shift follows the service type, covered later in this chapter. IaaS places the most responsibility on you. The provider covers physical security, power, and connectivity. SaaS places most of the responsibility on the provider. PaaS sits in the middle and splits responsibility between you and the provider.

![Shared responsibility across on-premises, IaaS, PaaS, and SaaS](https://github.com/user-attachments/assets/731d03f9-f511-4ac0-b39b-fb90e571e728)

_Figure: The shared responsibility model. More of the stack moves to the provider as you go from on-premises to IaaS, PaaS, and SaaS._

You always keep:

- The information and data stored in the cloud.
- Devices allowed to connect to your cloud (phones, computers, and so on).
- The accounts and identities of the people, services, and devices in your environment.

The provider always owns:

- The physical datacenter.
- The physical network.
- The physical hosts.
- The infrastructure underneath the service.

The service model decides who owns:

- Operating systems.
- Network controls.
- Applications.
- Identity and access.

Identity and access is shared in PaaS and SaaS. You manage your users, roles, and policies. The provider runs the authentication platform, such as Microsoft Entra ID. Infrastructure shifts entirely to the provider as soon as you leave on-premises for IaaS.

</details>

<details id="define-cloud-models">
<summary><strong>Define cloud models</strong></summary>

Cloud models define how cloud resources are deployed. The three main models are private, public, and hybrid.

![Private, public, and hybrid cloud](https://github.com/user-attachments/assets/6f4d77d0-f401-4f5b-93b3-e068083e2d17)

_Figure: Private cloud is dedicated to one organization. Public cloud is offered to anyone who buys it. Hybrid cloud connects the two._

**Private cloud.** A private cloud is used by a single entity. It grew out of the traditional datacenter: IT services are delivered over the network, and the resources stay dedicated to one organization. Your IT team has much greater control. It also costs more and gives you fewer of the benefits of a public cloud. A private cloud may run in your on-site datacenter or in a dedicated datacenter offsite, sometimes hosted by a third party.

**Public cloud.** A public cloud is built, controlled, and maintained by a third-party cloud provider. Anyone who wants to purchase cloud services can use the resources. That general availability is the key difference from a private cloud.

**Hybrid cloud.** A hybrid cloud uses public and private clouds together in one connected environment. A private cloud can surge onto public cloud resources for a temporary spike in demand. Hybrid can also add a layer of security: you choose which services stay in the public cloud and which run on private infrastructure.

| Public cloud                                                 | Private cloud                                          | Hybrid cloud                                             |
| ------------------------------------------------------------ | ------------------------------------------------------ | -------------------------------------------------------- |
| No capital expenditure to scale up                           | Complete control over resources and security           | The most flexibility                                     |
| Applications can be provisioned and deprovisioned quickly    | Data is not collocated with other tenants' data        | You decide where each application runs                   |
| You pay only for what you use                                | Hardware must be purchased for startup and maintenance | You control security, compliance, and legal requirements |
| You do not have complete control over resources and security | You maintain and update the hardware                   |                                                          |

</details>

<details id="multicloud-azure-arc-and-azure-vmware-solution">
<summary><strong>Multicloud, Azure Arc, and Azure VMware Solution</strong></summary>

A fourth, and increasingly common, case is multicloud: you use more than one public cloud provider. You might want different features from different providers, or you might have started with one provider and be migrating to another. Either way, you manage resources and security in two or more public clouds.

Azure Arc is a set of technologies that helps you manage that environment. It applies whether you run only on Azure, in a private cloud in your datacenter, in a hybrid configuration, or across multiple cloud providers at once.

Azure VMware Solution is the path when you are already established with VMware in a private cloud and want to move to a public or hybrid cloud. It lets you run VMware workloads in Azure with integration and scalability.

</details>

<details id="describe-the-consumption-based-model">
<summary><strong>Describe the consumption-based model</strong></summary>

Cloud computing operates on a consumption-based model. You pay for the IT resources you use, and nothing more. Instead of buying and maintaining a datacenter, you rent compute and storage and release them when you are done.

Traditional IT budgeting uses two terms:

- **Capital expenditure (CapEx)** is up-front spending on physical infrastructure: servers, network hardware, and datacenter space.
- **Operational expenditure (OpEx)** is ongoing spending on services over time.

You pay for cloud services as you consume them, so cloud computing is an operational expense.

The consumption-based model gives you:

- No upfront cost for hardware or datacenter infrastructure.
- No need to buy and manage capacity that may sit idle.
- The ability to add resources when demand increases.
- The ability to release resources when demand decreases.

![Traditional capacity planning versus cloud capacity](https://github.com/user-attachments/assets/c43e2d4e-72f6-4ac3-ae3a-5e55ae0bdc9e)

_Figure: A traditional datacenter is sized in advance. Cloud capacity is added for a peak and removed when demand drops._

With a traditional datacenter, you estimate future needs ahead of time. Overestimate, and you pay for infrastructure that sits idle. Underestimate, and applications slow down. Fixing that means ordering, installing, and provisioning more hardware, power, and cooling.

In the cloud, you adjust resources to match actual demand. Add virtual machines when you need more capacity, and remove them when demand drops. You pay for what you use, not for idle capacity. In practice you scale out during a peak and scale back in when traffic subsides.

Cloud providers use pay-as-you-go pricing. You typically pay only for the services you consume, which helps you:

- Plan and manage operating costs.
- Run infrastructure more efficiently.
- Scale as the workload changes.

The provider maintains the underlying infrastructure, including power, cooling, hardware, and networking, so you can focus on the business problem and on new capabilities for your users.

</details>

<details id="cloud-concepts-knowledge-check">
<summary><strong>Cloud concepts knowledge check</strong></summary>

1. What is cloud computing?
   - A. Delivery of computing services over the internet.
   - B. Delivery of storage services over the internet.
   - C. Delivery of websites accessible via the internet.

   **Answer:** A. Delivery of computing services over the internet.

2. Which cloud model uses some datacenters focused on providing cloud services to anyone that wants them, and some datacenters focused on a single customer?
   - A. Public cloud.
   - B. Hybrid cloud.
   - C. Multicloud.

   **Answer:** B. Hybrid cloud.

3. According to the shared responsibility model, which cloud service type places the most responsibility on the customer?
   - A. Infrastructure as a Service (IaaS).
   - B. Software as a Service (SaaS).
   - C. Platform as a Service (PaaS).

   **Answer:** A. Infrastructure as a Service (IaaS).

</details>

<details id="high-availability-and-scalability">
<summary><strong>High availability and scalability</strong></summary>

When you build or deploy a cloud application, two of the largest considerations are uptime (availability) and the ability to handle demand (scale). After this part of the chapter you should be able to describe high availability and scalability, reliability and predictability, security and governance, manageability, and sustainability.

![High availability keeps a service up through disruptions](https://github.com/user-attachments/assets/8a57651e-21ec-437a-8924-df7e95ddfadc)

_Figure: High availability is about the resource being there when it is needed._

When you deploy an application, a service, or any IT resource, it has to be available when it is needed. High availability focuses on maximum availability, regardless of disruptions or events. When you architect the solution, account for the service availability guarantees. Azure is a highly available cloud environment, and the uptime guarantees depend on the service. Those guarantees are part of the service-level agreements (SLAs).

![Vertical scaling changes the size of a resource; horizontal scaling changes the count](https://github.com/user-attachments/assets/8ee08fdd-d44d-4ed3-9fd6-d7f43d6caab5)

_Figure: Scalability adjusts resources to meet demand, then releases them so you are not paying for idle capacity._

Scalability is the ability to adjust resources to meet demand. If peak traffic overwhelms your systems, you add resources to handle it. Because the cloud is consumption-based, you only pay for what you use. If demand drops, you reduce the resources and the cost.

Scaling comes in two varieties. Vertical scaling changes the capability of a resource. Horizontal scaling changes the number of resources.

**Vertical scaling.** If an app needs more processing power, you scale up by adding CPUs or RAM to the virtual machine. If you over-specified it, you scale down by lowering the CPU or RAM.

**Horizontal scaling.** If demand jumps, you scale out, automatically or manually, by adding virtual machines or containers. If demand drops, you scale in, automatically or manually.

</details>

<details id="reliability-and-predictability">
<summary><strong>Reliability and predictability</strong></summary>

Reliability and predictability are two cloud benefits that let you build solutions with confidence.

![Reliability is recovery from failure without the service stopping](https://github.com/user-attachments/assets/b74db325-ef84-42ee-9858-4f9a865d58ef)

_Figure: Reliability is the ability to recover from failures and continue to function. It is a pillar of the Azure Well-Architected Framework._

Reliability is the ability of a system to recover from failures and continue to function. It is one of the pillars of the Microsoft Azure Well-Architected Framework.

The cloud's decentralized design supports a reliable and resilient infrastructure. You can deploy resources in regions around the world. If one region has a catastrophic event, other regions are still running. You can design applications to take advantage of that, and in some cases the cloud environment itself shifts to a different region with no action from you. Later parts of this series cover how Azure uses global scale for reliability.

![Predictability covers both performance and cost](https://github.com/user-attachments/assets/79b4c855-08c3-4d03-a728-3151ade79a3c)

_Figure: Predictability is either performance (the experience stays good) or cost (the spend can be forecast)._

Predictability lets you move forward with confidence. It can mean performance predictability or cost predictability. Both are heavily influenced by the Microsoft Azure Well-Architected Framework. A solution built around that framework has cost and performance you can predict.

**Performance.** Performance predictability is about predicting the resources needed for a good customer experience. Autoscaling, load balancing, and high availability support it. If you suddenly need more resources, autoscaling deploys them and scales back when demand drops. If traffic piles onto one area, load balancing redirects some of it to less stressed areas.

**Cost.** Cost predictability is about forecasting cloud spend. You can track resource use in real time, monitor resources so you use them efficiently, and apply analytics to find patterns that improve planning. Tools such as the Azure Pricing Calculator estimate potential spend.

</details>

<details id="security-and-governance">
<summary><strong>Security and governance</strong></summary>

Whether you deploy infrastructure as a service or software as a service, cloud features support governance and compliance.

![Governance and security tooling around a cloud deployment](https://github.com/user-attachments/assets/5206298a-ccc8-44bc-92bc-b768e522f83e)

_Figure: Templates, auditing, and patching keep deployed resources inside your standards._

Templates help ensure that deployed resources meet your technical standards and regulatory requirements. As standards change, you update resources at scale. Cloud-based auditing flags resources that fall outside your baseline and offers mitigation. Depending on the operating model, software patches and updates may be applied automatically, which helps both governance and security.

On the security side, you can match the cloud solution to the control you want. If you want maximum control, infrastructure as a service gives you the physical resources and lets you manage the operating systems and installed software, including patches and maintenance. If you want patches and maintenance handled for you, platform as a service or software as a service may fit better.

Cloud providers are typically well suited to handle distributed denial of service (DDoS) attacks, which makes the network more robust. Establish a governance footprint early so the cloud footprint stays updated, secure, and well managed.

</details>

<details id="manageability">
<summary><strong>Manageability</strong></summary>

A major benefit of cloud computing is manageability. There are two kinds, and both matter.

![Management of the cloud: scale, deploy from templates, monitor, and alert](https://github.com/user-attachments/assets/23b6f20d-c894-4a1e-af7c-6cebbf6ae959)

_Figure: Management of the cloud is how you operate the resources themselves._

**Management of the cloud** means managing your cloud resources. You can:

- Automatically scale resource deployment based on need.
- Deploy resources from a preconfigured template, so you are not configuring each one by hand.
- Monitor the health of resources and automatically replace failing ones.
- Receive automatic alerts from configured metrics, so you see performance in real time.

![Management in the cloud: portal, CLI, APIs, and PowerShell](https://github.com/user-attachments/assets/ca32644c-f3c1-423d-ba91-48e59fb25bf7)

_Figure: Management in the cloud is the set of tools you use to operate the environment._

**Management in the cloud** means how you manage the environment and the resources. You can manage them:

- Through a web portal.
- With a command-line interface.
- With APIs.
- With PowerShell.

An operations team can deploy resources from templates, monitor health in the portal, and automate recurring tasks with CLI or PowerShell scripts. That combination cuts manual effort and keeps configurations consistent.

</details>

<details id="sustainability">
<summary><strong>Sustainability</strong></summary>

Cloud computing can support sustainability goals when teams actively optimize how resources are deployed and used.

![Sustainability comes from matching deployed resources to real demand](https://github.com/user-attachments/assets/d2d5b3de-f4fb-46c9-8590-3315546ab9b1)

_Figure: Large-scale cloud operations can waste less than many isolated datacenters, if you actually scale unused capacity down._

Cloud providers operate at large scale, which can improve resource utilization compared with many isolated on-premises environments. In Azure you can also reduce waste by matching deployed resources to actual demand.

Practices that support sustainability and cost efficiency:

- Scale resources down when demand decreases.
- Turn off or deallocate resources that are not in use.
- Choose efficient services and configurations so you are not overprovisioned.
- Use governance and monitoring to track usage and optimize deployments over time.

A development environment that runs only during business hours can shut down overnight and on weekends. That cuts consumption and still meets the team's needs. At a fundamentals level, sustainability in the cloud is the same operational habit: right-size, automate, monitor, and keep optimizing.

</details>

<details id="cloud-benefits-knowledge-check">
<summary><strong>Cloud benefits knowledge check</strong></summary>

1. Which type of scaling involves adding or removing resources (such as virtual machines or containers) to meet demand?
   - A. Vertical scaling.
   - B. Horizontal scaling.
   - C. Direct scaling.

   **Answer:** B. Horizontal scaling.

2. What is characterized as the ability of a system to recover from failures and continue to function?
   - A. Reliability.
   - B. Predictability.
   - C. Scalability.

   **Answer:** A. Reliability.

3. Which cloud practice most directly supports sustainability by reducing unnecessary resource use?
   - A. Automatically scaling down resources when demand drops.
   - B. Deploying every workload as always-on peak capacity.
   - C. Using only on-premises hardware.

   **Answer:** A. Automatically scaling down resources when demand drops.

</details>

<details id="infrastructure-as-a-service">
<summary><strong>Infrastructure as a service</strong></summary>

Infrastructure as a service (IaaS) is the most flexible category of cloud services. It gives you the maximum control of your cloud resources. The cloud provider maintains the hardware, network connectivity to the internet, and physical security. You are responsible for everything else:

- Operating system installation, configuration, and maintenance.
- Network configuration.
- Database and storage configuration.

With IaaS you are renting the hardware in a cloud datacenter. What you do with that hardware is up to you.

The shared responsibility model divides duties by layer. The diagram shows networking, storage, servers, runtime, and the rest of the stack, and which layers you operate in each service model.

![Infrastructure layers and who operates them in each service model](https://github.com/user-attachments/assets/9ebef677-7785-4b88-ad53-e6fed64351c5)

_Figure: Each service model changes which layers of the stack you still operate._

![IaaS leaves the operating system and above with you](https://github.com/user-attachments/assets/d3622775-0493-49f6-a5c0-73b607bc4d76)

_Figure: In IaaS the provider keeps the physical infrastructure and internet connectivity. You manage the operating system, patching, configuration, and many security controls._

That split is maximum flexibility and the largest operational responsibility. Common cases:

- **Lift-and-shift migration.** You set up cloud resources similar to the on-premises datacenter, then move the workloads onto that IaaS infrastructure.
- **Testing and development.** You rapidly replicate established configurations for development and test. You can start and shut down environments quickly and still keep complete control.

</details>

<details id="platform-as-a-service">
<summary><strong>Platform as a service</strong></summary>

Platform as a service (PaaS) is the middle ground between renting space in a datacenter (IaaS) and paying for a complete deployed solution (SaaS). The provider maintains the physical infrastructure, physical security, and the connection to the internet. The provider also maintains the operating systems, middleware, development tools, and analytics services that make up the solution. You do not license or patch the operating systems and databases.

PaaS is a complete development environment without the work of maintaining all of the development infrastructure.

![PaaS leaves the application and the data with you](https://github.com/user-attachments/assets/325ac27f-714e-4d2c-9d34-d27b71d1178c)

_Figure: In PaaS the provider manages the physical infrastructure and the platform, including operating systems, middleware, and managed runtimes. You focus on application code, data, and access. Some networking and application security settings are shared._

Common cases:

- **Development framework.** Developers build or customize cloud applications on a framework and built-in software components. Scalability, high availability, and multitenant capability are included, so developers write less of that plumbing.
- **Analytics or business intelligence.** Tools provided as a service let teams analyze and mine data, find patterns, and predict outcomes to improve planning and operations.

</details>

<details id="software-as-a-service">
<summary><strong>Software as a service</strong></summary>

Software as a service (SaaS) is the most complete cloud service model from a product perspective. You rent or use a fully developed application. Email, financial software, messaging, and connectivity software are common SaaS examples.

SaaS is the least flexible model and the easiest to get running. It requires the least technical knowledge to employ.

![SaaS leaves data, identity, and device access with you](https://github.com/user-attachments/assets/87d59d2a-26d4-4750-8109-5fc2959a3527)

_Figure: In SaaS the provider manages almost the whole application stack, including infrastructure, platform, and application maintenance. You manage data, identity and access, and which devices can connect._

A team on a SaaS collaboration platform focuses on user onboarding, access controls, and data governance. The provider handles infrastructure patching, application updates, and availability. Common cases:

- Email and messaging.
- Productivity applications.
- Finance and expense tracking.

</details>

<details id="cloud-service-types-knowledge-check">
<summary><strong>Cloud service types knowledge check</strong></summary>

1. Which cloud service type is most suited to a lift-and-shift migration from an on-premises datacenter to a cloud deployment?
   - A. Infrastructure as a Service (IaaS).
   - B. Platform as a Service (PaaS).
   - C. Software as a Service (SaaS).

   **Answer:** A. Infrastructure as a Service (IaaS).

2. What type of cloud service would a finance and expense tracking solution typically be?
   - A. Infrastructure as a Service (IaaS).
   - B. Platform as a Service (PaaS).
   - C. Software as a Service (SaaS).

   **Answer:** C. Software as a Service (SaaS).

</details>

<details id="practice-prompts">
<summary><strong>Practice prompts</strong></summary>

Use these in Copilot Chat to rehearse the chapter:

- Explain shared responsibility across on-premises, IaaS, PaaS, and SaaS using one concrete business application example.
- Compare public, private, hybrid, and multicloud models, then recommend the best fit for three different organizational scenarios.
- Create a financial comparison of CapEx versus OpEx for moving a workload to a consumption-based cloud model.
- Evaluate an on-premises system and map cloud improvements for availability, scalability, reliability, security, and manageability.
- Design a KPI dashboard to measure whether cloud adoption is delivering the expected technical and business benefits.
- Analyze tradeoffs where cloud benefits may be limited, including cost, governance complexity, and sustainability constraints.
- For one application portfolio, choose IaaS, PaaS, or SaaS for each workload and explain the responsibility tradeoffs.
- Show how operational responsibilities shift when moving from IaaS to PaaS, including security, patching, and scalability implications.
- Create a short scenario quiz on cloud service types with answer explanations focused on selecting the right model.

</details>

## Summary

- Cloud computing is the delivery of computing services over the internet, including VMs, storage, databases, networking, and newer services such as IoT, ML, and AI.
- You always own your data, the devices that connect, and the accounts and identities. The provider always owns the physical datacenter, network, and hosts.
- IaaS leaves the most work with you. SaaS leaves the most with the provider. PaaS splits the stack. A cloud SQL database is the provider's engine and your data. SQL Server on a VM is yours to patch.
- Public cloud is shared and on demand. Private cloud is dedicated and costs more control. Hybrid connects both. Multicloud means more than one public provider. Azure Arc manages across those environments. Azure VMware Solution runs VMware workloads in Azure.
- Cloud spend is OpEx. CapEx is buying the hardware up front. Consumption-based pricing means you add capacity for a peak and release it afterward.
- High availability is uptime, backed by an SLA. Vertical scaling changes the size of a resource. Horizontal scaling changes how many resources you run.
- Reliability is recovering from failure and continuing to function. Predictability is forecasting performance and cost. Both sit on the Well-Architected Framework.
- Sustainability here is an operating habit: scale down, turn off what is idle, and stop overprovisioning.
- Lift-and-shift fits IaaS. A development framework or analytics service fits PaaS. Email, productivity, and expense tracking fit SaaS.
- Describe cloud concepts is 25–30% of AZ-900. Architecture and services is 35–40%. Management and governance is 30–35%.

## References

- [Describe cloud concepts (learning path)](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/)
- [Exam AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
- [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/)
- [Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/1-introduction)
- [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)
- [Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
- [Introduction to Azure VMware Solution](https://learn.microsoft.com/en-us/azure/azure-vmware/introduction)
- [Introduction to Azure hybrid cloud services](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-hybrid-services/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
