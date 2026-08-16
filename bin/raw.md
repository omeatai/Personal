## Install Tools and Configure AWS CLI

Hey guys, a very quick lesson.

Just to advise you on some of the tools that you're going

to need to install as well as the AWS command line interface.

First thing you need to do is make sure

that before you finish this section of the course,

the very last lesson of this section has some code.

What you need to do is when you go to that lesson,

you will find a link that will take you over to a github

page. And from there, you can download the code

if you're a bit more advanced and you know how to use GIT,

you can also simply synchronize the repository.

The next thing you need to do is install visual studio code.

We're going to be using visual studio code

so that we can open various different code,

snippets and instruction files.

So on Google here, I'm simply gonna search for visual studio code.

This is a Microsoft product. It's completely free.

And if you find it on the internet,

you're going to be able to download it

for your operating system and simply install it.

So that's all you need to do,

whichever operating system you have just choose the

relevant download and then install visual studio code.

The next thing you need to do is install the AWS command line interface

again on Google. I'm simply going to search for AWS command line interface.

And here I want to click on the install or update to the latest version of the AWS CLI.

OK. So we will be able to run command line.

This will enable us to run CLI commands from our computers.

Now, what you can see here is we've got Linux

Mac Os and Windows.

So just choose the relevant operating system and follow

the instructions to install the package on your computer.

Lastly, we want to check that we can access aws cloudshell.

Cloudshell provides a command line interface in the cloud.

I prefer using it these days over the AWS CLI on my computer. In most cases,

it's also preconfigured with credentials for the command line interface.

After you've installed it,

you won't be able to run any aws commands because you haven't authenticated.

I'm gonna show you how to configure credentials a bit later

on after we've created our individual I am user account,

but cloudshell is already authenticated as you as the user you're logged in with.

So it's a really easy way of accessing the command line interface in the cloud

back in the aws management console.

I'm simply gonna search for cloudshell, click on cloudshell.

And what this should do is spin up an environment for us which usually takes

up to 30 seconds.

Now, I do know that some students have had challenges with getting cloudshell.

It's something to do with Aws restricting access to cloudshell for

new accounts with new credit cards that they haven't seen before.

I've used the same credit card over multiple accounts, so I don't have an issue, but I

have known some students to have experienced that problem.

If that's the case, you'll need to contact Aws support and ask them to enable it.

If they won't do it initially,

then you just have to use the AWS command line interface on your computer,

which I will show you how to do

the actual aws CLI commands are identical.

It doesn't matter whether you're using cloudshell or your own computer.

However, of course, your operating system commands are gonna be different.

This is a Linux command line interface here on your computer.

You might be using windows.

If that's the case,

then navigating your file system is gonna be

slightly different to what I do in cloudshell.

But the actual cli commands will be the same.

Now, we can see that the font's quite small on cloudshell.

In the top right hand corner,

I can adjust the settings and make it a bit larger.

So now you can see more easily if I run aws help,

then we should see the help interface for the AWS command line interface and

I can use my space bar just to go through and see the various options

and type Q

to quid out of there. Then I can run commands like AWS S3 LS.

If I had any buckets, any folders in my Amazon S3 service,

then I would be able to see them.

Now,

I don't have any because this a brand new account.

However,

we can tell by the fact that I didn't receive an

error message that I do have credentials to perform that operation.

So that's the good thing about cloudshell.

It's preconfigured with credentials for us. So that's it for this video.

Make sure you download the code, make sure you install visual studio code,

install the command line interface if you want to

be able to run the cli on your computer

and make sure that you can access cloudshell and you're all set up.
