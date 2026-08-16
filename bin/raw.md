## IAM policy evaluation

In this lesson, you'll learn about IAM policy evaluation.

So you need to understand the evaluation logic.

So what happens when somebody tries to make access to a particular resource?

What is the process?

And this is the chart, the evaluation logic workflow that comes from

AWS. I'm going to read through this.

Firstly, up in the top left here,

every decision starts with a deny.

So remember all permissions are not allowed by default, everything is denied

and then AWS

is going to look for and allow of some sort.

So it needs to evaluate all the applicable policies.

Now, is there an explicit deny?

Remember that an explicit deny will always override

any allow.

So immediately the final decision is deny if there is an explicit deny.

Now, if not

the process continues.

AWS is going to check is the principal's account, a member of an organization

with an applicable service control policy.

Now, if that isn't the case, then

the process just goes on to the next stage. If it is the case,

it needs to check if there's an allow. So if there's an SCP

but it doesn't have an allow, then deny

is the final decision

if there isn allow, then again, we carry on to the next stage.

Does the requested resource have a resource based policy?

Remember,

resource based policies apply to things like S3 with bucket policies.

Now, if there is a resource based policy,

it needs to check for and allow and if there is,

then you need to understand the process for resource based policies

and how they work together with the identity based policy.

Well, look at that later.

Now, if there isn't an allow,

then it needs to continue checking the identity based policy.

If there is an identity based policy that applies,

then the process continues and it's going to check for an allow.

If not, then, well, we don't have and allow in the resource based policy.

If there is one and we don't have one and identity based policy. So of course,

it's an implicit deny.

Now, if there isn't allow, then again, the process will continue.

So, so there is an allow for the action

but then AWS will check if the principal has a permissions boundary applied.

If the answer is yes, then again,

it's going to check for an allow in the permissions boundary that's applied

to that principle.

If that's good, then we carry on. If not, there's a deny.

In the last stage here, AWS is going to check is the principal a session principle.

If the answer is no, then there's an allow

if the answer is yes then it needs to check for a session policy

with an allow, it will go to allow and if not a deny.

And again, it will check here.

Is this a role session?

If yes, then allow. And if not, then no,

this is a bit complicated. I know,

but it's worth spending a bit of time understanding this evaluation logic.

Now, what are the steps for authorizing requests?

So we can have our request coming from a variety of sources, the console,

the CLI or the API,

they go through to IAM.

And the first thing that needs to happen is authentication.

AWS needs to authenticate the principle that makes the request.

So for example,

a user name and password for the console that checks that you

are who you say you are because you know the password.

So perhaps a user is logging in.

Now the request context is formed.

The request context includes the actions,

these are the actions or operations that the principle in this case,

the user account wants to perform

the resources are the resources objects,

the AWS services, for example, on which the actions need to be performed.

The principle,

the user role, Federated user or application that sent the request

is identified in the request context

and then environment data. So

information about the IP address to user agent SSL status and so on

is also present because for example, you might have a policy

that restricts access based on the source IP address.

That's why that information is important

in the request context.

Next, we have the resource data,

data related to the resource that is being requested.

Number two, in the second stage, here

is processing the request context.

So in this case, the user has an identity based policy applied

and the S3 bucket they're trying to access has a resource based policy applied.

So AWS will evaluate whether to authorize that access

and it will do so by evaluating all the policies within the account.

In this case,

the user wants to retrieve an object using the S3

get object API action and has been granted that access

and that is that final stage.

So that's determining whether a request is allowed or denied.

Now, there are a few different types of policy.

We've talked about identity based policies before

these are attached to users, groups and roles

and resource policies which are attached to resources,

defining the permissions for a specific principle to access the resource.

We also have permissions boundaries,

these set the maximum permissions that identity based policies can grant

and IAM entity.

And also we have organizations, service control policies.

They specify the maximum permissions for

an organization or an organizational unit

and the accounts that are created or contained within that organization Oor OU

lastly, we have session policies,

these are used with the assumed role API actions.

In this final slide,

I want to show you another visual representation

of how policies are evaluated within AWS.

So we have an identity based policy

and resource based policy.

Now what happens when we have these multiple policies applied?

Well, what actually happens

is the effective permissions are those

that are granted

in either the identity based policy or the resource based policy.

Next, we have an identity based policy

and the permissions boundary.

In this case,

the effective permissions are only

the permissions that are allowed in both the identity based policy

and that are allowed through the permissions boundary.

And then lastly, we have an identity based policy

and an organization's SCP.

And again, in this case,

the effective permissions are those that are granted in both the SCP

and the identity based policy.

And there are some determination rules

by default or requests are implicitly denied

though the root user has full access,

an explicit allow in an identity based or resource based policy

overrides this default.

And if a permissions boundary organizations SCP or session policy is present,

it might override the allow with an implicit deny.

Lastly, an explicit deny in any policy overrides any allows.
