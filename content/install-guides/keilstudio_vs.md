---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Keil Studio for VS Code

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cortex-m
- microcontroller
- mcu
- iot
- ide
- vs code
- vscode
- visual studio
- cmsis


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/108029

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Keil Studio](https://keil.arm.com/) is the next generation software development environment for Arm Cortex-M based microcontroller devices. The desktop version is available as a set of [Visual Studio Code](https://code.visualstudio.com/) extensions.

Alternatively, [Keil Studio Cloud](/install-guides/keilstudiocloud/) provides similar functionality, but runs in a browser and requires no installation. 

## Before you begin

[Download](https://code.visualstudio.com/download), install, and start `Visual Studio Code` on your desktop.

Linux, macOS, and Windows are supported. 

## Install the Keil Studio extensions

The `Keil Studio Pack` extensions is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack).

Install the Keil Studio extensions: 

1. Open the `Extensions` view in Visual Studio Code
2. Search for `Keil Studio Pack`
3. Click the `Install` button to install all extensions in the `Keil Studio Pack`

Visual Studio Code installs the extensions. The extensions are now available in the `Activity Bar`.

You will be prompted to enable an [MDK Community License](https://www.keil.arm.com/mdk-community/) for non-commercial use. Accept this option if you do not have a license and agree to non-commercial use.

If you have a commercial license for `Keil MDK` installed, decline this option.

## Get started

Follow the [Getting started with an example project](https://developer.arm.com/documentation/108029/latest/Get-started-with-an-example-project) tutorial to verify the extensions are installed correctly.

## Extension information

Use the table below to find additional information about the VS Code extensions.

| Extension | Description |
|-----------|-------------|
| [Arm CMSIS csolution](https://github.com/ARM-software/vscode-cmsis-csolution/blob/main/README.md) | provides support for working with CMSIS solutions (csolution projects).|
| [Arm Device Manager](https://github.com/ARM-software/vscode-device-manager/blob/main/README.md) | allows you to manage device connections for Arm Cortex-M based microcontrollers, development boards and debug probes.|
| [Arm Embedded Debugger](https://github.com/ARM-software/vscode-embedded-debug/blob/main/README.md) | allows you to do flashing and debugging on Arm Cortex-M targets implementing the Microsoft Debug Adapter Protocol (DAP). |
| [Arm Remote Build](https://github.com/ARM-software/vscode-remote-build/blob/main/README.md) | allows you to undertake remote builds of projects for Arm Cortex-M targets. |
| [Arm Virtual Hardware](https://github.com/ARM-software/vscode-virtual-hardware/blob/main/README.md) | allows you to manage Arm Virtual Hardware and run embedded applications on them. |
| [Keil Studio Pack](https://github.com/ARM-software/vscode-keil-studio-pack/blob/main/README.md) |  installs recommended extensions for embedded and IoT software development on Arm-based microcontroller (MCU) devices. |
