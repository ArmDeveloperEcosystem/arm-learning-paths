---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Windows Sandbox for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- sandbox
- windows
- woa
- windows on arm

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview

author_primary: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Windows Sandbox is a lightweight desktop environment from Microsoft that lets you safely run your applications in isolation. Software that is installed in the Windows Sandbox environment is completed isolated from the host machine. You can install Windows Sandbox on an Arm machine running Windows 11, version 22H2 and later. 

A number of developer ready Windows on Arm [devices](../../learning-paths/laptops-and-desktops/intro/find-hardware/) are available.

Windows on Arm instances are available with Microsoft Azure. For more information, see [Deploy a Windows on Arm virtual machine on Microsoft Azure](../../learning-paths/cross-platform/woa_azure/).

## Enable Virtualization
To run Windows Sandbox, you need to ensure that virtualization is enabled on your machine.

Ensure that Arm machine is running Windows 11, version 22H2 or later.
 
On a physical machine, virtualization is enabled in the BIOS. To verify, go through the following steps:

* Right click on the Windows Start Menu and select Terminal(Admin)

* Run `systeminfo.exe` on your Windows Terminal and press Enter

Details about your system will be printed on the terminal. Check the `Hyper-V requirements` section at the bottom of the Window. Verify that that the Virtualization Enabled in Firmware option says Yes.

![Install #center](/install-guides/_images/sandbox_virt_0.png)

If the Hyper-V requirements section displays the following message "A hypervisor has been detected. Features required for Hyper-V will not be displayed.", it means that some virtualization technology is installed and you can proceed with enabling Windows Sandbox.

![Install #center](/install-guides/_images/sandbox_virt_1.png)

{{% notice Note %}} If this message is not displayed or the Virtualization Enabled in Firmware option says No, you will have to enable virtualization in your BIOS. The BIOS settings for Virtualization can vary depending on your physical device but is generally found under Advanced settings. {{% /notice %}}

With virtualization now enabled, you can proceed to installing Windows Sandbox on your machine.

## Install Windows Sandbox

{{% notice Note %}}
You must enable Windows Sandbox on a physical Windows on Arm machine. It cannot be enabled on a virtual machine such as an Azure Arm instance running Windows 11. 
{{% /notice %}}

On the Windows search bar type "Turn Windows Features on or off". 
From the Windows Features list, select Windows Sandbox and then click OK. Restart your computer if you are prompted.

![Install #center](/install-guides/_images/sandbox_1.png)

After your machine restarts, click on the Start menu and select Windows Sandbox. 

It will take a few minutes for Windows Sandbox to launch. 

You are now ready to use Windows Sandbox on your Windows on Arm machine. 
