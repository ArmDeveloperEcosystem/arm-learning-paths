---
title: Arm Keil Studio for VS Code
description: Install Arm Keil Studio extensions for Visual Studio Code and verify the setup for Cortex-M embedded development on desktop hosts.

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

minutes_to_complete: 15

author: Ronan Synnott

official_docs: https://developer.arm.com/documentation/108029

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---
[Arm Keil Studio](https://keil.arm.com/) is the next generation software development environment for Arm Cortex-M based microcontroller devices. The desktop version is available as a set of [Visual Studio Code](https://code.visualstudio.com/) extensions.

Alternatively, [Keil Studio Cloud](/install-guides/keilstudiocloud/) provides similar functionality, but runs in a browser and requires no installation. 

## Download and install Visual Studio Code

[Download](https://code.visualstudio.com/download), install, and start Visual Studio Code on your desktop.

Linux, macOS, and Windows are supported. 

## Install the Keil Studio extensions

The **Keil Studio Pack** extension is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack).

Install the Keil Studio extensions: 

1. Open the **Extensions** view in Visual Studio Code
2. Search for **Keil Studio Pack**
3. Select the **Install** button to install all extensions in the **Keil Studio Pack**

![The Keil Studio Pack extension shown in the VS Code Extensions marketplace view, with the Arm publisher name and Install button visible#center](/install-guides/_images/ks-extension.webp "Keil Studio Pack in the VS Code Extensions marketplace")

## Verify the installation

After installation, the Keil Studio icons appear in the **Activity Bar** on the left side of VS Code.

![VS Code Activity Bar showing the Keil Studio extension icons after successful installation of the Keil Studio Pack#center](/install-guides/_images/ks-installed.webp "Keil Studio extensions visible in the VS Code Activity Bar")

To verify the extensions are working correctly, follow the [Work with CMSIS solutions](https://mdk-packs.github.io/vscode-cmsis-solution-docs/create_app.html#) tutorial.

## More information

Use the table below to find additional information about the VS Code extensions.

| Extension | Description |
|-----------|-------------|
| [Arm CMSIS csolution](https://github.com/ARM-software/vscode-cmsis-csolution/blob/main/README.md) | Provides support for working with CMSIS solutions (csolution projects). |
| [Arm Device Manager](https://github.com/ARM-software/vscode-device-manager/blob/main/README.md) | Allows you to manage device connections for Arm Cortex-M based microcontrollers, development boards and debug probes. |
| [Arm Embedded Debugger](https://github.com/ARM-software/vscode-embedded-debug/blob/main/README.md) | Allows you to do flashing and debugging on Arm Cortex-M targets implementing the Microsoft Debug Adapter Protocol (DAP). |
| [Arm Remote Build](https://github.com/ARM-software/vscode-remote-build/blob/main/README.md) | Allows you to undertake remote builds of projects for Arm Cortex-M targets. |
| [Arm Virtual Hardware](https://github.com/ARM-software/vscode-virtual-hardware/blob/main/README.md) | Allows you to manage Arm Virtual Hardware and run embedded applications on them. |
| [Keil Studio Pack](https://github.com/ARM-software/vscode-keil-studio-pack/blob/main/README.md) | Installs recommended extensions for embedded and IoT software development on Arm-based microcontroller (MCU) devices. |
