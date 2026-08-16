## Permissions Boundaries

In this lesson, I'm going to cover permissions boundaries, permissions,

boundaries are an advanced feature of I AM in

which we can define the maximum permissions that are available

to an I AM entity via an identity based policy.

So I will explain to you why that's

important and how we can implement permissions boundaries.

So let's start with an example here. We have Joanne.

Joanne needs to access certain resources in AWS.

She's been assigned some permissions via this policy which is a developer policy

and it allows full control of S3 cloudwatch easy two and I am.

In addition to

the identity based policy,

we've also assigned a permissions boundary to Joanne.

Now you can see the permissions boundary has fewer permissions.

It only has S3 cloud watch and EC2,

the permissions boundary is actually there to set the maximum permissions that

the entity can have and they're assigned to users and to roles.

So in this case, assigned to

Joan directly what this means is even though theoretically,

Joanne should have I am permissions via this developer

policy where she has full control of this service.

It's not present at all on the permissions boundary,

which means it's actually limited.

Therefore, she can do things like list buckets in Amazon S3.

But Joanne will not be able to create a user account in. I am.

The permissions boundary has restricted the maximum

permissions that we can assign to Joanne.

So why is this important?

Well,

let's have a look at one particular potential attack which can be

mitigated by using a permissions boundary

and that's called privilege escalation.

So here's the scenario we have Lindsay

Lindsay has I am full access.

Therefore, she can do anything she wants to do in I am but not any other Aws service.

So she can't launch easy two instances for example or create VPC S.

Now, Lindsay goes ahead and creates a user. We'll call the user X user,

that user, she then assigns administrator access permissions,

she's able to do this because she has I am full access permissions.

She can create users and assign any policy she wants to them.

So Lindsay applies the administrator access and ex

user now becomes more powerful than her.

She can then log in with the ex user account

and do something that perhaps she shouldn't,

which is to go and mine Bitcoins on company dollars.

So this is a privilege escalation attack.

Lindsay has created a user and that user has more permissions than she does

and she's able to then log in as that user and perform api actions.

OK? So this is bad news. Let's mitigate this problem with a permissions boundary.

So here we have Lindsay, she has I am full access. She still needs those permissions.

That is her job role.

However,

what we do then is add the permissions boundary.

The permissions boundary ensures that users created by Lindsay

have the same or fewer permissions than her.

So Lindsay still can create the ex user account

and assign the administrator access permissions policy.

But when she logs in as that user,

she won't have more permissions than she already does.

So that is preventing privilege escalation using a permissions boundary.
