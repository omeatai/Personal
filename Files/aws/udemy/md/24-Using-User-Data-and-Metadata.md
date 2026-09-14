[← Course contents](../../01.md)

# 24. Using User Data and Metadata

**Course**: [AWS Certified Solutions Architect Associate (SAA-C03)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/learn/)
**Transcript**: [`../notes/24-Using-user-Data-and-Metadata.txt`](../notes/24-Using-user-Data-and-Metadata.txt)

## Introduction

In this hands-on lesson, we put EC2 user data and instance metadata to the test. We will launch two Amazon EC2 instances to explore the differences between the older IMDSv1 and the more secure IMDSv2 (which requires an authentication token). Finally, we will write a bash script that retrieves metadata to dynamically build a web page, testing it manually first before automating the process completely using the EC2 user data field.

## Detailed Explanation

<details>
  <summary>Step 1 — Launch two instances to test IMDS versions</summary>

### Step 1 — Launch two instances to test IMDS versions

- [x] **Launch an instance with IMDSv1 enabled**
  - In the EC2 console, launch a new instance and name it "IMDS V1" to easily identify it.
  - Select the default Amazon Linux 2023 AMI and `t2.micro` instance type.
  - Proceed without a key pair.
  - Ensure the selected security group (e.g., "Web Access") allows inbound Port 22 (SSH) and Port 80 (HTTP). Port 80 is required for the web server later.

![**Figure 1.** Starting the instance launch process](../images/24/1.png)
![**Figure 2.** Naming the first instance IMDS V1](../images/24/2.png)
![**Figure 3.** Selecting the Amazon Linux 2023 AMI](../images/24/3.png)
![**Figure 4.** Setting instance type to t2.micro](../images/24/4.png)
![**Figure 5.** Proceeding without a key pair](../images/24/5.png)
![**Figure 6.** Configuring network settings to allow SSH and HTTP traffic](../images/24/6.png)

- [x] **Configure Advanced Details for IMDSv1**
  - Scroll to the bottom of the page and expand **Advanced details**.
  - Locate **Metadata accessible** and ensure it is enabled.
  - Change the metadata version setting from the default to make the V2 token **optional**. This effectively allows IMDSv1 requests.
  - Click **Launch instance**.

![**Figure 7.** Expanding Advanced details in the launch wizard](../images/24/7.png)
![**Figure 8.** Changing metadata settings to make the V2 token optional](../images/24/8.png)
![**Figure 9.** Launching the first instance](../images/24/9.png)

- [x] **Launch an instance with default IMDSv2 settings**
  - Start launching a second instance and name it "IMDS V2 Only".
  - Use the exact same AMI, instance type, key pair, and security group settings.
  - Leave the **Advanced details** metadata settings at their defaults ("V2 only, token required").
  - Launch the instance.

![**Figure 10.** Naming the second instance IMDS V2 Only](../images/24/10.png)
![**Figure 11.** Selecting the AMI and Key Pair for the second instance](../images/24/11.png)
![**Figure 12.** Configuring the security group for the second instance](../images/24/12.png)
![**Figure 13.** Leaving Metadata settings at their default V2 Only state](../images/24/13.png)
![**Figure 14.** Verifying the security group rules allow Port 80 and 22 from anywhere](../images/24/14.png)

</details>

<details>
  <summary>Step 2 — Retrieve metadata using IMDSv1 (No Token)</summary>

### Step 2 — Retrieve metadata using IMDSv1 (No Token)

- [x] **Connect to the IMDSv1 instance**
  - Wait for the "IMDS V1" instance to be up and running.
  - Use EC2 Instance Connect to access the browser-based command line.

![**Figure 15.** Selecting the IMDS V1 instance in the console](../images/24/15.png)
![**Figure 16.** Clicking Connect for the selected instance](../images/24/16.png)
![**Figure 17.** The EC2 Instance Connect tab](../images/24/17.png)
![**Figure 18.** Successfully connected to the instance command line](../images/24/18.png)

- [x] **Run metadata queries**
  - Use the `curl` command against `http://169.254.169.254/latest/meta-data/` to retrieve specific pieces of data.
  - Query for the instance ID:
    ```bash
    curl http://169.254.169.254/latest/meta-data/instance-id
    ```
  - The result is printed inline before the next command prompt.
  - Query for the AMI ID:
    ```bash
    curl http://169.254.169.254/latest/meta-data/ami-id
    ```

![**Figure 19.** Running the curl command to get the instance ID](../images/24/19.png)
![**Figure 20.** The instance ID output displayed before the prompt](../images/24/20.png)
![**Figure 21.** Running the curl command to get the AMI ID](../images/24/21.png)
![**Figure 22.** The AMI ID output displayed before the prompt](../images/24/22.png)

- [x] **Explore the metadata directory structure**
  - Query the base URL to see a list of all available options.
  - To find placement info, append `placement/`:
    ```bash
    curl http://169.254.169.254/latest/meta-data/placement/
    ```
  - Retrieve the specific Availability Zone:
    ```bash
    curl http://169.254.169.254/latest/meta-data/placement/availability-zone
    ```

![**Figure 23.** Listing the placement directory options](../images/24/23.png)
![**Figure 24.** Output of the placement directory contents](../images/24/24.png)
![**Figure 25.** Requesting the exact availability zone](../images/24/25.png)
![**Figure 26.** The availability zone output displayed before the prompt](../images/24/26.png)

</details>

<details>
  <summary>Step 3 — Retrieve metadata using IMDSv2 (Token Required)</summary>

### Step 3 — Retrieve metadata using IMDSv2 (Token Required)

- [x] **Attempt an unauthenticated request**
  - Connect to the "IMDS V2 Only" instance via EC2 Instance Connect.
  - Try to run a standard IMDSv1 `curl` command.
  - You will receive an "Unauthorized" message because this instance demands a token.

![**Figure 27.** Connecting to the IMDS V2 Only instance terminal](../images/24/27.png)
![**Figure 28.** Attempting to run a curl request without a token](../images/24/28.png)
![**Figure 29.** The 401 Unauthorized error message returned by the service](../images/24/29.png)

- [x] **Generate and use a session token**
  - Run a specific `curl -X PUT` command to retrieve a token and store it in an environment variable named `TOKEN`.
    ```bash
    TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
    ```
  - Verify the token was stored successfully by running `echo $TOKEN`.
  - Pass the token as a header in your metadata request:
    ```bash
    curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id
    ```
  - The request succeeds, securely returning the instance ID.

![**Figure 30.** Generating the authentication token and saving it to an environment variable](../images/24/30.png)
![**Figure 31.** Running the authenticated curl request successfully using the token header](../images/24/31.png)

</details>

<details>
  <summary>Step 4 — Combine metadata and a bash script manually</summary>

### Step 4 — Combine metadata and a bash script manually

- [x] **Understand the bash script**
  - A bash script (starting with `#!/bin/bash`) can be used to update OS patches, install the Apache web service (`httpd`), and start it on boot.
  - The script leverages IMDSv2 metadata queries with tokens to dynamically fetch the instance ID, AMI ID, and instance type, writing them into an `index.html` file.

![**Figure 32.** Explanation of the bash script commands for installing Apache](../images/24/32.png)
![**Figure 33.** The rest of the bash script generating the custom index.html page](../images/24/33.png)
![**Figure 34.** Copying the full script to the clipboard](../images/24/34.png)

- [x] **Run the script on the instance**
  - In the "IMDS V2 Only" terminal, create a new file: `nano script.sh`.
  - Paste the script, save, and exit.
  - Make the script executable: `chmod +x script.sh`.
  - Run the script with root privileges: `sudo ./script.sh`.

![**Figure 35.** Clearing the terminal to start fresh](../images/24/35.png)
![**Figure 36.** Opening the nano text editor to create script.sh](../images/24/36.png)
![**Figure 37.** Pasting the bash script into nano](../images/24/37.png)
![**Figure 38.** Saving the file in nano](../images/24/38.png)
![**Figure 39.** Using chmod to make the script executable](../images/24/39.png)
![**Figure 40.** Executing the script using sudo](../images/24/40.png)
![**Figure 41.** The terminal output as the script updates packages and installs httpd](../images/24/41.png)

- [x] **Verify the web server**
  - Return to the EC2 console and copy the instance's public IP address.
  - Open it in a new browser tab. You should see a custom web page displaying the instance's metadata.

![**Figure 42.** Copying the public IPv4 address of the instance](../images/24/42.png)
![**Figure 43.** Viewing the custom web page populated with instance metadata](../images/24/43.png)

</details>

<details>
  <summary>Step 5 — Automate provisioning using the User Data field</summary>

### Step 5 — Automate provisioning using the User Data field

- [x] **Launch a third instance with user data**
  - Launch a new instance named "User Data Test".
  - Use the exact same AMI, `t2.micro`, and web-accessible security group.
  - Under **Advanced details**, locate the **User data** text box at the very bottom.
  - Paste the exact same bash script into the User data box.
  - Launch the instance.

![**Figure 44.** Starting a new instance launch](../images/24/44.png)
![**Figure 45.** Naming the instance User Data Test](../images/24/45.png)
![**Figure 46.** Selecting the security group for HTTP access](../images/24/46.png)
![**Figure 47.** Scrolling down to the Advanced details section](../images/24/47.png)
![**Figure 48.** Pasting the bash script into the User data text box](../images/24/48.png)
![**Figure 49.** Launching the final instance](../images/24/49.png)

- [x] **Verify automation and clean up**
  - Wait a couple of minutes for the instance to boot up and automatically run the bootstrap script.
  - Copy the public IP and access it in a browser to see the generated webpage.
  - You can view (but not re-run) user data under **Instance settings > Edit user data** while the instance is stopped.
  - Once verified, terminate all three instances to avoid unnecessary charges.

![**Figure 50.** Waiting for the instance state to become running](../images/24/50.png)
![**Figure 51.** Copying the public IPv4 address of the new instance](../images/24/51.png)
![**Figure 52.** Viewing the custom web page generated automatically on boot](../images/24/52.png)
![**Figure 53.** Terminating all instances to clean up the lab](../images/24/53.png)

</details>

<details>
  <summary>Lab</summary>

## Lab

### Step 1: Launch EC2 Instances and Query IMDSv1

1. Launch an Amazon Linux 2023 EC2 instance. In **Advanced details**, set **Metadata accessible** to enabled, and change the version to **V2 token optional**.
2. Connect to the instance via EC2 Instance Connect.
3. Query the instance ID using IMDSv1:
   ```bash
   curl http://169.254.169.254/latest/meta-data/instance-id
   ```

### Step 2: Query Metadata using IMDSv2

1. Launch a second Amazon Linux 2023 instance. Leave the metadata setting at its default (**V2 only, token required**).
2. Connect to the instance via EC2 Instance Connect.
3. Try running the IMDSv1 curl command; it will fail with `Unauthorized`.
4. Generate a session token:
   ```bash
   TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
   ```
5. Use the token to fetch the instance ID:
   ```bash
   curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id
   ```

### Step 3: Automate Setup with User Data

1. Launch a third instance. Under **Network settings**, attach a security group allowing Port 80 (HTTP).
2. Expand **Advanced details**, and paste the following bash script into the **User data** field:
   ```bash
   #!/bin/bash
   # Update OS patches
   yum update -y
   # Install Apache Web Server
   yum install -y httpd
   # Start and enable Apache
   systemctl start httpd
   systemctl enable httpd
   # Generate custom webpage with IMDSv2 metadata
   TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
   INSTANCE_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
   AMI_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ami-id)
   INSTANCE_TYPE=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-type)
   echo "<h1>Hello from your EC2 Instance!</h1><p>Instance ID: $INSTANCE_ID</p><p>AMI ID: $AMI_ID</p><p>Instance Type: $INSTANCE_TYPE</p>" > /var/www/html/index.html
   ```
3. Launch the instance, wait 2 minutes for it to boot and run the script.
4. Open the instance's public IP address in a web browser to verify the web server is running and displaying the fetched metadata.
5. Terminate all instances when finished.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Can you run IMDSv1 commands on an instance if it was launched with the default Amazon Linux 2023 settings?

<details>
<summary>Answer</summary>

- [x] No, the latest Amazon Linux instances default to IMDSv2 only (token required). To run unauthenticated IMDSv1 queries, you must explicitly configure the metadata version to make the token optional during launch.

</details>

### Question 2: What happens if you stop an instance and edit its user data script?

<details>
<summary>Answer</summary>

- [x] You can edit and view the user data script while the instance is stopped, but the script will **not** run again when the instance starts. User data is designed to execute strictly on the very first boot of the instance.

</details>

</details>

## Summary

In this hands-on exercise, you verified the security differences between IMDSv1 (which processes unauthenticated `curl` requests) and IMDSv2 (which requires generating an auth token via `PUT` request). You also used a bash script to install the Apache web server and dynamically generate a webpage utilizing metadata commands. By embedding this script in the EC2 **User data** field during launch, the entire configuration occurs automatically on boot, demonstrating a highly effective way to bootstrap cloud environments.

## References

- [AWS Certified Solutions Architect Associate (SAA-C03)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-hands-on/learn/)
- Transcript: [`../notes/24-Using-user-Data-and-Metadata.txt`](../notes/24-Using-user-Data-and-Metadata.txt)
