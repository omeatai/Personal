# 16. IAM Best Practices

**Course:** [AWS Certified Solutions Architect Associate (SAA-C03) – Neal Davis](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)  

---

## Introduction

This short theory lesson walks through **IAM security best practices**. AWS now pushes **federation** (**IAM Identity Center** or another **identity provider**) so **human users** get **temporary credentials**, and **workloads** should use **IAM roles** plus **STS** instead of long-lived **access keys** in applications. Also required: **MFA** (especially **root** and privileged accounts), **rotate** access keys if you must use them, **lock away root**, apply **least privilege**, start with **AWS managed policies** then tighten, use **IAM Access Analyzer**, clean up unused identities, add **policy conditions**, verify **public** and **cross-account** access, set **guardrails** across accounts (**Organizations** / **Control Tower**), and use **permissions boundaries** when you delegate IAM. Read the **AWS article** linked to the lesson for more depth.

## Detailed Explanation

- [x] **Read the AWS article too**
  - This lesson is a **fast** run-through.
  - A **link** is attached to the lesson; open the **AWS website** article and review each practice in more detail.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/79cbad8b-5dc5-44a0-bfd9-47b6602d2b9d" />

- [x] **Require human users to federate with an identity provider (temporary credentials)**
  - AWS now pushes **IAM Identity Center** or another form of **federation** into AWS, rather than long-lived **IAM user** accounts.
  - Many companies already use **IAM users**, **groups**, and **roles** and will **not** move away soon.
  - The recommendation especially applies if you are **new to AWS**: set up an **identity provider** federation configuration from the start.
  - Each user then receives **temporary credentials**.
  - That **reduces exposure** if a username-and-password account is compromised, and it **lowers the chance** of that happening in the first place.
- [x] **Require workloads to use IAM roles (temporary credentials via STS)**
  - Do **not** store **access keys** in applications.
  - Configure applications to use **IAM roles**.
  - The workload then gets **temporary credentials** from the **AWS Security Token Service (STS)**.
- [x] **Require multi-factor authentication (MFA)**
  - Require MFA for **all accounts**.
  - Especially **root** and **privileged** accounts.
  - The instructor’s bar: **everybody**.
- [x] **Rotate access keys regularly when long-term credentials are required**
  - AWS would **prefer** you do **not** use access keys, but they remain **useful** and many people still use them.
  - If you do use them, **rotate** them regularly.
  - Do not leave the same keys in place for too long in case they are **compromised**.
- [x] **Safeguard root user credentials; do not use root for everyday tasks**
  - Typical company pattern: set a **very complex password** on **root**, enable **MFA**, and **lock that password away**.
  - Do **not** use the root account for day-to-day work (often **not for any purpose** once setup is done).
  - All **administrators** should have their **own** accounts.
- [x] **Apply least privilege**
  - Give users **only** the permissions they need to do their job.
  - The same rule applies to **applications**: only the permissions required for the operations they must perform in AWS.
- [x] **Start with AWS managed policies, then move toward least privilege**
  - **AWS managed policies** are useful when you are **new** to AWS: they are **preconfigured** for common **use cases** and **job roles**.
  - They often do **not** provide true least privilege — they may grant **too much** or, sometimes, **not enough**.
  - As you gain experience writing policies, move toward **your own** policies that lock down **exactly** what you need.

<img width="3440" height="1440" alt="image" src="https://github.com/user-attachments/assets/e84d0b7a-dfb7-4733-9352-08bda9a46b65" />

- [x] **Use IAM Access Analyzer to generate least-privilege policies from activity**
  - Access Analyzer can look at **user activity** and show which **API actions** they actually call.
  - Use that to work out what they **need**, then **adjust** their permissions.
- [x] **Regularly review and remove unused identities and credentials**
  - Clean up unused **users**, **roles**, **permissions**, **policies**, and **credentials** (including old **access keys**).
  - Less leftover identity surface means **less exposure**.
- [x] **Use conditions in IAM policies to further restrict access**
  - Example: a **condition** that requires the caller to come from a **specific IP address** or **IP range** (for example the **company** range).
  - The principal then gets access to the resources **only** if the request originates from that range.
  - That is one example of tightening a policy beyond Allow / Action / Resource alone.
- [x] **Verify public and cross-account access with IAM Access Analyzer**
  - Same family of work as generating least-privilege policies: inspect what access is actually granted.
  - Confirm only the **right** permissions are in place, including **public** and **cross-account** access.
- [x] **Validate IAM policies for secure and functional permissions**
  - Check that policies both **work** and stay **secure** — not overly open, and not missing required actions.
- [x] **Establish permissions guardrails across multiple accounts**
  - When you have **multiple AWS accounts**, manage them with shared **security** and **governance**.
  - Tools the instructor names: **AWS Organizations** and **AWS Control Tower**.
- [x] **Use permissions boundaries to delegate permissions management**
  - A **permissions boundary** sets the **maximum** permissions a particular user can ever receive.
  - Use it when you **delegate** who can attach policies inside an account.
  - If someone accidentally grants **too many** permissions through a policy, the boundary still **caps** them so they never exceed what they are supposed to have.

<details>
  <summary>Lab</summary>

## Lab

No labs in this topic; the content is conceptual only. There is no console walkthrough. Apply these practices in later **HOL** IAM work and when you design accounts.

### **Overview**

- [ ] This lesson lists **IAM best practices**; there is nothing to click in the console here.
- [ ] You will:
  - [ ] Prefer **federation** / **IAM Identity Center** for humans, and **roles + STS** for workloads.
  - [ ] Require **MFA**, protect **root**, and **rotate** access keys if you must use them.
  - [ ] Apply **least privilege** (start with managed policies, then tighten; use **Access Analyzer**).
  - [ ] Add **conditions**, clean up unused identities, and use **Organizations** / **Control Tower** plus **permissions boundaries** for guardrails.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

No terminal commands in this lesson. The practices are conceptual; later HOL lessons use the console and, where needed, the AWS CLI.

```bash
# No commands in this topic; the lesson is conceptual only.
```

</details>

<details>
  <summary>Code</summary>

## Code

No policy JSON is shown in this lesson. The instructor’s examples are conceptual: **roles** instead of access keys, **IP conditions**, and a **permissions boundary** as a maximum cap.

```text
# Humans:  federate (Identity Center / IdP) → temporary credentials
# Apps:    assume an IAM role → STS temporary credentials (do not embed access keys)
# Extra:   Condition on source IP (company range) further restricts a policy
# Cap:     permissions boundary = maximum permissions a user can ever receive
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How does AWS want human users to access AWS, and why?

<details>
<summary>Answer</summary>

- [x] Require humans to use **federation** with an **identity provider** (for example **IAM Identity Center**).
- [x] They then access AWS with **temporary credentials**.
- [x] That **reduces exposure** if a username-and-password IAM user is compromised, and it **lowers the chance** of that happening.

</details>

### Question 2: Should existing companies immediately abandon IAM users, groups, and roles?

<details>
<summary>Answer</summary>

- [x] **No.** Many companies already use IAM users, groups, and roles and will **not** move away soon.
- [x] The federation recommendation especially applies if you are **new to AWS**.

</details>

### Question 3: How should workloads authenticate to AWS?

<details>
<summary>Answer</summary>

- [x] Use **IAM roles** so the application gets **temporary credentials**.
- [x] Those credentials come from the **AWS Security Token Service (STS)**.
- [x] Do **not** store **access keys** in applications.

</details>

### Question 4: Who should use multi-factor authentication?

<details>
<summary>Answer</summary>

- [x] **All accounts**.
- [x] Especially **root** and **privileged** accounts.
- [x] The instructor’s bar: **everybody**.

</details>

### Question 5: What is AWS’s stance on access keys, and what should you do if you use them?

<details>
<summary>Answer</summary>

- [x] AWS would **prefer** you do **not** use long-term access keys.
- [x] They are still **useful**, and many people still use them.
- [x] If you need long-term credentials, **rotate** the keys **regularly** so they are not left in place if compromised.

</details>

### Question 6: How should you treat the root user?

<details>
<summary>Answer</summary>

- [x] Set a **very complex password**, enable **MFA**, and **lock the password away**.
- [x] Do **not** use root for **everyday** tasks (typically **not at all** after setup).
- [x] Every **administrator** should have their **own** account.

</details>

### Question 7: What does least privilege mean for users and for applications?

<details>
<summary>Answer</summary>

- [x] Users get **only** the permissions they need to do their job.
- [x] Applications get **only** the permissions required for the AWS operations they must perform.

</details>

### Question 8: Why start with AWS managed policies if they are not least privilege?

<details>
<summary>Answer</summary>

- [x] They are **preconfigured** for common **use cases** and **job roles**, which helps when you are **new** to AWS.
- [x] They may grant **too much** or **not enough**.
- [x] After you know how to write policies, move to **custom** policies that lock down **exactly** what you need.

</details>

### Question 9: How does IAM Access Analyzer help you reach least privilege?

<details>
<summary>Answer</summary>

- [x] It looks at **access activity** (which **API actions** users actually call).
- [x] You then **generate** or **adjust** policies so they match what is **needed**.

</details>

### Question 10: What unused items should you regularly review and remove?

<details>
<summary>Answer</summary>

- [x] Unused **users**
- [x] Unused **roles**
- [x] Unused **permissions** and **policies**
- [x] Unused **credentials** (including old **access keys**)
- [x] Cleanup reduces **exposure**.

</details>

### Question 11: Give an example of using a condition in an IAM policy.

<details>
<summary>Answer</summary>

- [x] Require the request to come from a **specific IP address** or **IP range** (for example the **company** range).
- [x] Access is granted **only** if the caller comes from that range.

</details>

### Question 12: What kinds of access should you verify with IAM Access Analyzer besides unused activity?

<details>
<summary>Answer</summary>

- [x] **Public** access to resources
- [x] **Cross-account** access
- [x] Confirm only the **right** permissions are granted.

</details>

### Question 13: What does “validate IAM policies” mean in this lesson?

<details>
<summary>Answer</summary>

- [x] Check that policies give **secure** and **functional** permissions.
- [x] Same idea as the other Access Analyzer points: right access, not too open, and still usable.

</details>

### Question 14: How do you establish permissions guardrails across multiple AWS accounts?

<details>
<summary>Answer</summary>

- [x] Manage the accounts together with shared **security** and **governance**.
- [x] Use **AWS Organizations** and **AWS Control Tower**.

</details>

### Question 15: What is a permissions boundary used for when you delegate IAM?

<details>
<summary>Answer</summary>

- [x] It sets the **maximum** permissions a particular user can ever receive.
- [x] If someone accidentally attaches a policy that is **too open**, the boundary **caps** them.
- [x] That lets you **delegate** permissions management inside an account without losing the cap.

</details>

### Question 16: What is the difference between federation for humans and roles for workloads?

<details>
<summary>Answer</summary>

- [x] **Humans:** federate through an **IdP** / **IAM Identity Center** so people get **temporary** credentials instead of standing IAM user passwords.
- [x] **Workloads:** applications **assume roles** and get temporary credentials from **STS**, instead of embedding **access keys**.

</details>

### Question 17: Which practices specifically reduce the blast radius of a leaked password or access key?

<details>
<summary>Answer</summary>

- [x] **Federation** / **temporary credentials** instead of long-lived IAM user passwords.
- [x] **Roles + STS** instead of access keys in applications.
- [x] **MFA** on accounts (especially root and privileged).
- [x] **Rotate** access keys if you still use them.
- [x] **Remove unused** users, roles, and credentials.

</details>

</details>

## Summary

AWS wants **humans** to **federate** (**IAM Identity Center** or another **IdP**) and **workloads** to use **IAM roles** with **STS** **temporary credentials**—not standing IAM user passwords or access keys in apps. Require **MFA** for everyone, especially **root** and privileged users; **lock root away** after a strong password and MFA. If you must use **access keys**, **rotate** them. Apply **least privilege** to users and applications: start with **AWS managed policies**, then write tighter custom policies; use **IAM Access Analyzer** from real **API activity**, and to check **public** / **cross-account** access. Add **conditions** (for example a **company IP range**), delete unused identities and credentials, set multi-account **guardrails** with **Organizations** and **Control Tower**, and use a **permissions boundary** as a **maximum** cap when you delegate IAM. Read the **AWS article** linked to the lesson.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03) Course – Neal Davis (Udemy)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/)
- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
- [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [MFA in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [Rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey)
- [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
- [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
- [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies)
- [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)
- [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)
- [IAM condition keys for source IP](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceip)
- [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
