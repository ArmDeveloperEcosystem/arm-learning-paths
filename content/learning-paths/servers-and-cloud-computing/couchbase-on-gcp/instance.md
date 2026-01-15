---
title: Create a Google Axion C4A Arm virtual machine on GCP 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will learn how to provision a Google Axion C4A Arm virtual machine on Google Cloud Platform (GCP) using the `c4a-standard-4` (4 vCPUs, 16 GB memory) machine type in the Google Cloud Console.  

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
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


- Under **OS and Storage**, select **Change**. Choose an Arm64-based OS image. For this Learning Path, select **SUSE Linux Enterprise Server**.
- For the license type, select **Pay As You Go**.
- Click **Select** to confirm your OS choice.
- Under **Networking**, enable **Allow HTTP traffic**.
- In the **Network tags** field, add `allow-tcp-8091` to allow Couchbase traffic.

![Screenshot showing the Google Cloud Console interface with the Networking tab open for a VM instance. The primary subject is the configuration of a firewall rule allowing TCP traffic on port 8091. The Network tags field contains allow-tcp-8091. The wider environment includes other VM configuration options and navigation menus. The tone is neutral and instructional. Visible text includes Network tags and allow-tcp-8091.  alt-text#center](images/network-config.png "Adding the TCP/8091 firewall rule to our VM")

- Select **Create** to launch your VM instance.
- After the VM is ready, you'll see an **SSH** button next to your instance in the VM list. The public IP address for your VM also appears here.
- Copy the public IP address—you'll need it later to connect to Couchbase.
- Select **SSH** to open a shell session directly in your browser.

![Screenshot showing the Google Cloud Console interface with the SSH option highlighted for a running VM instance. The primary subject is the SSH button next to the VM, indicating how to open a shell session in the browser. The wider environment includes the VM instance list, navigation menus, and status indicators. Visible text includes SSH and the public IP address for the VM. The tone is neutral and instructional. alt-text#center](images/gcp-pubip-ssh.png "Invoke a SSH session into your running VM instance")

A window from your browser should come up and you should now see a shell into your VM instance:

![Screenshot of a terminal shell open in a browser window, displaying a command prompt for a SUSE Linux Enterprise Server VM instance on Google Cloud Platform. The primary subject is the active shell session, ready for user input. The wider environment includes browser interface elements and navigation menus. Visible text includes the command prompt and system information. The tone is neutral and instructional. alt-text#center](images/gcp-shell.png "Terminal shell in your VM instance")

Next, let's install Couchbase!