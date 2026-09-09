# 19. IAM Cheat Sheet

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

End-of-section **cheat sheets** list **core exam knowledge** so you can review without wading through AWS docs. This sheet is **IAM**: what you can manage, the **new-user** default, **users / groups / roles / policies**, **authentication** methods, **MFA**, **evaluation logic**, **managed vs inline** policies, **instance profiles**, **STS**, **federation**, and **cross-account** access. IAM is **not** for application-level authentication. It is **global**, **eventually consistent**, and replicates across data centers worldwide.

## Detailed Explanation

<details>
  <summary>Step 1 — Know what IAM manages and how new users start</summary>

### Step 1 — Know what IAM manages and how new users start

- [x] **What IAM is and what you manage**
  - **IAM** = AWS **Identity and Access Management**.
  - Securely control **individual** and **group** access to AWS resources.
  - Makes it easy to give **multiple users** secure access.
  - You can manage: **users**, **groups**, **access policies**, **roles**, **user credentials**, **password policies**, **MFA**, and **API keys** (CLI / programmatic).
  - Provides **centralized control** of the account and **shared access**.
- [x] **New users and IAM users**
  - New users have **NO** access to any AWS services by default — they can only **log in** to the console.
  - Permission must be **explicitly granted**.
  - An IAM user is an individual granted access to an AWS account.
  - Each user has three main components: a **username**, a **password**, and **permissions**.
  - You can apply **granular** permissions and assign **access keys**, **passwords**, and **MFA** devices.
  - IAM is **not** used for **application-level** authentication.
- [x] **Federation (high level)**
  - **Identity federation** (including **AD**, **Facebook**, and others) can give secure access **without** creating an IAM user.

</details>

<details>
  <summary>Step 2 — Enforce MFA and remember IAM’s global, eventually consistent design</summary>

### Step 2 — Enforce MFA and remember IAM’s global, eventually consistent design

- [x] **MFA**
  - Can be enabled / enforced on the **account** and on **individual users**.
  - Uses a device that generates random **six-digit**, **single-use** codes.
  - Three ways to authenticate with MFA:
    - **Management Console** — username, password, and authentication code.
    - **AWS API** — restrictions in IAM policies; developers request **temporary** credentials and pass MFA parameters in **STS** API requests.
    - **AWS CLI** — temporary credentials from STS (`aws sts get-session-token`).
  - Best practice: MFA for **all** users; **U2F** or **hardware** MFA for **privileged** users.
- [x] **IAM is global and eventually consistent**
  - IAM is **universal (global)** — it does **not** apply to regions.
  - It is **eventually consistent**.
  - Data is replicated across **multiple data centers** worldwide.

</details>

<details>
  <summary>Step 3 — Handle root access, sign-in, and programmatic entry points</summary>

### Step 3 — Handle root access, sign-in, and programmatic entry points

- [x] **Root, power user, and temporary credentials**
  - The **root account** is created when you set up AWS. It has complete **Admin** access by default (the only identity that does).
  - Best practice: do **not** use root for anything other than **billing**.
  - **Power user** access: all permissions **except** managing **groups** and **users** in IAM.
  - Temporary security credentials = **access key ID** + **secret access key** + **security token**.
  - IAM can assign temporary credentials so users get **temporary** access to services / resources.
- [x] **Sign-in**
  - You must provide **account ID** or **account alias** plus username and password.
  - Sign-in URL includes the ID or alias, for example `https://My_AWS_Account_ID.signin.aws.amazon.com/console/`.
  - Or sign in at `https://console.aws.amazon.com/` and enter the ID / alias manually.
- [x] **Integrations and how to call IAM**
  - IAM integrates with many AWS services.
  - IAM supports **PCI DSS** compliance.
  - AWS recommends **AWS SDKs** for programmatic IAM API calls.
  - You can also use the **IAM Query API** to call the IAM web service directly.

</details>

<details>
  <summary>Step 4 — Trace a request from principal to allow or deny</summary>

### Step 4 — Trace a request from principal to allow or deny

- [x] **IAM elements — principals and requests**
  - A **principal** is an entity that can take an action on an AWS resource.
  - Your administrative IAM user is your **first** principal.
  - Users and services can **assume a role**; IAM supports **federated users** and **programmatic** application access.
  - IAM **users**, **roles**, **federated users**, and **applications** are all principals.
  - Principals send **requests** via the **console**, **CLI**, **SDKs**, or **APIs**.
  - A request includes: the **action** (operation), the **resource**, and **principal / environment** information.
  - AWS builds a **request context**: principal, **aggregate permissions**, environment data (**IP**, user agent, SSL status), and **resource** data.

<img width="962" height="461" alt="image" src="https://github.com/user-attachments/assets/764845ed-5822-4deb-a469-cb4cd29469f5" />

- [x] **Authentication vs authorization**
  - A principal must be **authenticated** to send a request.
  - Console: **username** and **password**.
  - API / CLI: **access key** and **secret key**.
  - **Authorization:** IAM uses the request context to find matching **policies** and allow or deny.
  - Policies are **JSON** documents in IAM.
  - Policy kinds here: **user (identity) based** and **resource-based**.
  - IAM checks **each** policy that matches the request context.
  - A single policy with a **deny** → IAM **denies** and **stops** evaluating (**explicit deny**).
- [x] **Evaluation logic (cheat-sheet version)**
  - By default all requests are denied (**implicit deny**).
  - An **explicit allow** overrides the implicit deny.
  - An **explicit deny** overrides any explicit allows.
  - Only **root** has access to all resources by default.

```text
# Evaluation (short)
# 1) implicit deny (except root full access)
# 2) explicit allow (identity- or resource-based) can allow
# 3) boundary / SCP / session policy may implicit-deny that allow
# 4) explicit deny in ANY policy wins and stops evaluation
```
- [x] **Actions and resources**
  - **Actions** are defined by a service — view, create, edit, delete, and so on.
  - Actions not **explicitly allowed** are denied.
  - To allow an action, include it in a policy on the **principal** or the **affected resource**.
  - A **resource** is an entity in a service (examples: **EC2** instances, **S3** buckets, **IAM** users, **DynamoDB** tables).
  - Each service defines the actions you can perform on its resources.

</details>

<details>
  <summary>Step 5 — Compare console passwords, access keys, and server certificates</summary>

### Step 5 — Compare console passwords, access keys, and server certificates

- [x] **Authentication methods — console password**
  - Password for interactive sessions such as the **Management Console**.
  - You can allow users to change their own passwords.
  - To allow only **selected** users: disable the “all users” option and grant change-password via an **IAM policy**.
- [x] **Authentication methods — access keys**
  - Combination of **access key ID** and **secret access key**.
  - A user can have **two active** access keys at a time.
  - Used for programmatic calls: **API**, **CLI**, **PowerShell**.
  - You can create, modify, view, or **rotate** them.
  - IAM returns the ID and secret at **creation**; the **secret is shown only then**. If lost, create a **new** key.
  - Store keys **securely**.
  - Users can change their own keys through **IAM policy** (not from the console).
  - You can **disable** a key so it cannot be used for API calls.
- [x] **Authentication methods — server certificates**
  - **SSL/TLS** certificates to authenticate with **some** AWS services.
  - AWS recommends **AWS Certificate Manager (ACM)** to provision, manage, and deploy them.
  - Use IAM for certificates **only** when you must support **HTTPS** in a region **ACM does not** support.

<img width="737" height="441" alt="image" src="https://github.com/user-attachments/assets/0e0f8402-b47b-497f-aa28-4c1a207ad0b8" />

</details>

<details>
  <summary>Step 6 — Review users, groups, and roles in detail</summary>

### Step 6 — Review users, groups, and roles in detail

- [x] **IAM users (detail)**
  - Entity that represents a **person** or a **service**.
  - Can be assigned: access key ID + secret (API / CLI / SDK) and/or a **console password**.
  - By default users **cannot access anything**.
  - Root credentials: **email** used to create the account + **password**.
  - Root has **full admin**; those permissions **cannot be restricted**.
  - Root best practices: do **not** use root credentials, do **not share** them, create an IAM user with admin as needed, enable **MFA**.
  - Users that represent applications are **service accounts**.
  - Up to **5,000 users** per account.
  - Each user has a **friendly name** and an **ARN** that uniquely identifies them across AWS.
  - A **unique ID** is returned only when you create the user via **API**, **PowerShell**, or **CLI**.
  - Create **individual** IAM accounts (do not share accounts).
  - Access keys are **not** a console password and **cannot** log you into the console.
  - Access key ID + secret can be generated **once**; regenerate if lost.
  - A **password policy** can enforce length / complexity (applies to **all** users).
  - Allow or disallow password changes with an IAM policy.
  - Change access keys and passwords **regularly**.

<img width="959" height="462" alt="image" src="https://github.com/user-attachments/assets/c1e3d56d-53cf-49f1-a837-798d298502f1" />

- [x] **Groups**
  - Collections of users with **policies** attached.
  - A group is **not an identity** and **cannot** be a **principal** in a policy.
  - Use groups to assign permissions; follow **least privilege**.
  - You **cannot nest** groups.

<img width="914" height="486" alt="image" src="https://github.com/user-attachments/assets/2c88a7b3-8851-4d37-8f0a-3e6a8c89365e" />

- [x] **Roles**
  - Created, then **assumed** by trusted entities; they define permissions for AWS service requests.
  - Delegate permissions to users and services **without** permanent credentials (username / password).
  - IAM users or AWS services assume a role to get **temporary** credentials for API calls.
  - **No** password or access keys are stored on the role itself.
  - Users can assume a role **temporarily** for a specific task.
  - A **federated** user who signs in via an external IdP can be assigned a role.
  - Temporary credentials with roles **automatically expire**.
  - Assume via **console**, **CLI**, **PowerShell**, or **API**.

<img width="575" height="487" alt="image" src="https://github.com/user-attachments/assets/c66967b7-b5a6-498e-a221-3c0135524164" />

</details>

<details>
  <summary>Step 7 — Attach roles to EC2 and delegate with trust policies</summary>

### Step 7 — Attach roles to EC2 and delegate with trust policies

- [x] **IAM roles with EC2**
  - Grant apps on **EC2** permission for AWS API requests using **instance profiles**.
  - Only **one role** per EC2 instance at a time.
  - Assign the role at **launch** or **any time after**.
  - CLI / API: you must create **instance profiles** **manually** (the **console** does this automatically / transparently).
  - Applications retrieve temporary credentials from **instance metadata**.
- [x] **Role delegation (two policies)**
  - **Permissions policy** — grants the role user the required permissions on a resource.
  - **Trust policy** — specifies the **trusted accounts** allowed to assume the role.
  - Wildcards (`*`) **cannot** be specified as a **principal**.
  - A permissions policy must also be attached to the **user in the trusted account**.

</details>

<details>
  <summary>Step 8 — Write policies and choose a delivery type</summary>

### Step 8 — Write policies and choose a delivery type

- [x] **Policies**
  - Documents that define permissions; applied to users, groups, and roles.
  - Written in **JSON** (attribute / value pairs).
  - All permissions **implicitly denied** by default.
  - The **most restrictive** policy is applied.
  - Use the **IAM Policy Simulator** to understand, test, and validate policies.
  - Use the **Condition** element for extra logic.

<img width="619" height="499" alt="image" src="https://github.com/user-attachments/assets/c1fcff05-b8ed-4504-a48f-4abb3186188d" />

- [x] **Three policy delivery types**
  - **AWS managed** — created and administered by **AWS**; common **job-function** use cases; attach to many users / groups / roles **within and across** accounts; you **cannot** change the permissions.
  - **Customer managed** — standalone policy you create in **your** account; attach to many identities **in that account only**; often copied from a managed policy then customized; use when AWS managed policies do not fit.
  - **Inline** — embedded in the user, group, or role (**1:1**). Deleting the entity **deletes** the policy. AWS recommends **managed** in most cases. Inline is useful when you must be sure those permissions are **not** assigned to anyone else.
- [x] **AWS managed policies are standalone**
  - A standalone policy has its own **ARN** that includes the policy name.
  - You cannot change permissions in AWS managed policies.
  - Job-function managed policies include: **Administrator**, **Billing**, **Database Administrator**, **Data Scientist**, **Developer Power User**, **Network Administrator**, **Security Auditor**, **Support User**, **System Administrator**, **View-Only User**.
- [x] **IAM policy evaluation logic (advanced)**
  - Default: all requests **implicitly denied**. Root has **full access**.
  - An **explicit allow** in an identity-based or resource-based policy overrides that default.
  - If a **permissions boundary**, **Organizations SCP**, or **session policy** is present, it might override the allow with an **implicit deny**.
  - An **explicit deny** in **any** policy overrides any allows.
  - **Identity-based:** attached to a user, group, or role; grant permissions to entities (users and roles).
  - **Resource-based:** grant permissions to the **principal** named on the resource.
  - **Permissions boundary:** maximum an identity-based policy can grant to a user or role.
  - **SCPs:** maximum for an **organization** or **OU**.
  - **Session policies:** passed when you programmatically create a temporary session for a role or federated user.

<img width="1024" height="470" alt="image" src="https://github.com/user-attachments/assets/f7713753-3341-4fb8-be0c-754b4ffeb668" />

</details>

<details>
  <summary>Step 9 — Pass roles with instance profiles and issue STS credentials</summary>

### Step 9 — Pass roles with instance profiles and issue STS credentials

- [x] **IAM instance profiles**
  - A **container** for an IAM role used to pass role information to an **EC2** instance when it **starts**.
  - An instance profile can contain **only one** IAM role; a role can be in **multiple** instance profiles.

```bash
# Create an instance profile (required manually on CLI / API; console does this for you)
aws iam create-instance-profile

# Add a role to an instance profile
aws iam add-role-to-instance-profile

# List instance profiles (account-wide, or those that include a role)
aws iam list-instance-profiles
aws iam list-instance-profiles-for-role

# Get one instance profile
aws iam get-instance-profile

# Remove a role from an instance profile
aws iam remove-role-from-instance-profile

# Delete an instance profile
aws iam delete-instance-profile
```

<img width="1024" height="407" alt="image" src="https://github.com/user-attachments/assets/681c79dd-c895-42f2-897e-b4ae9df4d47e" />

- [x] **AWS STS**
  - Web service that issues **temporary**, **limited-privilege** credentials for IAM users or **federated** users you authenticate.
  - By default STS is a **global** service; requests go to `https://sts.amazonaws.com`.
  - You can send STS requests to **regional** endpoints (lower **latency**).
  - Credentials still work **globally**.
  - STS supports **CloudTrail** (logs to an **S3** bucket).
  - Temporary credentials work like long-term access keys, except: they are **short-term** (minutes to hours); after **expiry** AWS no longer accepts them; they are **not stored** with the user — generated **dynamically**; the user can request **new** ones if still permitted.
  - Advantages: no need to **distribute / embed** long-term keys; access without defining an AWS identity (basis of **roles** and **federation**); limited lifetime so you need not **rotate** or **revoke** them; after expiry they **cannot be reused** (you set duration up to a maximum).
  - STS returns: access key ID + secret, a **session token**, and **expiration / duration**.
- [x] **STS APIs**
  - **`AssumeRole`** — IAM users only (can be used for **MFA**).
  - **`AssumeRoleWithSAML`** — anyone who passes a **SAML** auth response from a known / trusted IdP.
  - **`AssumeRoleWithWebIdentity`** — anyone who passes a **web identity token** from a known / trusted IdP.
  - **`GetSessionToken`** — IAM user or **root** (can be used for **MFA**).

```bash
# MFA / CLI: obtain temporary credentials from STS
aws sts get-session-token
```

Default STS endpoint: `https://sts.amazonaws.com`. You can use a **regional** STS endpoint for lower latency; credentials still work **globally**.
  - **`GetFederationToken`** — IAM user or **root**.
  - AWS recommends **Amazon Cognito** for federation with **Internet** identity providers.

</details>

<details>
  <summary>Step 10 — Federate users, cross accounts, and review best practices</summary>

### Step 10 — Federate users, cross accounts, and review best practices

- [x] **Where users can come from**
  - **Federation (typically AD):** **SAML 2.0**; temporary access from AD credentials; does **not** need an IAM user; **SSO** to the console without assigning IAM credentials.
  - **Federation with mobile apps:** **Facebook / Amazon / Google** or other **OpenID** providers.
  - **Cross-account access:** users in one account access resources in another — via a **resource-based** policy on the resource, **or** by **assuming a role** (identity-based) in that account.
- [x] **STS identity-broker scenarios**
  - **Scenario 1:** Identity Broker talks to **LDAP** and **STS**. Broker authenticates with **LDAP first**, then **STS**. The application then gets **temporary** access to AWS resources.
  - **Scenario 2:** Broker talks to **LDAP** and **STS**. Broker authenticates with **LDAP first**, then gets an **IAM role** associated with the user. The application authenticates with **STS**, **assumes that role**, and uses the role to call the service.
- [x] **Cross-account access**
  - Useful when a customer has separate accounts (example: **development** and **production**).
  - Makes it easier to work in a **multi-account** / **multi-role** environment by **switching roles** in the console.
  - Sign in with your IAM username, then switch the console to manage another account **without** entering another username and password.
  - Same two mechanisms: **resource-based** policy on the target resource, or **assume a role** in the other account.

<img width="804" height="347" alt="image" src="https://github.com/user-attachments/assets/b013de18-433b-4d73-a946-8690cab3c420" />

- [x] **IAM best-practice checklist**
  - Lock away **root user access keys**.
  - Use **roles** to delegate permissions.
  - Grant **least privilege**.
  - Get started with **AWS managed policies**.
  - **Validate** your policies.
  - Prefer **customer managed** over **inline**.
  - Use **access levels** to review permissions.
  - Configure a **strong password policy**.
  - Enable **MFA**.
  - Use roles for apps on **EC2**.
  - Do **not share** access keys.
  - **Rotate** credentials regularly.
  - **Remove** unnecessary credentials.
  - Use **policy conditions** for extra security.
  - **Monitor** activity in the account.

</details>

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is a **cheat sheet**, not a console walkthrough. The notes mention a short video on root MFA and deleting the root access key — that is not reproduced here.

### **Overview**

- [ ] Use this sheet for **revision**, not as a first-pass lesson.
- [ ] You will:
  - [ ] Recite the **new-user** default, **root** vs **power user**, and **MFA** (console / API / CLI).
  - [ ] Distinguish **managed**, **customer managed**, and **inline** policies.
  - [ ] Trace **evaluation** (implicit deny → allow → boundary/SCP/session → explicit deny).
  - [ ] Name **instance profiles**, **STS** APIs, and the two **identity-broker** flows.

```bash
# Create an instance profile (required manually on CLI / API; console does this for you)
aws iam create-instance-profile

# Add a role to an instance profile
aws iam add-role-to-instance-profile

# List instance profiles (account-wide, or those that include a role)
aws iam list-instance-profiles
aws iam list-instance-profiles-for-role

# Get one instance profile
aws iam get-instance-profile

# Remove a role from an instance profile
aws iam remove-role-from-instance-profile

# Delete an instance profile
aws iam delete-instance-profile
```

```bash
# MFA / CLI: obtain temporary credentials from STS
aws sts get-session-token
```

Default STS endpoint: `https://sts.amazonaws.com`. You can use a **regional** STS endpoint for lower latency; credentials still work **globally**.

```text
# Console sign-in (account in the URL)
https://My_AWS_Account_ID.signin.aws.amazon.com/console/
# Or enter account ID / alias at
https://console.aws.amazon.com/

# Role delegation
#   permissions policy → what the role can do
#   trust policy       → who may assume (no * as Principal)
#   plus a policy on the user in the trusted account

# STS returns: access key ID + secret, session token, expiration
# AssumeRole | AssumeRoleWithSAML | AssumeRoleWithWebIdentity
# GetSessionToken | GetFederationToken
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What can you manage with IAM, and what is it not for?

<details>
<summary>Answer</summary>

- [x] Users, groups, access policies, roles, credentials, password policies, **MFA**, and **API keys**.
- [x] Centralized control and **shared access** to the account.
- [x] IAM is **not** for **application-level** authentication.

</details>

### Question 2: What access does a new IAM user have, and what three components does a user have?

<details>
<summary>Answer</summary>

- [x] **No** access to services — they can only **log in**.
- [x] Permissions must be **explicitly granted**.
- [x] Three components: **username**, **password**, **permissions**.

</details>

### Question 3: How can you authenticate with MFA (three ways), and what is the privileged-user best practice?

<details>
<summary>Answer</summary>

- [x] **Console:** username, password, and a **six-digit** code.
- [x] **API:** policy restrictions; pass MFA parameters on **STS** requests.
- [x] **CLI:** `aws sts get-session-token`.
- [x] MFA for **all** users; **U2F** or **hardware** MFA for **privileged** users.

</details>

### Question 4: Is IAM regional? What consistency model does it use?

<details>
<summary>Answer</summary>

- [x] IAM is **universal / global** — not tied to a region.
- [x] It is **eventually consistent**.
- [x] Data is replicated across **multiple data centers** worldwide.

</details>

### Question 5: What is the root account for, and what does Power user allow?

<details>
<summary>Answer</summary>

- [x] Root is created at signup and has complete **Admin** access by default.
- [x] Best practice: use root for **billing** only.
- [x] **Power user:** everything **except** managing IAM **users** and **groups**.

</details>

### Question 6: What makes up temporary security credentials?

<details>
<summary>Answer</summary>

- [x] **Access key ID**
- [x] **Secret access key**
- [x] **Security token**

</details>

### Question 7: What is a principal, and what is in a request context?

<details>
<summary>Answer</summary>

- [x] A **principal** is an entity that can act on an AWS **resource** (users, roles, federated users, applications).
- [x] Request context includes the **principal**, **aggregate permissions**, environment (**IP**, user agent, SSL), and **resource** data.

</details>

### Question 8: Recite the short evaluation rules (implicit / explicit).

<details>
<summary>Answer</summary>

- [x] Default is **implicit deny** (except **root** has full access).
- [x] An **explicit allow** overrides implicit deny.
- [x] An **explicit deny** overrides any allows and **stops** evaluation.

</details>

### Question 9: Access keys — how many can be active, when is the secret shown, and can they log into the console?

<details>
<summary>Answer</summary>

- [x] Up to **two active** keys per user.
- [x] The **secret** is returned **only at creation**; if lost, create a **new** key.
- [x] Keys are **not** a password and **cannot** sign in to the console.

</details>

### Question 10: When do you use IAM for server certificates instead of ACM?

<details>
<summary>Answer</summary>

- [x] Prefer **ACM** to provision, manage, and deploy **SSL/TLS** certificates.
- [x] Use **IAM** only when you need **HTTPS** in a region **ACM does not** support.

</details>

### Question 11: What cannot a group be, and can you nest groups?

<details>
<summary>Answer</summary>

- [x] A group is **not an identity** and **cannot** be a **principal** in a policy.
- [x] You **cannot nest** groups.

</details>

### Question 12: What two policies are on a delegated role, and can the trust principal be `*`?

<details>
<summary>Answer</summary>

- [x] **Permissions policy** — what the role can do on resources.
- [x] **Trust policy** — which **trusted accounts** may assume the role.
- [x] Wildcards (`*`) **cannot** be specified as a **principal**.
- [x] The user in the trusted account also needs a **permissions** policy.

</details>

### Question 13: How do IAM roles work with EC2 and instance profiles?

<details>
<summary>Answer</summary>

- [x] An **instance profile** is a **container** that passes a role to an instance at **start**.
- [x] **One role** per instance at a time; a role can sit in **multiple** profiles.
- [x] Console creates the profile for you; **CLI / API** require creating it **manually**.
- [x] Apps get temporary credentials from **instance metadata**.

</details>

### Question 14: AWS managed vs customer managed vs inline — who owns them, and when is inline useful?

<details>
<summary>Answer</summary>

- [x] **AWS managed:** AWS owns them; job functions; attach **across accounts**; **cannot** edit permissions.
- [x] **Customer managed:** you own them; attach only **in your account**; customize when managed policies do not fit.
- [x] **Inline:** **1:1** with the entity; deleted when the entity is deleted.
- [x] Prefer **managed**; use inline when those permissions must **not** be reused on anyone else.

</details>

### Question 15: If a boundary, SCP, or session policy is present, what can happen to an explicit allow?

<details>
<summary>Answer</summary>

- [x] It might override the allow with an **implicit deny**.
- [x] An **explicit deny** in **any** policy still wins over any allow.

</details>

### Question 16: Name the five STS APIs and who can call each.

<details>
<summary>Answer</summary>

- [x] **`AssumeRole`** — IAM users only (can include **MFA**).
- [x] **`AssumeRoleWithSAML`** — a **SAML** response from a trusted IdP.
- [x] **`AssumeRoleWithWebIdentity`** — a **web identity token** from a trusted IdP.
- [x] **`GetSessionToken`** — IAM user or **root** (can include **MFA**).
- [x] **`GetFederationToken`** — IAM user or **root**.

</details>

### Question 17: What are the advantages of STS temporary credentials?

<details>
<summary>Answer</summary>

- [x] You do not **distribute** or **embed** long-term keys in an application.
- [x] Users can access AWS **without** an IAM identity (roles and **federation**).
- [x] Limited lifetime — no need to **rotate** or **revoke** when done.
- [x] After **expiry** they cannot be reused.

</details>

### Question 18: How do the two identity-broker scenarios differ?

<details>
<summary>Answer</summary>

- [x] Both: broker talks to **LDAP** and **STS**; **LDAP authenticates first**.
- [x] **Scenario 1:** broker then authenticates with **STS**; the app gets **temporary** access.
- [x] **Scenario 2:** broker gets the user’s **IAM role**; the app calls **STS**, **assumes the role**, and uses that role to call the service.

</details>

### Question 19: How do you get cross-account access?

<details>
<summary>Answer</summary>

- [x] Put a **resource-based** policy on the resource in the other account with the permissions you need.
- [x] **Or** assume a **role** (identity-based) in that account.
- [x] In the console you can **switch roles** without signing in again (useful for **dev** vs **prod** accounts).

</details>

### Question 20: How many IAM users per account, and what IDs does a user have?

<details>
<summary>Answer</summary>

- [x] Up to **5,000** users per account.
- [x] A **friendly name** and an **ARN** that uniquely identifies the user across AWS.
- [x] A **unique ID** is returned only when you create the user via **API**, **PowerShell**, or **CLI**.

</details>

</details>

## Summary

**IAM** centrally controls who can use AWS resources (**users**, **groups**, **roles**, **policies**, credentials, **MFA**, API keys). It is **not** for app-level auth. New users can **log in** with **no** access. IAM is **global** and **eventually consistent**. Use **root** for **billing** only; **Power user** cannot manage IAM users/groups. **MFA** is a six-digit code via console, API+STS, or `aws sts get-session-token`; hardware/U2F for privileged users. Auth methods: console **password**, **access keys** (two active; secret once; not for console login), **server certificates** (prefer **ACM**). **Groups** are not principals and cannot nest. **Roles** have no long-term keys; **trust** + **permissions** policies (no `*` principal); **EC2** uses an **instance profile** (one role per instance; CLI creates profiles manually). Evaluation: **implicit deny** → **explicit allow** → boundary/**SCP**/session may implicit-deny → **explicit deny** wins. Prefer **AWS** then **customer managed** policies; **inline** is 1:1. **STS** issues temporary credentials (`AssumeRole*`, `GetSessionToken`, `GetFederationToken`); federate with **SAML**/AD, **OpenID** mobile IdPs, or **cross-account** resource policies / role switch. Identity brokers: LDAP first, then STS (direct temps or assume a role). Best practices: lock root keys, least privilege, MFA, roles on EC2, rotate/remove credentials, conditions, monitor.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
- [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)
- [Job functions managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
- [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
- [MFA in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
- [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
- [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)
- [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)
- [GetSessionToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html)
- [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html)
- [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
- [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
- [Switch to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)
- [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
- [IAM and PCI DSS](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-compliance.html)
