---
title: Provision a Google Axion C4A virtual machine for Yocto image builds on Arm
description: Provision a Google Axion C4A virtual machine with Ubuntu 22.04 and sufficient storage to build NVIDIA Jetson Yocto images on Arm.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up a virtual machine on Google Cloud Platform

You'll provision a Google Axion C4A virtual machine (VM) on Google Cloud Platform (GCP) using the `c4a-standard-32` machine type. 

`c4a-standard-32` provides 32 vCPUs and 128 GB of memory. This VM size is required for building a Yocto-based image. 

{{% notice Note %}}
For general guidance on setting up a Google Cloud account and project, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/). 
{{% /notice %}}

### Provision a Google Axion C4A VM in Google Cloud console

To create a virtual machine using the C4A instance type:

- Open the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine** > **VM instances**.
- Select **Create instance**.
- Under **Machine configuration**:
  - Specify an **Instance name**, **Region**, and **Zone**.
  - Set **Series** to **C4A**.
  - Select **c4a-standard-32** as the machine type.

![Google Cloud Console VM creation page with the C4A machine series selected and the c4a-standard-32 machine type highlighted#center](images/gcp-vm.png "Creating a Google Axion C4A virtual machine in the Google Cloud Console")

- Under **OS and storage**, select **Change**, then choose an Arm-based operating system image.
  - For this Learning Path, select **Ubuntu 22.04 LTS** (Arm64).
  - Increase **Size (GB)** from **10** to **500** to allocate sufficient disk space.
- Select **Choose** to apply the image changes.

![Google Cloud Boot disk panel with Ubuntu 22.04 LTS Arm64 selected and the disk size set to 500 GB#center](images/gcp-ubuntu.png "Ubuntu 22.04 LTS Arm64 boot disk configured with 500 GB")

- Under **Networking**, keep the default settings. Browser-based SSH access works without additional firewall rules.
- Select **Create** to launch the virtual machine.

After the instance starts, select **SSH** next to the VM in the instance list to open a browser-based terminal session.

![Google Cloud Console VM instances list with the SSH button highlighted for a running C4A instance#center](images/gcp-ssh.png "Connecting to a running C4A virtual machine using SSH")

A new browser window opens with a terminal connected to your VM.

![Google Cloud SSH-in-browser terminal showing a shell prompt that confirms a successful connection to the C4A virtual machine#center](images/gcp-shell.png "Terminal session connected to the virtual machine")

{{% notice Note %}}
The `c4a-standard-32` instance has significant compute costs. Delete the VM after you complete the Learning Path.
{{% /notice %}}

## What you've accomplished and what's next

You've now provisioned a Google Axion C4A VM and configured it for Arm-based Yocto image builds.

Next, you'll use this VM to build a Yocto image for your target hardware. 
