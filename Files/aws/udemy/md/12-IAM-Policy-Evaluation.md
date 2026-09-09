[← Course contents](../../01.md)

# 12. IAM policy evaluation

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This lesson covers **IAM policy evaluation logic**: what AWS does when a principal tries to access a resource. Every decision **starts with deny** (nothing is allowed by default). An **explicit deny** always wins. Then AWS walks applicable **SCPs**, **resource-based policies**, **identity-based policies**, **permissions boundaries**, and **session policies**, looking for an **allow**. Requests arrive from the **console**, **CLI**, or **API**; IAM **authenticates** first, then builds a **request context** and evaluates **all** relevant policies. Effective permissions depend on the combination: identity + resource is a **union**; identity + boundary or identity + SCP is an **intersection**.

## Detailed Explanation

<details>
  <summary>Step 1 — Start every decision with a deny</summary>

### Step 1 — Start every decision with a deny

- [x] **Default: start with deny**
  - Every decision **starts with a deny**.
  - Permissions are **not allowed by default** — everything is denied until AWS finds an **allow**.
  - AWS then evaluates **all applicable policies**.
- [x] **Explicit deny always wins**
  - If any applicable policy has an **explicit deny**, the **final decision is deny**.
  - An explicit deny **always overrides** any allow.
  - If there is no explicit deny, evaluation continues.

</details>

<details>
  <summary>Step 2 — Check for an applicable Organizations SCP</summary>

### Step 2 — Check for an applicable Organizations SCP

- [x] **AWS Organizations SCPs**
  - AWS checks whether the principal’s **account** is in an **organization** with an applicable **service control policy (SCP)**.
  - If **no** applicable SCP, skip to the next stage.
  - If there **is** an SCP: there must be an **allow** for the action.
  - SCP present but **no allow** → **deny**.
  - SCP **allow** → continue.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c98c7faa-db9b-45a3-b952-1a19fa1951d8" />

</details>

<details>
  <summary>Step 3 — Evaluate resource-based and identity-based policies</summary>

### Step 3 — Evaluate resource-based and identity-based policies

- [x] **Resource-based policy**
  - Does the requested resource have a **resource-based policy**?
  - Example: **Amazon S3 bucket policies**.
  - If a resource-based policy exists, AWS checks for an **allow**.
  - How resource-based and identity-based policies combine is covered **later**; if there is a resource-based allow, that path still matters.
  - If there is **no** resource-based allow, evaluation continues to **identity-based** policies.
- [x] **Identity-based policy**
  - If an identity-based policy applies, AWS checks for an **allow**.
  - **No allow** in the resource-based policy **and** **no allow** in the identity-based policy → **implicit deny**.
  - If there **is** an allow for the action, evaluation continues.

</details>

<details>
  <summary>Step 4 — Apply permissions boundaries and session policies</summary>

### Step 4 — Apply permissions boundaries and session policies

- [x] **Permissions boundary**
  - AWS checks whether the principal has a **permissions boundary**.
  - If **yes**, the boundary must also **allow** the action for that principal.
  - Boundary allow → continue.
  - Boundary does **not** allow → **deny**.
- [x] **Session principal / session policy**
  - AWS checks whether the principal is a **session principal**.
  - If **no** → **allow** (at this stage).
  - If **yes** → there must be a **session policy** with an **allow**; otherwise **deny**.
  - The instructor also notes a **role session** check on the AWS chart (this stage is dense — spend time on the official evaluation diagram).

</details>

<details>
  <summary>Step 5 — Trace how a request is authenticated and given context</summary>

### Step 5 — Trace how a request is authenticated and given context

- [x] **Steps for authorizing a request**
  - Requests come from the **Management Console**, the **CLI**, or the **API**, and go to **IAM**.
  - **1. Authenticate** the principal (prove who they are). Example: **username and password** for the console.
  - **2. Form the request context**, then **process** it (evaluate policies).
  - **3. Decide** whether the request is **allowed** or **denied**.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/830afefb-b062-4dc8-bda9-f509fa6f858a" />

- [x] **What is in the request context**
  - **Actions:** operations the principal wants to perform.
  - **Resources:** AWS objects/services the actions target.
  - **Principal:** the **user**, **role**, **federated user**, or **application** that sent the request.
  - **Environment data:** **IP address**, **user agent**, **SSL** status, and similar — needed for policies that restrict by **source IP**.
  - **Resource data:** data related to the resource being requested.
- [x] **Processing the request context (example)**
  - The user has an **identity-based** policy.
  - The **S3 bucket** has a **resource-based** policy (bucket policy).
  - AWS evaluates **all** policies in the **account**.
  - Example request: **S3 GetObject** to retrieve an object — allowed if the evaluation grants that action.

</details>

<details>
  <summary>Step 6 — Compare the policy types and their combined effect</summary>

### Step 6 — Compare the policy types and their combined effect

- [x] **Policy types**
  - **Identity-based policies:** attached to **users**, **groups**, and **roles**.
  - **Resource-based policies:** attached to **resources**; they define permissions for a **specific principal** to access that resource.
  - **Permissions boundaries:** set the **maximum** permissions identity-based policies can grant an **IAM entity**.
  - **Organizations SCPs:** set the **maximum** permissions for an **organization** or **organizational unit (OU)** and the **accounts** in that org/OU.
  - **Session policies:** used with **AssumeRole** API actions.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9157bf4b-e2b2-490a-af94-7bda5ab05078" />

- [x] **Effective permissions when multiple policies apply**
  - **Identity-based + resource-based:** effective permissions are those granted in **either** policy (**union**).
  - **Identity-based + permissions boundary:** effective permissions are only those allowed in **both** (**intersection**).
  - **Identity-based + Organizations SCP:** effective permissions are those granted in **both** (**intersection**).

```text
# Combinations (as in the lesson)
identity + resource-based     => UNION         (allow in either)
identity + permissions boundary => INTERSECTION (allow in both)
identity + Organizations SCP  => INTERSECTION  (allow in both)
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5739ec8b-5fbe-4e12-8869-42f7c12ec210" />

</details>

<details>
  <summary>Step 7 — Memorize the determination rules</summary>

### Step 7 — Memorize the determination rules

- [x] **Determination rules (exam facts)**
  - By default, requests are **implicitly denied**.
  - The **root user** has **full access**.
  - An **explicit allow** in an **identity-based** or **resource-based** policy **overrides** the default deny.
  - If a **permissions boundary**, **Organizations SCP**, or **session policy** is present, it **might override** that allow with an **implicit deny**.
  - An **explicit deny** in **any** policy **overrides any allows**.

```text
# Determination rules
default          => implicit deny (except root: full access)
explicit allow   => overrides default deny (identity- or resource-based)
boundary / SCP / session policy present => may override allow with implicit deny
explicit deny    => overrides any allow (any policy)
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e728dd00-622e-482c-a6e5-9dacd7b7cd4a" />

</details>

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. There is no console walkthrough. Use the evaluation chart and the determination rules for exam revision.

### **Overview**

- [ ] This lesson is **policy evaluation logic** only; you do not attach policies in the console here.
- [ ] You will:
  - [ ] Remember: default **deny**, then look for an **allow**; **explicit deny** always wins.
  - [ ] Walk SCP → resource-based → identity-based → permissions boundary → session policy.
  - [ ] Contrast **union** (identity + resource) vs **intersection** (identity + boundary, identity + SCP).
  - [ ] Recite the **request context** fields: actions, resources, principal, environment data, resource data.

```text
# Combinations (as in the lesson)
identity + resource-based     => UNION         (allow in either)
identity + permissions boundary => INTERSECTION (allow in both)
identity + Organizations SCP  => INTERSECTION  (allow in both)

# Determination rules
default          => implicit deny (except root: full access)
explicit allow   => overrides default deny (identity- or resource-based)
boundary / SCP / session policy present => may override allow with implicit deny
explicit deny    => overrides any allow (any policy)
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How does every IAM authorization decision start?

<details>
<summary>Answer</summary>

- [x] With a **deny**.
- [x] Permissions are **not allowed by default**.
- [x] AWS then looks for an **allow** while evaluating **all applicable policies**.

</details>

### Question 2: What happens if any policy contains an explicit deny?

<details>
<summary>Answer</summary>

- [x] The **final decision is deny**.
- [x] An **explicit deny always overrides** any allow.

</details>

### Question 3: When does AWS evaluate an Organizations SCP?

<details>
<summary>Answer</summary>

- [x] When the principal’s **account** is in an **organization** with an **applicable SCP**.
- [x] If there is no applicable SCP, evaluation **skips** this stage.
- [x] If an SCP applies but has **no allow**, the decision is **deny**.

</details>

### Question 4: What is an example of a resource-based policy in this lesson?

<details>
<summary>Answer</summary>

- [x] An **Amazon S3 bucket policy**.
- [x] Resource-based policies are attached to the **resource**, not to the user.

</details>

### Question 5: When is the result an implicit deny at the identity/resource stage?

<details>
<summary>Answer</summary>

- [x] When there is **no allow** in the **resource-based** policy.
- [x] **And** there is **no allow** in the **identity-based** policy.

</details>

### Question 6: What does AWS check if the principal has a permissions boundary?

<details>
<summary>Answer</summary>

- [x] Whether the **permissions boundary** also **allows** the action.
- [x] If it does not allow → **deny**.
- [x] If it allows → evaluation **continues**.

</details>

### Question 7: What happens if the principal is a session principal?

<details>
<summary>Answer</summary>

- [x] AWS checks for a **session policy** with an **allow**.
- [x] Session policy allow → **allow**.
- [x] No session-policy allow → **deny**.
- [x] If the principal is **not** a session principal, this stage can result in **allow**.

</details>

### Question 8: Where can an access request come from, and what is the first IAM step?

<details>
<summary>Answer</summary>

- [x] The **Management Console**, the **CLI**, or the **API**.
- [x] First, IAM **authenticates** the principal (for example, **username and password** at the console).

</details>

### Question 9: What information is in the request context?

<details>
<summary>Answer</summary>

- [x] **Actions** (operations the principal wants to perform)
- [x] **Resources** (the AWS objects/services those actions target)
- [x] **Principal** (user, role, federated user, or application)
- [x] **Environment data** (IP address, user agent, SSL status, and similar)
- [x] **Resource data** (data related to the requested resource)

</details>

### Question 10: Why is environment data (such as source IP) in the request context?

<details>
<summary>Answer</summary>

- [x] A policy might **restrict access** based on **source IP address**.
- [x] AWS needs that information in the context to evaluate those conditions.

</details>

### Question 11: In the S3 example, which policies does AWS evaluate?

<details>
<summary>Answer</summary>

- [x] The user’s **identity-based** policy.
- [x] The bucket’s **resource-based** policy.
- [x] AWS evaluates **all** applicable policies in the **account**.
- [x] The example action is **S3 GetObject**.

</details>

### Question 12: Where is each policy type attached, and what does it control?

<details>
<summary>Answer</summary>

- [x] **Identity-based:** attached to **users**, **groups**, and **roles**.
- [x] **Resource-based:** attached to **resources**; permissions for a **specific principal** to access that resource.
- [x] **Permissions boundaries:** **maximum** permissions identity-based policies can grant an **IAM entity**.
- [x] **Organizations SCPs:** **maximum** permissions for an **organization** or **OU** and the **accounts** in it.
- [x] **Session policies:** used with **AssumeRole** API actions.

</details>

### Question 13: What are the effective permissions for identity-based plus resource-based policies?

<details>
<summary>Answer</summary>

- [x] Permissions granted in **either** policy.
- [x] That is a **union**, not an intersection.

</details>

### Question 14: What are the effective permissions for identity-based plus a permissions boundary?

<details>
<summary>Answer</summary>

- [x] Only permissions allowed in **both** the identity-based policy **and** the boundary.
- [x] That is an **intersection**.

</details>

### Question 15: What are the effective permissions for identity-based plus an Organizations SCP?

<details>
<summary>Answer</summary>

- [x] Permissions granted in **both** the **SCP** and the **identity-based** policy.
- [x] That is an **intersection**.

</details>

### Question 16: What is the default for requests, and what is special about the root user?

<details>
<summary>Answer</summary>

- [x] By default, requests are **implicitly denied**.
- [x] The **root user** has **full access**.

</details>

### Question 17: How can an explicit allow still fail, and what always wins?

<details>
<summary>Answer</summary>

- [x] An **explicit allow** in an identity-based or resource-based policy **overrides** the default deny.
- [x] A **permissions boundary**, **SCP**, or **session policy** might still override that allow with an **implicit deny**.
- [x] An **explicit deny** in **any** policy **overrides any allows**.

</details>

</details>

## Summary

IAM evaluation **starts with deny**. An **explicit deny** in any policy **always wins**. AWS then checks an **Organizations SCP** (if the account is in an org), a **resource-based** policy (for example an **S3 bucket policy**), an **identity-based** policy, a **permissions boundary**, and a **session policy** for session principals. No allow in resource-based **and** identity-based is an **implicit deny**. Requests from the **console**, **CLI**, or **API** are **authenticated** first; the **request context** holds **actions**, **resources**, **principal**, **environment data**, and **resource data**. Identity + resource = **union**; identity + boundary and identity + SCP = **intersection**. Root has full access; default is implicit deny; boundary/SCP/session can turn an allow into an implicit deny.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Determining whether a request is allowed or denied within an account](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-access-policy-language.html)
- [Policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)
- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)
