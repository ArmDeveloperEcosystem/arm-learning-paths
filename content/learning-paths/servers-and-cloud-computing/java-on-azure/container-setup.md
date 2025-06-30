---
title: Setup Azure Linux 3.0 Environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


You have an option to choose between working with the Azure Linux 3.0 Docker image or inside the virtual machine created with the OS image.

### Working inside Azure Linux 3.0 Docker container
The Azure Linux Container Host is an operating system image that's optimized for running container workloads on Azure Kubernetes Service (AKS). Microsoft maintains the Azure Linux Container Host and based it on CBL-Mariner, an open-source Linux distribution created by Microsoft. To know more about Azure Linux 3.0, kindly refer [What is Azure Linux Container Host for AKS](https://learn.microsoft.com/en-us/azure/azure-linux/intro-azure-linux).
 
Azure Linux 3.0 offers support for AArch64. However, the standalone virtual machine image for Azure Linux 3.0 or CBL Mariner 3.0 is not available for Arm. Hence, to use the default software stack provided by the Microsoft team, you can create a docker container with Azure Linux 3.0 as a base image, and run the Java application inside the container, with the default JDK provided by the Microsoft team via Azure Linux 3.0 environment. 

#### Create Azure Linux 3.0 Docker Container 
The [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/artifact/mar/azurelinux/base/core/about) offers updated docker image for the Azure Linux 3.0.  

To create a docker container, install docker, and then follow the below instructions: 

```console
sudo docker run -it --rm mcr.microsoft.com/azurelinux/base/core:3.0
```
The default container startup command is bash. tdnf and dnf are the default package managers.

### Working with Azure Linux 3.0 OS image
As of now, the Azure Marketplace offers official virtual machine images of Azure Linux 3.0 only for x64-based architectures, published by Ntegral Inc. However, native Arm64 (AArch64) images are not yet officially available. Hence, for this Learning Path, you can create your own custom Azure Linux 3.0 virtual machine image for AArch64 using the [AArch64 ISO for Azure Linux 3.0](https://github.com/microsoft/azurelinux#iso).

Refer [Create an Azure Linux 3.0 virtual machine with Cobalt 100 processors](https://learn.arm.com/learning-paths/servers-and-cloud-computing/azure-vm) for the details.

Whether you're using an Azure Linux 3.0 Docker container, or a virtual machine created from a custom Azure Linux 3.0 image, the deployment and benchmarking steps remain the same.

Once the setup has been established, you can proceed with the Java Installation ahead.
