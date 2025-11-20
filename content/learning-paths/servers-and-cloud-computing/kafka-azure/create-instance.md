---
title: Create an Arm-based cloud virtual machine using Microsoft Cobalt 100 CPU 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

You can create an Arm-based Cobalt 100 virtual machine in several ways: using the Microsoft Azure portal, the Azure CLI, or Infrastructure as Code (IaC) tools. This Learning Path uses the Azure portal to walk you through creating a virtual machine with an Arm-based Cobalt 100 processor, which is from the D-Series v6 general-purpose virtual machines. 

These VMs are designed for a wide range of workloads and offer Arm-based performance with the Cobalt 100 CPU. To learn more about the Dpsv6 size series, see the official [Dpsv6 size series guide](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series) from Microsoft Azure.

If you have never used the Microsoft Cloud Platform before, see the Microsoft guide on how to [Create a Linux virtual machine in the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal?tabs=ubuntu). 

## Create an Arm-based Azure virtual machine 

Creating a virtual machine based on Azure Cobalt 100 is no different from creating any other virtual machine in Azure. To create an Azure virtual machine, launch the Azure portal and navigate to **Virtual Machines**.

- Select **Create**, and click on **Virtual Machine** from the drop-down list.
- Inside the **Basic** tab, fill in the Instance details such as **Virtual machine name** and **Region**.
- Choose the image for your virtual machine (for example, Ubuntu Pro 24.04 LTS) and select **Arm64** as the VM architecture.
- In the **Size** field, click on **See all sizes** and select the D-Series v6 family of virtual machines. Select **D4ps_v6** from the list.

![Azure portal showing the selection of the D-Series v6 family of virtual machines, with D4ps_v6 highlighted as the chosen size. The interface displays a list of available VM sizes, including CPU, memory, and pricing details. The wider environment is the Azure portal's virtual machine creation workflow, with a clean and organized layout. The tone is neutral and informative, focused on guiding users through the selection process. Visible text includes D-Series v6, D4ps_v6, CPU, memory, and price columns. alt-text#center](images/instance.png "Selecting the D-Series v6 family of virtual machines")

- Select **SSH public key** as an authentication type. Azure automatically generates an SSH key pair for you and allows you to store it for future use. It is a fast, simple, and secure way to connect to your virtual machine.
- Fill in the administrator username for your VM.
- Select **Generate new key pair**, and select **RSA SSH Format** as the SSH key type. RSA can offer better security with keys longer than 3072 bits. Give a key pair name to your SSH key.
- In the **Inbound port rules**, select **HTTP (80)** and **SSH (22)** as the inbound ports.

![Azure portal interface displaying the Inbound port rules configuration step for an Azure Cobalt 100 Arm64 virtual machine (D4ps_v6). The main focus is on selecting HTTP port 80 and SSH port 22 as allowed inbound ports. The wider environment is the Azure portal's virtual machine creation workflow, with a clean and organized layout. Visible text includes Inbound port rules, HTTP 80, SSH 22, and options to add or remove ports. The tone is neutral and instructional, guiding users through network security settings for the VM. alt-text#center](images/instance1.png "Allow inbound port rules")

- Click on the **Review + Create** tab and review the configuration for your virtual machine. It should look like the following:

![Azure portal interface displaying the Review and Create step for an Azure Cobalt 100 Arm64 virtual machine. The primary subject is the summary panel showing selected configuration details, including Ubuntu Pro 24.04 LTS as the operating system, D4ps_v6 as the VM size, Arm64 architecture, and SSH public key authentication. The wider environment is the Azure portal's virtual machine creation workflow, with a clean and organized layout. Visible text includes Review and Create, Ubuntu Pro 24.04 LTS, D4ps_v6, Arm64, SSH public key, and configuration summary fields. The tone is neutral and informative, guiding users through the final review before VM deployment. alt-text#center](images/ubuntu-pro.png "Review and create an Azure Cobalt 100 Arm64 VM")

- Finally, when you are confident about your selection, click on the "Create" button, and click on the "Download Private key and Create Resources" button.

![Azure portal VM creation — Azure Cobalt 100 Arm64 virtual machine (D4ps_v6) alt-text#center](images/instance4.png "Download private key and create resources")

Your virtual machine is now ready and running. To connect, use SSH with your private key and the VM's public IP address.

![Azure portal VM creation — Azure Cobalt 100 Arm64 virtual machine (D4ps_v6) alt-text#center](images/final-vm.png "VM deployment confirmation in Azure portal")

{{% notice Note %}}

To learn more about Arm-based virtual machine in Azure, refer to *Getting Started with Microsoft Azure* in [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure).

{{% /notice %}}
