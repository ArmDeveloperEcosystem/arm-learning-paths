---
title: Create a Google Axion C4A virtual machine on Google Cloud
weight: 3

layout: learningpathall
---

## Overview

In this section, you provision a Google Axion C4A VM on Google Cloud Platform (GCP) using the `c4a-standard-4` machine type, which provides 4 vCPUs and 16 GB of memory.

{{% notice Note %}}
For general guidance on setting up a Google Cloud account and project, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A VM in the Google Cloud Console

To create a VM using the C4A instance type:

- Open the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine** > **VM instances**, and then select **Create instance**.
- Under **Machine configuration**:
  - Specify an **Instance name**, **Region**, and **Zone**.
  - Set **Series** to **C4A**.
  - Select **c4a-standard-4** as the machine type.

![Google Cloud Console VM creation page with the C4A machine series selected and the c4a-standard-4 machine type highlighted alt-txt#center](images/gcp-vm.png "Creating a Google Axion C4A VM in the Google Cloud Console")

- Under **OS and storage**, select **Change**, and then choose an Arm64-based operating system image.
  - For this Learning Path, select **SUSE Linux Enterprise Server**.
  - For the license type, choose **Pay as you go**.
  - Increase **Size (GB)** from **10** to **100** to allocate sufficient disk space.
  - Select **Choose** to apply the changes.
- Under **Networking**, enable **Allow HTTP traffic** and **Allow HTTPS traffic** to simplify access for later Kubernetes testing.
- Select **Create** to launch the virtual machine.

After the instance starts, click **SSH** next to the VM in the instance list to open a browser-based terminal session.

![Google Cloud Console VM instances list with the SSH button highlighted for a running C4A instance alt-txt#center](images/gcp-ssh.png "Connecting to a running C4A VM using SSH")

A new browser window opens with a terminal connected to your VM.

![Browser-based terminal window showing a command prompt on a SUSE Linux VM running on Google Axion C4A alt-txt#center](images/gcp-shell.png "Terminal session connected to the VM")

## What you've accomplished and what's next

You've successfully provisioned an Arm-based Google Axion C4A VM running SUSE Linux Enterprise Server. In the next section, you'll create a GKE cluster for hosting Argo CD deployments.
