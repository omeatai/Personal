## Setup Multi-Factor Authentication

In this lesson,

you'll learn about the IAM

authentication methods and multi-factor authentication.

So firstly,

let's look at the different authentication methods available within AWS.

IAM

So here we have a user account called John. John wants to access

AWS

and so he logs into the console

using a user name and a password optionally, he can supply

a MFA token, a multi

factor authentication token.

We'll talk about that a bit more in a moment

and this provides access to the management console.

So user name and password is used to access the management console.

John is authenticated

and can then be authorized to perform operations through the console.

On the other hand, John might want to use the CLI or the API

for this we can use what are called access keys.

These are composed of an access key ID and a secret access key.

And you can think of this also as like a

user name and password and it's called long term credentials.

You create this and it's stored in your account and you can use it long term,

you actually have to download a copy of this to be able to use it

yourself and then you're able to use it for as long as this access key is

active within your account. So this is for the

AWS API, whether you're using the CLI

or directly through programmatic input via the API itself.

So access keys are used for programmatic access,

user names and passwords are used for console access.

So let's look at multi factor authentication.

So let's look at multi factor authentication with multi factor authentication.

We have the something you know element.

That's what we're all used to, which is a password.

So the password is hopefully something complex,

but you don't want to write it down or share it with people. It's a secret.

It's something that only you should know. So that's your password.

We then add a second element and that is

something that you have something that you have can be

a smartphone with an application on it that generates a token or it can

be a physical token like the picture on the right hand side here.

So something

which has cryptography in.

So it uses encryption and various algorithms to prove that

you actually have that physical device in your possession.

So now even if someone finds out your password, they need to have this device as well.

A third way is called biometrics. That's something you are.

So things like retina scans and fingerprints, we don't use those in

AWS, but we do have the something you have factor here. The second factor can be

a authentication code or a token

that might be from a physical device.

So we have our user, our user has a password, then we add that second element.

So we could use a virtual MFA device.

For example, Google authenticator on your smart phone or a hardware device.

The hardware device can use security keys and what

are called time based one time password tokens.

It's a best practice that we enable multi factual authetication for the

root account and also for our own individual IAM user accounts as well.

So then of course,

we are less prone to any issues from losing

our passwords or someone guessing what our password is.

We now have to have that physical device present

whenever we want to log in through the console.

Now, we can also use multi factor authentication

with the CLI

and the API as well and that will cover in a bit more detail later on in the course.

Hi guys.

In this lesson we're gonna set

up Multi-Factor Authentication

for our IAM user account.

I'm logged into the AWS Management console

and I'm logged in with my individual IAM user.

As you can see, there are a couple

of security recommendations.

One is to add MFA for the root user,

and the other is to add MFA for ourselves,

so our individual IAM user account.

I'm gonna show you how to set it up for yourself.

You can also log in and set it up

for the root user account as well.

You could choose the 'Add MFA" button,

but I'm gonna go to the user account

and show you how to do it here.

I'm gonna choose my username,

go to "Security credentials",

and then I want to assign an MFA device.

The MFA device can use an authenticator app,

for example, Google Authenticator or Authy.

I'm gonna choose one called Authy

and I'm gonna give it a name "AuthyPhone".

There's also an option to use security keys

and hardware tokens.

So let's click on "Next".

Now, there are three steps.

The first one is to install the application

such as Google Authenticator

on your mobile device or computer.

Then you need to open your Authenticator app

and show the QR code on this page,

and then use the app to scan the code.

Alternatively, you can type in a secret key.

I'm gonna show the QR code

and then I'm gonna use my app

to scan the QR code.

Once you've done that,

you should enter your MFA code

that's on your application.

So mine is 414018.

Then I need to wait for that code to expire

and get the next code

and enter that one on the second code box here.

My next code is 561486.

Okay, now I can add MFA.

So that's done.

I'm now able to use MFA to log into my account.

So let's log out

and I'm gonna try to log back in again.

So let's sign into the console,

enter my account id, my username and my password,

and then of course it's gonna ask me

for that second factor of authentication,

the MFA code.

My current code is 820902.

So let's submit that code

and now I'm logged back in again.

So now we have two-factor authentication

for our account.
