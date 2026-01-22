---
title: Create an Arm-based virtual machine using Microsoft Cobalt 100 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Arm-based Azure virtual machine using Cobalt 100

You can create an Arm-based Cobalt 100 virtual machine using the Microsoft Azure console, the Azure CLI tool, or Infrastructure as Code (IaC). For this Learning Path, you use the Azure console to create a virtual machine with an Arm-based Cobalt 100 processor. 

You'll focus on the general-purpose virtual machine of the D series. For more details, see [Dpsv6 size series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series) in the Microsoft Azure documentation.  

If you haven't used Microsoft Azure before, see [Create a Linux virtual machine in the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal?tabs=ubuntu). 

## Create an Arm-based Azure virtual machine 

To create an Azure virtual machine based on Cobalt 100, launch the Azure portal and navigate to **Virtual Machines**.

* Select **Create**, and click on **Virtual Machine** from the drop-down list.
* In the **Basic** tab, fill in the instance details such as **Virtual machine name** and **Region**.
* Choose the image for your virtual machine (for example, **Ubuntu 24.04 LTS**) and select **Arm64** as the VM architecture.
* In the **Size** field, select **See all sizes** and select the **D-Series v6** family of virtual machines. Select **D4ps_v6** from the list.

![Azure portal showing VM size selection with D-Series v6 family and D4ps_v6 instance type highlighted alt-txt#center](images/instance.png "Select the D-Series v6 family of virtual machines")

* Select **SSH public key** as an authentication type. Azure automatically generates an SSH key pair for you and allows you to store it for future use.
* Fill in the administrator username for your virtual machine.
* Select **Generate new key pair**, and select **RSA SSH Format** as the SSH key type. RSA offers better security with keys longer than 3072 bits. Give a key pair name to your SSH key.
* In **Inbound port rules**, select **HTTP (80)** and **SSH (22)** as the inbound ports.

![Azure portal VM configuration page showing inbound port rules section with HTTP and SSH ports selected alt-txt#center](images/instance1.png "Allow inbound port rules")

Select the **Review + Create** tab and review the configuration for your virtual machine.

![Azure portal review page showing complete VM configuration including Ubuntu 24.04 LTS ARM64 image and D4ps_v6 size alt-txt#center](images/ubuntu-pro.png "Review and Create an Azure Cobalt 100 Arm64 VM")

When you're confident about your selection, select the **Create** button, and select the **Download Private key and Create Resources** button.

![Azure portal dialog box prompting to download the SSH private key with filename shown alt-txt#center](images/instance4.png "Download Private key and Create Resources")

Your virtual machine is ready and running in a few minutes. Press **Go to Resource** to view the new virtual machine details. You can SSH into the virtual machine using the private key and the public IP address.

![Azure portal showing deployed VM overview page with status as running and public IP address visible alt-txt#center](images/final-vm.png "VM deployment confirmation in Azure portal")

{{% notice Note %}}

For more information about Arm-based virtual machines in Azure, see [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure).

{{% /notice %}}
