[Back to Microsoft Learn | AZ-900: Azure Fundamentals ](../../../azure_ai.md)

# Chapter 1 - Introduction to Cloud Infrastructure: Describe cloud concepts

New to the cloud? Introduction to Cloud Infrastructure is a four-part series that teaches you basic cloud concepts, provides a streamlined overview of many Azure services, and guides you with hands-on exercises to deploy your first services for free. Complete all of the learning paths in the series if you're preparing for Exam AZ-900: Microsoft Azure Fundamentals. This is the first learning path in the series, Introduction to Cloud Infrastructure: Describe cloud concepts. The other learning paths in the series are Part 2: Describe Azure architecture and services, Part 3: Describe Azure management and governance, and Part 4: Apply Azure skills in guided projects.

Introduction to Microsoft Azure Fundamentals
Completed
100 XP
3 minutes
Microsoft Azure is a cloud computing platform with an ever-expanding set of services to help you build solutions that meet your technical goals. Azure services support everything from simple to complex. You can host simple web services for internet-facing apps, run fully virtualized computers for custom software solutions, or use cloud-based services like remote storage, database hosting, and centralized account management. Azure also offers capabilities in artificial intelligence (AI) and Internet of Things (IoT).

In this series, you cover cloud computing basics, get introduced to some of the core services provided by Microsoft Azure, and learn more about the governance and compliance services that you can use.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/875ccd14-111a-4102-9d09-0de73cc005b8" />

What is Azure Fundamentals?
Azure Fundamentals is a series of three learning paths that familiarize you with Azure and its many services and features and one learning path that gives you a chance to explore Azure and build solutions to realistic IT challenges.

Whether you're interested in compute, networking, or storage services; learning about cloud security best practices; or exploring governance and management options, think of Azure Fundamentals as your curated guide to Azure.

Azure Fundamentals includes guided content and knowledge checks that reinforce key concepts.

Technical IT experience isn't required; however, having general IT knowledge will help you get the most from your learning experience.

Why should I take Azure Fundamentals?
If you're just beginning to work with the cloud, or if you already have cloud experience, Azure Fundamentals provides you with everything you need to get started.

No matter your goals, Azure Fundamentals has something for you. You should take this course if you:

Have general interest in Azure or in cloud computing
Want to earn official certification from Microsoft (AZ-900)
The Azure Fundamentals learning path series can help you prepare for Exam AZ-900: Microsoft Azure Fundamentals. This exam includes three knowledge domain areas:

AZ-900 Domain Area	Weight
Describe cloud concepts	25-30%
Describe Azure architecture and services	35-40%
Describe Azure management and governance	30-35%

Each domain area maps to a learning path in Azure Fundamentals. The percentages shown indicate the relative weight of each area on the exam. The higher the percentage, the more questions that part of the exam will contain. Be sure to read the exam page for specifics about what skills are covered in each area.

This training helps you develop a broad understanding of Azure.

Next unit: Introduction to cloud computing

Introduction to cloud computing
Completed
100 XP
1 minute
In this module, you're introduced to general cloud concepts. You start with an introduction to the cloud in general. Then you dive into concepts like shared responsibility, different cloud models, and explore the unique pricing method for the cloud.

If you're already familiar with cloud computing, this module may be largely review for you.

Learning objectives
After completing this module, you'll be able to:

Define cloud computing.
Describe the shared responsibility model.
Define cloud models, including public, private, and hybrid.
Identify appropriate use cases for each cloud model.
Describe the consumption-based model.
Compare cloud pricing models.
Next unit: What is cloud computing

What is cloud computing
Completed
100 XP
3 minutes
Cloud computing is the delivery of computing services over the internet. Computing services include common IT infrastructure such as virtual machines, storage, databases, and networking. Cloud services also expand the traditional IT offerings to include things like Internet of Things (IoT), machine learning (ML), and artificial intelligence (AI).

Because cloud computing uses the internet to deliver these services, it doesn’t have to be constrained by physical infrastructure the same way that a traditional datacenter is. That means if you need to increase your IT infrastructure rapidly, you don’t have to wait to build a new datacenter—you can use the cloud to rapidly expand your IT footprint.

Practical example
Suppose a retail team expects high traffic during a seasonal launch. Instead of buying and configuring extra physical servers months in advance, they can deploy additional compute capacity in the cloud for the launch period and scale down afterward. This approach improves agility and helps align spending to actual demand.

At a fundamentals level, cloud computing changes infrastructure planning from long procurement cycles to on-demand provisioning. Teams can test faster, recover faster, and adapt capacity as requirements change.

Cloud platforms also offer global reach, so teams can place services closer to users and design for regional resilience without building multiple physical datacenters.

Next unit: Describe the shared responsibility model

Describe the shared responsibility model
Completed
100 XP
3 minutes
You may have heard of the shared responsibility model, but you may not understand what it means or how it impacts cloud computing.

How responsibilities shift in cloud
Start with a traditional on-premises datacenter. Your team is responsible for maintaining the physical space, ensuring security, and maintaining or replacing the servers if anything happens. The IT department is responsible for maintaining all the infrastructure and software needed to keep the datacenter up and running. They're also likely to be responsible for keeping all systems patched and on the correct version.

With the shared responsibility model, these responsibilities get shared between the cloud provider and the consumer. Physical security, power, cooling, and network connectivity are the responsibility of the cloud provider. The consumer isn’t collocated with the datacenter, so it wouldn’t make sense for the consumer to have any of those responsibilities.

At the same time, the consumer is responsible for the data and information stored in the cloud. (You wouldn’t want the cloud provider to be able to read your information.) The consumer is also responsible for access security, meaning you only give access to those who need it.

Then, for some things, the responsibility depends on the situation. If you’re using a cloud SQL database, the cloud provider would be responsible for maintaining the actual database. However, you’re still responsible for the data that gets ingested into the database. If you deployed a virtual machine and installed an SQL database on it, you’d be responsible for database patches and updates, as well as maintaining the data and information stored in the database.

With an on-premises datacenter, you’re responsible for everything. With cloud computing, those responsibilities shift. The shared responsibility model is heavily tied into the cloud service types (covered later in this learning path): infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). IaaS places the most responsibility on the consumer, with the cloud provider being responsible for the basics of physical security, power, and connectivity. On the other end of the spectrum, SaaS places most of the responsibility with the cloud provider. PaaS, being a middle ground between IaaS and SaaS, rests somewhere in the middle and evenly distributes responsibility between the cloud provider and the consumer.

Responsibility by service model
The following diagram highlights how the Shared Responsibility Model informs who is responsible for what, depending on the cloud service type.

<img width="1920" height="1180" alt="image" src="https://github.com/user-attachments/assets/731d03f9-f511-4ac0-b39b-fb90e571e728" />

What always stays with you
When using a cloud provider, you’ll always be responsible for:

The information and data stored in the cloud
Devices that are allowed to connect to your cloud (cell phones, computers, and so on)
The accounts and identities of the people, services, and devices within your environment
What the provider always owns
The cloud provider is always responsible for:

The physical datacenter
The physical network
The physical hosts
Infrastructure
What depends on the service type
Your service model will determine responsibility for things like:

Operating systems
Network controls
Applications
Identity and access
For example, identity and access is shared in PaaS and SaaS—you manage your own users, roles, and policies, while the provider runs the authentication platform (such as Microsoft Entra ID). Infrastructure, on the other hand, shifts entirely to the provider as soon as you move off-premises to IaaS.

Next unit: Define cloud models

Define cloud models
Completed
100 XP
4 minutes
What are cloud models? The cloud models define the deployment type of cloud resources. The three main cloud models are: private, public, and hybrid.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6f4d77d0-f401-4f5b-93b3-e068083e2d17" />

Private cloud
A private cloud is a cloud environment used by a single entity. It evolved naturally from the traditional datacenter model, delivering IT services over the internet while keeping resources dedicated to one organization. Private cloud provides much greater control for your IT team. However, it also comes with greater cost and fewer of the benefits of a public cloud deployment. A private cloud may be hosted from your on-site datacenter, or in a dedicated datacenter offsite, potentially even by a third party.

Public cloud
A public cloud is built, controlled, and maintained by a third-party cloud provider. With a public cloud, anyone that wants to purchase cloud services can access and use resources. The general public availability is a key difference between public and private clouds.

Hybrid cloud
A hybrid cloud is a computing environment that uses both public and private clouds in an inter-connected environment. A hybrid cloud environment can be used to allow a private cloud to surge for increased, temporary demand by deploying public cloud resources. Hybrid cloud can be used to provide an extra layer of security. For example, users can flexibly choose which services to keep in public cloud and which to deploy to their private cloud infrastructure.

The following table highlights a few key comparative aspects between the cloud models.

Public cloud	Private cloud	Hybrid cloud
No capital expenditures to scale up	You have complete control over resources and security	Provides the most flexibility
Applications can be quickly provisioned and deprovisioned	Data isn't collocated with other tenants' data	You determine where to run your applications
You pay only for what you use	Hardware must be purchased for startup and maintenance	You control security, compliance, or legal requirements
You don't have complete control over resources and security	You are responsible for hardware maintenance and updates	

Multicloud
A fourth, and increasingly likely scenario is a multicloud scenario. In a multicloud scenario, you use multiple public cloud providers. Maybe you use different features from different cloud providers. Or maybe you started your cloud journey with one provider and are in the process of migrating to a different provider. Regardless, in a multicloud environment you deal with two (or more) public cloud providers and manage resources and security in both environments.

Azure Arc
Azure Arc is a set of technologies that helps manage your cloud environment. Azure Arc can help manage your cloud environment whether it's a public cloud solely on Azure, a private cloud in your datacenter, a hybrid configuration, or even a multicloud environment running on multiple cloud providers at once.

Azure VMware Solution
What if you're already established with VMware in a private cloud environment but want to migrate to a public or hybrid cloud? Azure VMware Solution lets you run your VMware workloads in Azure with seamless integration and scalability.

Next unit: Describe the consumption-based model



















































