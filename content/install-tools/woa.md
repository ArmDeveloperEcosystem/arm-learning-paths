---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Windows on Arm native build tools

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- clang
- compiler

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

### Link to official documentation
official_docs: 

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
This is a summary of native tooling available for [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview) (WoA) applications.

# Visual Studio

[Visual Studio 2022 17.4](https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices) (and higher) natively supports Windows on Arm.

For more information, see [this announcement blog](https://devblogs.microsoft.com/visualstudio/arm64-visual-studio-is-officially-here/) from Microsoft.

Previous releases required WoA applications to be cross-compiled on other hosts. When run on an Arm platform with x86 emulation, some features were not supported and performance was poor.

Check the [Microsoft Learn](https://learn.microsoft.com/en-us/windows/arm/overview) site For the latest updates on Arm-native development.

## Install C and C++ support

During installation process, you will be asked what workloads you wish to install. At a minimum, select `Desktop development with C++`.

See the [documentation](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation) for more information.

## Runtime libraries

If needed, download the Arm64 redistributable [runtime libraries](https://aka.ms/vs/17/release/vc_redist.arm64.exe) as described [here](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist).

# LLVM toolchain

[LLVM](https://llvm.org/) (LLVM 14 or higher) natively supports Windows on Arm.

Previous releases required cross-compiling on another host, or using x86 emulation. Typically compilation is twice as fast using the native toolchain vs emulation.

You can download the latest LLVM builds from [here](https://releases.llvm.org/download.html).
  - The pre-built binary for Windows on Arm is typically named `LLVM-<version>-woa64.exe`.

## Compatibility with existing Visual Studio / MSVC projects

LLVM supports `clang-cl`, a compatibility layer for Microsoft Visual C++ (MSVC). This means that most developers can use `clang-cl` to compile their C/C++ applications on Visual Studio/MSBuild on the Windows on Arm device, without needing to change the command line. This allows you to easily modify legacy projects that use MSVC to use native compilation.

# WindowsPerf

WindowsPerf is an open-source tool for performance analysis. The WindowsPerf project consists of a kernel mode driver `wperf-driver` and a user-space command line tool `wperf`. It can instrument Arm CPU performance counters. 	

To get started with WindowsPerf on your Windows on Arm machine, go to https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases/1.0.1

Then download `windowsperf-bin-1.0.1.zip` under Assets->Packages. Unzip the package. Under the wperf-driver directory, select `wperf-driver.inf`. Right click and install. This will install wperf-driver. You can now count events on your Windows on Arm machine. 

For more about the usage of `wperf` refer to the repository with examples [here](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/blob/main/wperf/README.md#usage-of-wperf).

