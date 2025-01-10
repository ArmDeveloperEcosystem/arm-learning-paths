---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Streamline

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- profiler
- perf
- spe
- Neoverse
- Cortex-A
- Armv8
- Armv8-A
- Armv9
- Armv9-A
- Mali
- immortalis
- Gaming
- Graphics
- Android
- Linux


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/101816

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Streamline Performance Analyzer](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) is an application profiler for Android, Linux and bare-metal applications.

Streamline is available as a component of [Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio) or [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

The version of Streamline provided with Performance Studio supports [certain Android targets](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Supported-Devices), as well as Linux user-space code.

For other use cases, use Arm Streamline as provided with Arm Development Studio.

## Download installer packages

Download the appropriate package from the [Product Download Hub](https://developer.arm.com/downloads).

 - [Arm Performance Studio](https://developer.arm.com/downloads/view/MOBST-PRO0)
 - [Arm Development Studio](https://developer.arm.com/downloads/view/DEVST-GLD0)

Arm Performance Studio supports Windows, Linux, and macOS hosts.

Arm Development Studio supports Windows and Linux hosts.

## Installation

### Arm Performance Studio

Full install instructions are given in section 3 of the Performance Studio [Release Notes](https://developer.arm.com/documentation/107649).

See also the Arm Performance Studio [install guide](/install-guides/ams/).

If working with an Android target, you must also install Android Debug Bridge (`adb`) available with [Android SDK platform tools](https://developer.android.com/studio/releases/platform-tools).

Add the Android SDK platform tools directory to your `PATH` environment variable.

### Arm Development Studio

Install Arm Development Studio using the instructions in the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio).

See also the Arm Development Studio [install guide](/install-guides/armds/).

## Setting up product license

Arm Development Studio is license managed. License setup instructions are available in the Arm Software Licensing [install guide](/install-guides/license/).

Arm Performance Studio is free of charge and is not license managed.

## Get started

To configure your target and/or application for Streamline, follow the appropriate instructions below depending on your use case:

 - [Android](https://developer.arm.com/documentation/101813)
 - [Linux](https://developer.arm.com/documentation/101814)
 - [Bare-metal (and RTOS)](https://developer.arm.com/documentation/101815)

Depending on your type of application, choose the appropriate guide below to get started with profiling your application using Streamline.

- [Profile your Android Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-Android-application)
- [Profile your Linux Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-Linux-application)
- [Profile your bare-metal Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-bare-metal-application)

For Android users, a thorough [tutorial](https://developer.arm.com/documentation/102477) is also available.

See also the [Get started with Arm Performance Studio](/learning-paths/mobile-graphics-and-gaming/ams/) learning path.
