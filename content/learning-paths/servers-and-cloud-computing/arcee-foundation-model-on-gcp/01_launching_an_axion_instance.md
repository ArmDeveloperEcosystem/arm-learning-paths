---
title: Provision your Axion environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Requirements

Before you begin, make sure you have the following:

- A Google Cloud account  
- Permission to launch a Google Axion instance of type `c4a-standard-16` (or larger)  
- At least 128 GB of available storage

If you're new to Google Cloud, check out the Learning Path [Getting Started with Google Cloud](/learning-paths/servers-and-cloud-computing/csp/google/).

## Launch and configure the Compute Engine instance

In the left sidebar of the [Compute Engine dashboard](https://console.cloud.google.com/compute), select **VM instances**, and then **Create instance**.

Use the following settings to configure your instance:

- **Name**: `arcee-axion-instance`  
- **Region** and **Zone**: the region and zone where you have access to c4a instances
- Select **General purpose**, then click **C4A**
- **Machine type**: c4a-standard-16 or larger

## Configure OS and Storage

In the left sidebar, select **OS and storage**.

Under **Operating system and storage**, click on **Change**

Select Ubuntu as the Operating system. For version select Ubuntu 24.04 LTS Minimal.

Set the size of the disk to 128 GB, then click on **Select**.

## Review and launch the instance

Leave the other settings as they are.

When you're ready, click on **Create** to create your Compute Engine instance.

## Monitor the instance launch

After a few seconds, you should see that your instance is ready.

If the launch fails, double-check your settings and permissions, and try again.

## Connect to your instance

Open the **SSH** dropdown list, and select **Open in browser window**.

Your browser may ask you to authenticate. Once you've done that, a terminal window will open.

You are now connected to your Ubuntu instance running on Axion.

{{% notice Note %}}
**Region**: make sure you're launching in your preferred Google Cloud region.  
**Storage**: 128 GB is sufficient for the AFM-4.5B model and dependencies.  
{{% /notice %}}

