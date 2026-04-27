---
title: Create an Azure Cobalt 100 Arm64 virtual machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prerequisites and setup

There are several common ways to create an Arm-based Cobalt 100 virtual machine, and you can choose the method that best fits your workflow or requirements:

- The Azure Portal
- The Azure CLI
- An infrastructure as code (IaC) tool

In this section, you'll launch the Azure Portal to create a virtual machine with the Arm-based Azure Cobalt 100 processor.

This Learning Path focuses on general-purpose virtual machines in the Dpsv6 series. For more information, see the [Microsoft Azure guide for the Dpsv6 size series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series).

While the steps to create this instance are included here for convenience, you can also refer to the [Deploy a Cobalt 100 virtual machine on Azure Learning Path](/learning-paths/servers-and-cloud-computing/cobalt/).

## Create an Arm-based Azure virtual machine

Creating a virtual machine based on Azure Cobalt 100 is no different from creating any other virtual machine in Azure. To create an Azure virtual machine:

- Launch the Azure portal and navigate to **Virtual Machines**.
- Select **Create**, and select **Virtual Machine** from the drop-down list.
- Inside the **Basic** tab, fill in the instance details such as **Virtual machine name** and **Region**.
- Select the image for your virtual machine (for example, Ubuntu 22.04 LTS Server) and select **Arm64** as the VM architecture.
- In the **Size** field, select **See all sizes** and select the D-Series v6 family of virtual machines.
- Select **D8ps_v6** from the list as shown in the diagram below:

![Azure Portal showing D-Series v6 VM size selection with D8ps_v6 highlighted alt-txt#center](images/instance.png "Select D8ps_v6 from the D-Series v6 family")

- For **Authentication type**, select **SSH public key**.

{{% notice Note %}}
Azure generates an SSH key pair for you and lets you save it for future use. This method is fast, secure, and easy for connecting to your virtual machine.
{{% /notice %}}

- Fill in the **Administrator username** for your VM.
- Select **Generate new key pair**, and select **RSA SSH Format** as the SSH Key Type.

{{% notice Note %}}
RSA offers better security with keys longer than 3072 bits.
{{% /notice %}}

- Give your SSH key a key pair name.
- In the **Inbound port rules**, select **HTTP (80)** and **SSH (22)** as the inbound ports, as shown below:

![Azure Portal showing inbound port rules with HTTP (80) and SSH (22) selected alt-txt#center](images/instance1.png "Configure inbound port rules for HTTP and SSH access")

- Now select the **Review + Create** tab and review the configuration for your virtual machine. It should look like the following:

![Azure Portal Review + Create tab showing VM configuration summary ready for deployment alt-txt#center](images/ubuntu-pro.png "Review VM configuration before creation")

- When you're happy with your selection, select the **Create** button and then **Download Private key and Create Resource** button.

![Azure Portal showing Create button and SSH key download dialog alt-txt#center](images/instance4.png "Download SSH key and create the virtual machine")

Your virtual machine should be ready and running in a few minutes. You can SSH into the virtual machine using the private key, along with the public IP details.

![Azure Portal showing successful VM deployment with confirmation details alt-txt#center](images/final-vm.png "Successful VM deployment confirmation")

{{% notice Note %}}To learn more about Arm-based virtual machines in Azure, see "Getting Started with Microsoft Azure" in [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure/).{{% /notice %}}

## What you've learned and what's next

You have successfully created an Azure Cobalt 100 Arm64 virtual machine running **Ubuntu 22.04 LTS Server** with SSH authentication configured. The VM is now fully prepared for running distributed data processing workloads.

On this VM, you have:

- Set up a stable ARM64 environment  
- Configured SSH access and hostname for cluster communication  
- Prepared the system for big data stack installation (Hadoop, Spark, Hive)  
- Ensured compatibility for Java 17 and ARM-based execution  

## What’s Next

On this VM, you will now build a **high-performance Spark SQL analytics platform** using modern acceleration technologies.

**You will:**

- Install and configure **Hadoop (HDFS + YARN)**  
- Install and configure **Apache Spark**  
- Set up **Hive Metastore (MySQL-based)**  
- Build and integrate **Gluten + Velox (native engine)**  
