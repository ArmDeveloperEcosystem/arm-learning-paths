---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Performance Studio
description: Install Arm Performance Studio on Windows, macOS, or Linux to profile Android and Linux applications with Arm performance analysis tools.

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- Gaming
- Graphics
- Android
- profiling
- mali
- immortalis
- cortex-a
- Install Arm Mobile Studio
- Streamline
- Performance Advisor
- RenderDoc
- Frame Advisor


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/107649

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
test_maintenance: true
test_images:
  - ubuntu:latest
---
[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) is a performance analysis tool suite for Android and Linux application developers. It shows you how well your game or app performs on production devices, so that you can identify problems that might cause slow performance, overheat the device, or drain the battery.

| Component | Functionality |
|----------|-------------|
| [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) with [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor)| Capture a performance profile that shows all the performance counter activity from the device. Generate an easy-to-read performance summary from an annotated Streamline capture, and get actionable advice about where you should optimize. |
| [Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) | Capture the API calls and rendering from a problem frame and get comprehensive geometry metrics to discover what might be slowing down your application. |
| [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) | Analyze how efficiently your shader programs perform on a range of Mali GPUs. |
| [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs) | The industry-standard tool for debugging Vulkan graphics applications, including early support for Arm GPU extensions and Android features. |


All features of Arm Performance Studio are available free of charge without any additional license.

## Download Arm Performance Studio

Arm Performance Studio is supported on Windows, Linux, and macOS hosts. Download the appropriate installer from [Arm Performance Studio Downloads](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads).

Full details about the supported OS and Android versions are given in the Arm Performance Studio [Release Notes](https://developer.arm.com/documentation/107649).

## Install Arm Performance Studio on Windows

Arm Performance Studio is provided as an installer executable. Double-click the `.exe` file and follow the instructions in the setup wizard.

Open the Performance Studio Hub from the **Windows Start** menu, or by double-clicking the shortcut in the installation directory. You can read a description of the tools and launch them from the Hub.

## Install Arm Performance Studio on macOS

Arm Performance Studio is provided as a `.dmg` package. Double-click the `.dmg` package and follow the instructions. The Arm Performance Studio directory tree is copied to your `Applications` directory.

Open the `Performance Studio.app` file in your `Applications` directory to launch the **Arm Performance Studio Hub**. You can read a description of the tools and launch them from the Hub.

## Install Arm Performance Studio on Linux

Arm Performance Studio for Linux is available for x86_64 hosts only. The tools profile Arm targets, such as Android devices and Arm Linux boards, from an x86_64 host.

Arm Performance Studio is provided as a gzipped tar archive.

{{% notice Note %}}
The following commands use Arm Performance Studio version 2026.4. The same commands work with other versions. Replace the filename with the file for your version of choice. To find the latest version, see [Arm Performance Studio Downloads](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads).
{{% /notice %}}

Extract the tar archive to your home directory:

```bash
tar xvzf Arm_Performance_Studio_2026.4_linux_x86-64.tgz -C $HOME
```

This creates the `Arm_Performance_Studio_2026.4` directory in your home directory.

Add the Streamline and Mali Offline Compiler directories to your `PATH` so you can run the `Streamline-cli` and `malioc` command-line tools from any directory. Add the following lines to your `~/.bashrc`, then start a new shell:

```bash
export PATH=$PATH:$HOME/Arm_Performance_Studio_2026.4/streamline
export PATH=$PATH:$HOME/Arm_Performance_Studio_2026.4/mali_offline_compiler
```

## Verify the installation

Confirm the Mali Offline Compiler is available:

```bash
malioc --version
```

The output is similar to:

```output
Mali Offline Compiler v2026.3.0 (Build bbe17b)
Copyright (c) 2007-2026 Arm Limited. All rights reserved.
```

Confirm the Streamline command-line tool is available:

```bash
Streamline-cli --version
```

The output is similar to:

```output
Streamline 9.8 (Build 9.8.0.v20260625_0741)
Copyright (c) 2010-2026 Arm Limited. All rights reserved.
```

To launch the graphical Performance Studio Hub, run the launcher script in the installation directory:

```bash
$HOME/Arm_Performance_Studio_2026.4/performance-studio-cli.sh
```

The Hub describes each tool and lets you launch Streamline, Frame Advisor, and RenderDoc for Arm GPUs.

## Get started with Arm Performance Studio

See the [Get started with Arm Performance Studio](/learning-paths/mobile-graphics-and-gaming/ams/) learning path for an overview of how to run each tool in Arm Performance Studio.
