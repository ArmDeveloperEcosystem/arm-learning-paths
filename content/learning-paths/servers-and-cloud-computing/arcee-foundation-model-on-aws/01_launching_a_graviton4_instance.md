---
title: Launch a Graviton4 instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Requirements

Before you begin, make sure you have the following:

- An AWS account  
- Permission to launch a Graviton4 EC2 instance of type `c8g.4xlarge` (or larger)  
- At least 128 GB of available storage

If you're new to EC2, check out [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/).

## Create an SSH key pair

To deploy the Arcee AFM-4.5B model, you'll first need an EC2 instance running on Arm-based Graviton4 hardware. Start by signing in to the [AWS Management Console](https://console.aws.amazon.com), then navigate to the **EC2** service. From there, you’ll create an SSH key pair that allows you to connect to your instance securely.

Open the **Key Pairs** section under **Network & Security** in the sidebar, and create a new key pair named `arcee-graviton4-key`. Choose **RSA** as the key type and **.pem** as the file format. Once you create the key, your browser will download the `.pem` file automatically.

To keep the key secure and usable, move it to your SSH configuration directory and restrict its permissions.

On macOS or Linux, you can run:

```bash
mkdir -p ~/.ssh
mv arcee-graviton4-key.pem ~/.ssh/
chmod 400 ~/.ssh/arcee-graviton4-key.pem
```

## Launch the EC2 instance

In the left sidebar of the EC2 dashboard, click **Instances** and then **Launch instances**.

### Configure instance settings

- **Name**: `Arcee-Graviton4-Instance`  
- **Application and OS image**:  
  - Choose the **Quick Start** tab  
  - Select **Ubuntu Server 24.04 LTS (HVM), SSD Volume Type**  
  - Ensure the architecture is **64-bit (ARM)**  
- **Instance type**: Select `c8g.4xlarge` or larger  

Under **Key pair name**, select `arcee-graviton4-key`.

### Configure network

- Choose a VPC with at least one public subnet  
- Select a public subnet  
- Enable **Auto-assign Public IP**

### Configure firewall

- Select **Create security group**  
- Choose **Allow SSH traffic from** and select **My IP**

{{% notice note %}}
You will only be able to connect to the instance from your current host, which is the safest setting. Selecting "Anywhere" allows anyone on the internet to attempt to connect—use at your own risk.

Although this tutorial only requires SSH access, you can reuse an existing security group if it allows SSH traffic.
{{% /notice %}}

### Configure storage

- **Root volume size**: `128` GB  
- **Volume type**: `gp3`

### Review and launch

Check all configuration settings and click **Launch instance**.

## Monitor the instance launch

After a few seconds, you should see a message like:

```
Successfully initiated launch of instance (i-xxxxxxxxxxxxxxxxx)
```

If the launch fails, double-check the instance type, permissions, or network setup.

To get connection info:
- Go to the **Instances** list
- Click the instance ID
- In the **Details** tab, copy the **Public DNS** hostname — you’ll use this to connect via SSH

## Connect to your instance

Open a terminal and connect to the instance using the key file:

```bash
ssh -i ~/.ssh/arcee-graviton4-key.pem ubuntu@<PUBLIC_DNS_HOSTNAME>
```

When prompted to verify the host authenticity, type `yes`.

You should now be connected to your Ubuntu instance on Graviton4.

{{% notice note %}}
**Region**: Make sure you're launching in your preferred AWS region.  
**AMI**: Confirm that the AMI is ARM64-compatible.  
**Security**: Restrict SSH access to your own IP for best practice.  
**Storage**: 128 GB is enough for the AFM-4.5B model and dependencies.  
**Backup**: Consider creating an AMI or snapshot once your setup is complete.
{{% /notice %}}

