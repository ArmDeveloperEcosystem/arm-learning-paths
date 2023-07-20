---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Keil Studio (VS Code Extension)

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
official_docs: https://github.com/ARM-software/vscode-keil-studio-pack/blob/main/extension-pack-web/README.md

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Keil Studio](https://keil.arm.com/) is the next generation software development environment for Arm Cortex-M based microcontroller devices. The desktop version is available as a set of [VS Code](https://code.visualstudio.com/) extensions that offer the same functionality as the cloud-native version.

It supports more than 10,000 Arm Cortex-M-based devices and is easy to learn and use.

## Before you begin

- Install [Microsoft Visual Studio Code](https://code.visualstudio.com/) on your machine (Linux, macOS, Windows are supported).

## Install the extensions

The [Keil Studio VS Code extensions](https://github.com/ARM-software/vscode-keil-studio-pack) are available for [Desktop](https://github.com/ARM-software/vscode-keil-studio-pack/blob/main/extension-pack-desktop/README.md) and [Web-based](https://github.com/ARM-software/vscode-keil-studio-pack/blob/main/extension-pack-web/README.md) instances.

1. In VS Code, go to the `Extensions` view.
2. Search for `Keil Studio Pack`.
3. Click the `Install` button for the appropriate extension pack.

Visual Studio Code installs the extensions. All recommended extensions are now available in the `Extensions` view.

## Get started

In the `Extensions` view, select the `Keil Studio Pack` extension and follow the supplied tutorial to verify everything is installed correctly.

For more information on the extensions, see the links below.

| Extension | Description |
|-----------|-------------|
| [Arm CMSIS csolution](https://github.com/ARM-software/vscode-cmsis-csolution/blob/main/README.md) | provides support for working with CMSIS solutions (csolution projects).|
| [Arm Device Manager](https://github.com/ARM-software/vscode-device-manager/blob/main/README.md) | allows you to manage device connections for Arm Cortex-M based microcontrollers, development boards and debug probes.|
| [Arm Embedded Debugger](https://github.com/ARM-software/vscode-embedded-debug/blob/main/README.md) | allows you to do flashing and debugging on Arm Cortex-M targets implementing the Microsoft Debug Adapter Protocol (DAP). |
| [Arm Remote Build](https://github.com/ARM-software/vscode-remote-build/blob/main/README.md) | allows you to undertake remote builds of projects for Arm Cortex-M targets. |
| [Arm Virtual Hardware](https://github.com/ARM-software/vscode-virtual-hardware/blob/main/README.md) | allows you to manage Arm Virtual Hardware and run embedded applications on them. |
| [Keil Studio Pack](https://github.com/ARM-software/vscode-keil-studio-pack/blob/main/README.md) |  installs recommended extensions for embedded and IoT software development on Arm-based microcontroller (MCU) devices. |
