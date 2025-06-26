---
title: Launching a Graviton4 instance
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## System Requirements

  - An AWS account

  - A Linux or MacOS host

  - A c8g or r8g instance (4xlarge or larger)

  - At least 128GB of storage

## AWS Console Steps

Follow these steps to launch your EC2 instance using the AWS Management Console:

### Step 1: Create an SSH Key Pair

1. **Navigate to EC2 Console**

   - Go to the [AWS Management Console](https://console.aws.amazon.com)

   - Search for "EC2" and click on "EC2" service

2. **Create Key Pair**

   - In the left navigation pane, click "Key Pairs" under "Network & Security"

   - Click "Create key pair"

   - Enter name: `arcee-graviton4-key`

   - Select "RSA" as the key pair type

   - Select ".pem" as the private key file format

   - Click "Create key pair"

   - The private key file will automatically download to your computer

3. **Secure the Key File**

   - Move the downloaded `.pem` file to the SSH configuration directory
     ```bash
     mkdir -p ~/.ssh
     mv arcee-graviton4-key.pem ~/.ssh
     ```

   - Set proper permissions (on Mac/Linux):
     ```bash
     chmod 400 ~/.ssh/arcee-graviton4-key.pem
     ```

### Step 2: Launch EC2 Instance

1. **Start Instance Launch**

   - In the left navigation pane, click "Instances" under "Instances"

   - Click "Launch instances" button

2. **Configure Instance Details**

   - **Name and tags**: Enter `Arcee-Graviton4-Instance` as the instance name

   - **Application and OS Images**: 
     - Click "Quick Start" tab

     - Select "Ubuntu" 

     - Choose "Ubuntu Server 24.04 LTS (HVM), SSD Volume Type"

     - **Important**: Ensure the architecture shows "64-bit (ARM)" for Graviton compatibility

   - **Instance type**: 
     - Click on "Select instance type"

     - Select `c8g.4xlarge` or larger

3. **Configure Key Pair**

     In "Key pair name", select the SSH keypair you created earlier (`Arcee-Graviton4-Instance`)
   
4. **Configure Network Settings**

   - **Network**: Select a VPC with a least one public subnet. 

   - **Subnet**: Select a public subnet in the VPC

   - **Auto-assign Public IP**: Enable

   - **Firewall (security groups)**

     - Click on "Create security group"

     - Click on "Allow SSH traffic from"

     - In the dropdown list, select "My IP". 
     
     Note 1: you will only be able to connect to the instance from your current host, which is the safest setting. We don't recommend selecting "Anywhere", which would allow anyone on the Internet to attempt to connect. Use at your own risk.

     Note 2: although this demonstration only requires SSH access, feel free to use one of your existing security groups as long as it allows SSH traffic.

5. **Configure Storage**

   - **Root volume**: 
     - Size: `128` GB

     - Volume type: `gp3`

7. **Review and Launch**

   - Review all settings in the "Summary" section

   - Click "Launch instance"

### Step 3: Monitor Instance Launch

1. **View Launch Status**

   After a few seconds, you should see a message similar to this one:

   `Successfully initiated launch of instance (i-<unique instance ID>)`

   If instance launch fails, please review your settings and try again.

2. **Get Connection Information**

   - Click on the instance id, or look for the instance in the Instances list in the EC2 console.

   - In the "Details" tab of the instance, note the "Public DNS" host name

   - This is the host name you'll use to connect via SSH, aka `PUBLIC_DNS_HOSTNAME`

### Step 4: Connect to Your Instance

1. **Open Terminal/Command Prompt**

2. **Connect via SSH**
   ```bash
   ssh -i ~/.ssh/arcee-graviton4-key.pem ubuntu@<PUBLIC_DNS_HOSTNAME>
   ```

3. **Accept Security Warning**

   - When prompted about authenticity of host, type `yes`

   - You should now be connected to your Ubuntu instance

### Important Notes

- **Region Selection**: Ensure you're in your preferred AWS region before launching

- **AMI Selection**: The Ubuntu 24.04 LTS AMI must be ARM64 compatible for Graviton processors

- **Security**: please think twice about allowing SSH from anywhere (0.0.0.0/0). We strongly recommend restricting access to your IP address

- **Storage**: The 128GB EBS volume is sufficient for the Arcee model and dependencies

- **Backup**: Consider creating AMIs or snapshots for backup purposes


