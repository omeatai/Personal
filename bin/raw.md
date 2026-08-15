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

Hey guys,

in this video I'm gonna walk you through the different types of AWS accounts,

which one you should choose,

and then we're actually gonna go into AWS and we're gonna sign up

for an account.

So I'm gonna show you how to do it and you

can follow along and create your own account as well.

So there are essentially two different types of AWS account.

There's a free plan account

and a paid plan.

Now by the way,

this came into effect.

July

2025.

Before that,

we did have something called the free tier,

but there was really only one type of account.

You signed up for an account

and you were given

some access to certain services for 12 months for free,

and there was a certain limitation on how much

of each of those services you could consume.

But it was a very simple model.

Now what AWS have done is they've changed that a little bit and they've created

now the free plan or the paid plan.

So when you sign up,

you actually choose which one you want.

Now for new customers only,

you are eligible for the free plan and you get free credits.

Also,

if you purchase the pay plan,

you also get the same free credits,

it's $100 free credits and then you can actually earn another

$100 of credits by taking a few actions in the console.

So it's changed a little bit from what it used to be.

It's only available to new customers,

which means you're only gonna get the credits once according to AWS.

However,

one of the main benefits is that the free

plan now reduces the risk or eliminates really the risk

that you can run up a surprise bill.

So if you're new to AWS,

it's quite a good thing.

So let's have a look at the differences between these two plans.

So when you sign up,

regardless of which plan you choose,

you're gonna get 100.

credits that you can use.

So those will be applied against any service consumption.

So you start using a service,

it's going to be uh basically a consumption-based pricing model.

You've got some credits.

So AWS just takes from the credits rather than charging your credit card.

You get $100 when you sign up,

and then AWS allow you to earn additional credits,

essentially by taking some actions in the console.

I think they just want.

Encourage you to actually go in and start doing a few things.

So you take a few actions,

you configure a few things,

and they give you some more credits.

I'm not sure if that'll be there forever

or whether it's some kind of temporary promo,

but it's there today.

That applies to both the free plan

and the paid plan.

On the free plan you'll get access to always free services.

So there are some services that have a,

a tier of usage,

so you can use a certain amount of

that service each month for free.

You get that on the pay plan as well,

and you also get access to short-term trial offers.

On the free plan,

you are able to access select AWS services and features,

so not everything is available.

So this means that you are limited in what you can do.

Essentially they're removing the ability to do things that

would just eat up all your credits instantly.

So you're only going to be allowed to access certain services.

Now there are quite a lot that you can.

Most of what we do in the training you can access on the free plan,

but there are some exceptions which I'll cover shortly.

With the pay plan,

you can access everything.

And it's really on you,

the risk is on you now.

If you go over your credits,

you're just gonna get charged.

On a free plan,

if you use up all your credits,

it just shuts the account for you so you don't get charged.

There's no charges incurred during usage of the free plan.

So like I say,

what will happen if you use up all Your credits,

they're gonna close the account or you can then upgrade to a paid plan.

On the pay plan,

you will pay for any charges that exceed your credit balance.

So once you've expired all your credit,

you're just gonna get charged to your credit card.

On the free plan,

it expires after 6 months or once all the credits are used up,

whichever comes first.

On a pay plan,

of course that doesn't

actually apply,

it's just going to remain active and charge you for any services you use.

After.

The account has expired,

you can upgrade to a paid plan

within a 90 day grace period.

So essentially the account gets closed down because you've reached

6 months or you've used up all your credit,

and then you've got 90 days to choose whether you want to

uh actually upgrade that account to a paid plan

and that will reopen the account for you.

Of course that doesn't apply to paid plans.

There's a couple of links here that I'm going to share.

These are in the slides,

they should also be attached to the lesson.

And let's have a look at these web pages.

So this is the first one.

If you search in Google for AWS Free Tier,

this should be the first link that you find.

And here we can actually create our free tier account,

which we're going to do shortly.

So what it says here,

new AWS customers can get started at no cost

with the free tier and gain $100 credit at sign

up and $100 more to earn as you explore key

services such as taking some actions in the console.

So you get up to $200 in credits,

that's the same for the pay plan.

You get free usage of select.

AWS services.

And of course,

on the free plan,

there's no charges incurred unless you switch to a paid plan.

Whereas with the paid plan,

you can then go beyond your credit threshold and start paying for services,

and that will happen automatically.

Of course,

that means that you can scale beyond credit thresholds

and access all AWS services on the paid plan.

Now,

if you want to search for specific services,

You can do so here,

we can actually filter.

And for example,

I can see what's available on the free plan and whatever's available on

the free plan will also be available on the pay plan as well,

of course,

but then the pay plan has access to more services.

So for example,

with the free plan,

you will be able to use EC2

as long as you access certain instance types.

If you were on the pay plan,

you could access any instance type and you just get charged accordingly

and it just comes out of your credits until the credits expire.

So you can look through any individual service and find out what

you actually get

on the free plan.

So all of these are available on the free plan,

there's over 100,

you can scroll down,

click on show more,

and there's some more information here about the differences between

the different plans.

There's also a free tier FAQ.

So again,

it's worth reading this and just fully understanding what you're signing up for,

but I'm gonna explain most of this in the video.

And there's this additional page here

in the user guide for the billing and cost

management console which talks more about the free plan.

So there's some reading you can do.

Now a quick and important note on upgrading from the free plan to the paid plan.

There's.

A couple of ways you can actually upgrade.

One is manually and the other is through a service

or feature that actually causes this to happen automatically,

like AWS organizations.

Now this is a quote from the AWS website,

and they tell us that if your account is converted from

the free account plan to the paid account plan through organizations,

AWS partner programs or other enterprise programs.

Any remaining three tier credits will expire and will

not be applied to your paid account usage,

so you lose your credits.

Now the one that really applies here in the courses is AWS organizations.

We're not gonna use partner programs or enterprise programs.

But in quite a few of my courses,

not all of them,

but many,

we use AWS organizations.

Now,

what you don't want to do is just go in

and create an organization and then lose your credits.

So what you can do instead to work around that is

manually upgrade from the free account plan to the paid account plan

before you use AWS organizations,

and then your free tier credits will carry over and be automatically applied

to any future bills.

And also,

3 tier credits actually expire 12 months from the date you opened your account.

But remember that if you create a free account,

it gets automatically shut down after 6 months,

even if you have credits

left.

So when you upgrade,

you will actually be able to preserve those credits a bit longer.

So which plan should you choose?

Choose the free plan if you're worried about getting a surprise bill.

Very good for beginners,

if you're not familiar with AWS.

Yeah,

then you've got that peace of mind that you're not gonna get charged for anything.

You've got those credits and if you use them all up,

then AWS just shuts your account rather than charging you any more money.

Good if you're new to AWS and you want to get familiar before you upgrade,

and for short-term uses.

So if you're just doing a single course,

it's only gonna take you a couple of months,

maybe more,

maybe less,

and you don't need access to all of the services,

then this will be OK as well.

Choose a pay plan if you're familiar with AWS and you're confident with pricing

and cost controls.

Now,

everybody who uses AWS should

make sure that they get familiar with how AWS

charges and what the costs are for different services.

Cost controls mean,

well,

shutting down a service,

terminating it,

deleting something to make sure you don't get charged,

and also,

very importantly,

setting up billing alarms so you get notified

when you.

Reach a certain amount of expenditure.

So 5 $10.20 dollars,

whatever you want to set it to,

you will then receive an email when you get,

when you actually approach all your forecast to hit that limit.

And that's something I'll show you how to do later on

in the course.

You should also choose a paid plan if you need to

access services that are not included in the free plan.

There is quite a lot that I do in many of

my courses that would not be included in the free plan.

For example,

registering Route 53 domain names and using AWS organizations

as a couple of examples.

So to do those labs,

you would need a paid plan.

Also,

of course,

longer term uses after 6 months because your free plan

account will expire after 6 months.

So free plan best for beginners who want a

safe time-limited way to explore AWS without complex billing.

And the pay plan

is best for students building larger or more varied projects or needing

access to more advanced services,

many of which we will be using in the hands-on lessons.

So basically,

eventually everybody should be on a pay plan.

You do need to become familiar

with how AWS charges and using cost controls and,

you know,

being diligent when you're using AWS.

And

in the actual hands on lessons,

I generally will tell you and often show you

what to do in terms of terminating and switching

off services at the end of the lesson,

but you do also need to take some self responsibility as well.

Make sure that you're familiar with how AWS charges and monitor that yourself.

Make sure Get that billing alarm set up as well.

So what are you going to need to set up your account?

Firstly,

you will need a credit card for setting up the account and paying any bills.

This is true even if you're setting up a free plan account.

AWS still want the credit card on file so that they

can use it when you switch to a paid plan.

You're also going to need a unique email address for this account,

so that means it's unique across AWS.

It's not been used to open any other AWS account.

You should check if you can use a dynamic alias with your existing email address.

For example,

if you're using Gmail,

it does support dynamic aliases.

So if my email address was john@gmail.com,

I would be able to use John plus

and then something unique.

OK,

and that would be my account alias essentially,

so whatever I want to call my AWS account,

and that helps me to remember it.

And then at gmail.com.

So then you can create multiple unique email addresses

for different AWS accounts but using the same inbox.

You'll also need a unique AWS account name.

So AWS provides an account ID which is quite a long number

to identify your individual accounts.

The account name is just a friendly name that we can use,

so words rather than numbers,

much easier to remember.

So what I try to do is make my account name and

the alias I'm using in my dynamic alias for my email,

the same.

And then also the alias the same as well.

Now the account name and the alias do need to

be unique across AWS so it has to be something.

That has not been used before.

And by the way,

the alias is used to construct

a URL that we can then use to log in

using that friendly name.

You'll also need a phone to receive an

SMS verification code during the sign up process.

OK,

so that's everything.

If you've got this information,

let's go straight over to AWS and we.

Gonna create a free tier account.

If not,

pause the video,

get it together,

and then you can resume.

So I'm back in the AWS website here

on the AWS Free Tier page,

and I'm gonna click on Create a free tier account.

I now need to enter the root user email address,

so that's that unique email address

that I discussed a moment ago.

And then the account name.

Once you've entered those two pieces of information,

click on verify email address,

and it is gonna send a verification email to your

inbox that you need to go and attend to.

Once you've received the email,

copy the verification code in and click on verify.

You now need to set a root user password and make sure it's a strong password.

I'm now on the screen where I get to choose where.

I'm going to sign up for a free or paid plan.

So,

again,

we've gone through all this information.

It's free,

we get 6 months access,

we're gonna get up to $200 in credits.

I'm happy with that,

it's a good place to start,

so I'm gonna click on choose free plan.

Next,

you want to set personal.

You're using this for your own learning purposes,

it's not a business account.

And then fill out your personal information,

so your name.

phone number,

country,

region,

address,

and so on.

Once you've done that,

agree

to the terms and conditions and click on continue.

On the next page,

we now need to enter

our billing information.

So make sure your country is selected correctly,

enter your credit card details,

including expiration date and security code and your cardholder's name,

and then click on verify and continue.

Next,

you need to confirm your Identity by entering

your phone number and clicking on send SMS.

I've received my verification code,

so I'm gonna put that in and then click on continue.

Step 4 or 5.

So congratulations,

you have now created a free tier account.

Now AWS will be activating this account and that might take a few minutes.

And then as I mentioned on the screen here,

you will then receive an email when that process is complete.

And at that point,

we can head across to the AWS management console,

and it has logged us straight in.

So in this case,

because I'm currently in Europe,

it's logged me into a European region,

you might want to change to a US region or it

should pop you into one of the US regions by default.

Generally for the course,

we're gonna be using United States North Virginia as the region

in which we perform

most activities.

Now because I clicked straight from the registration confirmation,

I was automatically logged in,

but.

You will also need to know how to manually log in.

So for example,

if I sign out from the console here

and then go to sign back in again,

now it's gonna ask for the account ID or alias and then an IAM username or password.

This is the identity and access management service.

Now we don't have that information at this

point because we haven't created an IAM account.

What we've essentially created when we open the account

for the first time is the root user account.

So I need to click on this button here,

sign in using root user email.

Then

I can enter the email address that I used at sign up

and then enter the password

and then sign in.

So now I am signed in again and I've shown

you how to sign in using the root user account.

In subsequent lessons,

I'm gonna show you how to log in with an IAM user account that we create.

I'm gonna show you around the console more

and we're gonna configure,

for example,

billing alarms and other settings for our account.
