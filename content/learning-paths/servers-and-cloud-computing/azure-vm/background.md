---
title: "Build and run Azure Linux 3.0 on an Arm-based Azure virtual machine"

weight: 2

layout: "learningpathall"
---

## What is Azure Linux 3.0 and how can I use it?

Azure Linux 3.0 is a Microsoft-developed Linux distribution designed for cloud-native workloads on the Azure platform. It is optimized for running containers, microservices, and Kubernetes clusters, with a focus on performance, security, and reliability. 

Azure Linux 3.0 includes native support for the Arm architecture (AArch64), enabling efficient, scalable, and cost-effective deployments on Arm-based Azure infrastructure.

## Can I run Azure Linux 3.0 on Arm-based Azure virtual machines?

At the time of writing, Azure Linux 3.0 isn't available as a prebuilt virtual machine image for Arm-based VMs in the Azure Marketplace. Only x86_64 images (published by Ntegral Inc.) are available. This means you can't directly create an Azure Linux 3.0 VM for Arm from the Azure portal or CLI.

## How can I create and use a custom Azure Linux image for Arm?

To run Azure Linux 3.0 on an Arm-based VM, you'll need to build a custom image manually. Using [QEMU](https://www.qemu.org/), an open-source machine emulator and virtualizer, you can build the image locally. After the build completes, upload the resulting image to your Azure account as either a managed disk or a custom image resource. This process lets you deploy and manage Azure Linux 3.0 VMs on Arm-based Azure infrastructure, even before official images are published in the Marketplace. This gives you full control over image configuration and early access to Arm-native workloads.

This Learning Path guides you through the steps to:

- Build an Azure Linux 3.0 disk image with QEMU
- Upload the image to Azure
- Create a virtual machine from the custom image

By the end of this process, you'll be able to run Azure Linux 3.0 VMs on Arm-based Azure infrastructure.

## What tools do I need to build the Azure Linux image locally?

You can build the image on either an Arm or x86 Ubuntu system. First, install the required tools:

Install QEMU and related tools:

```bash
sudo apt update && sudo apt install qemu-system-arm qemu-system-aarch64 qemu-efi-aarch64 qemu-utils ovmf -y
```

You'll also need the Azure CLI. To install it, follow the [Azure CLI install guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest). 

If you're using an Arm Linux machine, see the [Azure CLI install guide](/install-guides/azure-cli/).

## How do I verify the Azure CLI installation?

After installing the CLI, verify it's working by running the following command:

```bash
az version
```

You should see an output similar to the following:

```output
{
  "azure-cli": "2.75.0",
  "azure-cli-core": "2.75.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
}
```

In the next section, you'll learn how to build the Azure Linux 3.0 disk image using QEMU.