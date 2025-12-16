---
title: Create a Google Axion C4A Arm virtual machine for Gardener
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create your Google Axion C4A VM

You'll provision a Google Axion C4A Arm-based virtual machine on Google Cloud Platform (GCP) to host your Gardener installation. The C4A series uses Arm Neoverse-V2 cores, providing cost-effective performance for cloud-native workloads like Kubernetes cluster management.

You'll use the `c4a-standard-4` machine type, which provides 4 vCPUs and 16 GB of memory—sufficient resources for running Gardener Local with Garden, Seed, and Shoot clusters.

{{% notice Note %}}
For detailed GCP setup instructions, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Configure machine settings

Navigate to the [Google Cloud Console](https://console.cloud.google.com/) and go to **Compute Engine > VM Instances**. Click **Create Instance**.

Under **Machine configuration**, configure the following settings:

- Set **Instance name** to a descriptive name like `gardener-vm`
- Select your preferred **Region** and **Zone** (C4A instances are available in select regions)
- Set **Series** to **C4A**
- Select **c4a-standard-4** for the machine type

![Google Cloud Console VM creation screen showing C4A series and c4a-standard-4 machine type selected #center](images/gcp-vm.png)

### Select the operating system

Under **Boot disk**, click **Change** to configure the operating system and storage.

Select **SUSE Linux Enterprise Server** as your operating system. SUSE provides excellent support for Arm64 architecture and includes the container tools needed for Gardener.

For the license type, select **Pay As You Go** to use SUSE's subscription-based licensing.

Increase the disk size from the default 10 GB to 50 GB by setting **Size (GB)** to `50`. Gardener requires additional storage for Docker images, Kubernetes components, and cluster data.

Click **Select** to confirm your boot disk configuration.

### Configure networking

Under **Firewall**, enable both **Allow HTTP traffic** and **Allow HTTPS traffic**. These settings allow your Gardener cluster to serve web traffic and API endpoints.

### Create and connect to your VM

Click **Create** to provision your virtual machine. The VM creation takes one to two minutes.

After creation completes, locate your running instance in the VM instances list. Click **SSH** to open a browser-based terminal connection to your VM.

![SSH button in VM instances list #center](images/gcp-ssh.png)

A new browser window opens with a terminal shell connected to your VM:

![Browser-based SSH terminal connected to VM #center](images/gcp-shell.png)

### Verify your Arm64 VM

Confirm that your VM is running on Arm64 architecture:

```console
uname -m
```

The output is:

```output
aarch64
```

This confirms your VM is running on Arm64 (aarch64) architecture, ready for Gardener installation.

---

You have successfully created a Google Axion C4A Arm-based virtual machine running SUSE Linux Enterprise Server. Your VM is configured with the resources needed to run Gardener Local and is ready for software installation. You're now ready to install Gardener and its dependencies!