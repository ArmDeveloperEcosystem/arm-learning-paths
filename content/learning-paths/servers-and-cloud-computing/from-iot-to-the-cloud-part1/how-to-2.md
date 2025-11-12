---
title: Creating the Virtual Machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Virtual Machine

### Virtual Machine Azure Resource
Let's start by creating the Virtual Machine. Go to https://portal.azure.com and sign in. You will see this screen which enables you to create Azure resources:
![Azure portal#left](figures/01.webp "Figure 1. A fragment of the Azure Portal")

In the search box, type **VM**, and pick the first item on the list (Virtual machines):
![Selecting Virtual Machine resource#left](figures/02.webp "Figure 2. Selecting the virtual machine Azure resource")

In the Virtual machines, click **+ Create** (in the top left corner), and then select **Azure virtual machine**:
![Creating Virtual Machine#left](figures/03.webp "Figure 3. Creating the virtual machine")

This takes you to the **Create a Virtual Machine** wizard as shown below:
![Creating Virtual Machine#left](figures/04.webp "Figure 4. Virtual machine wizard")

### Virtual machine configuration
Configure your VM with the following settings:

1. Subscription: select your subscription
2. Resource group: click Create new link, then type **rg-arm64**, and click OK
3. Virtual machine name: **vm-arm64**
4. Region: select depending on your physical location
5. Availability options: select **No infrastructure redundancy required**
6. Security type: **Standard**
7. VM architecture: **arm64**
8. Image: **Ubuntu Server 20.04 LTS – ARM64 Gen 2**
9. Size:
    * Click **See all sizes**
    * In the **Select a VM size**, type **D2pds** in the search box
    * Select **D2pds_v5**

{{% notice Note %}} This size might not be available due to quota limits. If this happens, click **Request quota link** (which is located next to the **VM size** name). This will activate a New Quota Request. Type **2** under New limit and click Submit. Wait a few minutes for the quota limits to be updated.{{% /notice %}}

At this point, your configuration should look like this example:
![Creating Virtual Machine#left](figures/05.webp "Figure 5. Virtual machine wizard (configured)")

Let's now configure other aspects of the Virtual Machine:
1.	Administrator account. **Select Password**, and then populate with:
    * Username: **arm**
    * Password: type your password (make a note of this password as you'll need it to connect to VM)
    * Confirm password: re-type your password
2.	Inbound port rules. Keep them default: **SSH(22)**

![Creating Virtual Machine#left](figures/06.webp "Figure 6. Administrator account and inbound rules of the virtual machine")

Click the **Review + create** button. The Azure Portal will validate your configuration and, if all is correct, you will see a green box saying: **Validation passed**: 

![Creating Virtual Machine#left](figures/07.webp "Figure 7. A summary of the create virtual machine wizard")

Click the Create button. The portal will now start the process of creating your VM. You will notice that, apart from the VM itself, the portal creates additional resources for you: 
* Public IP address (you'll need to use it to connect to the VM and then to see your application running)
* Network Security Group
* Virtual network
* Network interface
* Virtual disk

Wait a few moments for the deployment to be completed:
![Creating Virtual Machine#left](figures/08.webp "Figure 8. A confirmation screen")

Finally, click the **Go to resource** button. You'll be redirected to the overview of your newly created virtual machine in Microsoft Azure:
![Creating Virtual Machine#left](figures/09.webp "Figure 9. An overview of the virtual machine")

Note your Public IP address (top right part of the overview). In this tutorial, this is **52.149.156.228**.
