---
title: Set up an Azure Linux 3.0 environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Set up an Azure Linux 3.0 environment

You can deploy your Spark workload either in an Azure Linux 3.0 Docker container or on a virtual machine created from a custom Azure Linux 3.0 image.

## Work inside an Azure Linux 3.0 Docker container

The Azure Linux Container Host is an operating system image optimized for running container workloads on Azure Kubernetes Service (AKS). Microsoft maintains the Azure Linux Container Host, which is based on CBL-Mariner, an open-source Linux distribution created by Microsoft. 

To learn more, see [What is Azure Linux Container Host for AKS](https://learn.microsoft.com/en-us/azure/azure-linux/intro-azure-linux).

Azure Linux 3.0 supports AArch64. However, a standalone virtual machine image for Azure Linux 3.0 or CBL Mariner 3.0 is not yet available for Arm. To use the default Microsoft software stack, you can run a Docker container with Azure Linux 3.0 as the base image and run your Spark application inside the container.

### Option 1: Run an Azure Linux 3.0 Docker container

The [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/artifact/mar/azurelinux/base/core/about) offers updated Docker images for Azure Linux 3.0.

To run a Docker container with Azure Linux 3.0, install [Docker](/install-guides/docker/docker-engine/) and run:

```console
sudo docker run -it --rm mcr.microsoft.com/azurelinux/base/core:3.0
```

The default container starts with a Bash shell. Both `tdnf` and `dnf` are available as package managers inside the container.

### Option 2: Create a virtual machine with an Azure Linux 3.0 image

Currently, the Azure Marketplace offers official virtual machine images of Azure Linux 3.0 only for `x86_64` architectures, published by Ntegral Inc. While native Arm64 (AArch64) images are not yet available, you can create your own custom Azure Linux 3.0 virtual machine image for AArch64 using the [AArch64 ISO for Azure Linux 3.0](https://github.com/microsoft/azurelinux#iso).

For detailed steps, see [Create an Azure Linux 3.0 virtual machine with Cobalt 100 processors](/learning-paths/servers-and-cloud-computing/azure-vm).

---

Whether you use an Azure Linux 3.0 Docker container or a virtual machine created from a custom image, the Spark deployment and benchmarking steps in the following sections remain the same.

Once the setup is complete, continue to the next section to install and run Spark.
