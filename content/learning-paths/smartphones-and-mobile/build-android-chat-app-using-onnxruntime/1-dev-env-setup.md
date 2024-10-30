---
title: Create a development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this learning path, you will learn how to build and deploy a simple LLM-based chat app to an Android device using ONNX Runtime. You will learn how to build the ONNX Runtime and ONNX Runtime generate() API and how to run the Phi-3 model for the Android application.

Your first task is to prepare a development environment with the required software:

- Android Studio (latest version recommended)
- Android NDK (tested with version 27.0.12077973)
- Python 3.11
- CMake (tested with version 3.28.1)
- Ninja (tested with version 1.11.1)

The following instructions were tested on an x86 Windows machine with at least 16GB of RAM.

## Install Android Studio and Android NDK

Follow these steps to install and configure Android Studio:

1. Download and install the latest version of [Android Studio](https://developer.android.com/studio/). 

2. Navigate to **Tools > SDK Manager**.

3. In the **SDK Platforms** tab, check **Android 14.0 ("UpsideDownCake")**.

4. In the **SDK Tools** tab, check **NDK (Side by side)**.

5. Click **OK** and **Apply**.

## Install Python 3.11

Download and install [Python version 3.11](https://www.python.org/downloads/release/python-3110/)

## Install CMake

CMake is an open-source tool that automates the build process for software projects, helping to generate platform-specific build configurations.

[Download and install CMake](https://cmake.org/download/)

{{% notice Note %}}
The instructions were tested with version 3.28.1
{{% /notice %}}

## Install Ninja

Ninja is a minimalistic build system designed to efficiently handle incremental builds, particularly in large-scale software projects, by focusing on speed and simplicity. The Ninja generator is used to build on Windows for Android.

[Download and install Ninja]( https://github.com/ninja-build/ninja/releases)

{{% notice Note %}}
The instructions were tested with version 1.11.1
{{% /notice %}}

You now have the required development tools installed to follow this learning path.
