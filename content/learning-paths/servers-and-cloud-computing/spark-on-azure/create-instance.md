---
title: Create an Arm based cloud virtual machine using Azure Cobalt 100
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

There are several ways you can create an Azure Cobalt 100 Arm-basedvirtual machine : the Microsoft Azure console, the Azure CLI tool, or using your choice of IaC (Infrastructure as Code). In this Learning Path you will use the Azure console to create a virtual machine with Arm-based Azure Cobalt 100 Processor.


#### Create an Arm-based Azure Virtual Machine

Creating a virtual machine based on Azure Cobalt 100 is no different from creating any other virtual machine in Azure. To create an Azure virtual machine, launch the Azure portal and navigate to Virtual Machines.

Select “Create”, and fill in the details such as Name, and Region. Choose the image for your virtual machine (for example – Ubuntu 24.04) and select “Arm64” as the virtual machine architecture.

In the “Size” field, click on “See all sizes” and select the D-Series v6 family of Virtual machine. Select “D4ps_v6” from the list and create the virtual machine.

![Instance Screenshot](./instance-new.png)

The virtual machine should be ready and running; You can then SSH into the virtual machine using the generated PEM key, along with the Public IP address of the running instance.

{{% notice Note %}}

To learn more about Arm-based virtual machine in Azure, refer to “Getting Started with Microsoft Azure” in [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure).

{{% /notice %}}
