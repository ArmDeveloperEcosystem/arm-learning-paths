---
# User change
title: Create Windows on Arm virtual machine in Azure cloud

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"

---
Upon completing this learning path, you will learn how to create a Windows on Arm virtual machine in the Azure cloud.

{{% notice Note %}}
These same instructions can be used to deploy a Linux image on the Arm Virtual Machine. Simply select a Linux distribution instead of Windows.
{{% /notice %}}

## Create a Windows on Arm Virtual Machine

[Microsoft Azure](https://portal.azure.com/#home) is Microsoft's cloud computing platform. You can log into Azure using either your personal subscription or your organization's subscription.

To begin:

1. Login to your Azure account.
2. From the Azure search bar, begin typing the word "virtual machines" until the [Virtual Machines](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Compute%2FVirtualMachines) service appears as a selection. 

![Search and Select VMs](Images/search_and_click_vm.png)

3. Click on Virtual Machines.

The Virtual Machines page appears.

4. Click `Create` > `Azure virtual machine`.

![Create an Azure VM](Images/click_create_vm.png)

The `Create a virtual machine` page appears.

5. Select a valid `Subscription`.
6. Select a `Resource group` - Optional; you may leave blank.
7. Enter a `Virtual Machine name` - We'll call it armtest-0 for this example.
8. Select a `Region` - For best performance, select the region closest to you.
9. Select `Standard` for `Security Type`.
10. Select `See all images` - You can find this under the `Image` dropdown.

![Config the VM Part 1](Images/config-vm-1.png)

The `Marketplace` page appears.

11. Enter `windows 11` into the search bar and press enter.
12. Click the `Image Type` filter and select `Arm64`.

![Select ARM images](Images/image_type.png)

You are  presented with all available Arm VM images.

13. From the drop-down at the bottom of the `Microsoft Windows 11 Preview arm64` tile, select `Windows 11 Professional 24H2 - Arm64`.

![img2](Images/select_24h2.png)

Next, for `VM Architecture` select `Arm64`.

You will then be returned to the `Create a virtual machine` dialog screen with your selections. Change the `Security type` setting to `Standard`. 

Under the `Administrator account` section enter a `Username` and `Password` in the fields provided. You will use these credentials to access your Windows virtual machine.

In the `Inbound port rules` section of the dialog, select `Allow selected ports` and choose `RDP (3389)` from the drop-down menu.

Finally, under the `Licensing` section you will need to confirm that you have an eligible Windows 10/11 license with multi-tenant hosting rights. To learn more about the licensing before you select this checkbox read this [documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/windows-desktop-multitenant-hosting-deployment).

Leaving other settings as default, click `Review + create`.

All your selections will be validated and you can click `Create` to launch your Windows on Arm virtual machine.

Once the deployment of your virtual machine is complete, click on `Go to Resource`. From here you will be able to view the `Public IP address` of your virtual machine which you will use in the next step to connect to your VM instance. 

## Connect to your Windows on Arm VM

On your local host PC, launch the `Remote Desktop Connection` application.

Enter the `Public IP Address` of the Windows VM as the `Computer` to be connected to.

Next, username (set earlier while creating the VM instance), and when prompted the password, and you will connect.

![RDP #center](Images/rdp.png)

You can now interact with the VM in the same way as you would a local desktop.

If you have issues connecting to your instance, see this Microsoft article:
* [How to connect using Remote Desktop and sign on to an Azure virtual machine running Windows](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/connect-rdp)

## Explore your VM

Open `Control Panel` > `System`, and verify that `Device` > `System Type` identifies as an Arm-based processor.

![System #center](Images/system.png)
