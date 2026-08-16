## Setup Individual User Account

Welcome to another lesson.

In this lesson, we're going to create an individual user account that we can then use to log in to

AWS.

So there are two different types of user.

One is the root user.

The root user is the user that was created using an email address that we specified when we created

our AWS account.

The root user account has full and unrestricted access to the account and it's very difficult, in fact,

to remove any of those permissions or privileges.

That means it's a very powerful user and it's a best practice not to use that user account.

So now that we've created our account, the best practice is you create a really strong password, you

hide that password away and you don't use your root user account again.

So what we should do is create an Iam user.

This will have a friendly name like John plus the account ID or Alias.

That's what you then use to sign in to the console and we can apply permissions using an Iam permissions

policy.

So let's head back to the AWS management console and create our Iam user.

I'm back in the console here and I'm still logged in with my root user account and I'm on the Iam management

console here so you can just search for Iam.

If you just log back in again, go to Iam and you should see a page that's very similar to this one.

So what we need to do here is choose users and then add users and I'm going to give mine a name.

Simply going to be Neil.

I do want to provide user access to the management console, so I need to select this option here.

I recommend using a user in a federated identity through identity sensor.

We're not going to use that option.

We're going to create an Iam user for password.

I'm going to specify a custom password and I don't want to be forced to change it at next login.

I can now click on next I can choose to add permissions to my user.

I'm not going to do that yet.

I'm just going to click on next and then create user.

So I now have a user account created.

I can sign in to the console using this sign in URL, or I can specify this account alias when specifying

an Iam user, I will need to also use the username.

I'll show you how to do this in a moment.

So let's return to the users list.

Now.

One of the most important things to understand is that our user account does not have any permissions

by default.

If I select my user, we can see that there are no permissions policies assigned, and if I go to groups,

there are no groups assigned.

Now, one of the best ways to assign the permissions to our user account is through a group.

So what I can do is go to user groups, create group.

I'm going to call this one simply admins.

It's going to be a very powerful group.

It's going to have full administrator access.

So if I just search for administrator, we should find this administrator access managed policy here.

This one is managed by AWS.

It's pre-created for us.

If I click on the little plus, we can actually see the policy the way that these policies are defined

is using Json code, that's JavaScript object notation and you'll learn how to read these.

This is a very simple one.

Effectively, this policy says that the effect should be to allow all actions.

So the star is what's known as a wildcard.

Allow all actions on all resources.

So basically allow everything so very powerful.

Let's create the group and now we can go into the group and we can add users.

So I'm going to click on Add users, select my user account, and then add users and that's it.

I now have the permissions that I need.

This is a full administrative user now with full access permissions to AWS.

So let's log in as our Iam user in the top right hand corner, I'm going to sign out of my account,

then I'm going to choose log back in again and now I'm going to specify Iam user instead of root user.

I need to specify the account id.

Mine is DCT Dash Labs, dash AWS, then click on next and enter the username and the password.

Then I should be able to log in and that's it.

I am now logged in to my account as my individual user.

In the top right hand corner.

We can see that I'm now logged in as Neil at DCT Dash Labs, Dash AWS.

So that's it.

That's how simple it is to create a user and this user will have full administrative permissions.

And this is the user account I'm going to use for all of the lessons in the remainder of the course.
