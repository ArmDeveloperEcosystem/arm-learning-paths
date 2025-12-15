---
title: Create a Google Axion C4A Arm virtual machine on GCP 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you provision a Google Axion C4A Arm virtual machine on Google Cloud Platform (GCP) using the `c4a-standard-4` (4 vCPUs, 16 GB memory) machine type in the Google Cloud Console.  

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A Arm VM in Google Cloud Console

To create a virtual machine based on the C4A instance type, navigate to the [Google Cloud Console](https://console.cloud.google.com/) and go to **Compute Engine > VM Instances**. Select **Create Instance**.

Under **Machine configuration**, populate fields such as **Instance name**, **Region**, and **Zone**. Set **Series** to `C4A` and select `c4a-standard-4` for machine type.

   ![Create a Google Axion C4A Arm virtual machine in the Google Cloud Console with c4a-standard-4 selected alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")

Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**. Select "Pay As You Go" for the license type and press **Select**.

Under **Networking**, enable **Allow HTTP traffic** and add "allow-tcp-15672" as a network tag in the **Network tags** text field.

![Adding the TCP/15672 firewall rule to the VM](images/network-config.png "Adding the TCP/15672 firewall rule to the VM")

Select **Create** to launch the instance. Once created, you see an **SSH** option and the public IP address for your VM in the list of VM instances. Save the public IP address as you need it in the next step. Select the **SSH** option to launch an SSH shell into your VM instance.

![Invoke an SSH session via your browser alt-text#center](images/gcp-pubip-ssh.png "Invoke an SSH session into your running VM instance")

A window opens from your browser and you see a shell into your VM instance.

![Terminal Shell in your VM instance alt-text#center](images/gcp-shell.png "Terminal shell in your VM instance")

Next, install RabbitMQ.