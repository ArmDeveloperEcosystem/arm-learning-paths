---
title: "Build and run Azure Linux 3.0 on Arm-based virtual machines"

weight: 2

layout: "learningpathall"
---

## What is Azure Linux 3.0 and how can I use it?

Azure Linux 3.0 is a Microsoft-developed Linux distribution designed for cloud-native workloads on the Azure platform. It is optimized for running containers, microservices, and Kubernetes clusters, with a focus on performance, security, and reliability. 

Azure Linux 3.0 includes native support for the Arm (AArch64) architecture, enabling efficient, scalable, and cost-effective deployments on Arm-based Azure infrastructure.

## Can I run Azure Linux 3.0 on Arm-based Azure virtual machines?

Currently, Azure Linux 3.0 isn't available as a ready-made virtual machine image for Arm-based VMs in the Azure Marketplace. Only x86_64 images, published by Ntegral Inc., are available. This means you can't directly create an Azure Linux 3.0 VM for Arm from the Azure portal or CLI.

## How can I create a custom Azure Linux image for Arm?

You can still run Azure Linux 3.0 on Arm-based Azure VMs by creating your own disk image. Using [QEMU](https://www.qemu.org/), an open-source machine emulator and virtualizer, you can build a custom Azure Linux 3.0 Arm image locally. After building the image, upload it to your Azure account as a managed disk or custom image. This process allows you to deploy and manage Azure Linux 3.0 VMs on Arm infrastructure, even before official images are available.

This Learning Path guides you through the steps to:

- Build an Azure Linux 3.0 disk image with QEMU
- Upload the image to Azure
- Create a virtual machine from the custom image

By the end of this process, you'll be able to run Azure Linux 3.0 VMs on Arm-based Azure infrastructure.

## What tools do I need to build an Azure Linux image locally?

To get started, install the dependencies on your local Linux machine. The instructions work for both Arm and x86 machines running Ubuntu. 

Install QEMU and related tools:

```bash
sudo apt update && sudo apt install qemu-system-arm qemu-system-aarch64 qemu-efi-aarch64 qemu-utils ovmf -y
```

You'll also need the Azure CLI. To install it, follow the [Azure CLI install guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest). 

If you're using an Arm-based system, you can also see the [Azure CLI install guide](/install-guides/azure-cli/) for Arm Linux systems. 

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

## What’s the next step after setting up my environment?

Next, you'll learn how to build the Azure Linux 3.0 disk image using QEMU.