---
title: Create an Arm based cloud VM using Microsoft Cobalt 100 CPU 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

There are several ways to create an Arm-based Cobalt 100 VM : the Microsoft Azure console, the Azure CLI tool, or using your choice of IaC (Infrastructure as Code). This guide will use the Azure console to create a VM with Arm-based Cobalt 100 Processor. 

This learning path focuses on the general-purpose VMs of the D series. Please read the guide on [Dpsv6 size series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series) offered by Microsoft Azure.  

If you have never used the Microsoft Cloud Platform before, please review the microsoft [guide to Create a Linux virtual machine in the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal?tabs=ubuntu). 

#### Create an Arm-based Azure Virtual Machine 

Creating a virtual machine based on Azure Cobalt 100 is no different from creating any other VM in Azure. To create an Azure virtual machine, launch the Azure portal and navigate to Virtual Machines. 

Select “Create”, and fill in the details such as Name, and Region. Choose the image for your VM (for example – Ubuntu 24.04) and select “Arm64” as the VM architecture. 

In the “Size” field, click on “See all sizes” and select the D-Series v6 family of VMs. Select “D4ps_v6” from the list and create the VM. 

![Instance Screenshot](./instance.png)

The VM should be ready and running; you can SSH into the VM using the PEM key, along with the Public IP details. 

{{% notice Note %}}

To learn more about Arm-based VMs in Azure, refer to “Getting Started with Microsoft Azure” in [Get started with Arm-based cloud instances](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/azure) .

{{% /notice %}}
