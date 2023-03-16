---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Streamline

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- profiler

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

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

Streamline is available as a component of [Arm Mobile Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio) or [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

The version of Streamline provided with Arm Mobile Studio supports [certain Android targets](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Supported-Devices) only.

For other use cases, use the version of Streamline provided with Arm Development Studio.

## Download installer packages

Download the appropriate package from the [Product Download Hub](https://developer.arm.com/downloads).

 - [Arm Mobile Studio](https://developer.arm.com/downloads/view/MOBST-PRO0)
 - [Arm Development Studio](https://developer.arm.com/downloads/view/DS000B)

## Installation

Install Arm Mobile Studio using these [instructions](https://developer.arm.com/documentation/102526).

Install Arm Development Studio using the instructions in the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio). See also [this article](../armds/).

If using an Android target, you must install Android Debug Bridge(adb) available with [Android SDK platform tools](https://developer.android.com/studio/releases/platform-tools).

Add the path to the downloaded Android SDK platform tools directory to your `PATH` environment variable.

## Setting up product license

Arm Mobile Studio is available as a free starter edition which is not license managed.

If using [Mobile Studio Professional Edition](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Editions), see the supplied readme for license setup instructions.

Arm Development Studio is license managed. License setup instructions are available [here](../license/).

## Get started

To configure your target and/or application for Streamline, follow the appropriate instructions below depending on your use case:

 - [Android](https://developer.arm.com/documentation/101813)
 - [Linux](https://developer.arm.com/documentation/101814)
 - [Bare-metal (and RTOS)](https://developer.arm.com/documentation/101815)

Depending on your type of application, choose the appropriate guide below to get started with profiling your application using Streamline.

- [Profile your Android Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-Android-application)
- [Profile your Linux Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-Linux-application)
- [Profile your bare-metal Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-bare-metal-application)
