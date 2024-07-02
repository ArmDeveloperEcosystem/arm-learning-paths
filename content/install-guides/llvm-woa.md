---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: LLVM toolchain for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- clang
- compiler
- windows
- woa
- windows on arm
- open source windows on arm


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

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

[LLVM version 12 or higher](https://llvm.org/) natively supports Windows on Arm. [View the supported Arm architecture features](https://developer.arm.com/Tools%20and%20Software/LLVM%20Toolchain#Supported-Devices) in the open-sourced LLVM toolchain.

## Download and install

The latest version (at the time of writing) of the LLVM toolchain with Windows on Arm native support is 18.1.8. [Download the pre-built binary](https://github.com/llvm/llvm-project/releases/download/llvmorg-18.1.8/LLVM-18.1.8-woa64.exe).

{{% notice Note %}}
A warning message may appear in your browser due to the publisher being listed as `Unknown`. The warning is:

`Microsoft Defender SmartScreen couldn't verify if this file is safe because it isn't commonly downloaded. Make sure you trust the file you're downloading or its source before you open it.`

It is safe to ignore this warning and proceed.
{{% /notice %}}

After download, run `LLVM-18.1.8-woa64.exe` on a Windows on Arm machine. The installer will start. By default, the installer does not add LLVM to the system `PATH`. If you easily want to invoke LLVM from any directory, select the option to `Add LLVM to the system PATH for all users`.

![img1 #center](/install-guides/_images/llvm-setup.png)

Proceed with `Install`. 

The setup will complete successfully. Select `Finish` to close the installer.

![img2 #center](/install-guides/_images/llvm-finish.png)

## Check the installation

Open a Windows Command prompt or a PowerShell prompt and run:

```console
clang --version
```
The output should look like:

```output
clang version 18.1.8
Target: aarch64-pc-windows-msvc
Thread model: posix
InstalledDir: C:\Program Files\LLVM\bin
```
 
## Other versions of LLVM

You can download other LLVM builds from [the download repository](https://releases.llvm.org/download.html).

{{% notice Note%}}
The pre-built binary for Windows on Arm is typically named `LLVM-<version>-woa64.exe`.
{{% /notice %}}
