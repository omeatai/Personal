## Configure Account and Create a Budget

In this lesson,

we're gonna make a few configuration changes to our account

and we're also gonna set a budget which will alert us

when we are forecast to or have exceeded a certain

threshold in terms of the dollars spent each month.

So what we're gonna do is we're going to set an.

Account Alias,

that makes it easier to log in when we're

using the identity and access management service for login.

And we're going to enable access to billing for IAM users.

We'll update our billing preferences with a few settings,

and then we're gonna create a budget that has an alarm associated with it.

I'm logged into my account,

currently I'm still using the root user.

We're gonna set up an IAM user a bit later on.

And what I want to do now is I want

to navigate to the identity and access management service,

so I can simply search for IAM and I favoriteed mine.

When I click on IAM that's gonna take me over to the console for this service.

Now we can see in the top right hand corner here that IAM is a global service.

We don't need to select a specific region.

That means that we only have to create the resources like user accounts in one place.

Now on the right hand side here we've got AWS account,

we can see the account ID,

that's a number,

and then we've got this account alias.

Now we can see here there's a sign in URL for IAM users.

We're gonna create users in future lessons.

Now it includes the account ID by default.

That's not really ideal,

it's not easy to remember.

So what we're going to do is create an account alias.

Now I've set my account name to DCT Lab training.

If you need to change that,

you can do so on the account tab,

we'll be going there shortly.

So I'm gonna try and create a alias which is the same.

Now this does need to be unique across

AWS.

So let's see if I can get this one.

And that works,

so I do now have that alias.

If you try and use the same one,

it won't work because it's now been taken.

That means that I can click on the sign in URL and simply use this for logging in.

So I'm gonna take a note of this somewhere so that later

on I can use it for logging in as an IAM user.

The next thing we're going to do is we're

gonna make some changes to our account settings.

So I'm gonna click in the top right hand corner here,

select account.

On this page we can change the account name if we need to.

I've already set mine to the account name that I want.

Let's scroll down on this page a little bit.

We can see some of the regions that have been enabled by default.

So not all regions are enabled by default.

You do have to enable certain regions if you want to use them.

In this case,

plenty of regions are enabled for me.

Now,

down here we can see this IAM user and roll access to billing information.

Once we've created an administrative user account using IAM,

we're no longer going to log in as the root account.

Sometimes you'll want to access billing information

and it will tell you you have to log in

as a route account.

If we enable this setting,

then we don't need to do that,

we can actually assign the relevant permissions through IAM.

And then access the billing information when we need to.

So I've set that setting.

Next on the left-hand side,

I'm gonna come down to billing preferences.

In here under alert preferences,

I want to select this option to receive AWS free tier alerts

and receive cloudwatch billing alerts.

And I need to put in my email address here.

This means I'm going to receive an email alert if

I use up my credits for free tier usage.

On the left-hand side,

I'm going to enable this option to receive

my invoices by PDF so I get them attached to my email.

It's easier than having to come back into AWS to look up

what I've been charged for.

The last thing to do now is on the left-hand side under budgets and planning,

I'm going to click on budgets.

This takes me to the AWS budgets service.

Here we're gonna create a budget

and under budget setup,

I'm going to use a template.

Now it's up to you,

you can use a zero spend budget if you're really cost sensitive.

I like to just set a monthly cost budget

and I'll just set it to

$5.

This means that I'm going to get an alert

in my email

when I'm forecast to reach my $5 across the month or I actually reach it.

And in fact,

it says here that I'll be notified in two

times.

One is when my actual spend reaches 85%,

and

then secondly,

when my actual spend reaches 100%.

So you get a couple of emails here.

There are the occasional charges for certain things like hosted zones,

once we create a route 53 hosted zone,

it's less than $1 a month usually for a hosted zone.

And then there's some other small charges,

occasionally a couple of dollars here and there,

but we shouldn't go over $5 except when we actually register a domain,

which will take us over that because

the cheapest domains are about $5 or $6.

OK,

so I'm gonna enter my email address and create budget,

and that's all I need to do,

it's gonna set everything up for me.

And that's it,

I've set up my budget.

Very,

very important step here,

you wanna make sure you do this.

As long as you follow my instructions and shut down and terminate resources,

you should not exceed this budget except when you're registering the domain.

However,

if you forget something,

at least you've got a backup and you're gonna get an email and that's gonna warn you.

And then you can come into.

The Cost Explorer service.

OK,

so on the left-hand side here,

if I just scroll up,

we've got this costs Explorer.

In Cost Explorer,

you can have a look at a breakdown of your spend.

OK,

there's nothing here yet,

so it says I have to wait 24 hours cos I've just opened this account.

But then you'll be able to come in here and see an itemized breakdown

of your spend.
