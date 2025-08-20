---
title: Provision a Google Cloud Axion Arm64 environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Requirements

Before you begin, make sure you meet the following requirements:

- A Google Cloud account  
- Permission to launch a Google Cloud Axion instance of type `c4a-standard-16` (or larger)  
- At least 128 GB of available storage  

If you're new to Google Cloud, see the Learning Path [Getting started with Google Cloud](/learning-paths/servers-and-cloud-computing/csp/google/).

## Requirements for Google Cloud Axion

Confirm that your account has sufficient quota for Axion instances and enough storage capacity to host the AFM-4.5B model and dependencies.

## Launch and configure a Google Cloud Axion VM

In the left sidebar of the [Compute Engine dashboard](https://console.cloud.google.com/compute), select **VM instances**, and then **Create instance**.

Use the following settings:

- **Name**: `arcee-axion-instance`  
- **Region** and **Zone**: the region and zone where you have access to `c4a` instances  
- **Machine family**: select **General purpose**, then **C4A**  
- **Machine type**: `c4a-standard-16` or larger  

## Configure operating system and storage

In the left sidebar, select **OS and storage**.  

- Under **Operating system and storage**, click **Change**  
- Select **Ubuntu 24.04 LTS Minimal** as the OS  
- Set the disk size to **128 GB**  
- Click **Select**  

## Review and create your Axion instance

Leave the other settings as they are.  

When you’re ready, click **Create** to launch your Compute Engine instance.

## Verify instance launch

After a few seconds, you should see your instance listed as **Running**.  

If the launch fails, double-check your settings and permissions, and try again.

## Connect to your Google Cloud Axion VM

Open the **SSH** dropdown list, and select **Open in browser window**.  

Your browser may ask you to authenticate. Once you’ve done that, a terminal window will open.  

You are now connected to your Ubuntu instance running on Google Cloud Axion.

{{% notice Note %}}
- **Region**: make sure you're launching in your preferred Google Cloud region.  
- **Storage**: 128 GB is sufficient for the AFM-4.5B model and dependencies.  
{{% /notice %}}
