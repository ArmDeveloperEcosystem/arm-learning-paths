---
title: Create an Arm based cloud virtual machine using Microsoft Cobalt 100 CPU 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Azure Cobalt 100 Arm64 VM using the Azure portal

You can create an Azure Cobalt 100 Arm64 virtual machine in several ways, including the Azure portal, the Azure CLI, or an Infrastructure as Code (IaC) tool. 

In this Learning Path, you’ll use the Azure portal to create a VM with the Cobalt 100 processor, following a process similar to creating any other virtual machine in Azure.

## Step-by-step: create the virtual machine 

To create an Azure virtual machine, open the **Azure portal** and go to **Virtual machines**.

- Select **Create** > **Virtual machine** from the toolbar
- In **Basics**, complete **Instance details** including **Virtual machine name** and **Region**
- In **Image**, choose **Ubuntu Pro 24.04 LTS**, then set **Architecture** to **Arm64**
- In **Size**, select **See all sizes**, choose the **Dpsv6 (D‑series v6)** family, then select **D4ps_v6**
   
   ![Azure portal VM creation — Azure Cobalt 100 Arm64 virtual machine (D4ps_v6)alt-text#center](images/instance.png "Select the D-Series v6 family of virtual machines")
- Under **Administrator account**, set **Authentication type** to **SSH public key**
- Enter the **Username** for the VM
- Select **Generate new key pair**, choose **SSH key type** (**ED25519** or **RSA**), and provide a **Key pair name**
- In **Inbound port rules**, set **Public inbound ports** to **Allow selected ports**, then select **HTTP (80)** and **SSH (22)**
   
   ![Azure portal VM creation — inbound port rules](images/instance1.png "Figure 2: Allow inbound port rules")
- Select **Review + create** and verify your configuration
   
   ![Azure portal review and create — Ubuntu Pro Arm64 VM](images/ubuntu-pro.png "Figure 3: Review and Create an Azure Cobalt 100 Arm64 VM")
- Select **Create**, then **Download private key and create resource**
    
    ![Azure portal VM creation — download private key](images/instance4.png "Figure 4: Download Private key and Create Resources")
- After deployment completes, select **Go to resource**. From **Overview**, copy the **Public IP address** and connect via SSH using your key

   ![Azure portal deployment confirmation — VM running](images/final-vm.png "Figure 5: VM deployment confirmation in Azure portal")

### Connect to your VM (example)

Use the command below, replacing placeholders with your values:
```bash
ssh -i <path-to-private-key> <username>@<public-ip-address>
```

{{% notice Note %}}
To learn more about Arm-based virtual machines in Azure, see "Getting started with Microsoft Azure" in [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure).
{{% /notice %}}
