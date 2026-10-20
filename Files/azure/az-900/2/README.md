[Back to Microsoft Learn | AZ-900: Azure Fundamentals ](../../../azure_ai.md)

# Chapter 2 - Introduction to Cloud Infrastructure: Describe Azure architecture and services

## Describe the core architectural components of Azure

New to the cloud? Introduction to Cloud Infrastructure is a four-part series that teaches you basic cloud concepts, provides a streamlined overview of many Azure services, and guides you with hands-on exercises to deploy your very first services for free. Complete all of the learning paths in the series if you are preparing for Exam AZ-900: Microsoft Azure Fundamentals. This is the second learning path in the series, Introduction to Cloud Infrastructure: Describe Azure architecture and services. The other learning paths in the series are Part 1: Describe cloud concepts, Part 3: Describe Azure management and governance, and Part 4: Apply Azure skills in guided projects.

Introduction
Completed
100 XP
1 minute
In this module, you’ll be introduced to the core architectural components of Azure. You’ll learn about Azure's physical layout: datacenters, availability zones, and regions; and you’ll learn about Azure's management structure: resources and resource groups, subscriptions, and management groups.

Learning objectives
After completing this module, you’ll be able to:

Describe Azure regions, region pairs, and sovereign regions.
Describe Availability Zones.
Describe Azure datacenters.
Describe Azure resources and Resource Groups.
Describe subscriptions.
Describe management groups.
Describe the hierarchy of resource groups, subscriptions, and management groups.
Next unit: What is Microsoft Azure

What is Microsoft Azure

Azure is a continually expanding set of cloud services that help you meet current and future IT challenges. Azure gives you the freedom to build, manage, and deploy applications on a massive global network using your favorite tools and frameworks.

What does Azure offer?
Limitless innovation. Build intelligent apps and solutions with advanced technology, tools, and services to take your operations to the next level. Seamlessly unify your technology to simplify platform management and deliver innovations efficiently and securely on a trusted cloud.

Bring ideas to life: Build on a trusted platform to advance your team's capabilities with industry-leading AI and cloud services.
Seamlessly unify: Efficiently manage all your infrastructure, data, analytics, and AI solutions across an integrated platform.
Innovate on trust: Rely on trusted technology from a partner who's dedicated to security and responsibility.
What can I do with Azure?
Azure provides hundreds of services that enable you to do everything from running your existing applications on virtual machines to exploring new software paradigms, such as intelligent bots and generative AI.

<img width="1800" height="840" alt="image" src="https://github.com/user-attachments/assets/fe0d2c39-a0e0-41ba-b2bd-23f2a8348b52" />

Many teams start exploring the cloud by moving their existing applications to virtual machines (VMs) that run in Azure. Migrating your existing apps to VMs is a good start, but the cloud is much more than a different place to run your VMs.

As your skills grow, you can modernize one workload at a time, such as moving from manually managed servers to managed databases, autoscaling web apps, or event-driven services.

Practical example
Suppose your organization runs an internal app with seasonal demand spikes. In Azure, you can host the app on virtual machines or managed app services, store data in managed databases, and monitor health from a centralized dashboard. As demand increases, you can scale resources up or out and then scale back when demand drops so you're not paying for unused capacity year-round.

For example, Azure provides Azure AI services and Azure OpenAI Service so you can add language, vision, speech, and generative AI capabilities to your applications. It also provides Azure Machine Learning, Internet of Things (IoT) services, and storage solutions that dynamically grow to accommodate massive amounts of data. Azure services enable solutions that aren't feasible without the power of the cloud.

Next unit: Get started with Azure accounts

Get started with Azure accounts
Completed
100 XP
4 minutes
To create and use Azure services, you need an Azure subscription. When you're working with your own applications and workloads, you create an Azure account, and a subscription is created for you. After you've created an Azure account, you're free to create additional subscriptions. For example, your team might use a single Azure account and separate subscriptions for development, testing, and production workloads. After you've created an Azure subscription, you can start creating Azure resources within each subscription.

<img width="1680" height="1080" alt="image" src="https://github.com/user-attachments/assets/ff83af39-8be4-4298-bba7-c1736021fd81" />

If you're new to Azure, you can sign up for a free account on the Azure website to start exploring at no cost to you. When you're ready, you can choose to upgrade your free account. You can also create a new subscription that enables you to start paying for Azure services you need beyond the limits of a free account.

Create an Azure account
You can purchase Azure access directly from Microsoft by signing up on the Azure website or through a Microsoft representative. You can also purchase Azure access through a Microsoft partner. Cloud Solution Provider partners offer a range of complete managed-cloud solutions for Azure.

What is the Azure free account?
The Azure free account includes:

Free access to popular Azure products for 12 months.
A credit to use for the first 30 days.
Access to more than 65 services that are always free.
The Azure free account is an excellent way for new users to get started and explore. To sign up, you need a phone number, a credit card, and a Microsoft or GitHub account. The credit card information is used for identity verification only. You won't be charged for any services until you upgrade to a paid subscription.

What is the Azure free student account?
The Azure free student account offer includes:

Free access to certain Azure services for 12 months.
A credit to use in the first 12 months.
Free access to certain software developer tools.
The Azure free student account is an offer for students that gives $100 credit and free developer tools. Also, you can sign up without a credit card.

If you're practicing by creating resources in Azure, monitor usage and remove resources you no longer need to avoid unexpected costs.

Next unit: Describe Azure physical infrastructure

Describe Azure physical infrastructure
Completed
100 XP
6 minutes
Azure's core architectural components can be broken down into two main groupings: the physical infrastructure and the management infrastructure. This unit covers the physical side — how Azure organizes its datacenters, regions, and availability zones to deliver reliable services worldwide.

Physical infrastructure
The physical infrastructure for Azure starts with datacenters. These datacenters are facilities with servers arranged in racks, with dedicated power, cooling, and networking infrastructure — similar to an on-premises datacenter, but at a much larger scale.

As a global cloud provider, Azure has datacenters around the world. However, you don't interact with individual datacenters directly. Instead, datacenters are grouped into Azure Regions and Azure Availability Zones that provide resiliency and reliability for your workloads.

The Global infrastructure site gives you a chance to interactively explore the underlying Azure infrastructure.

<img width="1680" height="620" alt="image" src="https://github.com/user-attachments/assets/8d1a4c84-296a-4a20-82ce-67ac793e42bb" />

Regions
A region is a geographical area on the planet that contains at least one, but potentially multiple datacenters that are nearby and networked together with a low-latency network. Azure intelligently assigns and controls the resources within each region to ensure workloads are appropriately balanced.

When you deploy a resource in Azure, you'll often need to choose the region where you want your resource deployed.

 Note

Some services or virtual machine (VM) features are only available in certain regions, such as specific VM sizes or storage types. There are also some global Azure services that don't require you to select a particular region, such as Microsoft Entra ID, Azure Traffic Manager, and Azure DNS.

Availability Zones
Availability zones are physically separate datacenters within an Azure region. Each availability zone is made up of one or more datacenters equipped with independent power, cooling, and networking. An availability zone is set up to be an isolation boundary. If one zone goes down, the other continues working. Availability zones are connected through high-speed, private fiber-optic networks.

<img width="1680" height="840" alt="image" src="https://github.com/user-attachments/assets/9350287c-e2f1-4b3f-85a7-8c76b139de97" />

Important

To ensure resiliency, a minimum of three separate availability zones are present in all availability zone-enabled regions. However, not all Azure Regions currently support availability zones.

Use availability zones for your workloads
When you run your own on-premises infrastructure, setting up redundancy means buying and maintaining duplicate hardware. With Azure, you can protect your workloads by spreading them across availability zones within a region.

You place your VMs, storage, databases, and other resources in one availability zone and replicate them to other zones within the same region. Keep in mind that there could be a cost to duplicating your services and transferring data between zones.

Azure services that support availability zones fall into three categories:

Zonal services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
Zone-redundant services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.

<img width="1680" height="800" alt="image" src="https://github.com/user-attachments/assets/ce76dba9-0fb1-4023-9178-f1bf5d7d2c62" />

Even with the additional resiliency that availability zones provide, it’s possible that an event could be so large that it impacts multiple availability zones in a single region. To provide even further resilience, Azure has Region Pairs.

Region pairs
Most Azure regions are paired with another region within the same geography (such as US, Europe, or Asia) at least 300 miles away. This approach allows for the replication of resources across a geography that helps reduce the likelihood of interruptions because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect an entire region. For example, if a region in a pair was affected by a natural disaster, services would automatically fail over to the other region in its region pair.

 Important

Not all Azure services automatically replicate data or automatically fall back from a failed region to cross-replicate to another enabled region. In these scenarios, recovery and replication must be configured by the customer.

Examples of region pairs in Azure are West US paired with East US and Southeast Asia paired with East Asia. Because the pair of regions is directly connected and far enough apart to be isolated from regional disasters, you can use them to provide reliable services and data redundancy.

<img width="1680" height="880" alt="image" src="https://github.com/user-attachments/assets/52a8d33f-5026-4239-9ff4-9bd4964e1cab" />

Additional advantages of region pairs:
If an extensive Azure outage occurs, one region out of every pair is prioritized to make sure at least one is restored as quickly as possible for applications hosted in that region pair.
Planned Azure updates are rolled out to paired regions one region at a time to minimize downtime and risk of application outage.
Data continues to reside within the same geography as its pair (except for Brazil South) for data-residency and compliance purposes.
 Important

Most regions are paired in two directions, meaning they are the backup for the region that provides a backup for them (West US and East US back each other up). However, some regions, such as Brazil South, are paired in only one direction. In a one-direction pairing, the Primary region does not provide backup for its secondary region. Brazil South is unique because it's paired with a region outside of its geography. Brazil South's secondary region is South Central US. The secondary region of South Central US isn't Brazil South. Additionally, some regions (such as Italy North, Poland Central, and Israel Central) don't have a traditional region pair and instead rely on availability zones and geo-redundant storage for resiliency.

Sovereign Regions
In addition to regular regions, Azure also has sovereign regions. Sovereign regions are instances of Azure that are isolated from the main instance of Azure. You may need to use a sovereign region for compliance or legal purposes.

Azure sovereign regions include:

US DoD Central, US Gov Virginia, US Gov Arizona, and more: These regions are physical and logical network-isolated instances of Azure for U.S. government agencies and partners. These datacenters are operated by screened U.S. personnel and include additional compliance certifications.
China East, China North, and more: These regions are available through a unique partnership between Microsoft and 21Vianet, whereby Microsoft doesn't directly maintain the datacenters.
Next unit: Describe Azure management infrastructure

Describe Azure management infrastructure
Completed
100 XP
7 minutes
The management infrastructure includes Azure resources and resource groups, subscriptions, and accounts. Understanding this hierarchy helps you organize resources, control who can access what, and manage costs as your Azure usage grows.

Azure resources and resource groups
A resource is the basic building block of Azure. Anything you create, provision, or deploy is a resource. VMs, virtual networks, databases, and Azure AI services are all examples of resources.

<img width="1680" height="680" alt="image" src="https://github.com/user-attachments/assets/ead4a495-39bb-4713-ad1a-7731cfdea966" />

Resource groups are groupings of resources. Every resource must belong to exactly one resource group. You can move some resources between groups, but a resource is only associated with one group at a time. Resource groups can't be nested, and they can't be renamed after creation, so choose a clear naming convention from the start.

Actions you apply to a resource group affect all resources inside it. Deleting a resource group deletes everything in it. Granting or denying access applies to all its resources.

For example, if you're setting up a temporary dev environment, grouping all the resources together lets you delete the entire group when you're done. If you're running multiple projects, create a separate resource group for each so each team only sees and manages its own resources.

There are no hard rules for structuring resource groups — choose the approach that works best for your situation.

Azure subscriptions
In Azure, subscriptions are a unit of management, billing, and scale. Subscriptions let you organize resource groups and control billing separately from access.

<img width="1680" height="760" alt="image" src="https://github.com/user-attachments/assets/142eb2d2-a84e-4832-9ebd-e3fe4f2979cc" />

Using Azure requires an Azure subscription. A subscription provides access to Azure products and services and serves as a billing unit. An Azure subscription links to an Azure account, which is an identity in Microsoft Entra ID or in a directory that Microsoft Entra ID trusts.

An account can have multiple subscriptions, but only one is required. In a multi-subscription account, you can configure different billing models and access policies. There are two types of subscription boundaries:

Billing boundary: Determines how an Azure account is billed. You can create multiple subscriptions for different billing requirements. Azure generates separate billing reports and invoices for each subscription.
Access control boundary: Azure applies access-management policies at the subscription level. For example, you might create one subscription for your development work and another for production, each with different spending limits and access rules.
Create additional Azure subscriptions
You might create additional subscriptions to separate:

Environments: Subscriptions for lifecycle stages such as sandbox, development, test, and production. Access control occurs at the subscription level, making this a natural boundary.
Team and workload boundaries: Give each project its own subscription so costs are easy to track, or separate sandbox environments from production.
Billing: Create subscriptions to track costs separately — for instance, one for production workloads and another for development and testing.
Azure management groups
Resources go into resource groups, and resource groups go into subscriptions. For a small environment, that's enough. But when you have many subscriptions across multiple teams or geographies, you need a way to manage access and policies at a higher level.

Azure management groups sit above subscriptions. You organize subscriptions into management groups and apply governance conditions — like access policies or compliance rules — to the group. All subscriptions in a management group automatically inherit those conditions, just as resources inherit settings from their resource group. Management groups can be nested up to six levels deep (not counting the root level or the subscription level), letting you build a hierarchy that mirrors your organization.

Every Microsoft Entra tenant has a single top-level Tenant Root Group. All other management groups and subscriptions fold up to this root group, which lets you apply governance policies globally.

Management group, subscriptions, and resource group hierarchy
You can build a flexible structure of management groups and subscriptions to organize your resources into a hierarchy for unified policy and access management.

<img width="1680" height="1020" alt="image" src="https://github.com/user-attachments/assets/678505fd-e2fa-4aab-8740-5a3820eaf084" />

Examples of how you could use management groups:

Apply a policy across subscriptions. You could limit VM locations to the US West Region in a group called Production. This policy inherits to all subscriptions under that management group and applies to all VMs in those subscriptions. The resource or subscription owner can't override it, which strengthens governance.
Grant access to multiple subscriptions at once. By placing subscriptions under a management group, you can create one Azure RBAC assignment on the group. All sub-management groups, subscriptions, resource groups, and resources underneath inherit those permissions — no need to script Azure RBAC across individual subscriptions.
Important facts about management groups:

A single directory supports up to 10,000 management groups.
Each management group and subscription can have only one parent.
Next unit: Module assessment

Module assessment
200 XP
4 minutes
Choose the best response for each question.

Check your knowledge

1. How many resource groups can a resource be in at the same time?

One

Two

Three
Answer: A
2. What happens to the resources within a resource group when an action or setting at the Resource Group level is applied?

Current resources inherit the setting, but future resources don't.

Future resources inherit the setting, but current ones don't.

The setting is applied to current and future resources.
Answer: C
3. What Azure feature replicates resources across regions that are at least 300 miles away from each other?

Region pairs

Availability Zones

Sovereign regions
Answer: A

Summary
Completed
100 XP
2 minutes
In this module, you learned about the physical and management structure of Microsoft Azure. You were introduced to the relationship between datacenters, availability zones, and regions. You explored how the infrastructure supports the benefits of the cloud, such as high availability and reliability. You also learned about the management infrastructure of Azure. You explored how resources and resource groups are related, and how subscriptions and management groups can help manage resources.

Learning objectives
You should now be able to:

Describe Azure regions, region pairs, and sovereign regions.
Describe Availability Zones.
Describe Azure datacenters.
Describe Azure resources and Resource Groups.
Describe subscriptions.
Describe management groups.
Describe the hierarchy of resource groups, subscriptions, and management groups.
Explore with Copilot
 Tip

Try one of these prompts in Copilot Chat:

"Build a concept map that connects regions, Availability Zones, datacenters, resources, resource groups, subscriptions, and management groups."
"Design a subscription and management-group structure for an organization with multiple departments and compliance boundaries."
"Explain region pairs and sovereign regions, then recommend a resiliency approach for a workload with strict data residency requirements."

## Describe Azure compute services

This module focuses on core Azure compute services and when to use each option.

Learning objectives
Upon completion of this module, you'll be able to:

Compare compute types, including container instances, virtual machines, and functions

Describe virtual machine (VM) options, including VMs, Virtual Machine Scale Sets, and availability sets

Describe resources required for virtual machines

Describe application hosting options, including Azure Web Apps, containers, and virtual machines

Describe AI, machine learning, and IoT/Edge service categories in Azure

Describe Azure containers
Completed
100 XP
6 minutes
Virtual machines reduce costs compared to physical hardware, but they're still limited to a single operating system per VM. If you want to run multiple instances of an application on a single host machine, containers are an excellent choice.

What are containers?
Containers are a virtualization environment. Much like running multiple virtual machines on a single physical host, you can run multiple containers on a single physical or virtual host. Unlike virtual machines, you don't manage the operating system for a container. Each virtual machine runs its own operating system that you can connect to and manage. Containers are lightweight and designed to be created, scaled out, and stopped dynamically. You can create and deploy virtual machines as application demand increases, but containers are a lighter-weight, more agile method. Containers help you respond to changes on demand and restart quickly after a crash or hardware interruption. One of the most popular container engines is Docker, and Azure supports Docker.

Compare virtual machines to containers
The following video highlights several of the important differences between virtual machines and containers:

Azure Container Instances
Azure Container Instances offer the fastest and simplest way to run a container in Azure, without managing any virtual machines or adopting extra services. Azure Container Instances are a platform as a service (PaaS) offering. You upload your containers and the service runs them for you.

Azure Container Apps
Azure Container Apps are similar in many ways to a container instance. They let you get up and running right away, they remove the container management overhead, and they're a PaaS offering. Container Apps also include built-in load balancing and scaling, so your design can adapt to changing demand.

Azure Kubernetes Service
Azure Kubernetes Service (AKS) is a container orchestration service. An orchestration service manages the lifecycle of containers. When you're deploying a fleet of containers, AKS can make fleet management simpler and more efficient.

<img width="2520" height="1560" alt="image" src="https://github.com/user-attachments/assets/592a8fca-72e4-46d8-a3f1-72d8532a407b" />

Use containers in your solutions
Containers are often used to create solutions that use a microservice architecture. In this architecture, you break solutions into smaller, independent pieces. For example, you might split a website into a container hosting your front end, another hosting your back end, and a third for storage. This split lets you maintain, scale, or update each part of your app independently.

Imagine your website back end reaches capacity, but the front end and storage aren't stressed. With containers, you can scale the back end separately to improve performance. You can also change the storage service or modify the front end without affecting the other components.

Next unit: Describe Azure functions

Describe Azure functions
Completed
100 XP
4 minutes
Azure Functions is an event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers. If you build an app using VMs or containers, those resources have to be “running” in order for your app to function. With Azure Functions, an event wakes the function, alleviating the need to keep resources provisioned when there are no events.

<img width="2480" height="1520" alt="image" src="https://github.com/user-attachments/assets/defaedb0-e43c-4cbe-9cfa-4600758adc6b" />

Serverless computing in Azure

Benefits of Azure Functions
Using Azure Functions is ideal when you're only concerned about the code running your service and not about the underlying platform or infrastructure. Functions are commonly used when you need to perform work in response to an event (often via a REST request), timer, or message from another Azure service, and when that work can be completed quickly, within seconds or less.

Functions scale automatically based on demand, so they may be a good choice when demand is variable.

Azure Functions runs your code when it's triggered and automatically deallocates resources when the function finishes. In this model, Azure charges you only for the CPU time used while your function runs.

<img width="2360" height="1520" alt="image" src="https://github.com/user-attachments/assets/3493cb3a-e578-4d26-acbc-f76560dc49e9" />

Functions can be either stateless or stateful. When they're stateless (the default), they behave as if they restart every time they respond to an event. When they're stateful (called Durable Functions), the runtime passes a context through the function to track prior activity.

Functions are a key component of serverless computing. They're also a general compute platform for running any type of code. If the needs of your app change, you can deploy the project in an environment that isn't serverless. This flexibility lets you manage scaling, run on virtual networks, and even completely isolate the functions.

Next unit: Describe AI, machine learning, and IoT/Edge services in Azure

Describe AI, machine learning, and IoT/Edge services in Azure
Completed
100 XP
4 minutes
Azure includes service categories that help you build intelligent and connected solutions without starting from scratch.

Azure AI services
Azure AI services provides prebuilt capabilities for common AI scenarios, such as language, speech, vision, and document processing. These services are useful when you want to add intelligent features through APIs instead of training your own model first.

Azure OpenAI Service is another AI option in Azure that supports generative AI scenarios, such as chat and content generation, with built-in security and governance controls.

Agentic AI patterns
Agentic applications combine an AI model with instructions, context, and tool use to complete multistep goals. In Azure, you usually build these patterns by combining Azure AI services and Azure OpenAI Service with your own application logic.

At a fundamentals level, treat agentic AI as an application pattern built from Azure AI capabilities, not as a separate compute service category.

Azure Machine Learning
Use Azure Machine Learning when you need to build, train, and manage custom machine learning models. This option is a better fit when your scenario requires model development, experimentation, and lifecycle management.

IoT and Edge services
Azure IoT services help you connect, monitor, and manage devices.

Azure IoT Hub enables secure, bi-directional communication between cloud services and IoT devices.
Azure IoT Central provides a simplified software as a service (SaaS) IoT platform for solution builders.
Azure IoT Edge extends cloud capabilities to edge devices so some workloads can run closer to where data is generated.
This flow commonly starts with devices sending telemetry through IoT Hub, then uses cloud analytics to generate insights and model updates that IoT Edge runtime applies near the devices. IoT Central can simplify solution management for these connected-device scenarios.

<img width="2720" height="1560" alt="image" src="https://github.com/user-attachments/assets/7c4b5412-c4d7-42eb-971c-4b010a6e98f0" />

Choosing the right option
At a fundamentals level, use this decision pattern:

<img width="2240" height="1840" alt="image" src="https://github.com/user-attachments/assets/341b9339-1d79-47eb-b05e-10bb9cbd338b" />

Use Azure AI services when you need prebuilt AI features exposed through APIs.
Use Azure Machine Learning when you need custom model development and management.
Use Azure IoT services when your solution centers on connected devices and telemetry.
Next unit: Describe application hosting options

Describe application hosting options
Completed
100 XP
3 minutes
If you need to host your application on Azure, you might initially turn to a virtual machine (VM) or containers. Both VMs and containers provide excellent hosting solutions. VMs give you maximum control of the hosting environment and allow you to configure it exactly how you want. VMs also may be the most familiar hosting method if you’re new to the cloud. Containers, with the ability to isolate and individually manage different aspects of the hosting solution, can also be a robust and compelling option.

There are other hosting options that you can use with Azure, including Azure App Service.

<img width="2640" height="1560" alt="image" src="https://github.com/user-attachments/assets/58a4bea6-9cae-49c5-85db-43690040fbe1" />

Azure App Service
App Service lets you build and host web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of your choice without managing infrastructure. It offers automatic scaling and high availability. App Service supports Windows and Linux and supports automated deployments from GitHub, Azure DevOps, or any Git repo for continuous deployment.

Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. It lets you focus on building and maintaining your app while Azure keeps the environment up and running. App Service supports multiple languages and frameworks, including .NET, .NET Core, Java, PHP, Python, and Node.js.

Types of app services
With App Service, you can host most common app styles:

Web apps
API apps
WebJobs
Mobile apps
App Service handles most of the infrastructure decisions you deal with in hosting web-accessible apps:

Deployment and management are integrated into the platform.
Endpoints can be secured.
Sites can be scaled quickly to handle high traffic loads.
The built-in load balancing and traffic manager provide high availability.
All of these app styles are hosted in the same infrastructure and share these benefits. This flexibility makes App Service the ideal choice to host web-oriented applications.

Web apps
App Service includes full support for hosting web apps by using ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP, or Python. You can choose either Windows or Linux as the host operating system.

API apps
Much like hosting a website, you can build REST-based web APIs by using your choice of language and framework. App Service provides full Swagger support and the ability to package and publish your API in Azure Marketplace. The published APIs can be consumed from any HTTP- or HTTPS-based client.

WebJobs
You can use the WebJobs feature to run a program (.exe, Java, PHP, Python, or Node.js) or script (.cmd, .bat, PowerShell, or Bash) in the same context as a web app, API app, or mobile app. They can be scheduled or run by a trigger. WebJobs are often used to run background tasks as part of your application logic.

Mobile apps
Use the Mobile Apps feature of App Service to quickly build a back end for iOS and Android apps. With just a few actions in the Azure portal, you can:

Store mobile app data in a cloud-based SQL database.
Authenticate customers against common social providers, such as MSA, Google, X, and Facebook.
Send push notifications.
Execute custom back-end logic in C# or Node.js.
On the mobile app side, there's SDK support for native iOS and Android, Xamarin, and React Native apps.

Next unit: Module assessment

Module assessment
Completed
200 XP
4 minutes
Great job! You passed the module assessment.
Module assessment passed

Great job! You passed the module assessment.
Score: 100%

Choose the best response for each question.

Check your knowledge

1. Which Azure Virtual Machine feature staggers updates across VMs based on their update domain and fault domain?

Availability sets
Correct

Scale sets

Update sets


2. Which Azure compute option is event-driven and serverless, so you can run code without managing virtual machines?

Azure Functions
Correct

Azure Virtual Machines

Azure Container Instances
3. Which Azure service lets organizations host web apps and APIs without managing the underlying infrastructure?

Azure App Service
Correct

Azure Virtual Machines

Azure ExpressRoute
4. Which Azure service category provides prebuilt APIs for capabilities like vision, speech, and language without training your own model from scratch?

Azure AI services
Correct

Azure Virtual Machines

Azure Virtual Networks
Next unit: Summary

Summary
Completed
100 XP
2 minutes
In this module, you learned about core Azure compute services and when to use them. You reviewed virtual machines and options such as virtual machine scale sets and virtual machine availability sets. You explored containers, Azure Functions, application hosting options, and Azure AI, machine learning, and IoT/Edge service categories.

You learned that agentic AI is an application pattern that can be built by combining Azure AI capabilities with application logic when a solution needs multistep reasoning and tool use.

Learning objectives
You should now be able to:

Compare compute types, including container instances, virtual machines, and functions.
Describe virtual machine options, including virtual machines (VMs), virtual machine scale sets, and virtual machine availability sets.
Describe resources required for virtual machines.
Describe application hosting options, including Azure Web Apps, containers, and virtual machines.
Describe AI, machine learning, and IoT/Edge service categories in Azure.
Recognize agentic AI as an application pattern built from Azure AI capabilities.
Additional resources
The following additional resources are intended to provide more information on topics in this module or on additional topics related to this module.

Host a web application with Azure App Service is a Microsoft Learn module that explores the process of hosting a web application in Azure.
Explore with Copilot
 Tip

Try one of these prompts in Copilot Chat:

"Build a decision matrix for when to use virtual machines, containers, Azure Functions, and Azure App Service across three realistic workloads."
"Explain scale sets, availability sets, and Availability Zones with one failure scenario that shows how each option improves resiliency."
"Create a short architecture walkthrough that combines compute hosting with one AI or IoT Edge service and explains why each component was chosen."

## Describe Azure networking services































