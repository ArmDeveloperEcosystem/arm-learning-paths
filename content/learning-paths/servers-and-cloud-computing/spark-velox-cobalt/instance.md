---
title: Create an Azure Cobalt 100 Arm64 virtual machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prerequisites and setup

You can create an Arm-based Cobalt 100 virtual machine using any of the following methods that best fits your workflow or requirements:

- The Azure Portal
- The Azure CLI
- An infrastructure as code (IaC) tool

In this section, you'll launch the Azure Portal to create a virtual machine (VM) with the Arm-based Azure Cobalt 100 processor.

This Learning Path focuses on general-purpose virtual machines in the Dpsv6 series. For more information, see the [Microsoft Azure guide for the Dpsv6 size series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series).

While the steps to create this instance are included here for convenience, for detailed steps, see the [Deploy a Cobalt 100 virtual machine on Azure Learning Path](/learning-paths/servers-and-cloud-computing/cobalt/). To learn more about Arm-based virtual machines in Azure, see "Getting Started with Microsoft Azure" in [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure/).

## Create an Arm-based Azure virtual machine on the Azure portal

To create an Azure virtual machine:

1. Launch the Azure portal and navigate to **Virtual Machines**.
2. Select **Create**, and select **Virtual Machine** from the drop-down list.
3. Inside the **Basic** tab, enter the instance details such as **Virtual machine name** and **Region**.
4. Select the image for your virtual machine (for example, Ubuntu 22.04 LTS Server) and select **Arm64** as the VM architecture.
5. In the **Size** field, select **See all sizes** and select the D-Series v6 family of virtual machines.
6. Select **D8ps_v6** from the list as shown in the following diagram:

![Azure Portal showing D-Series v6 VM size selection with D8ps_v6 highlighted#center](images/instance.png "Select D8ps_v6 from the D-Series v6 family")

7. For **Authentication type**, select **SSH public key**.

{{% notice Note %}}
Azure generates an SSH key pair for you and lets you save it for future use. This method is fast, secure, and easy for connecting to your virtual machine.
{{% /notice %}}

8. Fill in the **Administrator username** for your VM.
9. Select **Generate new key pair**, and select **RSA SSH Format** as the SSH Key Type.

{{% notice Note %}}
RSA offers better security with keys longer than 3072 bits.
{{% /notice %}}

10. Give your SSH key a key pair name.
11. In the **Inbound port rules**, select **HTTP (80)** and **SSH (22)** as the inbound ports, as shown in the following screenshot:

![Azure Portal showing inbound port rules with HTTP (80) and SSH (22) selected#center](images/instance1.png "Configure inbound port rules for HTTP and SSH access")

12. Select the **Review + Create** tab and review the configuration for your virtual machine. It should look like the following:

![Azure Portal Review + Create tab showing VM configuration summary ready for deployment#center](images/ubuntu-pro.png "Review VM configuration before creation")

13. After reviewing the configuration, select the **Create** button and then the **Download Private key and Create Resource** button.

![Azure Portal showing Create button and SSH key download dialog#center](images/instance4.png "Download SSH key and create the virtual machine")

Your virtual machine should be ready and running in a few minutes. You can SSH into the virtual machine using the private key, along with the public IP details.

![Azure Portal showing successful VM deployment with confirmation details#center](images/final-vm.png "Successful VM deployment confirmation")

## What you've learned and what's next

You've now successfully created an Azure Cobalt 100 Arm64 virtual machine running Ubuntu 22.04 LTS Server with SSH authentication configured. The VM is now fully prepared for running distributed data processing workloads.

Next, you'll build a high-performance Spark SQL analytics platform using modern acceleration technologies.
