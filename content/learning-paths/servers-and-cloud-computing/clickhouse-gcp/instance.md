---
title: Create a Google Axion C4A Arm virtual machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you’ll provision a Google Axion C4A Arm virtual machine on Google Cloud Platform (GCP) using the `c4a-standard-4` machine type (4 vCPUs, 16 GB memory). This configuration provides a consistent baseline for deploying and evaluating ClickHouse later in the Learning Path.

{{% notice Note %}} For help with GCP setup, see [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Provision a Google Axion C4A Arm virtual machine

To create a virtual machine based on the C4A instance type:

- Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine > VM Instances** and select **Create Instance**.
- Under **Machine configuration**:
  - Populate fields such as **Instance name**, **Region**, and **Zone**.
  - Set **Series** to `C4A`.
  - Select `c4a-standard-4` for the machine type.

  ![Create a Google Axion C4A Arm virtual machine in the Google Cloud Console with c4a-standard-4 selected alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")

- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**.
- Select **Pay As You Go** for the license type, then click **Select**.
- Under **Networking**, enable **Allow HTTP traffic**.
- Click **Create** to launch the instance.

Once the instance is created, you should see an **SSH** option to the right of the VM in the list. Click this to open an SSH session in your browser:

![Invoke an SSH session via your browser alt-text#center](images/gcp-ssh.png "Invoke an SSH session into your running VM instance")

A terminal window opens, showing a shell connected to your VM:

![Terminal shell in your VM instance alt-text#center](images/gcp-shell.png "Terminal shell in your VM instance")

Next, you’ll install ClickHouse on the running Arm-based virtual machine.