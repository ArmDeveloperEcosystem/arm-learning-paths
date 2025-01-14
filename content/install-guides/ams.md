---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Performance Studio

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- Gaming
- Graphics
- Android
- profiling
- mali
- immortalis
- cortex-a


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/107649

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio%20for%20Mobile) (formally known as `Arm Mobile Studio`) is a performance analysis tool suite for various application developers:

* Android application developers
* Linux application developers in Embedded and Cloud segments

It comprises of a suite of easy-to-use tools that show you how well your game or app performs on production devices, so that you can identify problems that might cause slow performance, overheat the device, or drain the battery.

[Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) is available in `2023.5` and later.

[RenderDoc for Arm GPUs](https://community.arm.com/arm-community-blogs/b/graphics-gaming-and-vr-blog/posts/beyond-mobile-arm-mobile-studio-is-now-arm-performance-studio) is available in `2024.0` and later.

[Graphics Analyzer](https://developer.arm.com/Tools%20and%20Software/Graphics%20Analyzer) is no longer provided. The final release was provided in the `2024.2` release.

All features of Arm Performance Studio are available free of charge without any additional license as of the `2022.4` release.

## Installation

Arm Performance Studio is supported on Windows, Linux, and macOS hosts. Download the appropriate installer from the [Arm Product Download Hub](https://developer.arm.com/downloads/view/MOBST-PRO0).

Full installation and application launch instructions are given in the Arm Performance Studio [Release Notes](https://developer.arm.com/documentation/107649).

### Windows

Run the supplied `Arm_Performance_Studio_<version>_windows_x86-64.exe` installer, and follow on-screen instructions.

### Linux

Unpack the supplied `Arm Performance Studio` bundle to the desired location. For example:
```command
tar -xf Arm_Performance_Studio_2024.3_linux_x86-64.tgz
```
### macOS

Run the supplied `Arm_Performance_Studio_<version>_macos_x86-64.dmg` installer, and follow on-screen instructions.

## Get started

See the [Get started with Arm Performance Studio for Mobile](/learning-paths/mobile-graphics-and-gaming/ams/) learning path for a collection of tutorials for each component of Performance Studio.
