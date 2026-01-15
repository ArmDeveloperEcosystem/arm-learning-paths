---
title: Create a Google Axion C4A Arm virtual machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section shows you how to create a Google Axion C4A Arm virtual machine on Google Cloud Platform (GCP) using the `c4a-standard-4` (4 vCPUs, 16 GB memory) machine type in the Google Cloud Console.  

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A Arm VM

To create a virtual machine based on the C4A instance type:
- Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine > VM Instances** and select **Create Instance**. 
- Under **Machine configuration**:
   - Populate fields such as **Instance name**, **Region**, and **Zone**.
   - Set **Series** to `C4A`.
   - Select `c4a-standard-4` for machine type.

   ![Screenshot of the Google Cloud Console showing the Compute Engine VM instance creation page with Machine configuration section expanded. The Series dropdown shows C4A selected, and the Machine type field displays c4a-standard-4 with specifications of 4 vCPUs and 16 GB memory visible alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")

- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server**. Pick the preferred version for your Operating System. Ensure you select the **Arm image** variant. Select **Select**.
- Under **Networking**, enable **Allow HTTP traffic**.
- Select **Create** to launch the instance.
