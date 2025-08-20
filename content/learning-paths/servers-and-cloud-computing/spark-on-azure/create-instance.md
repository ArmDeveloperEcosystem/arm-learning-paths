---
title: Create an Arm-based virtual machine using Azure Cobalt 100
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Create an Arm-based virtual machine using Azure Cobalt 100

You can create an Azure Cobalt 100 Arm-based virtual machine in several ways: using the Microsoft Azure console, the Azure CLI, or your preferred Infrastructure as Code (IaC) tool. In this Learning Path, you will use the Azure console to create a virtual machine with the Azure Cobalt 100 Arm-based processor.

## Create an Arm-based Azure virtual machine

Creating a virtual machine based on Azure Cobalt 100 is similar to creating any other virtual machine in Azure. To create an Azure virtual machine, open the Azure portal and go to **Virtual Machines**.

1. Select **Create**  
2. Enter details such as **Name** and **Region**  
3. Choose the image for your virtual machine (for example, Ubuntu 24.04) and select **Arm64** as the architecture  
4. In the **Size** field, click **See all sizes**, then choose the D-Series v6 family of virtual machines  
5. Select **D4ps_v6** from the list and create the virtual machine  

![Azure portal showing VM creation with D4ps_v6 selected](./instance-new.png)

Once the virtual machine is running, you can SSH into it using the generated PEM key and the public IP address of the instance.

{{% notice Note %}}

To learn more about Arm-based virtual machines in Azure, see [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure).

{{% /notice %}}
