---
title: Setup Azure Linux 3.0 Environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


You can choose between deploying Nginx in an Azure Linux 3.0 Docker container or on a virtual machine created from a custom Azure Linux 3.0 image.

### Working inside Azure Linux 3.0 Docker container
The Azure Linux Container Host is an operating system image that's optimized for running container workloads on Azure Kubernetes Service (AKS). Microsoft maintains the Azure Linux Container Host and based it on CBL-Mariner, an open-source Linux distribution created by Microsoft. To know more about Azure Linux 3.0, refer to [What is Azure Linux Container Host for AKS](https://learn.microsoft.com/en-us/azure/azure-linux/intro-azure-linux).
 
Azure Linux 3.0 offers support for AArch64. However, the standalone virtual machine image for Azure Linux 3.0 or CBL Mariner 3.0 is not available for Arm. To use the default software stack provided by the Microsoft team, you can run a docker container with Azure Linux 3.0 as a base image, and run the Nginx deployment inside the container. 

### Option 1: Run an Azure Linux 3.0 Docker Container
The [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/artifact/mar/azurelinux/base/core/about) offers updated docker image for the Azure Linux 3.0.  

To run a docker container with Azure Linux 3.0, install [docker](/install-guides/docker/docker-engine/), and then run the command: 

```console
sudo docker run -it --rm mcr.microsoft.com/azurelinux/base/core:3.0
```
The default container starts up with a bash shell. `tdnf` and `dnf` are the default package managers available to use on the container.

### Option 2: Create a virtual machine instance with Azure Linux 3.0 OS image
As of now, the Azure Marketplace offers official virtual machine images of Azure Linux 3.0 only for `x86_64` based architectures, published by Ntegral Inc. While native Arm64 (AArch64) images are not yet officially available, you can create your own custom Azure Linux 3.0 virtual machine image for AArch64 using the [AArch64 ISO for Azure Linux 3.0](https://github.com/microsoft/azurelinux#iso).

Refer to [Create an Azure Linux 3.0 virtual machine with Cobalt 100 processors](/learning-paths/servers-and-cloud-computing/azure-vm) for the detailed steps.

Whether you choose to use an Azure Linux 3.0 Docker container, or a virtual machine created from a custom Azure Linux 3.0 image, the Nginx deployment and benchmarking steps in the following sections will remain the same.

Once the setup has been established, you can proceed with the Nginx Installation ahead.
