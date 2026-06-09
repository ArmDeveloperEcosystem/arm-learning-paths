---
title: Create a Google Cloud C4A virtual machine for LlamaIndex
description: Learn how to create an Arm-based Google Cloud C4A virtual machine powered by Google Axion and connect to it with browser-based SSH.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the virtual machine

In this section, you'll create a Google Cloud C4A Arm-based virtual machine (VM). You'll use the `c4a-standard-4` machine type, which provides four vCPUs and 16 GB of memory. This VM will host your browser-based LlamaIndex RAG application.

### Configure the C4A virtual machine in the Google Cloud console

To create a virtual machine based on the C4A instance type in the console:

1. Navigate to the [Google Cloud console](https://console.cloud.google.com/).
2. Go to **Compute Engine** > **VM instances** and select **Create instance**.
3. Under **Machine configuration**, populate fields such as **Instance name**, **Region**, and **Zone**.
4. Set **Series** to `C4A`, then select `c4a-standard-4` for **Machine type**.

![Screenshot of the Google Cloud console showing the Machine configuration section. The Series dropdown is set to C4A and the machine type c4a-standard-4 is selected.#center](images/gcp-vm.png "Configuring machine type to C4A in Google Cloud Console")

5. Under **OS and storage**, select **Change** and then choose an Arm64-based operating system image. For this Learning Path, select **SUSE Linux Enterprise Server**.
6. For the license type, choose **Pay as you go**.
7. Increase **Size (GB)** from **10** to **100** to allocate sufficient disk space, and then select **Select**.
8. Select **Networking** from the column on the left.
9. Under **Network tags**, enter `allow-llamaindex-port` to link the VM to the firewall rule from the previous section and allow inbound access to port `8000` for the browser-based LlamaIndex RAG application and port `22` for SSH access.
10. Select **Create** to launch the virtual machine.

After the instance starts, select **SSH** next to the VM in the instance list to open a browser-based terminal session.

![Google Cloud console VM instances page displaying running instance with green checkmark and SSH button in the Connect column#center](images/gcp-pubip-ssh.png "Connecting to a running C4A VM using SSH")

A new browser window opens with a terminal connected to your VM.

![Browser-based SSH terminal connected to the Google Axion C4A VM. The shell prompt confirms that the instance is running and ready for the next step, where you'll install LlamaIndex and its dependencies.#center](images/gcp-shell.png "Terminal session connected to the VM")

## What you've accomplished and what's next

You've now provisioned a Google Cloud C4A VM and connected to it using SSH.

Next, you'll install LlamaIndex, Ollama, ChromaDB, and the required dependencies on your VM.
