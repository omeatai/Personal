## Create your own free AWS account

Welcome back in this video.

I'm going to give you a brief overview of what Aws accounts are,

how we create them and how we manage them.

And then in the next lesson,

I'm gonna show you how to create your own free tour account on Aws.

So to get started, what do you need to open an Aws account?

First thing is you will need a credit card.

Secondly, you're going to need a unique email address and by unique, I mean,

it cannot be associated with any other Aws account.

Now you can create multiple Aws accounts but you

will need a different email address for them.

But the credit card can be the same.

I often use dynamic email aliases.

So if your email address was John at gmail.com,

you can do John plus Aws account one at gmail.com and then Aws account two

at gmail.com and so on. That's a dynamic email alias.

It works with Gmail, it works with some other mail services as well.

So once you've got these two things, you can create an Aws account.

Now, when you do so

it's gonna create something called the account root user.

Now the account root user logs in with the

email address that you created the account with.

So there's gonna be an email address and a password.

Now, the root user has full control over the account.

You also cannot limit most of the permissions associated with the root user.

For that reason. It's an all powerful account

and we don't want to use it.

The best practice is to set a very strong password and then

not use the root user account unless you specifically need to.

What we do instead is we use the identity and access management service. I am

with I am we can create users, groups, roles and policies.

So what we do is we create a user account,

we then create a group to put the user into and

then we associate a policy that has permissions to that group.

You'll see how to do this in another lesson

that user can have uh a user name, like your own name. I use Neil, of course.

And so that is the user that you are then going to use subsequently to log in to Aws.

So it's very important to remember that it is an I am best practice to create

individual users and to avoid using the

root account unless you specifically need to.

And there are a few cases where the root account is required.

So we have our aws account, we can log in through the management console.

That's gonna be the easiest way to get started.

And from there, what we need to do is authenticate.

So when we log in with an I AM principle, like a user account,

we essentially have to authenticate.

And of course, we have these different methods of accessing AWS and managing it.

We can use the console. We can also use the command line interface.

Or if we're developing code,

we can leverage the API through a software development kit,

but we always need to authenticate prove who

that we are. Who we say we are.

For example, with a user name and password.

If you're logging into the management console,

then we get authorized to access certain resources.

And this is defined through policies.

The policies define what resources we're allowed to

access and what level of access we have.

For example, we might have access to EC2 instances, R DS, databases,

S free and low balances.

Now, all identities and resources are created within the AWS account.

There are ways that you can have multiple account

structures where you can centralize some of the management,

but each of the users will exist in one place and then

you have to implement measures to access resources across a different accounts.

So that's it for this lesson.

We're gonna go ahead in the next lesson and create our free to account

and make sure you've got a unique email address and a credit card ready.
