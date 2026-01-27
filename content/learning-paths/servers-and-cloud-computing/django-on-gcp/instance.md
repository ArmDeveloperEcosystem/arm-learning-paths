---
title: Create a Google Axion C4A Arm virtual machine on GCP 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Provision a Google Axion C4A Arm VM

You'll create a Google Axion C4A Arm-based virtual machine (VM) on Google Cloud Platform (GCP) using the `c4a-standard-4` machine type (4 vCPUs, 16 GB memory). This VM hosts your Django application.

{{% notice Note %}}
For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A Arm VM in Google Cloud Console

To create a virtual machine based on the C4A instance type:
- Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine > VM Instances** and select **Create Instance**. 
- Under **Machine configuration**:
   - Populate fields such as **Instance name**, **Region**, and **Zone**.
   - Set **Series** to `C4A`.
   - Select `c4a-standard-4` for machine type.

![Screenshot of the Google Cloud Console showing the Machine configuration section. The Series dropdown is set to C4A and the machine type c4a-standard-4 is selected#center](images/gcp-vm.png "Configuring machine type to C4A in Google Cloud Console")


- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**. 
- If using use **SUSE Linux Enterprise Server**. Select "Pay As You Go" for the license type. 
- Once appropriately selected, please Click **Select**. 
- Under **Networking**, enable **Allow HTTP traffic**.
- Also under **Networking**, in the "Network tags" text field add "allow-tcp-8000" as an additional tag

![Screenshot showing the Networking configuration section. The Allow HTTP traffic checkbox is enabled and the Network tags field contains django-server#center](images/network-config.png "Configuring networking and tags")

## Create the instance

Click **Create** to launch your VM instance. Google Cloud provisions the instance, which typically takes one to two minutes.
Once the instance is running, you'll see it listed in the VM instances table with a green checkmark. Note the External IP address displayed in the list; you'll need this to access your Django application later.

## Connect using SSH

Click the **SSH** button next to your running instance to open a browser-based terminal session.

![Screenshot of the VM instances list showing the SSH button next to a running instance. The external IP address is visible in the same row alt-txt#center](images/gcp-pubip-ssh.png "Launching an SSH session from the VM instances list")

A browser window opens with a terminal shell connected to your VM. You're now ready to install Django.

![Screenshot of a terminal shell in the browser, connected to the running VM instance. The shell displays a command prompt ready for input alt-txt#center](images/gcp-shell.png "Terminal shell connected to your VM")

## What you've accomplished and what's next

In this section, you provisioned a Google Axion C4A Arm VM and connected to it using SSH.

Next, you'll install Django and the required dependencies on your VM.