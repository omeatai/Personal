## IAM Best Practices

Hi guys.

In this quick lesson, we're going to go through some of the IAM best practices.

There will be a link attached to this lesson

and I recommend that you also go through the

article on the AWS website to understand each of

these best practices in a bit more detail,

but I'm going to run through them fairly quickly now.

Ok

The first one is to require human users to use federation

with an identity provider to access AWS using temporary credentials.

So here, AWS have started pushing us towards using the AWS

IAM Identity center

or some form of Federation

into AWS rather than using IAM user accounts.

Now, many, many companies are already using IAM users groups and roles.

So they're not going to move away from that for some time.

But this really applies to those who are new to AWS

that you should start setting up

this identity provider federation configuration.

So that then each of your users is

actually gaining temporary credentials which reduces any exposure

If for example, a user account with a user name and password is compromised,

it can also minimize the chance of that

Happening in the first place.

Next is to require workloads to use temporary

credentials with IAM roles to access AWS.

So again, this is about not storing things like access keys in applications.

Instead, we want to

configure our applications to use roles so that they

gain temporary credentials through the security token service.

Instead require multi factual authentication.

This is for all accounts, root accounts, privileged accounts.

Absolutely,

everybody rotate access keys regularly For use

cases that do require long term credentials.

AWS would prefer you don't use access keys but they are still quite useful.

Lots of people do use them.

So if you do use them, just rotate them over time quite regularly Obviously,

you don't want to exist for too long just in case they get compromised,

safeguard your root user credentials and don't use them for everyday tasks.

Typically companies will set a very complex password on the root user account,

configure multifactor authentication

and lock that password away. They won't use that account for any purposes at all.

All administrators should have their own accounts

apply at least privilege pretty straightforward

This one just means only give users the permissions

that they need that applies to applications as well.

So only ever provide the permissions that are

required for any user account to do their job

or any application to perform whatever operations they need to perform in

AWS. Get started with

AWS manage policies and move toward least privileged permissions.

AWS managed policies are great for anyone who is new to

AWS because they're pre configured for you for certain use cases and job roles,

but they might not provide least privileged permissions.

You might find that they provide a bit too much or maybe not enough in some cases.

So you want to kind of move away towards your

own policies that lock down exactly what you need.

But do that once you gain experience and you know how to write the policies properly,

use the IAM access analyzer to generate

least privileged policies based on access activity.

So you can use this tool to look at the activity of

users and then work out which API actions are they making,

you know what they need in terms of the permissions.

And then you can adjust the permissions that

they have based on that information regularly

review and remove unused users roles, permissions, policies and credentials.

So really just about cleaning up. So you have less

exposure if you like for any sort of old user

accounts or roles or permissions or credentials like access keys,

use conditions in IAM policies to further restrict access.

For example, we can configure a condition in a policy

that means that somebody has to come from a specific

IP address or range of IP addresses like the company

IP address range,

they will only get access to the resources if they're coming from that range.

That's just one example of using a condition to further restrict access,

verify public and cross account access to resources with IAM access

analyzer. Very much like the first bullet point on this page.

This is about using this tool to have a look at what permissions are being used,

make sure that only the right permissions are granted and also to

validate your IAM policies to ensure secure and functional permissions.

Very much the same thing here, establish permissions,

guardrails across multiple accounts.

This is really referring to where have multiple

AWS accounts and we want to essentially manage them

including having some security and governance across those accounts.

For example, we can use

AWS organizations and AWS

Control tower to implement those security measures and use

permissions boundaries to delegate permissions management within an account.

A permissions boundary essentially

gives you a maximum amount of permissions that can be used by any particular user.

So it's a way of again restricting permissions just in

case someone accidentally grants too many permissions through a policy.

Well, actually the boundary will sort of kick in

and ensure that they don't have more than they're ever supposed to have.
