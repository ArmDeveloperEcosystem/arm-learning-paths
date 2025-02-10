---
title: Arm Ecosystem FVPs and Architecture Envelope Models
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/100966
author: Ronan Synnott
weight: 4

### FIXED, DO NOT MODIFY
tool_install: false              # Set to true to be listed in main selection page, else false
multi_install: false             # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
Arm provides various Fixed Virtual Platforms (FVPs) free of charge.

* Architecture Envelope Models (AEMs) are generic FVPs suitable for early Arm Architecture exploration.

* Arm Ecosystem FVPs model Arm hardware subsystems, and are supported by relevant Open Source Software projects.

Host platform support will vary by FVP.

## Download

### Architecture Envelope Models

AEM FVPs can be downloaded directly from [Fixed Virtual Platforms](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) on the `Arm Developer` website.

### Ecosystem FVPs

Arm Ecosystem FVPs can be download from [Arm Ecosystem FVPs](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) on the `Arm Developer` website.


## Installation

### Linux
Unpack the downloaded package, and install the FVP library with the supplied script. For example:
```command
./FVP_Corstone_1000.sh --i-agree-to-the-contained-eula --no-interactive
```
For full list of available options, use `--help`:
```command
./FVP_Corstone_1000.sh --help
```

### Windows

Unzip the downloaded installation archive.

Run the installer (`<FVP_name>.msi`), and follow on-screen instructions.

## Verify installation

Arm Ecosystem FVPs and AEMs are not license managed.

To verify everything is working OK, run the installed FVP executable, located in the `models/<build_environment>` folder of the installed directory. No additional command options are needed for this step.

For example:
```command
./FVP_Corstone-1000
```
The FVP will launch, and output text in a terminal similar to:
```output
host_terminal_0: Listening for serial connection on port 5000
host_terminal_1: Listening for serial connection on port 5001
secenc_terminal: Listening for serial connection on port 5002
extsys_terminal: Listening for serial connection on port 5003
```
A visualization of the FVP will also be displayed.

Terminate the FVP with `Ctrl+C`.

## Integration with Arm Toolchains

These FVPs can be used in conjunction with [Arm Development Studio](/install-guides/armds) or [Keil MDK](/install-guides/mdk) (Cortex-M FVPs only) to provide a debug target without the need for real hardware.

Some of these FVPs are also directly supplied with these toolchains.
