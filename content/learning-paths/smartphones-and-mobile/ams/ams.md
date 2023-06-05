---
# User change
title: "What is Arm Mobile Studio?"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Arm Mobile Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio) is a performance analysis tool suite for developers to performance test their Android apps on Mali-based GPUs. It comprises of 4 easy-to-use tools that show you how well your game or app performs on off-the-shelf devices, so that you can identify problems that might cause slow performance, overheat the device, or drain the battery. 

| Component | Functionality |
|----------|-------------|
| [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) | captures a performance profile that shows all the performance counter activity from the device. |
| [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor) | generates an easy-to-read performance summary from an annotated Streamline capture, and get actionable advice about where you should optimize. |
| [Graphics Analyzer](https://developer.arm.com/Tools%20and%20Software/Graphics%20Analyzer) | enables you to analyze Open GL ES and Vulkan API calls in your application, to identify rendering defects and investigate problem scenes. |
| [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) | enables you to analyze how your shader programs would perform on a range of Mali GPUs. |

## Licensing

As of the 2022.4 release, all features of Arm Mobile Studio are available for use free of charge without any additional license.

## Installation

Arm Mobile Studio is supported on Windows, Linux, and macOS hosts. Download the appropriate installer from the [Arm Product Download Hub](https://developer.arm.com/downloads/view/MOBST-PRO0).

Full installation and application launch instructions are given in the Arm Mobile Studio [Release Notes](https://developer.arm.com/documentation/107649).

### Windows

Run the supplied `Arm_Mobile_Studio_<version>.exe` installer, and follow on-screen instructions.

### Linux

Unpack the supplied `Arm_Mobile_Studio_<version>_linux.tgz` installation package.
```command
tar -xf Arm_Mobile_Studio_2023.1_linux.tgz
```
### macOS

Run the supplied `Arm_Mobile_Studio_<version>_macos.dmg` installer, and follow on-screen instructions.
