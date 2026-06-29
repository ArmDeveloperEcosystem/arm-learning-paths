---
title: Provision a virtual machine on Google Cloud Platform to deploy Gerrit
description: Provision an Ubuntu 24.04 LTS C4A Arm virtual machine on Google Cloud and open an SSH session for the Gerrit installation.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a Google Axion C4A Arm virtual machine 

Provision a Google Axion C4A Arm virtual machine (VM) on Google Cloud Platform (GCP) using the `c4a-standard-4` machine type (4 vCPUs, 16 GB memory) in the Google Cloud console.  

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

### Use the Google Cloud console to create a C4A Arm virtual machine 

To create a VM based on the C4A instance type:

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2. Go to **Compute Engine > VM Instances** and select **Create Instance**. 
3. Under **Machine configuration**:
   - Populate fields such as **Instance name**, **Region**, and **Zone**.
   - Set **Series** to `C4A`.
   - Select `c4a-standard-4` for machine type.

![Google Cloud Console interface showing the Create Instance page with Machine configuration section. Series is set to C4A and machine type shows c4a-standard-4 selected. The dialog displays configuration options for CPU, memory, and other VM settings.#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")


4. Under **OS and Storage**, select **Change**. Choose an Arm64-based OS image. For this Learning Path, select **Ubuntu 24.04 LTS**.
5. Change the size of the primary disk from 10 GB to 100 GB
6. Click **Select** to confirm your OS choice.
7. Under **Networking**, enable **Allow HTTP traffic** and **Allow HTTPS traffic**.
8. In the **Network tags** field, add `allow-tcp-8080` to allow Gerrit dashboard traffic.

![Google Cloud console interface showing the Networking tab for VM instance configuration. The Network tags field displays allow-tcp-8080 to enable firewall rule for Gerrit dashboard traffic on port 8080. Other networking options and VM configuration controls are visible.#center](images/network-config.png "Adding the TCP/8080 firewall rule to our VM")

9. Select **Create** to launch your VM instance.

After the VM is ready, you'll see an **SSH** button next to your instance in the VM list. The public IP address for your VM also appears here. Copy the public IP address — you'll need it later to connect to Gerrit.

Select **SSH** to open a shell session directly in your browser.

![Google Cloud console showing the VM Instances list with a running VM instance. The SSH button is highlighted next to the instance entry, with the public IP address visible in the same row. This shows how to access the SSH terminal to connect to your Arm-based VM.#center](images/gcp-pubip-ssh.png "Invoke a SSH session into your running VM instance")

A window from your browser will come up and you'll now see a shell into your VM instance:

![Browser-based terminal window showing an active shell session on the Ubuntu VM instance. The command prompt is ready for input. This demonstrates successful connection to your C4A Arm virtual machine on Google Cloud.#center](images/gcp-shell.png "Terminal shell in your VM instance")

## What you've accomplished and what's next

You've now created an Arm-based Google Axion C4A VM instance that you'll use to deploy Gerrit. You've also opened a shell session into the instance.

Next, you'll install Gerrit on the VM instance. 
