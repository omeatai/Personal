## Creating IAM Users and Groups

Welcome back in this lesson.

We're going to head to the I AM service and we're gonna create a user

account that we can log in with and assign that user account to a group.

And then I'm gonna show you how you can actually log in as that user.

I'm back in the AWS management console. I'm gonna click on I AM

and I'm in the identity and access management service.

Now, what we're going to do is we're going to create a user

at the moment. There are no user accounts in this account.

First, I'm gonna create a user group,

the user group is the way that we're

gonna assign the permissions to the user account.

So we assign the permissions to the group and then we add

the user to the group and the user will inherit those permissions.

So what I'm gonna do here is create a group.

I'm simply gonna call this one admins because the account

I'm going to create is gonna be an administrative account.

Then I need to attach a permissions policy here.

I'm gonna choose administrator access. This is a very powerful policy.

The policies are written in javascript object notation

if I expand the policy here, we can see the

JSON code. So here this statement is fairly straightforward.

The effect is to allow

the action is a star. A star is a wildcard, it means anything.

So any action, all actions

and then the resources are star as well.

So another wildcard so essentially allow all actions

on all resources so you can do anything.

So that's what I want for this particular user account.

So I selected administrator access and then in the bottom right hand corner,

I'm going to create that group.

So now I have my admin

group. Next, I'm gonna click on users and create user.

I'm gonna provide a name. I'm simply gonna call my Neil.

Next,

I'm gonna select this option to provide the

user with access to the management console.

That means I'll be able to log in to the

management console rather than just using programmatic access methods.

Now, here we're given a choice, we can create an I AM user.

But what Aws are recommending is that we use the I Am Identity Center.

Now,

I am identity center provides some amazing features like single sign

on it provides access to business applications and multiple accounts.

It's a very,

very useful service and Aws are now trying to encourage people to start using it.

We will get into that later in the course. However, we do need to learn.

I Am as well because it's core to the Aws exams

and it's what I'm gonna use for a lot of.

So I'm actually using I Am for most of my accounts

because I don't need single sign on in many cases.

So here we're going to create an I AM user.

I'm gonna set a custom password and I'm gonna deselect

this requirement to change the password at the next login.

And then I'm gonna click on next.

We now have the option to add the user to a group,

which is exactly what we're going to do by selecting admins.

We could also copy permissions from existing users or attach policies directly.

But when we want to create multiple users who have the same permissions,

it's better to create a group rather than attaching policies

directly to every individual user account from a management perspective.

It's much easier. Now, I've selected my group, I'll click on next

and then create user. Now we're presented with the console sign in details.

We already know these from earlier on. This is what we're going to use to log in.

I'm gonna copy this so I can go straight across and

show you how to log in as this user account.

We know that the user name is Neil and the

console password is available here for us to copy.

Uh At this point in time, we won't be able to see it again.

We would have to change it in the future if we forget what it is.

So I'm done with creating the user account.

I can return back to the user list here and I'm going

to open a private window so I can log in separately.

So here I'm using a private window.

I'm gonna paste in the sign in link for I am.

This takes me to the login page. I'm gonna enter my user name

and then my password and then simply sign in.

So now I'm signed in

and I'm signed in with my individual user account for some reason.

It's, it's put me into Ohio. I was in us East before.

So let's just change back to us east.

Most of the labs that we do in the course are gonna be run using North Virginia.

It's not always essential,

but often it is required depending on the code that we

provide for you or the specific instructions that we show you.

So you can now see that I'm logged in as Neil at D CD lab training. Ok.

So I'm logged in as my individual user account

and this account has full administrative permissions so we can use it for

all of the lab exercises that we're going to perform in this course.

And from now on,

you should be logging in with your individual I

am user account and not with your root account.
