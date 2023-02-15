---
# User change
title: "Create Windows on Arm virtual machine in Azure cloud"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You will learn how to create a Windows on Arm virtual machine in the Azure cloud. This machine will be used as the GitHub self-hosted runner in your CI flow.

## Create Windows Virtual Machine for Arm64 architecture in Azure cloud

[Microsoft Azure](https://portal.azure.com/#home) is a cloud computing platform. You can log into Azure using either your personal subsciption or your organization's subscription.

Start by locating [Virtual Machines](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Compute%2FVirtualMachines) from the list of `Azure Services`, then click `Create` > `Azure virtual machine`.

You will be presented with the `Create a virtual machine` dialog. On this dialog, first select your Subscription` and `Resource group`. Then, enter a `Virtual Machine name` and select the `Region` in which you want to create your Windows on Arm Virtual machine.  

Next, for `VM Architecture` select `Arm64`. Then under `Image` click on `See all images` and filter on `Arm64` as show in the image below

![img1](Images/azure1.png)

You will be presented with all the VM images that are available for Arm64 architecture. Select `Windows 11 Professional - Arm64` from the drop-down menu under `Microsoft Windows 11 Preview arm64` as shown below.

![img2](Images/azure2.png)

You will then be returned to the `Create a virtual machine` dialog screen with your selections. Under the `Administrator account` section enter a `Username` and `Password` in the fields provided. You will use these credentials to access your Windows virtual machine.

In the `Inbound port rules` section of the dialog, select `Allow selected ports` and choose `RDP (3389)` from the drop-down menu. Finally, under the `Licensing` section you will need to confirm that you have an eligible Windows 10/11 license with multi-tenant hosting rights. To learn more about the licensing before you select this checkbox read this [documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/windows-desktop-multitenant-hosting-deployment). You can now select the `Review + create` button as shown below.

<IMG3>

All your selections will be validated and you can select the `Create` button to launch your Windows on Arm virtual machine. Once the deployment of your virtual machine is complete, select the `Go to Resource button`. From this page, you will be able to view the `Public IP address` of your virtual machine which you will use in the next step to connect to your VM instance. 

## Connect to your Windows on Arm VM instance

On your local host PC, launch the `Remote Desktop Connection` application.

Enter the `Public IP Address` of the Windows VM as the `Computer` to be connected to. 

Next, enter the username and password (set earlier while creating the VM instance), and you will connect. You can interact with the VM in the same way as you would a local desktop.

### Explore your instance

Open `Control Panel` > `System`, and verify that `Device` > `System Type` identifies as an ARM-based processor.




