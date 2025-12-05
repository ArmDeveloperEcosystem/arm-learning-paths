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

   ![Create a Google Axion C4A Arm virtual machine in the Google Cloud Console with c4a-standard-4 selected alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")


- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**. 
- If using use **SUSE Linux Enterprise Server**. Select "Pay As You Go" for the license type. 
- Once appropriately selected, please Click **Select**. 
- Under **Networking**, enable **Allow HTTP traffic**.
- Click **Create** to launch the instance.
- Once created, you should see a "SSH" option to the right in your list of VM instances.  Click on this to launch a SSH shell into your VM instance:

![Browser window showing the Google Cloud Console with the SSH button highlighted next to a running VM instance. The interface displays the VM name, status, and available actions. The environment is a web-based dashboard with navigation menus on the left. The emotional tone is neutral and instructional. Visible text includes VM instance details and the SSH button label. alt-text#center](images/gcp-ssh.png "Invoke a SSH session into your running VM instance")

- A window from your browser should come up and you should now see a shell into your VM instance:

![Terminal window displaying a shell prompt inside a Google Axion C4A Arm VM instance. The interface shows a command line ready for input, with the username and hostname visible at the prompt. The wider environment is a browser-based SSH session within the Google Cloud Console. The emotional tone is neutral and instructional. Visible text includes the shell prompt and any default welcome messages shown in the terminal. alt-text#center](images/gcp-shell.png "Terminal shell in your VM instance")


## What you've accomplished and what's next 

You have successfully provisioned a Google Axion C4A Arm virtual machine on Google Cloud Platform using the Console. You selected the Arm64-based SUSE Linux Enterprise Server image, configured networking, and launched your VM. You also connected to your instance using the built-in SSH feature. You now have a running Arm VM on GCP and access to its shell environment.

Next, you'll install Puppet on your new instance to automate configuration and management tasks. 