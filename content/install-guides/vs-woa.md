---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Visual Studio for Windows on Arm 

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- clang
- compiler
- ide
- vs
- windows
- woa
- windows on arm


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

### Link to official documentation
official_docs: 

author_primary: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Visual Studio 2022 17.4](https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices) (and higher) natively supports Windows on Arm.

## Download and Install

[Download the Visual Studio Installer](https://visualstudio.microsoft.com/vs/) to get started.

{{% notice Note%}}
There are 3 different versions available to download: Community, Professional and Enterprise.

Choose the appropriate version for your usage.
{{% /notice %}}

Once downloaded, run the `VisualStudioSetup.exe` file on a Windows on Arm machine. This is the installer.

# Install C and C++ support in Visual Studio
During the installation process, you will be asked to choose the workloads you want and customize your installation. At a minimum, select `Desktop development with C++`.

![img1 #center](/install-guides/_images/vs-woa.png)

# Install LLVM support in Visual Studio

To build native Windows Applications using the LLVM toolchain in Visual Studio, you need to install additional components.

In the installer, select the `Individual components` tab. Enter `clang` in the search bar.

Two results are displayed: The LLVM compiler and MSBuild support for LLVM. Select both these options:

![img2 #center](/install-guides/_images/llvm_vs.png)

{{% notice  Note%}}
Different versions of Visual Studio include different LLVM toolchain versions.

For example, Visual Studio 2022 Version `17.11.5` installs `LLVM 17.0.3`.
{{% /notice %}}

LLVM supports `clang-cl`, a compatibility layer for Microsoft Visual C++ (MSVC). This means that most developers can use `clang-cl` to compile their C/C++ applications on Visual Studio/MSBuild on the Windows on Arm device, without needing to change the command line. This allows you to easily modify legacy projects that use MSVC to use native compilation.

You can now proceed with `Install`. The installation process can take several minutes to complete. A reboot of your machine is required before you launch Visual Studio.

## Modify your installation
The workload and individual component selection can also be made at any time after you complete the installation of Visual Studio. To modify your installation, run `VisualStudioSetup.exe`, select `Continue` to accept the installation conditions and then choose `Modify`.

You can choose additional workloads and individual components to further customize your installation.

For the latest updates on Arm native development, check the [Microsoft Learn](https://learn.microsoft.com/en-us/windows/arm/overview) site.
