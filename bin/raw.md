## IAM Exam Cram

Hi guys,

there's an exam cram lesson for most sections in this course,

so I just wanna explain quickly what they are before we get started.

Exam crams are a quick run-through of important facts,

and I will go quite quickly.

You can always change the playback speed if I'm too fast for you.

You should use these after going through the section for revision and cramming.

Mainly,

I'm going to be reminding you about things rather than explaining.

Now that being said,

there may be some facts that are covered here

that weren't covered in the lessons or vice versa.

Some topics are quite suitable for this bullet point format,

and I prefer to keep it as visual as possible and

as engaging as possible throughout the main lessons in the course.

Now,

most lessons in this course are highly visual,

but exam crams are absolutely not,

they are deaf by bullet points.

I deliberately make sure that I have everyone

covered no matter what your learning style is.

Some people are more visual,

some people like to read,

and some people hands-on

is the most important way to learn.

So whatever way you learn best,

you're covered in this course,

and exam crams are an additional tool which is gonna be useful for most people.

So let's get started with the exam cram for IAM.

IAM is used to securely control individual and group access to AWS resources.

It makes it easy to provide multiple users with access to AWS resources.

And with IAM you can manage users,

groups,

access policies,

and roles,

and also user credentials.

User password policies can be configured

in IAM as well.

We can also enable multi-factor authentication,

and that's definitely recommended.

We can also generate API keys for programmatic access to IAM.

By default,

all new users are created with no access to any services,

they can only log in to AWS but they can't actually do anything.

Permissions must then be explicitly granted

to allow a user to access an AWS service.

IAM users are the individuals who've been granted access to an AWS account.

Now,

IAM is a universal or global service,

so it doesn't apply to specific regions.

IAM is eventually consistent.

What that means is if you make a change and then you immediately try to read

from IAM you might not see that change.

It might just take a bit longer.

For authentication methods,

we've got console passwords for logging into the management console,

access keys for programmatic access,

server certificates,

which can be used for some services as well.

IAM users are the entities that represent a person or a service.

By default,

they cannot access anything in the account.

The root user credentials are the email address used to create the account,

and there's a password associated with that account.

The root account has full administrative

permissions and they cannot be restricted.

IM users can be created to represent

applications,

and those are known then as service accounts.

You can have up to 5000 users per AWS account.

IAM groups are collections of users

and have policies attached to them.

A group's not an identity in itself,

so it can't be identified as a principle in a policy.

So where you have a policy statement and you put in the

ARN

of a principal like a user,

you can't do that with a group.

You use groups to assign permissions to users,

and you should always follow the principle

of lease privilege when assigning permissions.

You can't nest groups,

so you can't create a group within a group.

IEM roles are created

and then assumed by trusted entities,

and they're a way of delegating permissions to resources for users

and services.

Users and services can assume a role to obtain temporary security credentials,

and those are issued by the Security token Service,

the STS service.

IEM policies are documents that define the permissions,

and they can be applied to users,

groups and roles,

and include key value pairs that consist of an attribute and a value.

All permissions are implicitly denied by default.

The most restrictive policy is applied if

there's multiple policies with conflicting statements.

Now,

what are the types of policy?

We've got identity-based policies which you can attach

to users,

groups or roles.

We've got resource-based policies.

They get attached to resources like S3 buckets,

and you can define permissions for principals

accessing the resources using a resource policy.

We then got permissions boundaries.

These set the maximum permissions that an identity-based policy can grant

to an IAM entity.

Permissions boundaries aren't really covered at the associate level,

but they are at the professional level.

We then have Organisation's Service Control policies.

These specify the maximum permissions for an organization

or an OU.

And lastly,

we have session policies that are used with assumed role API actions.

Now,

onto the IAM best practices,

lock away your account root user access keys,

create individual users,

use groups to assign permissions to users,

grant lease privilege,

get started using permissions with AWS managed policies,

and use customer managed policies instead of inline policies.

Use access levels to review IM permissions,

always bearing in mind that lease privilege,

and configure a strong password policy for your users.

Enable multi-factor authentication.

Use roles for applications that run on EC2 instances,

and use roles to delegate permissions.

Do not share access keys,

always keep them to yourself and use them only for your account,

and rotate all credentials regularly

and remove any unnecessary credentials.

You can use policy conditions for extra

security when you're writing your IM policies.

And lastly,

monitor activity in your account to see what's actually happening.

And that's it for this exam cram.
