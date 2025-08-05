---
title: "About Azure Linux"

weight: 2

layout: "learningpathall"
---

## What is Azure Linux 3.0 and how can I use it?

Azure Linux 3.0 is a Microsoft-developed Linux distribution designed specifically for cloud-native workloads on the Azure platform. It is optimized for running cloud-native workloads, such as containers, microservices, and Kubernetes clusters, and emphasizes performance, security, and reliability. 

Azure Linux 3.0 includes native support for the Arm (AArch64) architecture, enabling efficient, scalable, and cost-effective deployments on Arm-based Azure infrastructure.

## Can I run Azure Linux 3.0 on Arm-based Azure virtual machines?

Currently, Azure Linux 3.0 is not available as a ready-made virtual machine image for Arm-based VMs in the Azure Marketplace. Only x86_64 images, published by Ntegral Inc., are offered. This means you cannot directly create an Azure Linux 3.0 VM for Arm from the Azure portal or CLI.

## How can I create a custom Azure Linux image for Arm?

However, you can still run Azure Linux 3.0 on Arm-based Azure VMs by creating your own disk image. Using QEMU, an open-source machine emulator and virtualizer, you can build a custom Azure Linux 3.0 Arm image locally. After building the image, you can upload it to your Azure account as a managed disk or custom image. This process allows you to deploy and manage Azure Linux 3.0 VMs on Arm infrastructure, even before official images are available.

This Learning Path guides you through the steps to build an Azure Linux 3.0 disk image with QEMU, upload it to Azure, and prepare it for use in creating virtual machines.

Following this process, you'll be able to create and run Azure Linux 3.0 VMs on Arm-based Azure infrastructure.

## What tools do I need to build an Azure Linux image locally?

To get started install the dependencies on your local Linux machine. The instructions work for both Arm or x86 running Ubuntu. 

```bash
sudo apt update && sudo apt install qemu-system-arm qemu-system-aarch64 qemu-efi-aarch64 qemu-utils ovmf -y
```

## What tools do I need to build an Azure Linux image locally?

You also need to install the Azure CLI. Refer to [How to install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest). You can also use the [Azure CLI install guide](/install-guides/azure-cli/) for Arm Linux systems. 

Make sure the CLI is working by running the version command and confirm the version is printed.

```bash
az version
```

You should see an output similar to:

```output
{
  "azure-cli": "2.75.0",
  "azure-cli-core": "2.75.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
}
```

## What’s the next step after setting up my environment?

Continue to learn how to prepare the Azure Linux disk image. 