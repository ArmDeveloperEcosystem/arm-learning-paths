---
title: Create a Google Axion C4A Arm virtual machine on GCP 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Provision a Google Axion C4A Arm VM

In this section you'll create a Google Axion C4A Arm-based virtual machine on Google Cloud Platform. You'll use the `c4a-standard-4` machine type, which provides 4 vCPUs and 16 GB of memory. This VM will host your OpenTelemetry application.

{{% notice Note %}}
For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A Arm VM in Google Cloud Console

To create a virtual machine based on the C4A instance type:

* Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
* Go to **Compute Engine > VM Instances** and select **Create Instance**.
* Under **Machine configuration**:
  * Populate fields such as **Instance name**, **Region**, and **Zone**.
  * Set **Series** to `C4A`.
  * Select `c4a-standard-4` for machine type.

![Screenshot of the Google Cloud Console showing the Machine configuration section. The Series dropdown is set to C4A and the machine type c4a-standard-4 is selected alt-txt#center](images/gcp-vm.png "Configuring machine type to C4A in Google Cloud Console")


* Under **OS and storage**, select **Change**, and then choose an Arm64-based operating system image.
  * For this Learning Path, select **SUSE Linux Enterprise Server**.
  * For the license type, choose **Pay as you go**.
  * Increase **Size (GB)** from **10** to **100** to allocate sufficient disk space.
  * Select **Choose** to apply the changes.
* Under **Networking**, enable **Allow HTTP traffic** and **Allow HTTPS traffic**
* Also, add the following tag: `allow-all-opentelemetry` to allow all TCP ports through for OpenTelemetry.
* For some organizations not using the **'default'** network interface, you may need to select the network appropriate for your organization. 
* Select **Create** to launch the virtual machine.

After the instance starts, select **SSH** next to the VM in the instance list to open a browser-based terminal session.

![Google Cloud Console VM instances page displaying running instance with green checkmark and SSH button in the Connect column alt-txt#center](images/gcp-pubip-ssh.png "Connecting to a running C4A VM using SSH")

A new browser window opens with a terminal connected to your VM.

![Browser-based SSH terminal window with black background showing Linux command prompt and Google Cloud branding at top alt-txt#center](images/gcp-shell.png "Terminal session connected to the VM")

## What you've accomplished and what's next

In this section:
- You provisioned a Google Axion C4A Arm VM with 4 vCPUs and 16 GB of memory
- You configured the VM with SUSE Linux Enterprise Server and 100 GB of storage
- You connected to your VM using SSH through the Google Cloud Console

Your VM is now ready to host the OpenTelemetry application. In the next section, you'll install Docker and Docker Compose, then deploy your instrumented Flask application.

Next, you'll install Docker, Docker Compose, and the OpenTelemetry-instrumented Flask application on your VM.
