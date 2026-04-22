---
title: Create an Azure X64 virtual machine as an "on-prem simulator"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Overview

In this section, you'll use the Azure portal to create a virtual machine with an x64 processor architecture.

This VM acts as your simulated on-premises x64 MySQL server.

### Create an Azure x64 virtual machine

To create an Azure virtual machine:

- Launch the Azure portal and navigate to **Virtual Machines**.
- Select **Create**, and select **Virtual Machine** from the drop-down list.
- Inside the **Basic** tab, fill in the instance details such as **Virtual machine name** and **Region**.
- Select the image for your virtual machine (for example, Ubuntu Pro 24.04 LTS) and select **x64** as the VM architecture.
- In the **Size** field, select **See all sizes** and select the D-Series v6 family of virtual machines.
- Select **D4ads_v6** from the list as shown in the diagram below:

![Azure Portal showing D-Series v6 VM size selection with x64 D4ads_v6 highlighted#center](images/instance.png "Select D4ads_v6 from the D-Series v6 x64 family")

- For **Authentication type**, select **SSH public key**.

{{% notice Note %}}
Azure can generate an SSH key pair for you and lets you save it for future use.
{{% /notice %}}

- Fill in the **Administrator username** for your VM.
- Select **Generate new key pair**, and select **RSA SSH Format** as the SSH Key Type.

{{% notice Note %}}
RSA offers better security with keys longer than 3072 bits.
{{% /notice %}}

- Give your SSH key a key pair name.
- In the **Inbound port rules**, select **HTTP (80)** and **SSH (22)** as the inbound ports, as shown below:

![Azure Portal showing inbound port rules with HTTP (80) and SSH (22) selected#center](images/instance1.png "Configure inbound port rules for HTTP and SSH access")

- Now select the **Review + Create** tab and review the configuration for your virtual machine. It should look like the following:

![Azure Portal Review + Create tab showing VM configuration summary ready for deployment#center](images/instance3.png "Review VM configuration before creation")

- When you're happy with your selection, select the **Create** button and then **Download Private key and Create Resource** button.

![Azure Portal showing Create button and SSH key download dialog#center](images/instance4.png "Download SSH key and create the virtual machine")

Your virtual machine should be ready and running in a few minutes. You can SSH into the virtual machine using the private key, along with the public IP details.

![Azure Portal showing successful VM deployment with confirmation details#center](images/final-vm.png "Successful VM deployment confirmation")

{{% notice Note %}}To learn more about virtual machines in Azure, see "Getting Started with Microsoft Azure" in [Get started with cloud instances](/learning-paths/servers-and-cloud-computing/csp/azure/).{{% /notice %}}

## What you've learned and what's next

You've created an Azure x64 virtual machine running Ubuntu 24.04 LTS with SSH authentication configured. The virtual machine is now ready to act as your simulated on-premises environment for this Learning Path.

Next, you will prepare this environment by installing MySQL and loading a sample database for migration.
