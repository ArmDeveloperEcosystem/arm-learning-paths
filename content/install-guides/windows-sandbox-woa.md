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

Windows Sandbox is a lightweight, desktop environment from Microsoft that enables you to safely run and test applications in isolation. Software installed in Windows Sandbox is completely isolated from the host machine. When the sandbox is closed, your installed software is deleted. You can create a new sandbox and start your testing again.

You can install Windows Sandbox on an Arm device running Windows 11, version 22H2, and later. 

A number of developer-ready [Windows on Arm devices](../../learning-paths/laptops-and-desktops/intro/find-hardware/) are available.

## Enable Virtualization

To run Windows Sandbox, you need to make sure that virtualization is enabled on your device.

On a physical machine, virtualization is enabled in the BIOS. 

Use the following steps to check the virtualization settings:

* Right-click on the Windows Start Menu and select Terminal(Admin)

* Enter `systeminfo.exe` and press Enter

Details about your system are printed on the terminal. 

Check the `Hyper-V requirements` section at the bottom of the Window. 

If you see:

`Virtualization Enabled in Firmware: Yes` 

as shown in the picture below, then you are ready to use Windows Sandbox.

![Virtualization 1](/install-guides/_images/sandbox_virt_0.png)

If you see:

`A hypervisor has been detected. Features required for Hyper-V will not be displayed.` 

as shown in the picture below, it also means you are ready to use Windows Sandbox.

![Virtualization 2 #center](/install-guides/_images/sandbox_virt_1.png)

{{% notice Note %}} If you don't see any messages about Hyper-V Requirements or you see: 

`Virtualization Enabled in Firmware: No` 

then you need to enable virtualization in your BIOS. 

The BIOS settings for Virtualization vary depending on your device, but are generally found under Advanced settings. 
{{% /notice %}}

With virtualization now enabled, you can install Windows Sandbox.

## Install Windows Sandbox

{{% notice Note %}}
You must enable Windows Sandbox on a physical Windows on Arm device. It cannot be enabled on a virtual machine such as an Azure Arm instance running Windows 11. 
{{% /notice %}}

On the Windows search bar type "turn windows features on or off" and open the Control panel. 

From the Windows Features list, select Windows Sandbox and then click OK. 

![Install #center](/install-guides/_images/sandbox_1.png)

If prompted, Restart your computer.

After your computer restarts, click on the Start menu and select Windows Sandbox. 

It will take a few minutes for Windows Sandbox to launch. 

You are now ready to use Windows Sandbox on your computer.

You can install software and perform any other testing activities in the temporary sandbox.

When you exit Windows Sandbox, the software you installed and any changes you made in the sandbox are gone. 

More information is available about the [Windows Sandbox architecture](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture).
