[← Course contents](../../01.md)

# 22. Connecting to Amazon EC2

**Course**: [AWS Certified Solutions Architect Associate (SAA-C03)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/learn/)
**Transcript**: [`../notes/22-Connecting-to-Amazon-EC2.txt`](../notes/22-Connecting-to-Amazon-EC2.txt)

## Introduction

In this lesson, we learn how to connect to Amazon EC2 instances using the Secure Shell (SSH) protocol for Linux and the Remote Desktop Protocol (RDP) for Windows. We'll explore connecting securely through EC2 Instance Connect in the browser, the standard SSH client, and RDP clients using key pairs for authentication.

## Detailed Explanation

<details>
  <summary>Step 1 — Understand connection types and requirements</summary>

### Step 1 — Understand connection types and requirements

- [x] **Prerequisites for connecting**
  - Your instance must have a public IP address or a public IP DNS address to connect from the outside world.
  - The security group must allow inbound traffic on the required ports (Port 22 for SSH/Linux, Port 3389 for RDP/Windows) from your source address (or `0.0.0.0/0` for any source).

![**Figure 1.** Connecting to Amazon EC2 title slide](../images/22/1.png)

![**Figure 2.** Viewing the public IPv4 address and DNS in the EC2 console](../images/22/2.png)

- [x] **Available connection methods**
  - **EC2 Instance Connect**: Connects directly from the browser using the AWS console.
  - **Session Manager**: Uses the Systems Manager service for a secure connection without opening inbound ports.
  - **SSH Client**: Connects from your home computer terminal using the private key (`.pem` file) downloaded earlier.

![**Figure 3.** The "Connect to instance" page showing various connection tabs](../images/22/3.png)

</details>

<details>
  <summary>Step 2 — Connect to a Linux instance using EC2 Instance Connect</summary>

### Step 2 — Connect to a Linux instance using EC2 Instance Connect

- [x] **Using EC2 Instance Connect**
  - Select your Linux server in the EC2 Management Console.
  - Click on **Connect**.
  - Choose the **EC2 Instance Connect** tab.
  - The default username is `ec2-user`. Leave it as is.
  - Click on **Connect** to open a browser-based command line.

![**Figure 4.** The EC2 Instance Connect tab ready to connect](../images/22/5.png)

- [x] **Testing the connection**
  - Run a command like `ifconfig` to show IP addresses.
  - Run `ping google.com` to verify internet connectivity.
  - Use `Ctrl+C` to stop the ping requests.

![**Figure 5.** The browser-based command line upon successful connection](../images/22/6.png)

![**Figure 6.** Running ifconfig in the terminal](../images/22/7.png)

![**Figure 7.** Running a ping test in the terminal](../images/22/8.png)

</details>

<details>
  <summary>Step 3 — Connect using an SSH Client (Optional)</summary>

### Step 3 — Connect using an SSH Client (Optional)

- [x] **Connecting from your home computer**
  - You need your private key file (`.pem`) downloaded when creating the key pair.
  - The AWS console provides the full SSH command, formatted like this:
    ```bash
    ssh -i "your-key-pair.pem" ec2-user@your-public-dns-name
    ```
  - Windows users may need to install an SSH client (a feature of Windows), while macOS and Linux have it pre-installed.

![**Figure 8.** The SSH client tab showing connection instructions and the command](../images/22/4.png)

</details>

<details>
  <summary>Step 4 — Connect to a Windows instance using RDP</summary>

### Step 4 — Connect to a Windows instance using RDP

- [x] **Using the RDP Client**
  - Select the Windows server in the EC2 console and click **Connect**.
  - Choose the **RDP client** tab.
  - You can either download the Remote Desktop file or use an RDP client on your computer (built into Windows, downloadable for Mac).

![**Figure 9.** The RDP client connection tab](../images/22/10.png)

![**Figure 10.** Adding a PC in a local RDP client](../images/22/11.png)

![**Figure 11.** The configured PC in the RDP client](../images/22/12.png)

- [x] **Retrieving the Administrator password**
  - Note the Public DNS name and the username (`Administrator`).
  - Click **Get password**.
  - Upload the private key file (`.pem`) downloaded previously.
  - Click **Decrypt password** to reveal the password.
  - Copy the password and use it in your RDP client to connect.

![**Figure 12.** Uploading the private key file to get the Windows password](../images/22/13.png)

![**Figure 13.** The private key contents displayed before decryption](../images/22/14.png)

![**Figure 14.** The decrypted Administrator password](../images/22/15.png)

![**Figure 15.** Entering the credentials in the RDP client](../images/22/16.png)

![**Figure 16.** Logged into the Windows Server desktop environment](../images/22/17.png)

![**Figure 17.** Checking the security group to ensure port 3389 is open for RDP](../images/22/18.png)

</details>

<details>
  <summary>Step 5 — Terminating instances</summary>

### Step 5 — Terminating instances

- [x] **Cleaning up resources**
  - Under **Instance state**, you can stop, reboot, or terminate instances.
  - Stopping an instance stops compute and memory billing, but storage is still billed.
  - Terminating an instance essentially deletes it.
  - Terminated instances will stay in the console for a short while before disappearing.

![**Figure 18.** Selecting Terminate instance from the Instance state menu](../images/22/19.png)

![**Figure 19.** The Terminate instance confirmation prompt](../images/22/20.png)

</details>

<details>
  <summary>Lab</summary>

## Lab

### Step 1: Connect to Linux EC2 Instance

1. In the EC2 console, select your Linux instance.
2. Click **Connect**, leave the user as `ec2-user`, and use **EC2 Instance Connect**.
3. Once connected, run:
   ```bash
   ifconfig
   ping google.com
   ```
4. Press `Ctrl+C` to stop the ping.

### Step 2: Connect to Windows EC2 Instance

1. In the EC2 console, select your Windows instance.
2. Click **Connect** and select **RDP client**.
3. Copy the **Public DNS**.
4. Click **Get password**, upload your `.pem` key pair file, and click **Decrypt password**.
5. Copy the decrypted password.
6. Open your local RDP client, paste the DNS name, use the username `Administrator`, and paste the password to log in.

### Step 3: Terminate Windows Instance

1. Select the Windows instance.
2. Click **Instance state** > **Terminate instance**.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What happens if a little red banner comes up saying it can't connect via EC2 Instance Connect?

<details>
<summary>Answer</summary>

- [x] Check two main things:
  1. The instance must have a public IP address.
  2. The instance's security group must have Port 22 open for SSH (with source `0.0.0.0/0` for any source).

![**Figure 20.** Checking the security group to ensure port 22 is open for SSH](../images/22/9.png)

</details>

### Question 2: Are you billed for compute when an instance is stopped?

<details>
<summary>Answer</summary>

- [x] No, stopping an instance means you are not billed for running compute and memory, but you will still pay for the storage allocated to the server.

</details>

</details>

## Summary

Connecting to EC2 instances requires proper networking setup, including a public IP and open ports in the security group (Port 22 for Linux/SSH, Port 3389 for Windows/RDP). You can easily connect to Linux directly from the browser using EC2 Instance Connect, and connect to Windows by decrypting the Administrator password with your private key and using an RDP client. Finally, remember to terminate instances you no longer need to avoid unnecessary charges.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/learn/)
- Transcript: [`../notes/22-Connecting-to-Amazon-EC2.txt`](../notes/22-Connecting-to-Amazon-EC2.txt)
