---
title: Create a Google Axion C4A virtual machine for XGBoost
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the virtual machine

Create a Google Axion C4A Arm-based virtual machine (VM) on Google Cloud Platform. For this Learning Path, you'll use the `c4a-standard-4` machine type. `c4a-standard-4`provides 4 vCPUs and 16 GB of memory.

The VM that you'll create will host XGBoost model training, hyperparameter tuning, benchmarking, and the inference API.

{{% notice Note %}}For help with Google Cloud Platform setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

To create a C4A VM in the Google Cloud console:

1. Navigate to the [Google Cloud console](https://console.cloud.google.com/).
2. Go to **Compute Engine** > **VM Instances** and select **Create Instance**.
3. Under **Machine configuration**, populate fields such as **Instance name**, **Region**, and **Zone**.
4. Set **Series** to `C4A`, then select `c4a-standard-4` for **Machine type**.

![Screenshot of the Google Cloud console showing the Machine configuration section. The Series dropdown is set to C4A and the machine type c4a-standard-4 is selected#center](images/gcp-vm.png "Selecting machine type as C4A in the Google Cloud console")

5. Under **OS and storage**, select **Change** and then choose an Arm64-based operating system image. For this Learning Path, select **SUSE Linux Enterprise Server**. 
6. For the license type, choose **Pay as you go**. 
7. Increase **Size (GB)** from **10** to **100** to allocate sufficient disk space, and then select **Choose**.
8. Expand **Advanced options** and select **Networking**.
9. Under **Network tags**, enter `allow-xgboost-8080` to link the VM to the firewall rule used for external API access and browser connectivity.
10. Select **Create** to launch the virtual machine.

After the instance starts, select **SSH** next to the VM in the instance list to open a browser-based terminal session.

![Google Cloud console VM instances page displaying running instance with green checkmark and SSH button in the Connect column#center](images/gcp-pubip-ssh.png "Connecting to a running C4A VM using SSH")

A new browser window opens with a terminal connected to your VM.

![Browser-based SSH terminal connected to the Google Axion C4A VM, showing the shell prompt ready for the next step#center](images/gcp-shell.png "Terminal session connected to the VM")

## What you've accomplished and what's next

You've now provisioned a Google Axion C4A Arm VM and connected to it using SSH. The VM is linked to the firewall rule that allows access to port 8080 for the XGBoost inference API. 

Next, you'll install XGBoost and configure a Python 3.11 environment for model training and benchmarking.
