---
title: Create a Google Axion C4A Arm virtual machine on GCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Provision a Google Axion C4A Arm VM

In this section, you'll provision a Google Axion C4A Arm virtual machine (VM) on Google Cloud Platform (GCP) using the `c4a-standard-4` (4 vCPUs, 16 GB memory) machine type.

{{% notice Note %}}
For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create your VM

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Select **Compute Engine** > **VM Instances** and click **Create Instance**.
- Under **Machine configuration**:
    - Fill in **Instance name**, **Region**, and **Zone**.
    - Set **Series** to `C4A`.
    - Choose `c4a-standard-4` for machine type.

    ![Screenshot of the Google Cloud Console showing the creation of a new VM instance. The c4a-standard-4 machine type is selected under Machine configuration. The interface displays fields for instance name, region, zone, and machine type selection. alt-text #center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")

- Under **OS and Storage**, click **Change** and select an Arm64-based OS image. For this Learning Path, choose **SUSE Linux Enterprise Server (SLES)**.
    - Select "Pay As You Go" for the license type.
    - Click **Select** to confirm your OS choice.
- Under **Networking**, enable **Allow HTTP traffic**.
- Click **Create** to launch your VM instance.
- Once created, find your VM in the list and click **SSH** to open an SSH session in your browser.

![Screenshot showing the SSH option next to a running VM instance in the Google Cloud Console. The SSH button is highlighted, indicating how to launch a secure shell session into the VM. alt-text #center](images/gcp-ssh.png "Invoke an SSH session into your running VM instance")

- A new browser window opens with a terminal shell connected to your VM.

![Screenshot of a terminal shell in the browser, connected to the running VM instance. The shell displays a command prompt, ready for user input. alt-text #center](images/gcp-shell.png "Terminal shell in your VM instance")


You have successfully provisioned an Arm-based VM on Google Cloud. Next, you'll install TensorFlow on your new instance!