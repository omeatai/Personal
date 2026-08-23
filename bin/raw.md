## IAM Architecture Patterns

Hello and welcome to the first Architecture Patterns lesson of the course.

What I'm trying to do with these lessons is take some of the knowledge that you've learned and put it

into the context of the type of scenarios you're going to see both in the exam and in the real world.

So, imagine you're a solutions architect and you're working for some customers and those customers are saying

that you need to build a solution. And they're going to present some specific requirements to you, present

some challenges that they're trying to deal with, and you've got to come up with the best solution

for the job.

That's the kind of thing that does come up in exam questions.

So, I'm going to pose a few scenarios for you here and give you my idea of what the best solution would

be.

The first requirement is that a select group of users only should be allowed to change their IAM password.

So we don't want to let everybody change their IAM passwords. But we do want some privileged users to

be able to do so.

In this case, you can create a group for the users and apply a permissions policy that grants the IAM

change password API permission.

Moving on to the next requirement, an Amazon EC2 instance must be delegated with permissions to an Amazon

DynamoDB table.

Now, we haven't covered DynamoDB yet, but it's another AWS service.

So how do you delegate permissions?

Well, you will create a role, assign a permissions policy to the role that grants access to the DynamoDB

database service.

A company has created their first AWS account.

They need to assign permissions to users based on job function.

Now, there's a couple of things to note here.

Firstly, this company has created their first ever AWS account, so they may well not have very good

skills with AWS.

So what do the IAM best practices tell you

in this scenario? Well, they suggest that you use the AWS managed policies. And those can be aligned

with specific common job functions.

A solutions architect needs to restrict access to an AWS service based on the source IP address of the

requester.

Remember, we looked at some example policies.

You can create an IAM permissions policy and use the condition element to control access based on source

IP address. A developer needs to make programmatic API calls from the AWS CLI.

In this case, you can instruct the developer to create a set of access keys and use those for any programmatic

access.

A group of users require full access to all Amazon EC2 API actions.

Well, in that case, you could create a permissions policy that uses a wildcard for the action element

relating to EC2. And that would look like the (ec2:\*) action.

And that's it for this architecture patterns lesson.
