---
title: Setting up development environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this Learning Path, you will learn how to

* Integrate Dawn (WebGPU) in the application.
* Use the APIs to render a simple 3D object.
* Profile and analyze the application.

The first step is to prepare a development environment with the required software:

* [Android Studio](https://developer.android.com/studio)
* Arm [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) Performance Analyzer
* Git.
* Python 3.10 or later.

## Install Android Studio and Android NDK

Follow these steps to install and configure Android Studio:

* Download and install the latest version of [Android Studio](https://developer.android.com/studio/).
* Start Android Studio and open the **Settings** dialog.
* Navigate to **Languages & Frameworks**, then **Android SDK**.
* In the **SDK Platforms** tab, check **Android 14.0 ("UpsideDownCake")**.
* In the **SDK Tools** tab
  1. Check **35.0.0** under **Android SDK Build-Tools 35**
  2. Check **27.x.xxxxxx** under **NDk(Side by side)**
  3. Check **3.xx.x** under **CMake** (latest is recommended)

## Install Arm Streamline

Profiling an application, to make sure it is performant is an important step in the Android application development cycle. The default profiler in the Android Studio is great to profile CPU related metrics, but does not provide details when it comes to GPUs. Arm has developed a comprehensive profiling software, Streamline, to profile both CPU and GPU. Streamline is an application profiler that can capture data from multiple sources, including:

* Program Counter (PC) samples from running application threads.
* Samples from the hardware Performance Monitoring Unit (PMU) counters in the Arm CPU, Arm® Mali™ GPUs, and Arm Immortalis™ GPUs.
* Thread scheduling information from the Linux kernel.
* Software-generated annotations and counters from running applications.

You can download and install latest version of [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) for your Operating System

{{% notice Tip %}}
If you wan to learn more about streamline, you can refer to the ["Getting Started with Streamline"](https://developer.arm.com/documentation/101816/0903/Getting-started-with-Streamline)
{{% /notice %}}
