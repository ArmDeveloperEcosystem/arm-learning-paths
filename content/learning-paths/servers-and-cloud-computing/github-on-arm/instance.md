---
title: Create the instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

This guide walks you through provisioning **Google Axion C4A Arm virtual machine** on GCP with the **c4a-standard-4 (4 vCPUs, 16 GB Memory)** machine type, using the **Google Cloud Console**.

If you haven't got a Google Cloud account, you can follow the Learning Path on [Getting Started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/) to get started.

### Create an Arm-based Virtual Machine (C4A)

To create a virtual machine based on the C4A Arm architecture:
1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to the card **Compute Engine** and click on **Create Instance**.
3. Under the **Machine Configuration**:
      - Fill in basic details like **Instance Name**, **Region**, and **Zone**.
      - Choose the **Series** as `C4A`.
      - Select a machine type such as `c4a-standard-4`.
![Instance Screenshot](./images/select-instance.png)
4. Under the **OS and Storage**, click on **Change**, pick **Ubuntu** as the Operating System with **Ubuntu 24.04 LTS Minimal** as the Version. Make sure you pick the version of image for Arm.
5. Under **Networking**, enable **Allow HTTP traffic** to test workloads like NGINX later.
6. Click on **Create**, and the instance will launch.

{{% notice Important %}}
You should not enable the **Allow HTTP traffic** permanently, since this poses a security risk. For the long-term, you should only allow traffic from the IP address you use to connect to the instance.
{{% /notice %}}

You can access the Google Cloud Console by clicking the **SSH** button in the instance overview. Use this command line interface (CLI) to run the commands in the remainder of this Learning Path.
