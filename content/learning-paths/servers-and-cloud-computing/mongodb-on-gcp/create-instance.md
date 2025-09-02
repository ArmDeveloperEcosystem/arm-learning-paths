---
title: Create Google Axion instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

This section walks you through creating a **Google Axion C4A Arm virtual machine** on GCP with the **c4a-standard-4 (4 vCPUs, 16 GB Memory)** machine type, using the **Google Cloud Console**.

If you haven't set up a Google Cloud account, check out the Learning Path on [Getting Started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).

### Create an Arm-based Virtual Machine (C4A)

To create a virtual machine based on the C4A Arm architecture:
1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2. Go to **Compute Engine** and click on **Create Instance**.
3. Under the **Machine Configuration**:
      - Fill in basic details like **Instance Name**, **Region**, and **Zone**.
      - Select the **Series** as `C4A`.
      - Choose a machine type such as `c4a-standard-4`.
![Instance Screenshot](./select-instance.png)
4. Under the **OS and Storage**, click on **Change**, and select **Red Hat Enterprise Linux** as the Operating System with **Red Hat Enterprise Linux 9** as the Version. Make sure you pick the version of image for Arm.
5. Under **Networking**, enable **Allow HTTP traffic** to allow interacting for later steps in the Learning Path.
6. Click on **Create**, and the instance will launch.

{{% notice Important %}}
Avoid enabling Allow HTTP traffic permanently, as it introduces a security vulnerability. Instead, configure access to allow only your own IP address for long-term use.
{{% /notice %}}

To access the Google Cloud Console, click the SSH button in your instance overview. This will open a command line interface (CLI), which you’ll use to run the remaining commands in this Learning Path. Continue to the next section to set up MongoDB on your instance.