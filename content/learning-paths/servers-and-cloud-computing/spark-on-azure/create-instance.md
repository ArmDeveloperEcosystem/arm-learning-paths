---
title: Create an Azure Cobalt 100 Arm64 virtual machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Azure Cobalt 100 Arm64 VM using the Azure portal

You can create an Azure Cobalt 100 Arm64 virtual machine in several ways, including the Azure portal, the Azure CLI, or an Infrastructure as Code (IaC) tool. 

In this Learning Path, you’ll use the Azure portal to create a VM with the Cobalt 100 processor, following a process similar to creating any other virtual machine in Azure.

## Step-by-step: create the virtual machine

1. In the Azure portal, go to **Virtual Machines** and select **Create**.  
2. Enter details such as **Name** and **Region**.  
3. Choose the image for your virtual machine (for example, Ubuntu 24.04) and select **Arm64** as the architecture.  
4. In the **Size** field, select **See all sizes**, then choose the D-Series v6 family of virtual machines.  
5. Select **D4ps_v6** from the list and create the virtual machine.  

![Azure portal VM creation — Azure Cobalt 100 Arm64 virtual machine (D4ps_v6) alt-text#center](./instance-new.png "Figure 1: Create an Azure Cobalt 100 Arm64 VM in the Azure portal")

Once the Arm64 virtual machine is running, you can SSH into it using the generated PEM key and the public IP address of the instance.

{{% notice Note %}}

To learn more about Arm-based virtual machines in Azure, see the Learning Path [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure).

{{% /notice %}}
