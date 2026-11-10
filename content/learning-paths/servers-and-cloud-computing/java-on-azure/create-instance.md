---
title: Create an Azure Cobalt 200 Arm VM
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Azure Cobalt 200 Arm64 VM using the Azure portal

You can create an Azure Cobalt 200 Arm64 virtual machine in several ways, including the Azure portal, the Azure CLI, or an Infrastructure as Code (IaC) tool.

In this Learning Path, you’ll use the Azure portal to create a VM with the Cobalt 200 processor, following a process similar to creating any other virtual machine in Azure.

Use a general-purpose **Standard_D4ps_v7** VM in the **Dpsv7** series, with 4 vCPUs and 16 GiB of memory. See Microsoft’s [Cobalt 200 VM families overview](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/) for details.

Your subscription and selected region must have access to Dpsv7 sizes and sufficient vCPU quota. This Learning Path was validated in **West US 2** on **Ubuntu 24.04 LTS (Arm64)**. Ubuntu Pro is optional.


## Create the virtual machine

To create an Azure virtual machine, open the Azure portal and go to **Virtual machines**.

Now follow these steps:

- Select **Create** > **Virtual machine** from the toolbar.
- In **Basics**, complete **Instance details** including **Virtual machine name** and **Region**.
- In **Image**, choose **Ubuntu 24.04 LTS**, then set **Architecture** to **Arm64**.
- In **Size**, select **See all sizes**, choose the **Dpsv7 (D-series v7)** family, then select **D4ps_v7**.

   ![Azure portal VM size selection#center](images/instance.png "VM size selection in the Azure portal")
- Under **Administrator account**, set **Authentication type** to **SSH public key**.
- Enter the `Username` for the VM.
- Select **Generate new key pair**, select **SSH key type** (**ED25519** or **RSA**), and provide a **Key pair name**.
- In **Inbound port rules**, set **Public inbound ports** to **Allow selected ports**, then select **HTTP (80)** and **SSH (22)**.
   ![Azure portal VM creation — inbound port rules alt-text#center](images/instance1.png "Allow inbound port rules")
- Select **Review + create** and verify your configuration.

- Select **Create**, then **Download private key and create resource**.

    ![Azure portal VM creation — download private key alt-text#center](images/instance4.png "Download private key and create resource")
- After deployment completes, select **Go to resource**. From **Overview**, copy the **Public IP address** and connect through SSH using your key.


## Connect to your VM (example)

Use the command below, replacing placeholders with your values:
```bash
ssh -i <path-to-private-key> <username>@<public-ip-address>
```

{{% notice Note %}}
To learn more about Arm-based virtual machines in Azure, see "Getting started with Microsoft Azure" in [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure/).
{{% /notice %}}
