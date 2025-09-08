---
# User change
title: Create Windows on Arm virtual machine in Azure cloud

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
<<<<<<< HEAD

---
If you don't have access to a Windows on Arm device, you can create a Windows on Arm virtual machine in the Azure cloud.
=======
---
You will learn how to create a Windows on Arm virtual machine in the Azure cloud.
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

{{% notice Note %}}
These same instructions can be used to deploy a Linux image on the Arm Virtual Machine. Simply select a Linux distribution instead of Windows.
{{% /notice %}}

<<<<<<< HEAD
## Create a Windows on Arm Virtual Machine

[Microsoft Azure](https://portal.azure.com/#home) is Microsoft's cloud computing platform. You can log into Azure using either your personal subscription or your organization's subscription.

To begin:

1. Login to your Azure account.
2. From the Azure search bar, begin typing the word "virtual machines" until the [Virtual Machines](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Compute%2FVirtualMachines) service appears as a selection. 

![Search and Select VMs](images/search_and_click_vm.png)

3. Select `Virtual Machines`.

The Virtual Machines page appears.

4. Click `Create` > `Azure virtual machine`.

![Create an Azure VM](images/click_create_vm.png)

The `Create a virtual machine` page appears.

5. Select a valid `Subscription`.
6. Select a `Resource group` - Optional; you may leave blank.
7. Enter a `Virtual Machine name` - We'll call it armtest-0 for this example.
8. Select a `Region` - For best performance, select the region closest to you.
9. Select `Standard` for `Security Type`.
10. Select `See all images` - You can find this under the `Image` dropdown.

![Config the VM Part 1](images/config-vm-1.png)

The `Marketplace` page appears.

11. Enter `windows 11` into the search bar and press enter.
12. Click the `Image Type` filter and select `Arm64`.

![Select Arm images](images/image_type.png)

You are  presented with all available Arm VM images.

{{% notice Note%}}
Note all the different Arm images (Windows and others) Azure provides; feel free to experiment with different Arm images from the Azure Marketplace upon completion of this learning path.
{{% /notice %}}

13. From the drop-down at the bottom of the `Microsoft Windows 11 Preview arm64` tile, select `Windows 11 Professional 24H2 - Arm64`.

![img2](images/select_24h2.png)

Upon selection, you are returned to the `Create a virtual machine` screen with your architecture set to `Arm64` and your image set to `Windows 11 Professional, version 24H2 - ARM64 Gen2`.

14. For `Size`, select `Standard_D2ps_v5 - 2 vcpus, 8 GiB memory`.

{{% notice Note%}}
The VM size suggested for this learning path is enough to demonstrate Windows on Arm in the Azure cloud, but may need to be adjusted to support other workloads.  For more information rightsizing your VM instances, please see [Rightsize to maximize your cloud investment with Microsoft Azure](https://azure.microsoft.com/en-us/blog/rightsize-to-maximize-your-cloud-investment-with-microsoft-azure/).   
{{% /notice %}}

15. For `Username` and `Password`, provide values which will be used to login to the Windows virtual machine.

16. For `Inbound port rules` > `Public inbound ports`, select `Allow selected ports` and choose `RDP (3389)` from the drop-down menu.

17. For `Licensing` confirm that you have an eligible Windows 10/11 license with multi-tenant hosting rights. To learn more about this checkbox, please visit [documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/windows-desktop-multitenant-hosting-deployment).

18. Leave all other settings as default.

19. Click `Review + create`.

![Review and Create](images/review_create.png)

The validation and confirmation page appears.

20. Upon review and validation of your settings, select `Create` to launch your Windows on Arm virtual machine.

![Create](images/create.png)

At this point, Azure will deploy your new Windows on Arm instance to the Azure cloud.  This may take a few moments to complete.

![Deploy](images/deploying.png)

Upon completion, your screen will look similar to:

![Deploy Complete](images/deploy_complete.png)


21. Click `Go to Resource`.

From this resource page, note the `Public IP address` of your virtual machine, as you will use in the next step to connect to your VM instance. 


![Public IP](images/public_ip.png)

## Connect to your Windows on Arm VM

1. On your local host PC, launch your RDP client application.

{{% notice Note%}}
In our example, we use the `Remote Desktop Connection` app as our RDP client, but you may choose any RDP client to use.   
{{% /notice %}}

2. Enter the `Public IP Address` you wrote down earlier as the `Computer` or remote host/IP to connect to.

3. Enter the username and password you set earlier while creating the VM instance.

4. Click connect.

![RDP #center](images/rdp.png)
=======
## Create Windows on Arm virtual machine

[Microsoft Azure](https://portal.azure.com/#home) is a cloud computing platform. You can log into Azure using either your personal subsciption or your organization's subscription.

Start by locating [Virtual Machines](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Compute%2FVirtualMachines) from the list of `Azure Services`, then click `Create` > `Azure virtual machine`.

You will be presented with the `Create a virtual machine` dialog. On this dialog, first select your `Subscription` and `Resource group`. Then, enter a `Virtual Machine name` and select the `Region` in which you want to create your Windows on Arm Virtual machine.  

Next, for `VM Architecture` select `Arm64`.

Then click on `See all images` (under `Image`) and filter `Image Type` for `Arm64` as show in the image below:

![img1](Images/azure1.png)

You will be presented with all the VM images that are available for Arm. Select `Windows 11 Professional - Arm64` from the drop-down menu under `Microsoft Windows 11` as shown below.

![img2](Images/azure2.png)

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
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

You can now interact with the VM in the same way as you would a local desktop.

If you have issues connecting to your instance, see this Microsoft article:
* [How to connect using Remote Desktop and sign on to an Azure virtual machine running Windows](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/connect-rdp)

## Explore your VM

Open `Control Panel` > `System`, and verify that `Device` > `System Type` identifies as an Arm-based processor.

<<<<<<< HEAD
![System #center](images/system.png)
=======
![System #center](Images/system.png)
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
