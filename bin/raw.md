## IAM policy simulator

In this lesson,

I'm gonna show you another tool for IAM,

which is the IAM policy simulator.

Now again, you'll find the link

for this attached to the lesson.

Otherwise, just search for IAM policy simulator.

You should end up on a page like this one.

Now what we've got here is on the left

we have to select the context.

So are we gonna apply this simulation to specific users,

groups, or roles?

Users is the default, here I can see my groups.

I've just got one, my admin group,

and then roles, a whole bunch of roles.

So I'll put it back to users.

I've got two user accounts, the Neil user account,

that's my one with full admin permissions.

And then I've got testuser,

which we use for the IAM policy generator lesson.

So that user should only have access

to a few API actions for S3

and EC2 instance API actions as well.

So that would be a good user to run this simulation against

because obviously it has very limited permissions in AWS.

So if I choose testuser, now we can see that it lists

whatever policies, permissions, boundaries, et cetera,

that are actually attached to this user account.

So we'd actually be able to see here,

oh well the user has an inline policy,

which is this test poll.

There might be other IAM policies applied

as well via groups and that kind of thing.

Or maybe there's a permissions boundary

or we wanna simulate a permissions boundary,

which we can actually do here as well.

So in this case, we have this policy attached.

So all I'm gonna do here is I'm just trying to see, okay,

I've attached this policy to this user

and I wanna see through this console what permissions

that user is going to have access to.

Now, if you had a very big complex policy

or you have a series of different policies applied,

some through groups, some through permissions policies

attached to the inline,

to the user account, for example,

then this becomes a lot better

'cause you're trying to work out what is the aggregate

permissions that the user's gonna have.

This is a very simple example,

but it just shows you how to use it.

So we have the inline policy. Now I can select services.

So for example, if I choose EC2, choose the EC2 option here,

then I can choose specific actions

or I can just select all of them, I've selected all

and then run a simulation.

And of course we can see lots

and lots of permissions are allowed, okay?

They're basically all allowed.

That's in the EC2 context.

If I chose EC2 autoscaling,

well I didn't allow that in the policy,

so I should get a bunch of denied.

So let's run a simulation,

just make sure I've got everything.

I'll clear this out. Sometimes it's a little bit finicky.

And then run a simulation again, select all, run.

Okay, now we get denied.

So now you can see Amazon EC2 autoscaling.

All of these are being denied.

What about S3?

So if I go to S3, type S3 here, select S3,

I'm just gonna clear these results.

Now for the S3 actions, again,

I could choose these specific actions,

or in my case, I'm just gonna select everything,

run the simulation, and I get a lot of denied.

I only actually allowed a few permissions.

So yeah, we can see here get bucket location,

that's allowed, we've got get objects,

and then we've got list all my buckets and list bucket.

So we can see exactly what this user will be able to do.

Now you may notice at the top here,

the mode is existing policies.

You can also choose new policy

and that's where you get this policy sandbox.

So now you can actually add your code in.

So you might be able to add some more restrictive code.

Let's do that, let's actually take

this policy statement here

which we created in the previous lesson.

And I'm gonna paste that in.

And what I'll do now is maybe I will just

restrict the actions a little bit more.

So I'll take these ones out, apply this policy,

I'll clear the results, run the simulation again,

have to select all, run simulation,

and now of course I get access denied

for a lot more permissions.

I've still got the get objects

and I've still got the list all my buckets.

But those are the only permissions.

So in this mode, you can now put in a policy that you plan

to apply to a user, or a group or a role,

and then you can actually simulate what permissions

that user, group, or role would actually provide.
