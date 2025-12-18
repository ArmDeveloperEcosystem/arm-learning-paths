---
title: Create a Google Axion C4A Arm virtual machine on GCP 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will learn how to provision a Google Axion C4A Arm virtual machine on Google Cloud Platform (GCP) using the `c4a-standard-4` (4 vCPUs, 16 GB memory) machine type in the Google Cloud Console.  

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A Arm VM in Google Cloud Console

To create a virtual machine based on the C4A instance type:
- Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine > VM Instances** and select **Create Instance**. 
- Under **Machine configuration**:
   - Populate fields such as **Instance name**, **Region**, and **Zone**.
   - Set **Series** to `C4A`.
   - Select `c4a-standard-4` for machine type.

   ![Screenshot of Google Cloud Console showing the machine configuration section with C4A series and c4a-standard-4 machine type selected alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")


- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**.
- If using **SUSE Linux Enterprise Server**, select "Pay As You Go" for the license type.
- Once appropriately selected, click **Select**. 
- Under **Networking**, enable **Allow HTTP traffic**.
- Click **Create** to launch the instance.
- Once created, you should see a "SSH" option to the right in your list of VM instances. Click on this to launch a SSH shell into your VM instance:

![Screenshot of VM instances list showing the SSH button in the Connect columnalt-text#center](images/gcp-ssh.png "Invoke a SSH session into your running VM instance")

- A window from your browser should come up and you should now see a shell into your VM instance:

![Screenshot of terminal window showing a command-line shell interface connected to the VM instance#center](images/gcp-shell.png "Terminal shell in your VM instance")

You're now ready to install Rust on your C4A instance.
