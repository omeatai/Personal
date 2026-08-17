## Access Evaluation Tools

In this lesson, we're going to look

at a couple of tools you could use for evaluating

the access that users have in the account.

I'm in the IAM Management console here,

and the first place I'm gonna look is Access Analyzer.

So Access Analyzer needs to be enabled for your account.

If it's the first time you're here,

you'll find a little button.

It's just a single click

and it will enable it for your account.

And then very quickly,

it's going to perform this access evaluation.

Now what it's found here is some findings

relating to S3 buckets and IAM roles.

So for example, we can see here that a bucket policy

is allowing access levels of read.

And this one is allowing write, read, and list.

If you click on the finding ID,

then it's giving you a little bit of a warning here

that this finding is for a resource

that is allowing public access.

So of course that could be an issue, not necessarily,

but if it is, then you can use this finding

to actually resolve the issue.

And here it's telling me the actual access level.

So the API Action S3 get Object is being allowed.

For the IAM role here,

we can see this is in relation to the Cognito service.

So there's the access level of write,

and that's for the Assume role with web identity.

So again, it's just something you might wanna look into.

So this is analyzing access and providing these findings,

which might warn you about potentially

something that's too open,

that's allowing more access than you might want it to.

There's archive rules here about how you archive.

You can see the analyzers here as well,

you can create new analyzers

and in the settings here,

you can see the Access Analyzer Administrator

and you can optionally add

a delegated administrator as well.

Another tool we have here is the credential report.

So this is more about credentials obviously.

You can download this report

and it's gonna look something like this.

So lemme just expand some of these rows or columns.

And so what you can see

is you can see that there's three users in this account,

plus the root account.

You can see when the user was created,

whether there's a password for console access,

when the password was last used, last changed,

if it's gonna be rotated,

whether MFA has been enabled as well.

So quite a bit of information here

that you can use to understand

how users are set up from a security perspective.

The next tool I'm going to show you is IAM Policy Simulator.

In a Policy Simulator, you can see the users in the account.

Now if I choose a user like Jack

and then select a service, let's say EC2

and maybe I wanna select all actions

and then run a simulation.

And it's gonna check what access this user has.

Now in this case, the user we can see has a policy

called Administrator Access applied.

So obviously it's coming back and saying aloud.

We can clear those results.

And then let's go back

and let's just choose this other user, Chris.

So Chris has a policy applied called bucket access.

So let's have a look at S3.

So I'm gonna choose S3,

but now I'm gonna check specific permissions.

So I'm interested in whether this user can create a bucket.

What about are they able to delete an object

or delete a bucket?

Do they have the Get Object API Action?

What about list all my buckets?

So these are some of the API actions

that the user might have.

And so I want to check those specific API actions.

So now I can run the simulation

and we can see that most of these permissions were denied.

Now there might be other permissions

that I haven't selected,

but in this case, only list all my buckets has been allowed.

So that's a useful tool to see

what permissions users are being granted

based on the policies that they have.

The last tool I'm gonna show you is if we go to Roles,

there's a great tool which can help us with working out

what permissions we need for a Role.

So let's choose a Role,

maybe I'm gonna choose this

Elastic Beanstalk EC2 role here.

Now this role has multiple policies applied.

Now at the bottom here,

we can see this generate policy option.

And this generates policies based on Cloudtrail events.

So if this role has been used recently

and you have a trail,

it's gonna be able to generate a policy

based on the API actions that we used

by this role as can be seen in the Cloudtrail trail.

So what you do is click on generate policy,

choose the timeframe.

So maybe I wanna say,

yeah, in the last 60 days, choose the trail.

I've got a trail in this region,

specify the regions, so maybe US-East.

And then you can choose to use an existing service role

and generate policy. And then when you do that,

it takes several minutes to generate the policy.

So I actually already did it.

I'll show you one which has completed,

let's just put in EC2,

and I've got this role, which I used recently.

So I did exactly what I just showed you.

And it's generated a policy

and we can now view the generated policy.

In the results here,

we can see an option to review the permissions,

and these are the permissions which

AWS thinks we need for this role.

So I can see the specific actions

for systems manager and EC2.

I could then go and add in

additional permissions if I want to,

and then I can click on next.

I can customize it through the JSON editor here as well.

And also add additional policy items

from the right hand side.

And then you can generate the policy

and then apply the policy to a role.

So that's another useful tool

that can help you to tighten up the permissions

you need to assign in this case to roles.
