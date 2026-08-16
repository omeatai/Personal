## AWS Identity and Access Management

Welcome to the AWS Identity and Access Management section. So the very first thing you need to understand

in quite a bit of detail to work with AWS is how to securely connect to your AWS account, both through

the console, through the command line, and through the API.

So we need to learn about the various different constructs, users, groups, roles, and policies.

We also need to learn how we can authenticate and be authorized to then access AWS services. And we

can do that through various things, including access keys, identity-based policies and resource-based

policies.

We can also configure multi-factor authentication and password policies to make sure that our accounts

are as secure as possible.

So you'll learn how to use the AWS IAM service in this section, and also the various best practices

that you need to know both for the exam and just to make sure that your accounts are secure.

-: Hey guys, welcome to this lesson.

In this lesson I'm gonna cover the AWS Identity

and Access Management Service known as IAM

or also sometimes called IAM

So IAM is a really important service to understand

because it's the service that we use

for authentication and authorization.

So here we have an AWS account with AWS IAM.

Of course, there's different ways that we can manage AWS.

We've got the console.

We've got the command line interface

and the API through SDKs.

So through IAM, we can create things like users and roles.

We can use federated users

and we can enable authentication for applications as well.

Now, all IAM principles must be authenticated

to send requests.

In other words, to send any kind of API request to AWS.

A principle is a person

or application that makes a request for an action,

that's an API action or operation on an AWS resource.

Now, firstly, we have authentication.

So that's essentially proving that you are

who you say you are.

For example, by supplying a password,

then we need authorization.

Authorization is where we either are allowed

or denied access to resources.

And here we have policies like identity-based policies

and resource-based policies,

which define what we are allowed to do.

So first through authentication,

we prove we are who we say we are.

Then AWS determines what we are allowed to actually do.

For example, performing API actions,

like run instances on EC2 that launches a virtual server,

get bucket retrieves information about buckets

and create user means to create a user in IAM.

So the API actions are authorized on the AWS resources.

A few of the core components of IAM are users, user groups,

roles and policies.

User groups are used for adding users

and then applying permissions policies.

So we have the user account,

you can log in with a user account.

We have the policy that determines

what users are allowed to do,

what API actions are they allowed

to take in the account or on a specific resource.

And so the way that we apply these policies

to multiple users is by attaching them to a user group.

So if we have several people

who have a common job role, we can attach a policy

that provides the permissions they need to do their job,

put all those users in the group,

and now we only have one permissions policy to manage.

So the user will gain the permissions applied to the group

through the policy,

these are called identity-based policies.

They get applied to users, groups and roles.

And roles are used for delegation,

and they are assumed.

We'll talk a bit more about that later.

But essentially what's happening here

is a role is an identity

which has permissions assigned to it via policy

and then you can assume the role

and take on whatever those permissions are.

It's kind of like putting that hat on,

that's why it's a picture of a hat.

You might put a hat on for your development role

and take on the development permissions.

Maybe then you're gonna do a CIS ops role.

You take off your development hat, put on the the role hat

for development, and you become a developer,

so that's what a role is.

We'll look at that more a bit later on.

Now the policies define the permissions for the identities

or resources they are associated with.

Let's look at IAM users in a bit more detail.

When you created your account, you supplied an email address

and that created the root user account.

And as I've mentioned before,

the root user has full permissions

and you can't restrict most of those permissions.

So it's a best practice not to use that account.

What you should do is set a very strong password

and enable multifactor authentication.

Then we're gonna create user accounts.

You can create up to 5,000 individual user accounts,

and those user accounts will have no permissions by default,

that's a really important point to remember.

So if you create a user account,

that user can log in

if you enable management console access,

but they can't do anything at all,

unless you specifically apply permissions to them.

So here we have a user. We've got Andrea.

Now, Andrea, when she logs in, we'll use her friendly name.

The friendly name is just a simple text string.

In this case it's actually her name, Andrea.

So you can log in very simply with Andrea.

and then a password.

Now, there's actually,

for every resource in AWS,

there's an Amazon resource name, okay.

You can see that here.

Now the text in red is the account number.

We can see a little bit,

it's an ARN, so it's an Amazon resource name,

it's an AWS resource, it's an IAM resource.

This is the account number,

we know that this type of resource is a user,

and then the friendly name is Andrea.

So that's a unique identifier for that resource within AWS.

Now, Andrea can log in via these different mechanisms.

We've got the management console

for which you use a username and password

and potentially multifactor authentication.

And then for the command line interface

and the API, we can use access keys.

So let's move on to user groups.

Great thing about user groups is it helps us

from a management perspective.

Here we've got the admin group,

the development group, and the operations group.

We can add our users in.

Some users might be in multiple groups,

and the groups are then used to apply permissions, okay.

So now we can take a permissions policy

that's relevant to those specific groups of users

and apply it to the group,

and those users will automatically

inherit those permissions.

Now, if a user is in multiple groups,

they will gain multiple sets of permissions

and they're combined together.

So the user will gain the permissions applied to the group

through the permissions policy.

For authentication methods, we can use a username password

with a multifactor authentication token

for that extra factual security.

We can use that mechanism for connecting

to the management console using an IAM account.

So here John is authenticated

and perform operations through the console.

Now, the other ways are the command line interface

and the API.

For this, we need to gain some credentials.

There's a couple of ways of doing this.

One is by generating something called an access key ID

and a secret access key,

it's kind of like a username and password.

And these can be used via the CLI and the API

to authenticate to the AWS API.

And we can use something called

the AWS Security Token Service

to generate short-term credentials as well.

So access keys are used for programmatic access.

I'll just finish this lesson by summarizing the differences

between the root user and an IAM user.

So remember that the root user is the one

in which you log in with the email address

that you used when you created the account,

and it has full access and is unrestricted,

also difficult to restrict.

Some permissions cannot be restricted

for the root user account.

There are some actions which you need the root user

to perform, but mostly once we've got our account up

and running, we don't need it.

So we can lock it away and not use that account.

And then we have our IAM user, which has a friendly name.

And when we log in using this user account,

we will supply either the alias for the account

or the account ID itself

and the permissions assigned to an IAM user come

through permissions policies.

If there's no permissions policies applied

to this user directly

or via any groups that the user is a member of,

then they won't have any permissions.

So you have to enable permissions

by assigning policies either directly

or usually preferably through a user group instead.
