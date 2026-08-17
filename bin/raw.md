## IAM policy structure

In this lesson, I'm going to go through I AM policy structure.

I'm gonna help you to understand how to read

JSON policies and how to utilize

JSON policies in I am.

So firstly, just as a reminder, of course, in AWS, everything is an API action.

So whenever you're performing anything through the console, the CLI or the SDK,

what you're actually doing is making an API call.

Each service has its own set of API actions.

And those are those particular individual actions that

we're trying to perform for that service.

So if we go in a console and launch an EC2 instance,

what's happening behind the scenes is an API action is

being called and that is the EC2 run instances.

If we stop an R DS database via the CLI or the console,

it's the R DS stop DB instance API action that is taking place.

So every service has these API actions

and we can get very specific in our policies if we wish to

in order to restrict or allow specific individual API actions,

or we can have more broad reaching policies that

allow or deny an entire service or more.

So let's have a look at an I AM policy.

Now, the first thing to note is they're written in javascript object notation.

All of the policies in Aws are Jason.

Now the version at the top here, don't worry about this date.

It's not a incorrect date, it's actually correct. So this is just a version of

JSON policy statements that are being used.

Next, we have a statement

and the statement is essentially a block of code

and each statement

has a series of individual actions, effects resources and so on.

And they're all evaluated together,

a policy may contain more than one permission statement.

So this block here could be followed by another one. And then there would be a comma

with

JSON. We've got to be very specific about the uh the formatting.

So if you miss a comma, for example, it does break the code.

So um usually the policy editors will highlight that for us.

For example, if you're using visual studio code and often

uh within the AWS management console as well, it will point out where the issues lie.

Now, the effect is either allow or deny. Those are the only two effects that we have.

So do we wanna deny something or do we want to allow it?

Next, we have the actions,

the actions list,

the specific resource operations that the policy is going to affect.

So are we allowing

S3 Dynamo DB or are we denying S3 dynamo DB?

So we specify whether we want to allow or deny.

Then what specifically is that we want to allow or deny

here, we can see that we have a series of API actions

S3 star, that's a wild card. That means all S3 actions,

Dynamo DB, we've got a bit more specific,

but we've gone down to describe level and then we have a wild card.

So there's probably several API actions that start with the word describe.

So it might be described table or something like that.

So there'll be a series of those and we want to allow all of them.

So we can get very specific if we want to or we can keep it a bit more generic.

Now, the resource lists the specific resources that the policy applies to.

So here we have the s reaction with a wild card. So all s reactions,

then we have two

of these resources for the S3 bucket.

So this is the A RN the Amazon resource name for a specific S3 bucket.

But why have we got two lines here? We've got one with a slash star.

Well,

the slash star means that we're assigning some

of the permissions to objects within the bucket.

Whereas this here is the bucket level.

So within S3, there are bucket level API actions and object level API actions.

Those are the the files that are actually stored in the

bucket that they can have their own permissions assigned to them.

So what we do with the star means all of the bucket level and

all of the object level permissions are going to be in this case allowed.

And so we have to specify two resources, one for the bucket,

one for the objects in the bucket.

And then we've got a dynamo DB table.

We specify the exact table with the account number in the region in

the middle here as well as the table name on the end.

Now, as I've mentioned, a star is a wild card. So it means everything from that point.

In this case, S3 colon star means

every API action that starts with S3.

That's all of the API actions for the Amazon S3 service.
