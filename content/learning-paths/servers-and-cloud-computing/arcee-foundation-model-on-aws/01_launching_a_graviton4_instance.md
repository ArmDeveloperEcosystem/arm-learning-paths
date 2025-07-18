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

If you're new to EC2, check out the Learning Path [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/).

## Create an SSH key pair

To deploy the Arcee AFM-4.5B model, you need an EC2 instance running on Arm-based Graviton4 hardware:

Start by signing in to the [AWS Management Console](https://console.aws.amazon.com), then navigate to the **EC2** service.

From there, you can create an SSH key pair that allows you to connect to your instance securely.

## Set up secure access 

Open the **Key Pairs** section under **Network & Security** in the sidebar, and create a new key pair named `arcee-graviton4-key`. 

Next, select **RSA** as the key type, and **.pem** as the file format. Once you create the key, your browser will download the `.pem` file automatically.

To keep the key secure and usable, move the `.pem` file to your SSH configuration directory and update its permissions to restrict access.

To do this, on macOS or Linux, run:

```bash
mkdir -p ~/.ssh
mv arcee-graviton4-key.pem ~/.ssh/
chmod 400 ~/.ssh/arcee-graviton4-key.pem
```

## Launch and configure the the EC2 instance

In the left sidebar of the EC2 dashboard, select **Instances**, and then **Launch instances**.

Use the following settings to configure your instance:

- **Name**: `Arcee-Graviton4-Instance`  
- **Application and OS image**:  
  - Select the **Quick Start** tab  
  - Select **Ubuntu Server 24.04 LTS (HVM), SSD Volume Type**  
  - Ensure the architecture is set to **64-bit (ARM)**  
- **Instance type**, select `c8g.4xlarge` or larger  
- **Key pair name**, select `arcee-graviton4-key` from the list

## Configure network

Set up your instance networking so that it can be accessed over the internet:

Choose a VPC that includes at least one public subnet.  

Select a public subnet from the list.  

Under **Auto-assign public IP**, choose **Enable**.

## Configure firewall

Select **Create security group**. Then select **Allow SSH traffic from** and select **My IP**.

{{% notice note %}}
You'll only be able to connect to the instance from your current host, which is the most secure setting. Avoid selecting **Anywhere** unless absolutely necessary, as this setting allows anyone on the internet to attempt a connection.

This Learning Path only requires SSH access. If you already have a security group that allows inbound SSH traffic, you can reuse it.
{{% /notice %}}

### Configure storage

- Set the **root volume size** to `128` GB . 
- Choose **gp3** as the volume type.

### Review and launch the instance

Review all your configuration settings.  
When you're ready, select **Launch instance** to create your EC2 instance.

## Monitor the instance launch

After a few seconds, you should see a confirmation message like the following:

```
Successfully initiated launch of instance (i-xxxxxxxxxxxxxxxxx)
```

If the launch fails, double-check the instance type, permissions, and network settings.

To retrieve the connection details:

- Go to the **Instances** list in the EC2 dashboard.  
- Select your instance by selecting **Instance ID**.  
- In the **Details** tab, copy the **Public DNS** value - you’ll use this to connect through SSH.

## Connect to your instance

Open a terminal and connect to the instance using the key file:

```bash
ssh -i ~/.ssh/arcee-graviton4-key.pem ubuntu@<PUBLIC_DNS_HOSTNAME>
```

When prompted to verify the host authenticity, type `yes`.

You should now be connected to your Ubuntu instance on Graviton4.

{{% notice Note %}}
**Region**: Make sure you're launching in your preferred AWS region.  
**AMI**: Confirm that the AMI is ARM64-compatible.  
**Security**: Restrict SSH access to your own IP for best practice.  
**Storage**: 128 GB is enough for the AFM-4.5B model and dependencies.  
**Backup**: Consider creating an AMI or snapshot once your setup is complete.
{{% /notice %}}

