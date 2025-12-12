---
title: Create a Google Axion C4A Arm virtual machine on GCP 
weight: 4

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

   ![Create a Google Axion C4A Arm virtual machine in the Google Cloud Console with c4a-standard-4 selected alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")


- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**. 
- If using use **SUSE Linux Enterprise Server**. Select "Pay As You Go" for the license type. 
- Once appropriately selected, please Click **Select**. 
- Under **Networking**, enable **Allow HTTP traffic**.
- Also under **Networking**, in the "Network tags" text field add "allow-tcp-15672" as an additional tag

![Adding the TCP/15672 firewall rule to our VM](images/network-config.png "Adding the TCP/15672 firewall rule to our VM")

- Click **Create** to launch the instance.
- Once created, you should see a "SSH" option to the right in your list of VM instances. You should also see the public IP address for your VM.
- Save off the public IP address for your VM as you will need this in the next step.
- Click on this to launch a SSH shell into your VM instance:

![Invoke a SSH session via your browser alt-text#center](images/gcp-pubip-ssh.png "Invoke a SSH session into your running VM instance")

- A window from your browser should come up and you should now see a shell into your VM instance:

![Terminal Shell in your VM instance alt-text#center](images/gcp-shell.png "Terminal shell in your VM instance")

Next, let's install RabbitMQ!