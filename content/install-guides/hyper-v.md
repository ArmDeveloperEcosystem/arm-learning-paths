---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Hyper-V on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- virtual machine
- vm
- windows
- woa
- windows on arm
- open source windows on arm


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://learn.microsoft.com/en-us/virtualization/

author_primary: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

You can use Hyper-V to create and run virtual machines using Windows 11 on Arm. 

{{% notice Note %}}
There is nothing to download to enable Hyper-V.
{{% /notice %}}

## What should I consider before installing Hyper-V?

Arm virtual machines on Windows with Hyper-V require `Windows 11 version 22H2` or newer. 

To check your Windows version hold down the Windows Key and press R. In the Run dialog box type `winver`.

A dialog will appear with your version information. 

Look for `Version 22H2` or newer. 

Here is a screenshot of `winver`:

![Windows version #center](/install-guides/_images/winver.png)


{{% notice Note %}}
You must enable Hyper-V on a physical computer. It cannot be enabled on a virtual machine such as an Azure Arm instance running Windows 11. 
{{% /notice %}}

Follow the instructions below to enable Hyper-V on Windows on Arm. 

There are multiple ways to enable Hyper-V:
- Use the Control Panel 
- Use the Command Prompt or PowerShell command line

Pick one alternative, you don't need to do both.

## How do I enable Hyper-V using the Control Panel?

1. Click the Windows button, find and open the Control Panel 

2. In Control Panel click `Programs` and then click Turn Windows features on or off

A dialog should appear:

![Hyper-V off #center](/install-guides/_images/hyper-v-1.png)

3. Select Hyper-V and click OK

![Hyper-V on #center](/install-guides/_images/hyper-v-2.png)

## How do I enable Hyper-V from the command line?

1. Open a Command Prompt or Windows PowerShell (as Administrator)

2. Run the `DISM` command below to enable Hyper-V:

```console
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

The output should include the message:

```output
The operation completed successfully.
```

## Restart 

Restart your computer to finish enabling Hyper-V.


## Start Hyper-V

Hyper-V Manager should now be available in the applications menu.

![Hyper-V manager #center](/install-guides/_images/hyper-v-manager.png)

You are now ready to use Hyper-V to create virtual machines on your Windows on Arm device. 
